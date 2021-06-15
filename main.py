from colorama import init, Fore, Back, Style
from time import sleep
import bot

def main():
    init(autoreset=True) 
    print(Style.BRIGHT + Back.RED + 'Welcome to the InstagramBot!')

    print('Please, write your instagram username: ')
    instagram_link = 'https://instagram.com/' + input('>> ')

    print('\nPlease, write the name of your accounts database: ')
    try:
        db_name = input('>> ')
        with open(db_name) as file:
            db = file.readlines()
    except:
        print('Something went wrong!')
        exit()

    print('\nPlease, write the name of your posts database: ')
    try:
        db_name = input('>> ')
        with open(db_name) as file:
            posts = file.readlines()
    except:
        print('Something went wrong!')
        exit()

    print(f'\nFound {len(db)} accounts!')
    print(f'Found {len(posts)} posts!')


    for i in range(len(db)):
        login, password = db[i].split(':')[0], db[i].split(':')[1]

        bot.subscribe_and_like(login, password, instagram_link, posts)

        print(Fore.RED + '\nDone!')

    for frame in '543210':
        if frame == '0':
            exit()
        print('\r', frame, ' seconds before closing...', sep='', end='', flush=True)
        sleep(1)

if __name__ == '__main__':
    main()