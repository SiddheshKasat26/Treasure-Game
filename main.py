print('''
                                           o         _ _ _ _ _
                                                _----|         I-I-I-I-I
                             _ _ _ _ _ _      o  ----|     o   \~~`~'~~/
                             ]-I-I-I-I-[ _----|      |_----|    |.    |
                             \~`\~~~/'~/  ----|     / \----|    |  /^\|
                              [*] ' __|       ^    / ^ \   ^    |_ |*||
                              |__    ,|      / \  /    `\ / \   |  ===|
                            __|  ___ ,|__   /    /=_=_=_=\   \  |,  __|
                            I_I__I_I__I_I  (====(_________)___|_|_____|___
                            \-\--|-|--/-/  |'    I~~[ ]~~I I_I__|IIII|_I_l
                             | [ ]    '|   | [~] |_`_~_ _[  \-\--|-|--/-/
                             |.   | |' |___|____`I_I_|_I_I___|---------|
                            / \| [] ~ .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
                           <===>  |  ~.|-=-=-=-=-=-=-=-=-=-=-|~  |  ~ / \
                           | []|`   []~||.|.|.|.|.|.|.|.|.|.||-~   ~ <===>
   O O      o o            | []| ` |   |/////////I\\\\\\\\\\||__. ~| |[*]I
  O * O    o * o           <===> ~   ' ||||| |   |   | ||||.||  []  ~<===>
   O O      o o             \T/  |~|-- ||||| | O | O | ||||.|| . |'~  \T/
   \I        I/              |     ~.~_||||| |~~~|~~~| ||||.|| | ~   | |
____I/______\I____\/..___.../|' v . | .|||||/____|____\|||| /|. . | . .|\.\/_
''')
Player = input("What is your name? ")
print("Welcome to the CASTLE.")
print("Your mission is to find the treasure which is hidden inside the Castle.")

ans = input("Are you ready? Y or N. ")
if ans == 'Y':
    print(f"All The Best {Player}👍.We hope you find the TREASURE 🤞.")
    print("So, Let's Begin💪 -->")
    print("You are at Main Door, and in front of you there are 5 rooms.(Room names are 1,2,3 and 4.)")
    room_number = int(input(f"Which room do you want to go {Player}? 1 2 3 4 => "))
    if room_number == 1:
        print("Sorry, You Died by falling in hole which was full of spikes😔.\nBETTER LUCK NEXT TIME👍")
    elif room_number == 2:
        room2 = input("Nice Choice! Now, which room you want to choose? Left or Right.(Type Left or Right only!) ")
        if room2 == "Left":
            print("Sorry, You Died here because LION ate you🦁.\nBETTER LUCK NEXT TIME👍")
        else:
            print("Sorry, You Died here because this room is FULL of Electricity(1000 Volts)🔌⚡💥😵.\nBETTER LUCK NEXT TIME👍")
    elif room_number == 3:
        print("Sorry, You Died in the room where there are more than 100 poisonous snakes🐍.\nBETTER LUCK NEXT TIME👍")
    elif room_number == 4:
        room4 = input("Nice Choice! Now, which room you want to choose? Left or Right.(Type Left or Right only!) ")
        if room4 == "Left":
            print("Sorry, You Died here because this room is full of DYNAMITES🧨.\nBETTER LUCK NEXT TIME👍")
        else:
            print(f"HURRAY!,You Did it {Player}🎉🎉🎉🎉🎉🎉.The room of Treasure is now yours💰💰💰💰💰💰.")
elif ans == 'N':
    print("Sorry to see you go, Please visit again.\nThis game is FUN!!!😀")
else :
    print("Ohh! You entered a wrong key. Try again!")
