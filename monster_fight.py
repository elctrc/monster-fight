"""
Ash's Monster Fight 1.0

by Asher and Robby Zar
"""

def main():
    """
    Main program
    """
    print '\n'
    print(
        r"""
        ___  ___                _             ______ _       _     _     __   _____
        |  \/  |               | |            |  ___(_)     | |   | |   /  | |  _  |
        | .  . | ___  _ __  ___| |_ ___ _ __  | |_   _  __ _| |__ | |_  `| | | |/' |
        | |\/| |/ _ \| '_ \/ __| __/ _ \ '__| |  _| | |/ _` | '_ \| __|  | | |  /| |
        | |  | | (_) | | | \__ \ ||  __/ |    | |   | | (_| | | | | |_  _| |_\ |_/ /
        \_|  |_/\___/|_| |_|___/\__\___|_|    \_|   |_|\__, |_| |_|\__| \___(_)___/
                                                        __/ |
                                                    |___/
        """
    )

    character = the_naming()

    if character['weapon']['name'] == 'fists':
        print '\nYou are quite courageous, ' + character['name'] + '.'
        print 'Using only your ' + character['weapon']['name'] + ' is both brave and foolhardy.\n'
    else:
        print '\nYou have chosen wisely, ' + character['name'] + '.'
        print 'The ' + character['weapon']['name'] + ' is a fine weapon.\n'

def the_naming():
    """
    Return the character object, which contains the name and weapon choice
    """

    char = {
        "name": None,
        "weapon": {
            "name": "fists",
            "bonus": 0,
            "reach": 0
        }
    }

    weapons = [
        {
            "name": "sword",
            "bonus": 2,
            "reach": 1
        },
        {
            "name": "nunchukas",
            "bonus": 1,
            "reach": 1
        },
        {
            "name": "bow and arrow",
            "bonus": 1,
            "reach": 2
        },
    ]

    char['name'] = raw_input('\n\nWhat is your name, brave adventurer?\n\n>> ')

    print '\nWell, hello there, ' + char['name'] + '. Let\'s fight a monster!'

    weapon_chosen = False
    i = 0

    while not weapon_chosen:
        weapon_choice = raw_input(
            '\nChoose your weapon:\n(s)word\n(n)unchukas\n(b)ow and arrow\n\n>> '
        )
        if weapon_choice == 's':
            char['weapon'] = weapons[0]
            weapon_chosen = True
        elif weapon_choice == 'n':
            char['weapon'] = weapons[1]
            weapon_chosen = True
        elif weapon_choice == 'b':
            char['weapon'] = weapons[2]
            weapon_chosen = True
        else:
            i += 1
            if i < 3:
                print '\nThat is not a valid weapon selection.'
            else:
                print   """
                    \nBoy, are you persistent. Very well, then. You\'ll have to make due with your fists!
                        """
                break

    return char

if __name__ == "__main__":
    main()
