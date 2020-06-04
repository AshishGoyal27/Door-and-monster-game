import random
def doors():
  print(''' 
_____1_____    _____2____   _____3_____
|  __  __  |  |  __  __  |  |  __  __  |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |__||__| |  | |__||__| |  | |__||__| |
|  __  __()|  |  __  __()|  |  __  __()|
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |  ||  | |  | |  ||  | |  | |  ||  | |
| |__||__| |  | |__||__| |  | |__||__| |
|__________|  |__________|  |__________|''')

def monster():
	print('''
        .-""-"-""-.
       | .--.-.--. |
       |` >       `|
       | <         |
       (__..---..__)
      (`|\o_/ \_o/|`)
       \(    >    )/
     [>=|   vvv   |=<]
        \__\   /__/
            '-'
 ''')
print('Halloween Game')

print('Avoid the monster!')

print('Three doors ahead...')
def game():
    doors()
    monsterDoor = random.randint(1, 3)
    print('Is the Monster behind door..')
    userDoor = int(input ('1,2, or 3?'))
    if userDoor ==  monsterDoor:
        print(' ARGHHH! MONSTER')
        monster()
    else:
        print('Phew! No Monster!')
        print('You enter the next room. ')
        print('Again Three doors ahead')
        game()
game()
