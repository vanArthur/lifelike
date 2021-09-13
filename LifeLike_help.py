import LifeLike_color

def help(index):
    print("")
    if index == 0:
        print(LifeLike_color.BOLD, LifeLike_color.UNDERLINE)
        print("This is a list of commands")
        print("For more information about a command,")
        print('use pls help (number)', LifeLike_color.END)
        print("    1: pls search         9: pls withdraw        17: pls upload")
        print("    2: pls beg           10: pls inventory       18: pls fish")
        print("    3: pls gamble        11: pls shop            19: pls maze")
        print("    4: pls slots         12: pls buy")
        print("    5: pls postmemes     13: pls sell")
        print("    6: pls hunt          14: pls drive")
        print("    7: pls balance       15: pls settings")
        print("    8: pls deposit       16: pls help")
        return ""
    elif index == 1:
        text = []
        text.append("   pls search")
        text.append("   Use the search command to search for coins around you!")
        text.append("   Delay: 30s")
        return "\n".join(text)
    elif index == 2:
        text = []
        text.append("   pls beg")
        text.append("   Use the beg command to beg for coins!")
        text.append("   Delay: 30s")
        return "\n".join(text)
    elif index == 3:
        text = []
        text.append("   pls gamble")
        text.append("   Use the gamble command to gamble all your money!")
        text.append("   Specify an amount with: max, half or an integer.")
        text.append("   Delay: 10s")
        return "\n".join(text)
    elif index == 4:
        text = []
        text.append("   pls slots")
        text.append("   Use the slots command to risk all your money!")
        text.append("   You need 2 or more equal emojis, the more the better!")
        text.append("   Specify an amount with: max, half or an integer.")
        text.append("   Delay: 10s")
        return "\n".join(text)
    elif index == 5:
        text = []
        text.append("   pls postmemes, pls postmeme, pls pm")
        text.append("   Use the postmemes command to post memes on ")
        text.append("   the internet, you get coins from the ads!")
        text.append("   Delay: 60s")
        return "\n".join(text)
    elif index == 6:
        text = []
        text.append("   pls hunt")
        text.append("   Use the hunt command to hunt for animals!")
        text.append("   The animals can be sold with the pls sell command.")
        text.append("   Delay: 60s")
        return "\n".join(text)
    elif index == 7:
        text = []
        text.append("   pls balance, pls bal")
        text.append("   Use the balance command to see the money you have!")
        text.append("   You can see the money in your wallet, bank and in total.")
        return "\n".join(text)
    elif index == 8:
        text = []
        text.append("   pls deposit, pls dep")
        text.append("   Use the deposit command to transfer money from")
        text.append("   your wallet to your bank!")
        return "\n".join(text)
    elif index == 9:
        text = []
        text.append("   pls withdraw, pls with")
        text.append("   Use the withdraw command to transfer money from")
        text.append("   your bank to your wallet!")
        return "\n".join(text)
    elif index == 10:
        text = []
        text.append("   pls inventory, pls inv")
        text.append("   Use the inventory command to see the items")
        text.append("   you have in your inventory, you can also see")
        text.append("   how much they sell for!")
        return "\n".join(text)
    elif index == 11:
        text = []
        text.append("   pls shop")
        text.append("   Use the shop command to see the items")
        text.append("   that are sold in the shop!")
        return "\n".join(text)
    elif index == 12:
        text = []
        text.append("   pls buy")
        text.append("   Use the buy command to buy items from the shop")
        return "\n".join(text)
    elif index == 13:
        text = []
        text.append("   pls sell")
        text.append("   Use the sell command to sell items from your inventory!")
        return "\n".join(text)
    elif index == 14:
        text = []
        text.append("   pls drive")
        text.append("   Use the drive command to drive past all the delays!")
        text.append("   Delay: 120s")
        return "\n".join(text)
    elif index == 15:
        text = []
        text.append("   pls setting, pls settings")
        text.append("   Use the settings command to change settings.")
        text.append("   Use pls settings help for list of settings")
        return "\n".join(text)
    elif index == 16:
        text = []
        text.append("   pls help")
        text.append("   If you see this message you know how this")
        text.append("   command works!")
        return "\n".join(text)
    elif index == 17:
        text = []
        text.append("   pls upload")
        text.append("   Upload a video to MeTube")
        text.append("   You earn money from the ads!")
        text.append("   delay: 300s")
        return "\n".join(text)
    elif index == 18:
        text = []
        text.append("   pls fish")
        text.append("   Catch fish with a fishing pole!")
        text.append("   You can sell the fish with 'pls sell'!")
        text.append("   delay: 45s")
        return "\n".join(text)
    elif index == 19:
        text = []
        text.append("   pls maze, pls mazegame")
        text.append("   Play a game to win money!")
        text.append("   Move the player with zqsd or wasd!")
        text.append("   To change use pls settings Keyboard toggle")

def settings(command):
    if command[0] in ("help", "info", "list"):
        print(LifeLike_color.BOLD, LifeLike_color.UNDERLINE)
        print("Here a list of settings and their current Value")
        print(LifeLike_color.END)
        print("     EXAMPLE: pls settings color False (capitals in True and False!)")
        print("")
        print("     1: color    ", str(LifeLike_color.colorSet))
    elif command[0] in ("colors", "color"):
        if len(command) < 2:
            print("Use True or False")
        elif command[1] in ("True", "False"):
            LifeLike_color.noColors(command[1])
    elif command[0] in ("keyboard", "Keyboard"):
            return "toggleKeys"
    return 0
