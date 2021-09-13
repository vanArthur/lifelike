import LifeLike_color
import LifeLikeMazeClass

import threading, random, time, shelve, os

debug = False

search_places = ["street", "laundromat", "dumpster", "dog", "mailbox", "car", "coat", "shoe", "sewer", "bed", "purse", "couch", "discord", "pocket", "hospital", "grass", "dresser", "attic","tree"]
beg_people = ["Logan Paul", "David Dobrik", "PewDiePie", "Felix Kjellberg", "Elon Musk", "JJ Olatunji", "KSI", "Deji", "Big Shack", "Bill Gates", "Tommyinit"]
slots_emojis  = ['💛', '💗', '💜', '💙', '💝', '💚', '💔', '🔱', '💖', '💛', '💗', '💜', '💙', '💝', '💚', '💔', '🔱', '💖','💛', '💗', '💜', '💙', '💝', '💚', '💔', '🔱', '💖']

shop = {"Hunting Rifle": 15000, "Laptop": 1500, "Fishing Pole": 15000, "Drivers License": 2500, "Camera": 4000, "Microphone": 1000}
notinshop = {"Hunting Rifle": 15000, "Laptop": 1500, "Fishing Pole": 15000,"Drivers License": 2500,"Camera": 4000, "Microphone": 1000,"Skunk": 120, "Rabbit": 180, "Duck": 600, "Deer":900, "Boar":1500, "Dragon": 12000, "Fish": 400, "Rare Fish": 1600, "Exotic Fish": 7000, "Legendary Fish": 9000}


#save the inventory of the player
def save_inv():
    shelvefile = shelve.open('save_game')
    shelvefile['inventory'] = inventory
    shelvefile['illegal_license'] = illegal_license
    shelvefile.close()

#get the inventory from the save file
shelvefile = shelve.open('save_game')
inventory = shelvefile["inventory"]
illegal_license = shelvefile["illegal_license"]
shelvefile.close()

#all the delays at 0s at start
search_delay = 0
beg_delay = 0
gamble_delay = 0
slots_delay = 0
meme_delay = 0
upload_delay = 0
hunt_delay = 0
drive_delay = 0
fish_delay = 0


## NOTE: search function
def search(wallet, bank):
    global search_delay
    if search_delay == 0:
        random.shuffle(search_places)
        print("")
        print('     Where do you want to search?')
        print("     ",LifeLike_color.BOLD ,search_places[0],", " ,search_places[1],", " ,search_places[2], LifeLike_color.END)
        print("")
        print("     ", end="")
        user_choise = input("I choose: ")
        if str(user_choise) == search_places[0] or user_choise == search_places[1] or user_choise == search_places[2]:
            if user_choise in ("street", "mailbox", "car", "purse"):
                if random.randint(1,2) == 1:
                    if wallet < 300 and bank < 300:
                        print("     You coulnt pay the fine, the cops beat you to death.")
                        print("     You lost all the coins in your wallet.")
                        if debug == False: search_delay = 30
                        return wallet * -1
                    fine = random.randint(100, 300)
                    print("     The",LifeLike_color.DBLUE,LifeLike_color.BOLD,"cops",LifeLike_color.END,"spotted you, you paid them ", LifeLike_color.BOLD ,fine, LifeLike_color.END, " coins.")
                    if debug == False: search_delay = 30
                    return fine * -1
            gain = random.randint(0, 500)
            if gain > 280 and random.randint(1,3) in (1,2):
                gain -= random.randint(100, 150)
            if random.randint(1, 5) == 1:
                print("")
                print('     You didnt find anything, better luck next time!')
                if debug == False: search_delay = 30
                return 0
            print("")
            print("     You searched the ", user_choise, " and found ",LifeLike_color.BOLD, gain,LifeLike_color.END, " coins!" )
            if debug == False: search_delay = 30
            return gain
        else:
            print("")
            print('     That is not an option bitch boy!')
            if debug == False: search_delay = 30
            return 0
    else:
        print("   You need to wait ", search_delay, " more seconds!")
        return 0

## NOTE: beg function
def beg():
    global beg_delay
    if beg_delay == 0:
        preBegGain = random.randint(1,5)
        if preBegGain < 3:
            begGain = random.randint(0, 500)
        else: begGain = random.randint(0, 100)

        print("   ", LifeLike_color.DGREEN, beg_people[random.randint(0,10)],LifeLike_color.END, "gave you",LifeLike_color.BOLD, begGain, LifeLike_color.END, "coins!" )
        if debug == False: beg_delay = 30
        return begGain
    else:
        print(LifeLike_color.RED, LifeLike_color.BOLD,"You asked me ", (30 - beg_delay), " seconds ago, leave me alone!", LifeLike_color.END)
        print("   You need to wait ", beg_delay, " more seconds!")
        return 0

## NOTE: gamble function
def gamble(parse_command, bank):
    global gamble_delay
    if gamble_delay == 0:
        print('')
        if len(parse_command) < 3:
            print('     You must specify a amount to gamble with!')
            return 0
        elif isinstance(parse_command[2], int) == False:
            print("     Not a valid amount, please use: max, half or an integer!")
            return 0

        investment = parse_command[2]
        if investment < 100:
            print("     You barely have any money to gamble with, come back with altleast 100!")
            print("     You have ",bank, " in your bank. Keep in mind, if u lose u lose!" )
            return 0
        else:
            user = random.randint(1, 12)
            print("     User rolled:    ",user)
            cpu = random.randint(1, 12)
            print("     Machine rolled: ",cpu)

            if user > cpu:
                multiplier = random.randint(15, 25) / 10
                print(LifeLike_color.GREEN, LifeLike_color.BOLD, '    User won!', LifeLike_color.END)
                won = int(("{:.0f}".format(investment * multiplier))) - investment
                print("     You won ", won)
                if debug == False: gamble_delay = 10
                return won

            elif user == cpu:
                print(LifeLike_color.YELLOW, LifeLike_color.BOLD, '   Its a tie', LifeLike_color.END)
                loss = investment / 4
                print('     U lost: ', int(("{:.0f}".format(loss))))
                if debug == False: gamble_delay = 10
                return  int("{:.0f}".format(loss)) * -1
            else:
                print(LifeLike_color.RED, LifeLike_color.BOLD,'   user lost ',investment,' coins', LifeLike_color.END)
                if debug == False: gamble_delay = 10
                return investment * -1
    else:
        print("   You need to wait ", gamble_delay, " more seconds!")
        return 0

## NOTE: slots function
def slots(parse_command, bank):
    global slots_delay
    if slots_delay == 0:
        if len(parse_command) < 3:
            print('     You must specify a amount to play slots!')
            return 0
        elif isinstance(parse_command[2], int) == False:
            print("     Not a valid amount, please use: max, half or an integer!")
            return 0

        investment = parse_command[2]
        if investment < 100:
            print("     You barely have any money to play slots, come back with altleast 100!")
            print("     You have ",bank, " in your bank. Keep in mind, if u lose u lose!" )
            return 0
        else:
            random.shuffle(slots_emojis)
            print('')
            print("   ", slots_emojis[0], slots_emojis[1], slots_emojis[2])

            if slots_emojis[0] == slots_emojis[1] == slots_emojis[2]:
                multiplier = random.randint(20, 40) / 10
                print(LifeLike_color.GREEN, LifeLike_color.BOLD, '   User won!', LifeLike_color.END)
                won = int(("{:.0f}".format(investment * multiplier))) - investment
                print("  You won ", won)
                if debug == False: slots_delay = 10
                return won
            elif slots_emojis[0] == slots_emojis[1] or slots_emojis[0] == slots_emojis[2] or slots_emojis[1] == slots_emojis[2]:
                multiplier = random.randint(20, 35) / 10
                print(LifeLike_color.GREEN, LifeLike_color.BOLD, '    User won!', LifeLike_color.END)
                won = int(("{:.0f}".format(investment * multiplier))) - investment
                print("  You won ", won)
                if debug == False: slots_delay = 10
                return won
            else:
                print(LifeLike_color.RED, LifeLike_color.BOLD,'  user lost ',investment,'coins',  LifeLike_color.END)
                if debug == False: slots_delay = 10
                return investment * -1
    else:
        print("   You need to wait ", slots_delay, " more seconds!")
        return 0

## NOTE: post a meme if u have a laptop in inventory
def postmeme():
    global meme_delay
    if meme_delay == 0:
        if inventory.count("Laptop") != 0:
            print(LifeLike_color.BOLD)
            print(" ",LifeLike_color.UNDERLINE, "What type of meme do you want to post?")
            print(LifeLike_color.END, LifeLike_color.BOLD, end="")
            print("    n: ■ Normie Meme")
            print("     e: ■ Edgy Meme")
            print("     r: ■ Repost Meme")
            print("     d: ■ Dank Meme", LifeLike_color.END)
            userInput = input(" --> ")
            print("")
            if userInput == "n":
                print("     You posted a fucking Normie Meme!!!")
                print('     What are you?')
                print('     A bitchboy???!')
            elif userInput == "e":
                print('     You posted a Edgy Meme')
                print("     You better hope it's not too edgy.")
                print("     Or do you WANT to get canceled?")
            elif userInput == "r":
                print('     You posted a Repost Meme')
                print("     A scummy move, but it could get many upvotes!")
            elif userInput == "d":
                print('     You posted a Dank Meme!!')
                print('     You are a real one!')
            else:
                print('Not an options bitchboy !')

            gain = random.randint(0, 1000)
            print('')
            print('     You posted a meme and got ',LifeLike_color.BOLD, gain,LifeLike_color.END, " coins" )
            print("     from the ad revenue!")
            if debug == False: meme_delay = 60
            return gain
        else:
            print("")
            print("     You dont have a Laptop.")
            print("     You can buy one from the shop!")
            print("     Use pls shop and pls buy!")
            return 0
    else:
        print("   You need to wait ", meme_delay, " more seconds!")
        return 0## NOTE: hunt if hunting rifle is in inventory
## NOTE: pls upload command
def upload():
    global upload_delay
    if upload_delay == 0:
        if inventory.count("Laptop") != 0 and inventory.count("Camera") != 0 and inventory.count("Microphone") != 0:
            categorys = ["Gaming Videos", "Vlogs", "Unboxing Videos", "Educational Videos", "Comedy Videos", "Tutorials", "Reviews"]
            print("     What type of video do you want to make?")
            random.shuffle(categorys)
            for index,category in enumerate(categorys):
                print(index, ": ", category, sep="")
            p_input = input("     Type a number: ")

            try:
                p_input = int(p_input)
            except:
                print("     Invalid input! Did you type a number?")
                if debug == False:upload_delay = 150
                return 0

            for i, category in enumerate(categorys):
                if p_input == i:
                    chosen_category = category
                    print("")
                    print("     recording")
                    print("")
                    for r in range(21):
                        progress = "#" * r
                        os.system('cls' if os.name=='nt' else 'clear')
                        for t in range(15):
                            print("")
                        print(LifeLike_color.BOLD, "   Recordig", chosen_category, LifeLike_color.END)
                        print(progress)
                        print(" " * len(progress), end="")
                        print(len(progress) * 5, "%", sep="")
                        time.sleep(0.2)
                    random.shuffle(categorys)
                    print(LifeLike_color.BOLD, "What is popular today: ", LifeLike_color.END)
                    for c,d in enumerate(categorys):
                        spacer = " " * (20 - len(d))
                        print(LifeLike_color.GREEN,d,spacer,"CPM: +",abs(c-6), LifeLike_color.END,sep="")
                    multiplier = abs((int(categorys.index(chosen_category)) - 3)-6)

                    views = random.randint(0, 10)

                    if views in (0,1, 2):
                        views = 0
                    elif views in (3,4,5, 6):
                        views = random.randint(0,10000)
                    elif views in (7,8, 9):
                        views = random.randint(0,100000)
                    else:
                        views = random.randint(0,1000000)
                    print('')
                    print("     A day has passed and you got",views,"views" )
                    print("     with an avarage CPM of ", multiplier, "!", sep="")
                    print(LifeLike_color.GREEN)
                    print("The ads on your video made you",LifeLike_color.BOLD, int("{:.0f}".format((views / 1000) * multiplier)), "coins!", LifeLike_color.END)
                    if debug == False:upload_delay = 300
                    return int("{:.0f}".format((views / 1000) * multiplier))

            print("     Invalid input! Did you type a number?")
            if debug == False:upload_delay = 150
            return 0
        else:
            print("")
            print("     You dont have a Laptop and/or a Camera and/or a Microphone")
            print("     You can buy them from the shop!")
            print("     Use pls shop and pls buy!")
            if debug == False:upload_delay = 150
            return 0
    else:
        print("   You need to wait ", upload_delay, " more seconds!")

        return 0
## NOTE: hunt if hunting rifle is in inventory

def hunt():
    global hunt_delay
    if hunt_delay == 0:
        if inventory.count("Hunting Rifle") != 0:
            randomHunt = random.randint(1, 130)
            if randomHunt <= 60:
                inventory.append("Skunk")
                item = "Skunk"
            elif randomHunt <= 90:
                inventory.append("Rabbit")
            elif randomHunt <= 105:
                inventory.append('Duck')
                item = "Duck"
            elif randomHunt <= 112:
                inventory.append("Deer")
                item = "Deer"
            elif randomHunt <= 116:
                inventory.append("Boar")
                item = "Boar"
            elif randomHunt <= 118:
                inventory.append("Dragon")
                item = (LifeLike_color.RED, "!======> Dragon <======!", LifeLike_color.END)

            else:
                print("     You hunted, but came back empty handed!")
                if debug == False:hunt_delay = 60
                return
            print("")
            save_inv()
            print("     You went hunting and brought back a", LifeLike_color.BOLD, item ,"!", LifeLike_color.END)
        else:
            print("")
            print("     How are you going to hunt without a", LifeLike_color.DBLUE,"Hunting Rifle?", LifeLike_color.END)
            print("     You can buy a Rifle from the shop!")
            print('     Use pls shop and pls buy!')
        if debug == False:hunt_delay = 60
    else:
        print("   You need to wait ", hunt_delay, " more seconds!")
        return

## NOTE: fish command if fishing rod in inventory
def fish():
    global fish_delay
    global inventory
    temp = []
    if fish_delay == 0:
        if inventory.count("Fishing Pole") > 0:
            rand = random.randint(1, 23)
            count = random.randint(1,4)
            if rand <= 12:
                while count != 0:
                    count -= 1
                    temp.append("Fish")
            elif rand <=15:
                temp.append("Rare Fish")
            elif rand <=17:
                temp.append("Exotic Fish")
            elif rand <=18:
                temp.append("Legendary Fish")
            else:
                print("     You went fishing but you didn't catch anything.")
                print("     How disappointing!")
                if debug == False: fish_delay = 45
                return
            print("""
                        __
                      //  |
                     //   |
                    //    |
                   //     |
                  //      |
                 //       ¿
                //""")
            item = temp[0]
            count = temp.count(item)
            if debug == False: fish_delay = 45
            for each in temp:
                inventory.append(each)
            temp = []
            print("You went fishing and caught" ,count, "fricking ", LifeLike_color.DGREEN, item, LifeLike_color.END)
            save_inv()
        else:
            print("")
            print("     How are you going to hunt without a", LifeLike_color.DBLUE,"Fishing Pole?", LifeLike_color.END)
            print("     You can buy a Fishing Pole from the shop!")
            print('     Use pls shop and pls buy!')
    else:
        print("   You need to wait ", fish_delay, " more seconds!")

    if debug == False: fish_delay = 45
    return
## NOTE: play the maze gamble
def playmaze(keyboardLayout):
    mzgame = LifeLikeMazeClass.maze(50, 25, 5, keyboardLayout)
    mzgame.generateGrid()
    mzgame.mazeGame()
    return mzgame.score * 10

## NOTE: open the plsinventory
def openinv():
    global inventory
    last = ""
    inventory = sorted(inventory, key=str.lower)
    if not inventory:
        print("")
        print("     Your inventory is empty.")
        print("     Go and buy something from the shop!")
        print("     Use: pls shop and pls buy")
    else:
        print("   ==========================================================")
        for item in inventory:
            if last != item:
                spacerLength = len(item)
                firstspacenLenght = len(str(inventory.count(item)))
                print("     ",inventory.count(item)," "* (3 - firstspacenLenght) ,item, " " * (15-spacerLength), "Sell Value: ", ("{:.0f}".format(notinshop[item]/3)))
            last = item
        print("   ==========================================================")
## NOTE: open the plsshop
def openshop():
    print("   ==========================================================")
    for item in shop:
        spacerLength = len(item)
        secspacerLength = len(str(shop[item]))
        print("     ",item, " " * (15-spacerLength) ,"Price: ",shop[item], " " * (5 - secspacerLength) , "Sell Value: ", ("{:.0f}".format(shop[item]/3)))
    print("   ==========================================================")

## NOTE: buy item from plsshop
def buy(buyingItem, wallet):
    global inventory
    for item in shop:
        if item.lower() == buyingItem.lower():
            if wallet >= shop[item]:
                inventory.append(item)
                inventory = sorted(inventory, key=str.lower)
                print('     Succesfully bought', LifeLike_color.DBLUE, item, LifeLike_color.END)
                save_inv()
                return int(("{:.0f}".format(shop[item])))
            else:
                print('')
                print("     You dont have enough money in your wallet!")
                print("     To buy this item you need", LifeLike_color.BOLD, ("{:.0f}".format(shop[item])), LifeLike_color.END)
                return 0
    print("")
    print("     We do not sell ", LifeLike_color.BOLD ,buyingItem, sep="")
    print("     Use pls shop, to see what we do sell!")
    return 0

## NOTE: selling items from your inv
def sell(command):
    tempcommand = []
    count = 1
    max = False
    sellItem = ""
    for each in command:
        if str(each).isnumeric():
            count = int(each)
        elif each in ("max"):
            max = True
        else:
            tempcommand.append(each)
    preSellItem = " ".join(tempcommand)
    for each in inventory:
        if each.lower() == preSellItem.lower():
            if max: count = inventory.count(each)
            if count > inventory.count(each):
                print("     You don't have ", count, " of that item!")
                return 0
            sellItem = each
    countNC = count
    if sellItem == "":
        print("     You dont have that in your inventory!")
        return 0
    gain = int(("{:.0f}".format(count * (notinshop[sellItem] / 3))))
    while count != 0:
        count -= 1
        inventory.remove(sellItem)
    print("     ", LifeLike_color.DGREEN, "You sold ", countNC," ", sellItem, "and got ", gain, " coins!", LifeLike_color.END)
    save_inv()
    return gain

## NOTE: drive past the delays
def road(roadLength, delay):
    global illegal_license
    global search_delay
    global beg_delay
    global gamble_delay
    global slots_delay
    global meme_delay
    global upload_delay
    global hunt_delay
    global fish_delay
    global drive_delay
    if inventory.count('Drivers License') > 0:
        if drive_delay == 0:
            repeat = roadLength
            roadCar = ["........|   🚘  |..",".......|   🚘  |...","......|   🚘  |....",".....|   🚘  |.....","....|   🚘  |......","...|   🚘  |.......","..|   🚘  |........"]
            roadnot = ["........|       |..",".......|       |...","......|       |....",".....|       |.....","....|       |......","...|       |.......","..|       |........"]
            currentRoad = random.randint(0,6)
            while repeat > 0:
                repeat -= 1
                print(roadCar[currentRoad], end="\r")
                time.sleep(delay)
                print(roadnot[currentRoad])
                if random.randint(1,2) == 1:
                    if currentRoad != 6: currentRoad += 1
                elif currentRoad !=0: currentRoad -= 1
            search_delay = 0
            beg_delay = 0
            gamble_delay = 0
            slots_delay = 0
            meme_delay = 0
            upload_delay = 0
            hunt_delay = 0
            fish_delay = 0
            if debug == False: drive_delay = 120
        else:
            print("   You need to wait ", drive_delay, " more seconds!")
    else:
        if illegal_license == False:
            illegal_license = True
            save_inv()
            print('')
            print("     I can't let you drive without a Drivers License!")
            print("     You'll kill yourself.")
            print("     ")
            print('     Euuhem, but between you and me,')
            print("     I know a guy who can get you one without taking lessons")
            print("     Look in the shop via pls shop!")
        else:
            print('')
            print("     Hey....")
            print("     Yes you there!")
            print("     You got that illega... eueuhm, I mean")
            print("     Totaly legal Drivers License yet?")
            print("     No?!")
            print("     What are you waiting for?")

def reset():
    global inventory
    global illegal_license
    inventory = []
    illegal_license = False
    save_inv()
    toggleDebug(False)


def countdown():
    global search_delay
    global beg_delay
    global gamble_delay
    global slots_delay
    global meme_delay
    global hunt_delay
    global upload_delay
    global fish_delay
    global drive_delay
    while True:
        if search_delay > 0: search_delay -= 1
        if beg_delay > 0: beg_delay -= 1
        if gamble_delay > 0: gamble_delay -= 1
        if slots_delay > 0: slots_delay -= 1
        if meme_delay > 0: meme_delay -= 1
        if upload_delay >0: upload_delay -= 1
        if hunt_delay > 0: hunt_delay -= 1
        if fish_delay > 0: fish_delay -= 1
        if drive_delay > 0: drive_delay -= 1
        time.sleep(1)

def toggleDebug(DoFaster):
    global search_delay
    global beg_delay
    global gamble_delay
    global slots_delay
    global meme_delay
    global upload_delay
    global hunt_delay
    global fish_delay
    global drive_delay
    global debug
    debug = DoFaster
    search_delay = 0
    beg_delay = 0
    gamble_delay = 0
    slots_delay = 0
    meme_delay = 0
    upload_delay = 0
    hunt_delay = 0
    fish_delay = 0
    drive_delay = 0

delay = threading.Thread(target=countdown, daemon=True)
delay.start()
