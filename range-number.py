# python3 coded by 'ha3ter@gmai.com'

print('''
 ____  _  _          ____ _____   _   _                 ____ _____      
|  _ \| || |  _ __  / ___|___ /  | \ | |_   _ _ __ ___ | __ )___ / _ __ 
| |_) | || |_| '_ \| |  _  |_ \  |  \| | | | | '_ ` _ \|  _ \ |_ \| '__|
|  _ <|__   _| | | | |_| |___) | | |\  | |_| | | | | | | |_) |__) | |   
|_| \_\  |_| |_| |_|\____|____/  |_| \_|\__,_|_| |_| |_|____/____/|_|   
                                                                                                                                        

''')
number_code = input('\n--> Give me the code Like [-98-[iran],-1-[U.S], .....] : ')
number = int(input('\n--> Give me the range Like [922,905,910,916,938, .....] : '))

if (number < 1000) and (number > 99):
    number = str(number)
    number = number_code + number + '0000000'

    for x in range(0, 9999999):
        number = (int(number) + 1)
        print('+' + str(number))
else:
    print('\nThe range entered is incorrect')
