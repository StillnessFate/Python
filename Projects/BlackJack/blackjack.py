import tkinter
import engine
import math
import random
import os

# 기본 개발 운영체제 : Windows
# macOS 크로스플랫폼 가능 (tkinter 최적화 문제로 성능이 저하됨)

def install_pip(package) :
    import importlib
    import pip

    installed_packages = pip.get_installed_distributions()
    installed_packages_list = [i.key for i in installed_packages]
    if package.lower() not in installed_packages_list :
        pip.main(['install', '--user', package])

def force_load(moduleName, parent = False):
    import sys
    import imp
    import site
    import os

    module = None
    p_name = ''
    name = moduleName
    filePath = ''
    ds = os.path.sep

    if moduleName == '' :
        return None

    if parent :
        p_name = name
        name = name + '.' + '__init__'
    else :
        if 1 < len(name.split('.')) :
            parent = name.split('.')[0]
            m = name.split('.')[1]
            if parent not in sys.modules.keys() :
                force_load(parent, True)

    if name in sys.modules.keys() :
        filePath = sys.modules[name].__file__
        if filePath.endswith('.pyc') or filePath.endswith('.pyo'):
            filePath = filePath[:-1]
    else :
        temp = name.replace('.',ds) + '.py'
        if type(site.getsitepackages()) == list :
            for sp_path in site.getsitepackages() :
                if os.path.isfile(sp_path + ds + temp) :
                    filePath = sp_path + ds + temp
                    break;
        elif type(site.getsitepackages()) == str :
            if os.path.isfile(site.getsitepackages() + ds + temp) :
                filePath = site.getsitepackages() + ds + temp
        if filePath == '' :
            if type(site.getusersitepackages()) == list :
                for sp_path in site.getusersitepackages() :
                    if os.path.isfile(sp_path + ds + temp) :
                        filePath = sp_path + ds + temp
                        break;
            elif type(site.getsitepackages()) == str :
                if os.path.isfile(site.getusersitepackages() + ds + temp) :
                    filePath = site.getusersitepackages() + ds + temp

    if p_name != '' :
        name = p_name
    if filePath != '' :
        module = imp.load_source(name, filePath)
        sys.modules[name] = module

    return module

def install_required_packages() :
    import sys
    import importlib
    import site

    Image = None
    ImageTk = None
    ImageDraw = None
    ImageFont = None
    loaded = False

    try :
        from PIL import Image, ImageTk, ImageDraw, ImageFont
        loaded = True
    except :
        print("필수 라이브러리를 설치합니다.(Pillow)")
        install_pip('Pillow')

    if not loaded :
        if engine.Propertys.OS == 'Windows' :
            importlib.reload(site)
            try :
                if ('PIL.Image' not in sys.modules.keys()) or ('PIL.ImageTk' not in sys.modules.keys()) or ('PIL.ImageDraw' not in sys.modules.keys()) or ('PIL.ImageFont' not in sys.modules.keys()) :
                    from PIL import Image, ImageTk, ImageDraw, ImageFont
            except :
                pass
        else :
            try :
                Image = force_load('PIL.Image')
                ImageTk = force_load('PIL.ImageTk')
                ImageDraw = force_load('PIL.ImageDraw')
                ImageFont = force_load('PIL.ImageFont')
            except :
                pass

    return Image, ImageTk, ImageDraw, ImageFont

Image, ImageTk, ImageDraw, ImageFont = install_required_packages()

if None in (Image, ImageTk, ImageDraw, ImageFont) :
    print("필수 라이브러리 설치에 실패하였습니다.(Pillow)")
    exit()


CARD_W = 100
CARD_H = 145

image_format = 'png'
image_resize_mode = Image.ANTIALIAS
if engine.Propertys.OS == 'Darwin' :
    image_format = 'gif'
    image_resize_mode = Image.NEAREST

image_path = {
    'icon': 'resources/images/icon.ico',
    'cards': 'resources/images/cards/',
    'deck': 'resources/images/deck.' + image_format,
    'back': 'resources/images/cards/back.' + image_format,
    'betting': 'resources/images/betting.' + image_format,
    'betting_lock': 'resources/images/betting_lock.' + image_format,
    'chip': 'resources/images/chip.' + 'png', # rotate
    '100': 'resources/images/100.' + image_format,
    '50': 'resources/images/50.' + image_format,
    '10': 'resources/images/10.' + image_format,
    'hit': 'resources/images/hit.' + image_format,
    'stay': 'resources/images/stay.' + image_format,
    'deal': 'resources/images/deal.' + image_format,
    'regame': 'resources/images/regame.' + image_format,
    'exit': 'resources/images/exit.' + image_format,
    'table': 'resources/images/table.' + image_format,
    'bar': 'resources/images/bar.' + image_format,
    'board': 'resources/images/board.' + image_format,
    'cursor': 'resources/images/cursor.' + image_format,
    'win': 'resources/images/win.' + image_format,
    'lose': 'resources/images/lose.' + image_format,
    'draw': 'resources/images/draw.' + image_format,
    'p_bj': 'resources/images/p_bj.' + image_format,
    'p_bs': 'resources/images/p_bs.' + image_format,
    'd_bj': 'resources/images/d_bj.' + image_format,
    'd_bs': 'resources/images/d_bs.' + image_format,
    'login': 'resources/images/login.' + image_format
}

font_path = {
    'RosewoodStd-Regular': 'resources/fonts/RosewoodStd-Regular.otf',
    'malgunbd': 'resources/fonts/malgunbd.ttf'
}


def length_dir(length, dir) : #degree
    rad = math.pi * (dir / 180.0)
    x = length * math.cos(rad)
    y = length * math.sin(rad)
    return (x, y)

def distance(x1, y1, x2, y2) :
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

def get_angle(x1, y1, x2, y2) :
    dx = x2 - x1
    dy = y2 - y1
    rad = math.atan2(dy, dx)
    degree = rad * (180 / math.pi)
    if degree < 0 :
        degree += 360
    return degree

def flatten_alpha(iamge) :
    alpha = iamge.split()[-1]  # Pull off the alpha layer
    alpha_bytes = alpha.tobytes()  # Original 8-bit alpha
    checked = []  # Create a new array to store the cleaned up alpha layer bytes
    # Walk through all pixels and set them either to 0 for transparent or 255 for opaque fancy pants
    transparent = 128  # change to suit your tolerance for what is and is not transparent

    for pixel in range(0, len(alpha_bytes)) :
        if alpha_bytes[pixel] < transparent:
            checked.append(0)  # Transparent
        else:
            checked.append(255)  # Opaque

    mask = Image.frombytes('L', iamge.size, bytes(checked))
    iamge.putalpha(mask)

    return iamge

def tick_leveling(num) :
    return (num / 30) * engine.Propertys.TPS

def tick_leveling_r(num) :
    return num * (30 / engine.Propertys.TPS)

class Game_BlackJack() :
    phases = ('ready', 'betting', 'pre_draw', 'draw', 'pre_player', 'player', 'pre_dealer', 'dealer', 'result', 'select', 'clean', 'branch')

    def __init__(self, window, objectManager) :
        self.call_pre_logic = False
        self.call_post_logic = True
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.phase_to = 'ready'
        self.phase = 'ready'
        self.outcome = None
        self.show_outcome = None
        self.dealer = None
        self.player = None
        self.deck = None
        self.bar = None
        self.betting_system = None
        self.objectManager = objectManager
        self.regame_toggle = False
        self.button_regame = None
        self.button_exit = None
        self.button_deal = None
        self.auto_regame = False

    def set_dealer(self, dealer) :
        self.dealer = dealer
        self.dealer.game_blackjack = self

    def set_player(self, player) :
        self.player = player
        self.player.game_blackjack = self

    def set_deck(self, deck) :
        self.deck = deck
        self.deck.game_blackjack = self

    def set_bar(self, bar) :
        self.bar = bar
        self.bar.game_blackjack = self

    def set_betting_system(self, betting_system) :
        self.betting_system = betting_system
        self.betting_system.game_blackjack = self

    def exit(self) :
        if self.phase == 'select' :
            self.regame_toggle = False
            self.next_phase()

    def regame(self) :
        if self.phase == 'select' :
            self.regame_toggle = True
            self.next_phase()

    def get_phase(self) :
        return self.phase

    def get_outcome(self) :
        return self.outcome

    def next_phase(self) :
        if self.phase != self.phases[-1] :
            self.phase_to = self.phases[self.phases.index(self.phase) + 1]
            #print(self.phase_to)

    def set_phase(self, phase) :
        self.phase_to = phase

    def logic(self) :
        if self.phase == 'ready' :
            self.betting_system.set_bet_money(200)
            if not self.player.auto_play :
                self.button_deal = Button(270, 530, 260, 50, self.window, ('deal', self.objectManager), lambda: self.player.deal())
                self.button_deal.set_depth(5)
                self.button_deal.moveto(270, 320, tick_leveling(7))
                self.objectManager.add_object_safe(self.button_deal)

            self.next_phase()
        elif self.phase == 'betting' :
            pass
        elif self.phase == 'pre_draw' :
            self.deck.add_command(Command('pick', (self.player, True)))
            self.deck.add_command(Command('pick', (self.player, True)))
            self.deck.add_command(Command('pick', (self.dealer, True)))
            self.deck.add_command(Command('pick', (self.dealer, False)))
            self.deck.add_command(Command('next_phase', None))
            self.next_phase()
        elif self.phase == 'draw' :
            pass
        elif self.phase == 'pre_player' :
            self.next_phase()
        elif self.phase == 'player' :
            pass
        elif self.phase == 'pre_dealer' :
            self.next_phase()
        elif self.phase == 'dealer' :
            pass
        elif self.phase == 'result' :
            player_point = self.player.get_total()
            dealer_point = self.dealer.get_total()

            player_blackjack = ((player_point == 21) and (len(self.player.get_hand()) == 2))
            dealer_blackjack = ((dealer_point == 21) and (len(self.dealer.get_hand()) == 2))
            player_bust = (21 < player_point)
            dealer_bust = (21 < dealer_point)
            game = ''

            if not player_bust and ((dealer_point < player_point) or dealer_bust) :
                game = 'win'
            elif (player_point < dealer_point) or player_bust :
                game = 'lose'
            else :
                if player_blackjack :
                    if dealer_blackjack :
                        game = 'draw'
                    else :
                        game = 'win'
                else :
                    if dealer_blackjack :
                        game = 'lose'
                    else :
                        game = 'draw'

            change = self.betting_system.get_bet_money()
            if game == 'win' :
                self.player.info['win'] += 1
                if player_blackjack :
                    change *= 1.5
            elif game == 'lose' :
                self.player.info['lose'] += 1
                change = -change
            elif game == 'draw' :
                self.player.info['draw'] += 1
                change = 0
            self.player.info['money'] += round(change)
            RecordManager.save_user_record(self.player.info)

            self.outcome = (game, player_blackjack, player_bust, dealer_blackjack, dealer_bust)
            #print(self.outcome)

            self.show_outcome = ShowOutcome(self.window, self.outcome, self)
            self.show_outcome.set_depth(-13)
            self.show_outcome.set_pos(400,-100)
            self.show_outcome.moveto(400,260, tick_leveling(7))
            self.objectManager.add_object_safe(self.show_outcome)
            if not self.auto_regame :
                self.button_regame = Button(250, 530, 120, 120, self.window, ('regame', self.objectManager), lambda: self.regame())
                self.button_regame.set_depth(-13)
                self.button_regame.moveto(250, 320, tick_leveling(7))
                self.objectManager.add_object_safe(self.button_regame)

                self.button_exit = Button(430, 530, 120, 120, self.window, ('exit', self.objectManager), lambda: self.exit())
                self.button_exit.set_depth(-13)
                self.button_exit.moveto(430, 320, tick_leveling(7))
                self.objectManager.add_object_safe(self.button_exit)
            
            self.next_phase()
        elif self.phase == 'select' :
            if self.auto_regame :
                self.regame()
        elif self.phase == 'clean' :
            self.player.reset()
            self.dealer.reset()
            self.deck.reset()
            self.betting_system.reset()
            if not self.auto_regame :
                self.button_regame.move_and_remove = True
                self.button_regame.moveto(250, 530, tick_leveling(7))
                self.button_exit.move_and_remove = True
                self.button_exit.moveto(430, 530, tick_leveling(7))

            self.next_phase()
        elif self.phase == 'branch' :
            if (self.player.state == None) and (self.dealer.state == None) and self.show_outcome.removed :
                if self.regame_toggle :
                    self.regame_toggle = False
                    self.set_phase('ready')
                else :
                    exit()

    def post_logic(self) :
        self.phase = self.phase_to

    def draw(self) :
        pass

class Deck() :
    def __init__(self, window) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.state = None
        self.x = 0
        self.y = 0
        self.width = CARD_W
        self.height = CARD_H + 15
        self.image = Image.open(image_path['deck'])
        self.tk_image = ImageTk.PhotoImage(self.image)
        
        self.game_blackjack = None
        self.target = None
        self.temp_card = None
        self.deck = self.fresh_deck()
        self.commandq = []

    def fresh_deck(self) :
        cards = []
        image_back = Image.open(image_path['back'])
        for s in Card.suits :
            for r in Card.ranks :
                new_card = Card(self.window, s, r, False)
                image = Image.open(image_path['cards'] + '{0}_of_{1}.'.format(r, s) + image_format)
                new_card.set_images(image, image_back)
                cards.append(new_card)
        random.shuffle(cards)
        return cards

    def reset(self) :
        if self.temp_card != None :
            self.temp_card.moveto_remove(self.temp_card.x, -150, tick_leveling(7), self.game_blackjack.objectManager)
        self.state = None
        self.target = None
        self.temp_card = None
        self.deck = self.fresh_deck()
        self.commandq = []

    def set_depth(self, depth) :
        self.depth = depth

    def get_state(self) :
        return self.state

    def get_command(self) :
        if self.commandq == [] :
            return None
        temp = self.commandq[0]
        self.commandq = self.commandq[1:]
        return temp

    def add_command(self, command) :
        self.commandq.append(command)

    def pick(self, target) :
        self.state = 'pick'
        self.target = target
        card = self.deck.pop()

        if self.target == self.game_blackjack.player :
            target_pos_y = 514 - CARD_H
        elif self.target == self.game_blackjack.dealer :
            target_pos_y = 6

        hand = self.target.get_hand()
        card.set_pos(self.x, self.y)
        card.set_depth(-len(hand))
        target_pos_x = 400 - (((CARD_W / 2) * (len(hand) + 2)) / 2)
        for c in hand :
            c.moveto(target_pos_x, target_pos_y, tick_leveling(3))
            target_pos_x += (CARD_W / 2)
        card.moveto(target_pos_x, target_pos_y, tick_leveling(3))

        return card

    def set_pos(self, x, y) :
        self.x = x
        self.y = y

    def logic(self) :
        if (self.game_blackjack.get_phase() != 'pre_draw') and (self.state == None) and (self.temp_card == None) :
            command = self.get_command()
            if command != None :
                if command.type == 'pick' :
                    self.target = command.val[0]
                    self.open = command.val[1]
                    self.temp_card = self.pick(self.target)
                    self.game_blackjack.objectManager.add_object_safe(self.temp_card)
                elif command.type == 'next_phase':
                    self.game_blackjack.next_phase()
        elif self.temp_card != None :
            if self.temp_card.state == None :
                if self.open != None :
                    self.target.get_card(self.temp_card, self.open)
                    self.open = None
                else :
                    self.temp_card = None
                    self.state = None

    def draw(self) :
        rw_x = self.window.RW(self.x)
        rw_y = self.window.RH(self.y)
        rw_width = self.window.RW(self.width)
        rw_height = self.window.RH(self.height)

        if (self.tk_image == None) or ((self.tk_image.width() != round(rw_width)) or (self.tk_image.height() != round(rw_height))) :
            temp_image = self.image.resize((round(rw_width), round(rw_height)), image_resize_mode)
            self.tk_image = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(rw_x + (rw_width / 2), rw_y + (rw_height / 2), image=self.tk_image)

class Command() :
    def __init__(self, type, val) :
        self.type = type
        self.val = val

class Card() :
    suits = ('diamonds', 'hearts', 'spades', 'clubs')
    ranks = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king')

    def __init__(self, window, suit, rank, face_up=True) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.x = 0
        self.y = 0
        self.width = CARD_W
        self.height = CARD_H
        self.moveto_x = self.x
        self.moveto_y = self.y
        self.minimum_dis = 2
        self.speed_div = 0
        self.state = None
        self.flip_phase = 0
        self.flip_progress = 0
        self.flip_speed = 0
        self.suit = suit
        self.rank = rank
        self.face_up = face_up
        self.image_face_up = face_up
        self.image = None
        self.image_back = None
        self.tk_image = None
        self.move_and_remove = False
        self.objectManager = None
        self.removed = False

    def set_images(self, image, image_back) :
        self.image = image
        self.image_back = image_back

    def is_face_up(self) :
        return self.face_up

    def flip(self, tick_time) :
        self.state = 'flip'
        self.flip_phase = 0
        self.flip_progress = 0.0
        self.flip_speed = 2.0 / tick_time

    def get_state(self) :
        return self.state

    def moveto_remove(self, x, y, div, objectManager) :
        self.objectManager = objectManager
        self.move_and_remove = True
        self.moveto(x, y, div)

    def moveto(self, x, y, div) :
        self.moveto_x = x
        self.moveto_y = y
        self.speed_div = div
        self.state = 'move'

    def set_pos(self, x, y) :
        self.x = x
        self.y = y

    def set_depth(self, depth) :
        self.depth = depth

    def get_depth(self, depth) :
        return self.depth

    def logic(self) :
        if self.state == 'move' :
            dis = distance(self.x, self.y, self.moveto_x, self.moveto_y)
            if self.minimum_dis < dis :
                speed = dis / self.speed_div
                ang = get_angle(self.x, self.y, self.moveto_x, self.moveto_y)
                tmep = length_dir(speed, ang)
                self.set_pos(self.x + tmep[0], self.y + tmep[1])
            else :
                self.set_pos(self.moveto_x, self.moveto_y)
                self.state = None
                if self.move_and_remove :
                    self.objectManager.remove_object_in_tick_end(self)
                    self.removed = True
        elif self.state == 'flip' :
            self.flip_progress += self.flip_speed
            if 1 <= self.flip_progress :
                if self.flip_phase == 0 :
                    self.flip_phase = 1
                    self.face_up = not self.face_up
                    self.flip_progress = 0
                else :
                    self.state = None

    def draw(self) :
        rw_x = self.window.RW(self.x)
        rw_y = self.window.RH(self.y)
        rw_width = self.window.RW(self.width)
        rw_height = self.window.RH(self.height)
        rw_width_original = rw_width

        if self.state == 'flip' :
            if self.flip_phase == 0 :
                rw_width *= (1.0 - self.flip_progress)
            else :
                rw_width *= self.flip_progress
            if rw_width <= 0 :
                rw_width = 1

        if (self.tk_image == None) or (self.image_face_up != self.face_up) or ((self.tk_image.width() != round(rw_width)) or (self.tk_image.height() != round(rw_height))) :
            if self.face_up :
                draw_image = self.image
            else :
                draw_image = self.image_back
            self.image_face_up = self.face_up

            temp_image = draw_image.resize((round(rw_width), round(rw_height)), image_resize_mode)
            self.tk_image = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(rw_x + (rw_width_original / 2), rw_y + (rw_height / 2), image=self.tk_image)

class Dealer() :
    def __init__(self, window) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.game_blackjack = None
        self.hand = []
        self.total = 0
        self.flip_all = 0
        self.state = None
        self.total_show = 0
        self.tk_image_text_total = None
        self.total_draw = 0
        self.total_text = 0
        self.font = ImageFont.truetype(font_path['malgunbd'], 48)

    def get_card(self, card, open) :
        if open :
            card.flip(tick_leveling(8))
        self.hand.append(card)
        self.total = self.get_total()
        self.total_show = self.get_total(True)

    def get_total(self, show_only = False) :
        total = 0
        for card in self.hand :
            if show_only and (not card.face_up and (card.state != 'flip')) :
                continue
            if card.rank == 'ace' :
                total += 11
            elif card.rank in ('jack', 'queen', 'king') :
                total += 10
            else :
                total += Card.ranks.index(card.rank) + 1

        return total

    def get_hand(self) :
        return self.hand

    def reset(self) :
        for card in self.hand:
            card.moveto_remove(card.x, -150, tick_leveling(7), self.game_blackjack.objectManager)
        self.total = 0
        self.total_show = 0
        self.flip_all = 0
        self.state = 'reset'

    def logic(self) :
        if self.state == 'reset' :
            if self.hand == list(filter(lambda card: card.removed, self.hand)) :
                self.hand = []
                self.state = None
        elif self.game_blackjack.get_phase() == 'dealer' :
            if self.game_blackjack.player.get_total() > 21 :
                self.game_blackjack.next_phase()
            elif self.game_blackjack.deck.get_state() == None :
                if self.flip_all == 0 :
                    for card in self.hand :
                        if not card.is_face_up() :
                            card.flip(tick_leveling(8))
                    self.flip_all = 1
                    self.total_show = self.get_total(True)
                elif self.flip_all == 1 :
                    if list(filter(lambda card: card.get_state() != None, self.hand)) == [] :
                        self.flip_all = 2
                else :
                    if self.total <= 16 :
                        command = Command('pick', (self, True))
                        self.game_blackjack.deck.add_command(command)
                    elif 17 <= self.total :
                        self.game_blackjack.next_phase()

        if self.total_draw != self.total_show :
            change = (self.total_show - self.total_draw) / tick_leveling(10)
            if tick_leveling_r(0.3) < abs(change) :
                self.total_draw += change
            else :
                self.total_draw = self.total_show

    def draw(self) :
        if (self.tk_image_text_total == None) or ((self.tk_image_text_total.width() != round(self.window.RW(120))) or (self.tk_image_text_total.height() != round(self.window.RH(26)))) or (self.total_text != self.total_draw) :
            text_color_fill = (30,15,5,255)
            if (self.total_show == 21) and (len(self.hand) == 2) :
                total_str = 'BlackJack!'
            else :
                total_str = '<' + str(round(self.total_draw)) + '>'
            image_text = Image.new('RGBA', (240, 57), (255,255,255,0))
            temp = ImageDraw.Draw(image_text)
            tw, th = temp.textsize(total_str, font=self.font)
            temp.text(((240 - tw) / 2, (57 - th) / 2), total_str, font=self.font, fill=text_color_fill)
            temp_image = image_text.resize((round(self.window.RW(120)), round(self.window.RH(26))), image_resize_mode)
            if engine.Propertys.OS == 'Darwin' :
                temp_image = flatten_alpha(temp_image)
            self.tk_image_text_total = ImageTk.PhotoImage(temp_image)
            self.total_text = self.total_draw
        self.canvas.create_image(self.window.RW(400), self.window.RH(206), image=self.tk_image_text_total)

class Player() :
    def __init__(self, window) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.game_blackjack = None
        self.hand = []
        self.total = 0
        self.money = 0
        self.info = None
        self.state = None
        self.auto_play = False
        self.tk_image_text_total = None
        self.total_draw = 0
        self.total_text = 0
        self.font = ImageFont.truetype(font_path['malgunbd'], 48)

    def set_money(self, money) :
        self.money = money

    def set_player_info(self, info) :
        self.info = info

    def get_player_info(self) :
        return self.info

    def get_money(self, money) :
        return self.money

    def set_depth(self, depth) :
        self.depth = depth

    def get_depth(self, depth) :
        return self.depth

    def get_card(self, card, open) :
        if open :
            card.flip(tick_leveling(8))
        self.hand.append(card)
        self.total = self.get_total()
        if 21 <= self.total :
            self.game_blackjack.next_phase()
        #print(self.total)

    def get_total(self) :
        total = 0
        ace = 0
        for card in self.hand :
            if card.rank in ('jack', 'queen', 'king') :
                total += 10
            elif card.rank == 'ace' :
                ace += 1
            else :
                total += Card.ranks.index(card.rank) + 1

        if 0 < ace :
            if total <= 10 :
                total += 11 + (ace - 1)
            else :
                total += ace

        return total

    def reset(self) :
        for card in self.hand :
            card.moveto_remove(card.x, 525, tick_leveling(7), self.game_blackjack.objectManager)
        self.total = 0
        self.money = 0
        self.state = 'reset'

    def hit(self) :
        if self.game_blackjack.get_phase() == 'player' and \
            self.game_blackjack.deck.get_state() == None :
            command = Command('pick', (self, True))
            self.game_blackjack.deck.add_command(command)

    def stay(self) :
        if self.game_blackjack.get_phase() == 'player' and \
            self.game_blackjack.deck.get_state() == None :
            self.game_blackjack.next_phase()

    def deal(self) :
        if self.game_blackjack.get_phase() == 'betting' :
            self.game_blackjack.next_phase()

    def get_hand(self) :
        return self.hand

    def logic(self) :
        if self.state == 'reset' :
            if self.hand == list(filter(lambda card: card.removed, self.hand)) :
                self.hand = []
                self.state = None
        elif self.game_blackjack.get_phase() == 'betting' :
            if self.auto_play :
                bet = random.randrange(1, 81) * 10
                self.game_blackjack.betting_system.add_bet_money(bet)
                self.deal()
        elif self.game_blackjack.get_phase() == 'player' :
            if self.auto_play and (self.game_blackjack.deck.get_state() == None) :
                if self.total <= 16 :
                    self.hit()
                elif 17 <= self.total :
                    self.stay()
        if self.total_draw != self.total :
            change = (self.total - self.total_draw) / tick_leveling(10)
            if tick_leveling_r(0.3) < abs(change) :
                self.total_draw += change
            else :
                self.total_draw = self.total
        
    def draw(self) :
        if (self.tk_image_text_total == None) or ((self.tk_image_text_total.width() != round(self.window.RW(120))) or (self.tk_image_text_total.height() != round(self.window.RH(26)))) or (self.total_text != self.total_draw) :
            text_color_fill = (30,15,5,255)
            if (self.total == 21) and (len(self.hand) == 2) :
                total_str = 'BlackJack!'
            else :
                total_str = '<' + str(round(self.total_draw)) + '>'
            image_text = Image.new('RGBA', (240, 57), (255,255,255,0))
            temp = ImageDraw.Draw(image_text)
            tw, th = temp.textsize(total_str, font=self.font)
            temp.text(((240 - tw) / 2, (57 - th) / 2), total_str, font=self.font, fill=text_color_fill)
            temp_image = image_text.resize((round(self.window.RW(120)), round(self.window.RH(26))), image_resize_mode)
            if engine.Propertys.OS == 'Darwin' :
                temp_image = flatten_alpha(temp_image)
            self.tk_image_text_total = ImageTk.PhotoImage(temp_image)
            self.total_text = self.total_draw
        self.canvas.create_image(self.window.RW(400), self.window.RH(306), image=self.tk_image_text_total)
        
class BettingSystem() :
    def __init__(self, window) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.game_blackjack = None
        self.bet_money = 0
        self.bet_money_draw = 0
        self.x = 0
        self.y = 0
        self.width = 200
        self.height = 80

        self.state = 'betting'
        self.image_betting = Image.open(image_path['betting'])
        self.image_betting_lock = Image.open(image_path['betting_lock'])
        self.tk_image_betting = None
        self.tk_image_text = None
        self.bet_money_text = 0
        self.font = ImageFont.truetype(font_path['RosewoodStd-Regular'], 150)

    def add_bet_money(self, money) :
        success = False
        if (self.game_blackjack.get_phase() == 'betting') and ((self.bet_money + money) <= 1000) :
            self.bet_money += money
            success = True

        return success

    def get_bet_money(self) :
        return self.bet_money

    def set_bet_money(self, money) :
        self.bet_money = money

    def set_depth(self, depth) :
        self.depth = depth

    def get_depth(self, depth) :
        return self.depth

    def set_pos(self, x, y) :
        self.x = x
        self.y = y

    def reset(self) :
        self.bet_money = 0
        self.state = 'betting'
        self.bet_money_text = 0

    def logic(self) :
        if self.bet_money_draw != self.bet_money :
            change = (self.bet_money - self.bet_money_draw) / tick_leveling(10)
            if tick_leveling_r(0.5) < abs(change) :
                self.bet_money_draw += change
            else :
                self.bet_money_draw = self.bet_money

        if self.game_blackjack.get_phase() == 'betting' :
            if self.state != 'betting' :
                self.state = 'betting'
                self.tk_image_betting = None
                self.tk_image_text = None
        elif self.state == 'betting' :
            self.state = 'lock'
            self.tk_image_betting = None
            self.tk_image_text = None

    def draw(self) :
        rw_x = self.window.RW(self.x)
        rw_y = self.window.RH(self.y)
        rw_width = self.window.RW(self.width)
        rw_height = self.window.RH(self.height)

        if (self.tk_image_betting == None) or ((self.tk_image_betting.width() != round(rw_width)) or (self.tk_image_betting.height() != round(rw_height))) :
            if self.state == 'betting' :
                temp_image = self.image_betting
            else :
                temp_image = self.image_betting_lock
            temp_image = temp_image.resize((round(rw_width), round(rw_height)), image_resize_mode)
            self.tk_image_betting = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(rw_x, rw_y, image=self.tk_image_betting)

        if (self.tk_image_text == None) or ((self.tk_image_text.width() != round(rw_width * 0.8)) or (self.tk_image_text.height() != round(rw_height * 0.8))) or (self.bet_money_text != self.bet_money_draw) :
            if self.state == 'betting' :
                text_color_fill = (0,255,255,255)
            else :
                text_color_fill = (255,255,255,255)
            money_str = str(round(self.bet_money_draw)) + '$'
            image_text = Image.new('RGBA', (400, 200), (255,255,255,0))
            temp = ImageDraw.Draw(image_text)
            tw, th = temp.textsize(money_str, font=self.font)
            temp.text(((400 - tw) / 2, (200 - th) / 2), money_str, font=self.font, fill=text_color_fill)
            temp_image = image_text.resize((round(rw_width * 0.8), round(rw_height * 0.8)), image_resize_mode)
            if engine.Propertys.OS == 'Darwin' :   
                temp_image = flatten_alpha(temp_image)
            self.tk_image_text = ImageTk.PhotoImage(temp_image)
            self.bet_money_text = self.bet_money_draw
        self.canvas.create_image(rw_x, rw_y, image=self.tk_image_text)

class Button() :
    def __init__(self, x, y, width, height, window, info, command) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colorMap = {'normal': 'white', 'select': 'gray', 'down': 'black'}
        self.color = self.colorMap['normal']
        self.state = 'normal'
        self.draw_state = 'normal'
        self.window = window
        self.canvas = window.get_canvas()
        self.command = command
        self.type = info[0]
        self.val = info[1]

        if self.type == 'betting' :
            self.image = Image.open(image_path['chip'])
            self.image = flatten_alpha(self.image)
            self.tk_image = None
            self.image_money = Image.open(image_path[self.val])
            self.tk_image_money = None
            self.image_rotate = 0
            self.rotate = 0
        elif self.type in ('hit', 'stay') :
            self.image = Image.open(image_path[self.type])
            self.image_draw = 'normal'
            self.tk_image = None
        elif self.type in ('deal', 'regame', 'exit') :
            self.image = Image.open(image_path[self.type])
            self.image_draw = 'normal'
            self.tk_image = None
            self.moveto_x = self.x
            self.moveto_y = self.y
            self.speed_div = 0
            self.minimum_dis = 2
            self.move_and_remove = False

    def is_inside_point(self, x, y) :
        result = False
        if self.type in ('betting', 'regame', 'exit') :
            radius = self.width / 2
            if distance(self.x + radius, self.y + radius, x, y) <= radius :
                result = True
        else :
            if (self.x <= x <= (self.x + self.width)) and (self.y <= y <= (self.y + self.height)) :
                result = True

        return result

    def moveto(self, x, y, div) :
        self.moveto_x = x
        self.moveto_y = y
        self.speed_div = div
        self.state = 'move'

    def set_pos(self, x, y) :
        self.x = x
        self.y = y

    def set_depth(self, depth) :
        self.depth = depth

    def get_depth(self, depth) :
        return self.depth

    def logic(self) :
        if self.type == 'betting' :
            if self.is_inside_point(self.window.mouse_x, self.window.mouse_y) :
                self.rotate += tick_leveling_r(4)
        elif self.type in ('deal', 'regame', 'exit') :
            if self.state == 'move' :
                dis = distance(self.x, self.y, self.moveto_x, self.moveto_y)
                if self.minimum_dis < dis :
                    speed = dis / self.speed_div
                    ang = get_angle(self.x, self.y, self.moveto_x, self.moveto_y)
                    tmep = length_dir(speed, ang)
                    self.set_pos(self.x + tmep[0], self.y + tmep[1])
                else :
                    self.set_pos(self.moveto_x, self.moveto_y)
                    self.state = 'normal'
                    if self.move_and_remove :
                        self.command()
                        self.val.remove_object_in_tick_end(self)
                return

        if self.window.mouseL_state == 'down' :
            if self.is_inside_point(self.window.mouse_x, self.window.mouse_y) :
                if self.is_inside_point(self.window.mouseL_click_x, self.window.mouseL_click_y) or self.state == 'down' :
                    self.state = 'down'
                    self.draw_state = 'down'
                else :
                    self.draw_state = 'select'
            else :
                self.draw_state = 'normal'
        elif self.window.mouseL_state == 'up' :
            if self.is_inside_point(self.window.mouse_x, self.window.mouse_y) :
                if self.state == 'down' :
                    if self.type == 'deal' :
                        self.draw_state = 'normal'
                        self.move_and_remove = True
                        self.moveto(self.x, 530, tick_leveling(7))
                        return
                    else :
                        self.command()
                self.draw_state = 'select'
            else :
                self.draw_state = 'normal'
            self.state = 'normal'

    def draw(self) :
        rw_x = self.window.RW(self.x)
        rw_y = self.window.RH(self.y)
        rw_width = self.window.RW(self.width)
        rw_height = self.window.RH(self.height)

        if self.type == 'betting' :
            if (self.tk_image == None) or ((self.tk_image.width() != round(rw_width)) or (self.tk_image.height() != round(rw_height))) or (self.image_rotate != self.rotate) :
                temp_image = self.image.rotate(self.rotate)
                if self.draw_state == 'down' :
                    rw_x += rw_width / 10
                    rw_y += rw_height / 10
                    rw_width = rw_width * 0.8
                    rw_height = rw_height * 0.8

                temp_image = temp_image.resize((round(rw_width), round(rw_height)), image_resize_mode)
                self.tk_image = ImageTk.PhotoImage(temp_image)
                self.image_rotate = self.rotate

                temp_image = self.image_money.resize((round(rw_width * 0.8), round((rw_height / 2) * 0.8)), image_resize_mode)
                self.tk_image_money = ImageTk.PhotoImage(temp_image)
            self.canvas.create_image(rw_x + (rw_width / 2), rw_y + (rw_height / 2), image=self.tk_image)
            self.canvas.create_image(rw_x + (rw_width / 2), rw_y + (rw_height / 2), image=self.tk_image_money)
        elif self.type in ('hit', 'stay', 'deal', 'regame', 'exit') :
            if (self.tk_image == None) or ((self.tk_image.width() != round(rw_width)) or (self.tk_image.height() != round(rw_height))) or (self.draw_state != self.image_draw) :
                if self.draw_state == 'down' :
                    rw_x += rw_width * (0.1 / 2)
                    rw_y += rw_height * (0.1 / 2)
                    rw_width = rw_width * 0.9
                    rw_height = rw_height * 0.9
                elif self.draw_state == 'select' :
                    rw_x += rw_width * (-0.05 / 2)
                    rw_y += rw_height * (-0.05 / 2)
                    rw_width = rw_width * 1.05
                    rw_height = rw_height * 1.05

                temp_image = self.image.resize((round(rw_width), round(rw_height)), image_resize_mode)
                self.tk_image = ImageTk.PhotoImage(temp_image)
                self.image_draw = self.draw_state
            self.canvas.create_image(rw_x + (rw_width / 2), rw_y + (rw_height / 2), image=self.tk_image)
        else :
            self.color = self.colorMap[self.draw_state]
            self.canvas.create_rectangle(rw_x, rw_y, rw_x + rw_width, rw_y + rw_height, fill=self.color)

class Table() :
    def __init__(self, window) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.image_table = Image.open(image_path['table'])
        self.tk_image_table = None
        self.x = 0
        self.y = 0
        self.width = 800
        self.height = 520

    def set_depth(self, depth) :
        self.depth = depth

    def get_depth(self, depth) :
        return self.depth

    def logic(self) :
        pass

    def draw(self) :
        rw_x = self.window.RW(self.x)
        rw_y = self.window.RH(self.y)
        rw_width = self.window.RW(self.width)
        rw_height = self.window.RH(self.height)

        if (self.tk_image_table == None) or ((self.tk_image_table.width() != round(rw_width)) or (self.tk_image_table.height() != round(rw_height))) :
            temp_image = self.image_table.resize((round(rw_width), round(rw_height)), image_resize_mode)
            self.tk_image_table = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(rw_x + (rw_width / 2), rw_y + (rw_height / 2), image=self.tk_image_table)

class Bar() :
    def __init__(self, window) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.game_blackjack = None
        self.x = 0
        self.y = 520
        self.width = 800
        self.height = 80

        self.image_bar = Image.open(image_path['bar'])
        self.tk_image_bar = None
        self.image_board = Image.open(image_path['board'])
        self.tk_image_board = None
        self.money_draw = 0
        self.money_text = 0
        self.win_text = 0
        self.draw_text = 0
        self.lose_text = 0
        self.tk_image_text_name = None
        self.tk_image_text_money = None
        self.tk_image_text_record = None
        self.font = ImageFont.truetype(font_path['malgunbd'], 48)

    def set_depth(self, depth) :
        self.depth = depth

    def get_depth(self, depth) :
        return self.depth

    def logic(self) :
        info = self.game_blackjack.player.get_player_info()
        money = info['money']
        if self.money_draw != money :
            change = (money - self.money_draw) / tick_leveling(10)
            if tick_leveling_r(0.5) < abs(change) :
                self.money_draw += change
            else :
                self.money_draw = money
        if (self.win_text != info['win']) or (self.draw_text != info['draw']) or (self.lose_text != info['lose']) :
            self.tk_image_text_record = None

    def draw(self) :
        rw_x = self.window.RW(self.x)
        rw_y = self.window.RH(self.y)
        rw_width = self.window.RW(self.width)
        rw_height = self.window.RH(self.height)
        info = self.game_blackjack.player.get_player_info()

        if (self.tk_image_bar == None) or ((self.tk_image_bar.width() != round(rw_width)) or (self.tk_image_bar.height() != round(self.window.RH(80)))) :
            temp_image = self.image_bar.resize((round(rw_width), round(self.window.RH(80))), image_resize_mode)
            self.tk_image_bar = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(rw_x + (rw_width / 2), round(self.window.RH(560)), image=self.tk_image_bar)

        if (self.tk_image_board == None) or ((self.tk_image_board.width() != round(self.window.RW(280))) or (self.tk_image_board.height() != round(self.window.RH(80)))) :
            temp_image = self.image_board.resize((round(self.window.RW(280)), round(self.window.RH(80))), image_resize_mode)
            self.tk_image_board = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(round(rw_x + (rw_width / 2)), round(self.window.RH(560)), image=self.tk_image_board)

        if (self.tk_image_text_name == None) or ((self.tk_image_text_name.width() != round(self.window.RW(260) * 0.95)) or (self.tk_image_text_name.height() != round(self.window.RH(26) * 0.8))) :
            text_color_fill = (30,15,5,255)
            name_str = "ID: " + info['id']
            image_text = Image.new('RGBA', (520, 52), (255,255,255,0))
            temp = ImageDraw.Draw(image_text)
            tw, th = temp.textsize(name_str, font=self.font)
            temp.text((0, (52 - th) / 2), name_str, font=self.font, fill=text_color_fill)
            temp_image = image_text.resize((round(self.window.RW(260) * 0.95), round(self.window.RH(26) * 0.8)), image_resize_mode)
            if engine.Propertys.OS == 'Darwin' :
                temp_image = flatten_alpha(temp_image)
            self.tk_image_text_name = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(self.window.RW(130), self.window.RH(532), image=self.tk_image_text_name)

        if (self.tk_image_text_money == None) or ((self.tk_image_text_money.width() != round(self.window.RW(260) * 0.95)) or (self.tk_image_text_money.height() != round(self.window.RH(26) * 0.8))) or (self.money_text != self.money_draw) :
            text_color_fill = (30,15,5,255)
            money_str = "Money: " + str(round(self.money_draw)) + '$'
            image_text = Image.new('RGBA', (520, 57), (255,255,255,0))
            temp = ImageDraw.Draw(image_text)
            tw, th = temp.textsize(money_str, font=self.font)
            if 520 < tw :
                money_str = "M: " + str(round(self.money_draw)) + '$'
            temp.text((0, (52 - th) / 2), money_str, font=self.font, fill=text_color_fill)
            temp_image = image_text.resize((round(self.window.RW(260) * 0.95), round(self.window.RH(26) * 0.8)), image_resize_mode)
            if engine.Propertys.OS == 'Darwin' :
                temp_image = flatten_alpha(temp_image)
            self.tk_image_text_money = ImageTk.PhotoImage(temp_image)
            self.money_text = self.money_draw
        self.canvas.create_image(self.window.RW(130), self.window.RH(559), image=self.tk_image_text_money)

        if (self.tk_image_text_record == None) or ((self.tk_image_text_record.width() != round(self.window.RW(260) * 0.95)) or (self.tk_image_text_record.height() != round(self.window.RH(26) * 0.8))) :
            text_color_fill = (30,15,5,255)
            self.win_text = info['win']
            self.draw_text = info['draw']
            self.lose_text = info['lose']
            record_str = "Record: " + str(self.win_text) + ' - ' + str(self.draw_text) + ' - ' + str(self.lose_text)
            image_text = Image.new('RGBA', (520, 52), (255,255,255,0))
            temp = ImageDraw.Draw(image_text)
            tw, th = temp.textsize(record_str, font=self.font)
            if 520 < tw :
                record_str = "R: " + str(self.win_text) + ' - ' + str(self.draw_text) + ' - ' + str(self.lose_text)
            temp.text((0, (52 - th) / 2), record_str, font=self.font, fill=text_color_fill)
            temp_image = image_text.resize((round(self.window.RW(260) * 0.95), round(self.window.RH(26) * 0.8)), image_resize_mode)
            if engine.Propertys.OS == 'Darwin' :
                temp_image = flatten_alpha(temp_image)
            self.tk_image_text_record = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(self.window.RW(130), self.window.RH(583), image=self.tk_image_text_record)

        self.canvas.create_line(self.window.RW(0), self.window.RH(520), self.window.RW(800), self.window.RH(520))
        self.canvas.create_line(self.window.RW(0), self.window.RH(546), self.window.RW(260), self.window.RH(546))
        self.canvas.create_line(self.window.RW(0), self.window.RH(572), self.window.RW(260), self.window.RH(572))
        self.canvas.create_line(self.window.RW(260), self.window.RH(520), self.window.RW(260), self.window.RH(600))
        self.canvas.create_line(self.window.RW(540), self.window.RH(520), self.window.RW(540), self.window.RH(600))

class Cursor() :
    def __init__(self, window) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.x = 0
        self.y = 0
        self.width = 30
        self.height = 30
        self.state = 'normal'
        self.image_cursor = Image.open(image_path['cursor'])
        self.tk_image_cursor = None

    def set_depth(self, depth) :
        self.depth = depth

    def get_depth(self, depth) :
        return self.depth

    def logic(self) :
        self.x = self.window.mouse_x
        self.y = self.window.mouse_y
        if self.window.mouseL_state == 'down' :
            self.state = 'l_down'
        elif self.window.mouseR_state == 'down' :
            self.state = 'r_down'
        else :
            self.state = 'normal'

    def draw(self) :
        rw_x = self.window.RW(self.x)
        rw_y = self.window.RH(self.y)
        rw_width = self.width
        rw_height = self.height

        if (self.tk_image_cursor == None) or ((self.tk_image_cursor.width() != round(rw_width)) or (self.tk_image_cursor.height() != round(rw_height))) :
            temp_image = self.image_cursor.resize((round(rw_width), round(rw_height)), image_resize_mode)
            self.tk_image_cursor = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(round(rw_x + (rw_width / 2)), round(rw_y + (rw_height / 2)), image=self.tk_image_cursor)

class ShowOutcome() :

    def __init__(self, window, outcome, game_blackjack) :
        self.call_pre_logic = False
        self.call_post_logic = False
        self.depth = 0
        self.window = window
        self.canvas = window.get_canvas()
        self.outcome = outcome
        self.game = outcome[0]
        self.player_blackjack = outcome[1]
        self.player_bust = outcome[2]
        self.dealer_blackjack = outcome[3]
        self.dealer_bust = outcome[4]
        self.game_blackjack = game_blackjack
        self.objectManager = game_blackjack.objectManager
        self.x = 0
        self.y = 0
        self.moveto_x = self.x
        self.moveto_y = self.y
        self.speed_div = 0
        self.minimum_dis = 2
        self.move_and_remove = False
        self.state = None
        self.removed = False
        self.image = None
        self.tk_image = None
        self.image_small = None
        self.tk_image_small = None

        if self.game == 'win' :
            self.image = Image.open(image_path['win'])
            if self.dealer_bust :
                self.image_small = Image.open(image_path['d_bs'])
            elif self.player_blackjack :
                self.image_small = Image.open(image_path['p_bj'])
        elif self.game == 'lose' :
            self.image = Image.open(image_path['lose'])
            if self.player_bust :
                self.image_small = Image.open(image_path['p_bs'])
            elif self.dealer_blackjack :
                self.image_small = Image.open(image_path['d_bj'])
        elif self.game == 'draw' :
            self.image = Image.open(image_path['draw'])

    def set_depth(self, depth) :
        self.depth = depth

    def get_depth(self, depth) :
        return self.depth

    def moveto(self, x, y, div) :
        self.moveto_x = x
        self.moveto_y = y
        self.speed_div = div
        self.state = 'move'

    def set_pos(self, x, y) :
        self.x = x
        self.y = y

    def logic(self) :
        if self.state == 'move' :
            dis = distance(self.x, self.y, self.moveto_x, self.moveto_y)
            if self.minimum_dis < dis :
                speed = dis / self.speed_div
                ang = get_angle(self.x, self.y, self.moveto_x, self.moveto_y)
                tmep = length_dir(speed, ang)
                self.set_pos(self.x + tmep[0], self.y + tmep[1])
            else :
                self.set_pos(self.moveto_x, self.moveto_y)
                self.state = None
                if self.move_and_remove :
                    self.objectManager.remove_object_in_tick_end(self)
                    self.removed = True
            return

        if self.game_blackjack.get_phase() not in ('result', 'select') :
            self.move_and_remove = True
            self.moveto(self.x, -100, tick_leveling(7))


    def draw(self) :
        rw_x = self.window.RW(self.x)
        rw_y = self.window.RH(self.y)

        if (self.image_small != None) and ((self.tk_image_small == None) or ((self.tk_image_small.width() != round(self.window.RW(self.image_small.size[0]))) or (self.tk_image_small.height() != round(self.window.RH(self.image_small.size[1]))))) :
            temp_image = self.image_small.resize((round(self.window.RW(self.image_small.size[0])), round(self.window.RH(self.image_small.size[1]))), image_resize_mode)
            self.tk_image_small = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(round(rw_x), round(rw_y - self.window.RH(80)), image=self.tk_image_small)

        if (self.tk_image == None) or ((self.tk_image.width() != round(self.window.RW(self.image.size[0]))) or (self.tk_image.height() != round(self.window.RH(self.image.size[1])))) :
            temp_image = self.image.resize((round(self.window.RW(self.image.size[0])), round(self.window.RH(self.image.size[1]))), image_resize_mode)
            self.tk_image = ImageTk.PhotoImage(temp_image)
        self.canvas.create_image(round(rw_x), round(rw_y), image=self.tk_image)


class RecordManager() :
    def get_userList() :
        result = []
        if os.path.isfile("users.txt") :
            file = open("users.txt", 'r')
            while True:
                line = file.readline()
                if not line :
                    break
                s = line.split()
                temp = {'id': s[0], 'money': int(s[1]), 'win': int(s[2]), 'draw': int(s[3]), 'lose': int(s[4])}
                result.append(temp)
            file.close()

        return result

    def save_user_record(record) :
        user_list = RecordManager.get_userList()
        new_user = True
        for idx, val in enumerate(user_list) :
            if val['id'] == record['id'] :
                user_list[idx] = record
                new_user = False
                break
        if new_user :
            user_list.append(record)

        file = open("users.txt", 'w')
        for x in user_list :
            temp = x['id'] + ' ' + str(x['money']) + ' ' + str(x['win']) + ' ' + str(x['draw']) + ' ' + str(x['lose']) + '\n'
            file.write(temp)
        file.close()

class LoginWindow() :
    def __init__(self) :
        self.__master = tkinter.Tk()
        self.master.title("Login")
        self.master.iconbitmap(image_path['icon'])
        self.window_size = "470x250"
        if engine.Propertys.OS == 'Darwin' :
            self.window_size = "532x265"
        self.master.geometry(self.window_size)
        self.master.resizable(False, False)
        self.user_info = None
        self.auto_play = tkinter.BooleanVar()
        self.auto_regame = tkinter.BooleanVar()

        self.frame = tkinter.Frame(self.master, width=self.master.winfo_width(), height=self.master.winfo_height())
        self.frame.grid()

        vcmd = (self.master.register(self.validate), '%d', '%P')
        self.labelframe_login = tkinter.LabelFrame(self.frame, text='Login', width=300, height=100)
        self.labelframe_login.grid(row=0, column=0, rowspan=4, columnspan=2, padx=10, pady=10)
        self.labelframe_ranking = tkinter.LabelFrame(self.frame, text='Ranking', width=195, height=228)
        self.labelframe_ranking.grid(row=0, column=2, rowspan=4, columnspan=2, padx=10, pady=10)

        self.canvas = tkinter.Canvas(self.frame, width=200, height=120)
        self.image_login = Image.open(image_path['login'])
        self.image_login = self.image_login.resize((190,119), image_resize_mode)
        self.tk_image_login = ImageTk.PhotoImage(self.image_login)
        self.text_ID = tkinter.Label(self.frame, text="ID :")
        self.entry_ID = tkinter.Entry(self.frame, validate = 'key',width=23, validatecommand = vcmd)
        self.button_OK = tkinter.Button(self.frame, text="OK", width=25, command=self.login)
        self.checkbutton_auto_play = tkinter.Checkbutton(self.frame, text="Auto Play", variable=self.auto_play, onvalue=True, offvalue=False)
        self.checkbutton_auto_regame = tkinter.Checkbutton(self.frame, text="Auto ReGame", variable=self.auto_regame, onvalue=True, offvalue=False)
        self.entry_ID.bind('<Return>', lambda x: self.login())
        
        self.canvas.grid(in_=self.labelframe_login, row=0, column=0, columnspan=2, padx=5)
        self.text_ID.grid(in_=self.labelframe_login, row=1, column=0, columnspan=2, sticky='W', padx=10)
        self.entry_ID.grid(in_=self.labelframe_login, row=1, column=0, columnspan=2, sticky='E', padx=10, pady=5)
        self.checkbutton_auto_play.grid(in_=self.labelframe_login, row=2, column=0, columnspan=2, sticky='W', padx=10)
        self.checkbutton_auto_regame.grid(in_=self.labelframe_login, row=2, column=0, columnspan=2, sticky='E', padx=10)
        self.button_OK.grid(in_=self.labelframe_login, row=3, column=0, columnspan=2, padx=10, pady=6, sticky='WE')

        ranking_str = '=========================\n'
        temp = RecordManager.get_userList()
        temp.sort(key=lambda record: record['money'], reverse=True)
        if 10 < len(temp) :
            temp = temp[:10]
        for idx, val in enumerate(temp) :
            ranking_str += str(idx + 1) + '위. ' + val['id'] + ' (' + str(val['money']) + '$)' + '\n'
        ranking_str += '========================='
        self.text_renk = tkinter.Label(self.frame, text=ranking_str, anchor='n', width=29, height=14)
        self.text_renk.grid(in_=self.labelframe_ranking, row=0, column=2, padx=0)

        self.canvas.create_image(95, 60, image=self.tk_image_login)

    def login_str_len_check(str) :
        l = 0
        for x in str:
            if x in "abcdefghijklmnopqrstuvwxyz0123456789_" :
                l += 0.75
            else :
                l += 1
        return round(l) <= 9

    def validate(self, action, text) :
        if (action == '0') or ((len(text) <= 15) and (' ' not in text) and LoginWindow.login_str_len_check(text)) :
            return True
        else :
            return False

    def login(self) :
        ID = self.entry_ID.get()
        if ID == '' :
            return

        userList = RecordManager.get_userList()
        for user in userList:
            if user['id'] == ID :
                self.user_info = user
                break
        if self.user_info == None :
            temp = {'id': ID, 'money': 1000, 'win': 0, 'draw': 0, 'lose': 0}
            RecordManager.save_user_record(temp)
            self.user_info=temp

        self.master.destroy()

    def get_user_info(self) :
        return self.user_info

    def start_main_loop(self) :
        self.master.mainloop()

    @property
    def master(self) :
        return self.__master

def main() :
    login = LoginWindow()
    login.start_main_loop()
    user_info = login.get_user_info()
    auto_play = login.auto_play.get()
    auto_regame = login.auto_regame.get()
    if user_info == None :
        exit()

    #=================================== Login

    engine.Propertys.set_tps(30) # Game logic processing speed setting
    engine.Propertys.set_fps(30) # Game screen render speed setting
    engine.Propertys.set_speed_factor(1) # Game speed factor setting
    engine.Propertys.set_tick_delay(5) # Game main loop delay setting
    engine.Propertys.set_show_fps(True) # Show render FPS in title bar

    window = engine.MainWindow()
    window.set_title("BackJack")
    window.master.iconbitmap(image_path['icon'])
    window.master.config(cursor="none")

    objectManager = engine.ObjectManager()
    game = engine.Game(objectManager)
    window.set_game_object(game)

    game_blackjack = Game_BlackJack(window, objectManager)
    game_blackjack.auto_regame = auto_regame
    player = Player(window)
    player.set_depth(10)
    player.auto_play = auto_play
    player.set_player_info(user_info)
    dealer = Dealer(window)
    deck = Deck(window)
    deck.set_depth(1)
    deck.set_pos(655, 180)
    bar = Bar(window)
    bar.set_depth(-15)
    betting_system = BettingSystem(window)
    betting_system.set_pos(400, 260)
    betting_system.set_depth(10)
    table = Table(window)
    table.set_depth(20)
    cursor = Cursor(window)
    cursor.set_depth(-100)

    game_blackjack.set_player(player)
    game_blackjack.set_dealer(dealer)
    game_blackjack.set_deck(deck)
    game_blackjack.set_bar(bar)
    game_blackjack.set_betting_system(betting_system)

    button_hit = Button(280, 530, 115, 60, window, ('hit', None), lambda: player.hit() if not auto_play else None)
    button_hit.set_depth(-20)
    button_stay = Button(405, 530, 115, 60, window, ('stay', None), lambda: player.stay() if not auto_play else None)
    button_stay.set_depth(-20)
    button_bet_100 = Button(550, 525, 70, 70, window, ('betting', '100'), lambda: betting_system.add_bet_money(100) if not auto_play else None)
    button_bet_100.set_depth(-20)
    button_bet_50 = Button(635, 525, 70, 70, window, ('betting', '50'), lambda: betting_system.add_bet_money(50) if not auto_play else None)
    button_bet_50.set_depth(-20)
    button_bet_10 = Button(720, 525, 70, 70, window, ('betting', '10'), lambda: betting_system.add_bet_money(10) if not auto_play else None)
    button_bet_10.set_depth(-20)

    objectManager.add_object(game_blackjack)
    objectManager.add_object(player)
    objectManager.add_object(dealer)
    objectManager.add_object(deck)
    objectManager.add_object(betting_system)
    objectManager.add_object(button_hit)
    objectManager.add_object(button_stay)
    objectManager.add_object(button_bet_100)
    objectManager.add_object(button_bet_50)
    objectManager.add_object(button_bet_10)
    objectManager.add_object(table)
    objectManager.add_object(bar)
    objectManager.add_object(cursor)

    window.start_main_loop()


main()