"Developer: Krishna Aggarwal & Dhruv Kalra; Class-section: 12th-A; RollNo. : 16 & 10"
"Submodule:- Main Menu (completed)"

def main_menu():
    from printing_tool import dtool
    from time import sleep
    print('  ____________________  ___   ____________________  ____  ____  ___');sleep(0.02)
    print(' /_  __/ ____/ ____/ / / / | / / ____/_  __/  _/ / / /  |/  /  |/  /');sleep(0.02)
    print('  / / / __/ / /   / /_/ /  |/ / __/   / /  / // / / / /|_/ / /|_/ / ');sleep(0.02)
    print(' / / / /___/ /___/ __  / /|  / /___  / / _/ // /_/ / /  / / /  / /  ');sleep(0.02)
    print('/_/ /_____/\____/_/ /_/_/ |_/_____/ /_/ /___/\____/_/  /_/_/  /_/   ')
    t="Create your own digital reality!!"
    print('\t\t\t',end=' ')
    for i in t:
        print(i,end='')
        sleep(0.002)
    print()
    a="MAIN MENU"
    b="1.Employee Details"
    c="2.Stock House"
    d="3.Billing"
    e="4.Setting"
    f="5.Exit"
    dtool(a);dtool(b);dtool(c);dtool(d);dtool(e);dtool(f)

def employee_menu():
    from printing_tool import dtool
    from time import sleep
    print("   ____           __                    ___      __       _ __  ");sleep(0.02)
    print("  / __/_ _  ___  / /__  __ _____ ___   / _ \___ / /____ _(_) /__");sleep(0.02)
    print(" / _//  ' \/ _ \/ / _ \/ // / -_) -_) / // / -_) __/ _ `/ / (_-<");sleep(0.02)
    print("/___/_/_/_/ .__/_/\___/\_, /\__/\__/ /____/\__/\__/\_,_/_/_/___/");sleep(0.02)
    print("         /_/          /___/                                     ")
    print()
    g='SUB MENU'
    a='1.Display all employee records'
    b='2.Search an employee record'
    c='3.Add an employee'
    d='4.Update an employee record '
    e='5.Remove an employee'
    f='6.Back to main menu'
    dtool(g);dtool(a);dtool(b);dtool(c);dtool(d);dtool(e);dtool(f)

def stock_house_menu():
    from printing_tool import dtool
    from time import sleep
    print("   ______________  _______ __  __ ______  __  __________ ");sleep(0.02)
    print("  / __/_  __/ __ \/ ___/ //_/ / // / __ \/ / / / __/ __/ ");sleep(0.02)
    print(" _\ \  / / / /_/ / /__/ ,<   / _  / /_/ / /_/ /\ \/ _/ ");sleep(0.02)
    print("/___/ /_/  \____/\___/_/|_| /_//_/\____/\____/___/___/ ")
    print()
    g='SUB MENU'
    a='1.Search an item record'
    b='2.Add an item'
    c='3.Update an item record'
    d='4.Remove an item record'
    e='5.Back to main menu'
    dtool(g);dtool(a);dtool(b);dtool(c);dtool(d);dtool(e)


    
def billing_menu():
    from printing_tool import dtool
    from time import sleep
    print("   ___  ______   __   _____  _______");sleep(0.02)
    print("  / _ )/  _/ /  / /  /  _/ |/ / ___/");sleep(0.02)
    print(" / _  |/ // /__/ /___/ //    / (_ /  ");sleep(0.02)
    print("/____/___/____/____/___/_/|_/\___/  ")
    print()
    a='SUB MENU:-'
    b='1.Create a new invoice'
    c='2.Search an invoice record'
    d='3.Delete an invoice record'
    e='4.Back to main menu'
    dtool(a);dtool(b);dtool(c);dtool(d);dtool(e)

def setting_menu():
    from printing_tool import dtool
    from time import sleep
    print("   _________________________  _______");sleep(0.02)
    print("  / __/ __/_  __/_  __/  _/ |/ / ___/");sleep(0.02)
    print(" _\ \/ _/  / /   / / _/ //    / (_ / ");sleep(0.02)
    print("/___/___/ /_/   /_/ /___/_/|_/\___/  ")
    print()
    a='SUB MENU:-'
    b='1.Account'
    c='2.Back Up'
    d='3.Bin'
    e='4.About us'
    f='5.Factory Reset'
    g='6.Back to main menu'
    dtool(a);dtool(b);dtool(c);dtool(d);dtool(e);dtool(f);dtool(g)
