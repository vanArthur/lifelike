version = 0.2


import LifeLike_color, LifeLike_games, LifeLike_help

from importlib import reload
import shelve, random

#get the saved variables from the save_game file
shelvefile = shelve.open('save_game')
wallet = shelvefile['wallet']
bank = shelvefile['bank']
newUser = shelvefile['newUser']
keyboardLayout = shelvefile["keyboardLayout"]
shelvefile.close()

running = True
debugger = False
previousCommand = ""


def toggleKeys():
    global keyboardLayout
    if keyboardLayout == "zqsd":
        keyboardLayout = "wasd"
    else: keyboardLayout = "zqsd"
    shelvefile = shelve.open('save_game')
    shelvefile['keyboardLayout'] = keyboardLayout
    shelvefile.close()


#getting command as user input
def get_command():
    global previousCommand
    global newUser
    if debugger:
        print(LifeLike_color.RED)
        print(LifeLike_color.BOLD  ,'[DEBUGGER] Type your commands here: ',LifeLike_color.END , end="")
    else: print(LifeLike_color.BOLD  ,'Type your commands here: ',LifeLike_color.END , end="")
    Usercommand = input()
    newUser = False
    previousCommand = Usercommand
    return Usercommand

def parse_command(command):
    global running
    global wallet
    global bank
    global debugger
    global newUser

    parse_command = command.split()
    if parse_command[0] != "pls":
        command = 'pls ' + command
        parse_command = command.split()
    if len(parse_command) < 2:
        print('unknown command')
        return
    #if command contains a int as string, then make it a int
    preValue = str(parse_command[0] + parse_command[1]).lower()
    for index, command in enumerate(parse_command):
        if parse_command[index].isnumeric():
            parse_command[index] = int(command)

    #replace keywords max and half with integers
    def strToIntWallet():
        for index, command in enumerate(parse_command):
            if command == "max":
                parse_command[index] = int(wallet)
            elif command == "half":
                parse_command[index] = int(wallet / 2)
    def strToIntBank():
        for index, command in enumerate(parse_command):
            if command == "max":
                parse_command[index] = int(bank)
            elif command == "half":
                parse_command[index] = int(bank / 2)


    def checkIfValid():
        if len(parse_command) < 3:
            print('You must specify an amount!')
            return False
        elif isinstance(parse_command[2], int) == False:
            print("Not a valid amount, please use: max, half or an integer!")
            return False
        else: return True

    #pls search command
    if preValue in ('plssearch'):
        gain = LifeLike_games.search(wallet, bank)
        if gain < 0:
            if wallet > (gain * -1):
                wallet += gain
            else:
                bank += gain
        else: wallet += gain
    #pls beg command
    elif preValue in ("plsbeg"):
        wallet += LifeLike_games.beg()
    #pls galble command
    elif preValue in ('plsgamble'):
        strToIntWallet()
        change = LifeLike_games.gamble(parse_command, bank)
        wallet += change
        if change != 0: print("     You now have ", wallet, " in wallet")
    #pls slots commands
    elif preValue in ('plsslots'):
        strToIntWallet()
        change = LifeLike_games.slots(parse_command, bank)
        wallet += change
        if change != 0:print("      You now have ", wallet, " in wallet")
    #pls postmemes command
    elif preValue in ("plspm", "plspostmemes", "plspostmeme"):
        wallet += LifeLike_games.postmeme()
    #pls upload command
    elif preValue in ("plsupload", "plsyt", "plsyoutube"):
        wallet += LifeLike_games.upload()
    #pls hunt command
    elif preValue in ("plshunt"):
        LifeLike_games.hunt()
    #pls fish command
    elif preValue in ("plsfish"):
        LifeLike_games.fish()
    #pls mazegame command
    elif preValue in ("plsmazegame", "plsmaze"):
        wallet += LifeLike_games.playmaze(keyboardLayout)
    #pls balance command
    elif preValue in ('plsbal', "plsbalance"):
        print("====================================")
        print("||    coins in ", LifeLike_color.RED , "wallet",LifeLike_color.END , wallet)
        print("||    coins in ", LifeLike_color.GREEN , "bank  ",LifeLike_color.END , bank)
        print("||    coins in ", LifeLike_color.CYAN, "total ", LifeLike_color.END, (wallet + bank))
        print("====================================")
    #pls deposit command
    elif preValue in ('plsdep', 'plsdeposit'):
        strToIntWallet()
        if checkIfValid() == False: return
        if int(parse_command[2]) > wallet:
            print("You cant deposit more than you have in your wallet dummy!")
            return
        bank += parse_command[2]
        wallet -= parse_command[2]
        print("     coins in ", LifeLike_color.RED , "wallet",LifeLike_color.END , wallet)
        print("     coins in ", LifeLike_color.GREEN , "bank",LifeLike_color.END , bank)
    #pls withdraw command
    elif preValue in ('plswith', 'plswithdraw'):
        strToIntBank()
        if checkIfValid() == False: return
        if parse_command[2] > bank:
            print("You cant withdraw more than you have in your bank dummy!")
            return
        bank -= parse_command[2]
        wallet += parse_command[2]
        print("     coins in ", LifeLike_color.RED , "wallet",LifeLike_color.END , wallet)
        print("     coins in ", LifeLike_color.GREEN , "bank",LifeLike_color.END , bank)
    #pls inventory command
    elif preValue in ("plsinv", "plsinventory"):
        LifeLike_games.openinv()
    #pls shop command
    elif preValue in ("plsshop"):
        LifeLike_games.openshop()
    #pls buy command
    elif preValue in ("plsbuy"):
        temp = []
        for index,each in enumerate(parse_command[0:]):
            if each in ("pls", "buy"):
                pass
            else: temp.append(parse_command[index])
        wallet -= LifeLike_games.buy(" ".join(temp), wallet)
    #pls sell commands
    elif preValue in ("plssell"):
        wallet += LifeLike_games.sell(parse_command[2:])
    #pls drive command
    elif preValue == 'plsdrive':
        LifeLike_games.road(20, 0.05)
    #pls settings command
    elif preValue in ("plssettings","plssetting"):
        ret = LifeLike_help.settings(parse_command[2:])
        if ret == "toggleKeys":
            toggleKeys()
    #pls help command(s)
    elif preValue in ("plshelp"):
        if len(parse_command) < 3:
            newUser = False
            LifeLike_help.help(0)
        elif len(parse_command) == 3:
            newUser = False
            print(LifeLike_help.help(parse_command[2]))
        else:
            newUser = False
            print("We do not currently have a help page for that!")
    #pls reset
    elif preValue == 'plsreset':
        print("Do you really want to ", LifeLike_color.RED, LifeLike_color.UNDERLINE, LifeLike_color.BOLD, "RESET", LifeLike_color.END, " your progress?", sep="")
        print("Type RESET to reset, press enter if you DO NOT want to RESET!")

        if input() == "RESET":
            wallet = 500
            bank = 0
            LifeLike_games.reset()
            newUser = True
            shelvefile = shelve.open('save_game')
            shelvefile['newUser'] = newUser
            shelvefile.close()
        else: return

    #exit the game
    elif preValue == 'plsexit' or preValue == 'plsstop':
        running = False
        return

    elif preValue == "plsversion":
        print(f"Lifelike version {version}")

    #debugger ===================================
    elif preValue == "plsdebug":
        if debugger == False:
            print('Password: ', end="")
            if input() == "bitchboygeorge":
            #if input() == "":
                print(LifeLike_color.RED)
                debugger = True
            else: print("Wrong password")
        else:
            debugger = False
            LifeLike_games.toggleDebug(False)
    elif debugger == True:
        if preValue == "plsgimme":
            wallet += parse_command[2]
        elif preValue == "plsset":
            wallet = parse_command[2]
        elif preValue == "plsreload":
            reload(LifeLike_games)
        elif preValue == "plsfaster":
            print(LifeLike_color.DGREEN,' All delays turned off!',LifeLike_color.END)
            LifeLike_games.toggleDebug(True)
        elif preValue == "plsslower":
            print(LifeLike_color.RED,'   All delays turned on!',LifeLike_color.END)
            LifeLike_games.toggleDebug(False)
    #end of debugger ===================================

    else:
        print('unknown command')
while running == True:
    if newUser == True:
        print(LifeLike_color.BOLD, LifeLike_color.RED)
        print("     If this is your first time playing, ")
        print("     use 'pls help' to get info on all the commands!")
        print(LifeLike_color.END)
    parse_command(get_command())
    shelvefile = shelve.open('save_game')
    shelvefile['wallet'] = wallet
    shelvefile['bank'] = bank
    shelvefile['newUser'] = newUser
    shelvefile.close()
    print('')
