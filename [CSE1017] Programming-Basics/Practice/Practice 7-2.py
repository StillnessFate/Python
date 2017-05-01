def gugudan1() :
	for y in range(2, 10) :
		for x in range(2, 10) :
			print(str(y) + ' x ' + str(x) + ' = ' + str(x * y).rjust(2), end = '  ')
			if x == 5 :
				print()
		print('\n')

def gugudan2() :
	for y in range(2, 10) :
		for x in range(2, 6) :
			print(str(x) + ' x ' + str(y) + ' = ' + str(x * y).rjust(2), end = '  ')
			if x == 5 :
				print()

	print()

	for y in range(2, 10) :
		for x in range(6, 10) :
			print(str(x) + ' x ' + str(y) + ' = ' + str(x * y).rjust(2), end = '  ')
			if x == 9 :
				print()

t = input("Type of Gugudan[Horizontal, Vertical]:")
print()
if(t == "Horizontal") :
	gugudan1()
elif(t == "Vertical") :
	gugudan2()
else :
	print("Neither horizontal of vertical")