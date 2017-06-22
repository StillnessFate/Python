import sys
if sys.version_info < (3, 3, 0) :
    print("Python 3.3 이상에서만 동작합니다.")
    exit()

from tkinter import *
import platform
import time


class Propertys() :
    TPS = 30
    FPS = 30
    RESOLUTION_W = 800
    RESOLUTION_H = 600
    SPEED_FACTOR = 1.0
    TICK_DELAY = 5 # ms
    OS = platform.system()
    SHOW_FPS = False

    def set_tps(tps) :
        Propertys.TPS = tps

    def set_fps(fps) :
        Propertys.FPS = fps

    def set_resolution_w(resolution_w) :
        Propertys.RESOLUTION_W = resolution_w

    def set_resolution_h(resolution_h) :
        Propertys.RESOLUTION_H = resolution_h

    def set_speed_factor(speed_factor) :
        Propertys.SPEED_FACTOR = speed_factor

    def set_tick_delay(tick_delay) :
        Propertys.TICK_DELAY = tick_delay

    def set_tick_delay(tick_delay) :
        Propertys.TICK_DELAY = tick_delay

    def set_show_fps(show_fps) :
        Propertys.SHOW_FPS = show_fps

class Game() :
    def __init__(self, objectManager) :
        self.objectManager = objectManager
        self.window = None
        self.canvas = None
        self.tickCount  = 0
        self.updateCycle = 1 / Propertys.TPS
        self.renderUpdateCycle = 1 / Propertys.FPS
        self.timeToConsume = self.updateCycle
        self.renderTimeToConsume = self.renderUpdateCycle

        self.previousTime = -1.0
        self.renderPreviousTime = 0.0
        self.realRenderPreviousTime = 0.0
        self.tickUpdate = False
        self.render_maintains = []
        self.save_fps = []

    def run(self) :
        self.input_processing()
        self.logic()
        self.render()
        self.canvas.after(Propertys.TICK_DELAY, self.run)

    def input_processing(self) :
        x = self.canvas.winfo_pointerx()
        y = self.canvas.winfo_pointery()
        abs_coord_x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        abs_coord_y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
        scale_sync_x = self.window.RW_M(abs_coord_x)
        scale_sync_y = self.window.RH_M(abs_coord_y)
        self.window.mouse_x = scale_sync_x
        self.window.mouse_y = scale_sync_y

        self.window.mouseL_click_x = self.window.RW_M(self.window.mouseL_click_x_nonSync)
        self.window.mouseL_click_y = self.window.RH_M(self.window.mouseL_click_y_nonSync)
        self.window.mouseL_state = self.window.mouseL_state_nonSync
        self.window.mouseR_click_x = self.window.RW_M(self.window.mouseR_click_x_nonSync)
        self.window.mouseR_click_y = self.window.RH_M(self.window.mouseR_click_y_nonSync)
        self.window.mouseR_state = self.window.mouseR_state_nonSync

    def pre_logic(self) :
        self.window.sync_resolution_scale()
        self.window.sync_canvas_size()

        for object in self.objectManager.get_list() :
            if object.call_pre_logic :
                object.pre_logic()

    def post_logic(self) :
        for object in self.objectManager.get_list() :
            if object.call_post_logic :
                object.post_logic()

        self.objectManager.tick_end_process()
                
    def logic(self) :
        currentTime = time.perf_counter()
        if self.previousTime < 0 :
            self.previousTime = currentTime
            self.timeToConsume = self.updateCycle
        delta  = currentTime - self.previousTime
        self.previousTime = currentTime
        self.timeToConsume += delta * Propertys.SPEED_FACTOR

        while self.timeToConsume >= self.updateCycle :
            self.tickCount += 1
            self.timeToConsume -= self.updateCycle

            self.pre_logic()
            # ==============로직 시작==============
            for object in self.objectManager.get_list() :
                object.logic()
            # ==============로직 끝==============
            self.post_logic()

            self.tickUpdate = True

    def add_render_maintain_object(self, object) :
        self.render_maintains.append(object)

    def remove_render_maintain_object(self, object) :
        if object in self.render_maintains :
            self.render_maintains.remove(object)

    def render(self) :
        currentTime = time.perf_counter()
        delta  = currentTime - self.renderPreviousTime
        self.renderPreviousTime = currentTime
        self.renderTimeToConsume += delta % self.renderUpdateCycle

        if (self.tickUpdate == False) or (self.renderTimeToConsume < self.renderUpdateCycle) :
            return

        self.tickUpdate = False
        self.renderTimeToConsume -= self.renderUpdateCycle
        self.save_fps.append(1 / (currentTime - self.realRenderPreviousTime))
        if Propertys.SHOW_FPS and ((Propertys.FPS // 5) <= len(self.save_fps)) :
            fps = sum(self.save_fps) / len(self.save_fps)
            fps = round(fps)
            self.window.set_title(None, '   FPS : ' + str(fps))
            self.save_fps = []
        self.realRenderPreviousTime = currentTime # FPS: 1 / (currentTime - self.realRenderPreviousTime)

        # ==============랜더링 시작==============
        for object in self.canvas.find_all():
            if object not in self.render_maintains :
                self.canvas.delete(object)
        #self.canvas.delete(ALL)
        for object in self.objectManager.get_list() :
            object.draw()
        # ==============랜더링 끝==============

    def get_objectManager(self) :
        return self.objectManager

    def set_window_object(self, window) :
        self.window = window
        self.canvas = self.window.get_canvas()

class ObjectManager() :
    def __init__(self) :
        self.objectList = []
        self.removeList = []
        self.addList = []

    def add_object(self, object) :
        self.objectList.append(object)
        self.objectList.sort(key=lambda object: object.depth, reverse=True)

    def add_object_safe(self, object) :
        self.addList.append(object)

    def remove_object(self, object) :
        if object in self.objectList :
            self.objectList.remove(object)

    def remove_object_in_tick_end(self, object) :
        self.removeList.append(object)

    def tick_end_process(self) :
        for object in self.removeList :
            self.remove_object(object)
        self.removeList = []

        for object in self.addList :
            self.add_object(object)
        self.addList = []

    def get_list(self) :
        return self.objectList

class MainWindow() :
    def __init__(self) :
        self.__master = Tk()
        self.title_text = ""
        self.title_text_additional = ""
        self.master.title(self.title_text + self.title_text_additional)

        self.defaultResolution_width = Propertys.RESOLUTION_W
        self.defaultResolution_height = Propertys.RESOLUTION_H
        self.width = self.defaultResolution_width
        self.height = self.defaultResolution_height

        self.resolutionScale_width = 1.0
        self.resolutionScale_height = 1.0
        self.master.geometry("{0}x{1}".format(self.width, self.height))

        self.frame = Frame(self.master, width=self.master.winfo_width(), height=self.master.winfo_height())
        self.frame.pack()

        self.canvas = Canvas(self.frame)
        self.canvas.pack()

        self.master.update()
        self.sync_resolution_scale()
        self.sync_canvas_size()
        
        self.game = None

        self.mouse_x = 0
        self.mouse_y = 0
        self.mouseL_click_x_nonSync = 0
        self.mouseL_click_y_nonSync = 0
        self.mouseL_click_x = 0
        self.mouseL_click_y = 0
        self.mouseL_state_nonSync = 'up'
        self.mouseL_state = 'up'
        self.mouseR_click_x_nonSync = 0
        self.mouseR_click_y_nonSync = 0
        self.mouseR_click_x = 0
        self.mouseR_click_y = 0
        self.mouseR_state_nonSync = 'up'
        self.mouseR_state = 'up'

        self.canvas.bind("<Button-1>", lambda x: self.set_mouse_state('L', 'down', x))
        self.canvas.bind("<ButtonRelease-1>", lambda x: self.set_mouse_state('L', 'up', x))
        if Propertys.OS == 'Windows' :
            self.canvas.bind("<Button-3>", lambda x: self.set_mouse_state('R', 'down', x))
            self.canvas.bind("<ButtonRelease-3>", lambda x: self.set_mouse_state('R', 'up', x))
        else :
            self.canvas.bind("<Button-2>", lambda x: self.set_mouse_state('R', 'down', x))
            self.canvas.bind("<ButtonRelease-2>", lambda x: self.set_mouse_state('R', 'up', x))

    def sync_resolution_scale(self) :
        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()

        self.resolutionScale_width = self.width / self.defaultResolution_width
        self.resolutionScale_height = self.height / self.defaultResolution_height

        self.resolutionScale_width = self.width / self.defaultResolution_width
        self.resolutionScale_height = self.height / self.defaultResolution_height

    def sync_canvas_size(self) :
        self.canvas['width'] = self.width
        self.canvas['height'] = self.height

    def RW(self, num) :
        return num * self.resolutionScale_width

    def RW_M(self, num) :
        return num * (1 / self.resolutionScale_width)

    def RH(self, num) :
        return num * self.resolutionScale_height

    def RH_M(self, num) :
        return num * (1 / self.resolutionScale_height)

    def is_inside_point(self, x, y) :
        if (x < 0 or self.defaultResolution_width < x) or (y < 0 or self.defaultResolution_height < y) :
            return False
        else :
            return True

    def is_inside_box(self, x1, y1, x2 ,y2) :
        if (min(x1, x2) < 0 or self.defaultResolution_width < max(x1, x2)) or (min(y1, y2) < 0 or self.defaultResolution_height < max(y1, y2)) :
            return False
        else :
            return True

    def get_canvas(self) :
        return self.canvas

    def set_game_object(self, game) :
        game.set_window_object(self)
        self.game = game
        self.canvas.after(0, game.run)

    def get_game_object(self) :
        return self.game

    def start_main_loop(self) :
        self.master.mainloop()

    def set_mouse_state(self, button, state, pos) :
        if button == 'L' :
            self.mouseL_click_x_nonSync = pos.x
            self.mouseL_click_y_nonSync = pos.y
            self.mouseL_state_nonSync = state
        elif button == 'R' :
            self.mouseR_click_x_nonSync = pos.x
            self.mouseR_click_y_nonSync = pos.y
            self.mouseR_state_nonSync = state

    def set_title(self, title = None, additional = "") :
        if title != None :
            self.title_text = title
        self.title_text_additional = additional
        self.master.title(self.title_text + self.title_text_additional)

    @property
    def master(self) :
        return self.__master