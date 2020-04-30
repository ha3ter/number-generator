# python3 coded by 'ha3ter@gmai.com'

print('''
 ____  _  _          ____ _____       _   _                 ____ _____      
|  _ \| || |  _ __  / ___|___ /      | \ | |_   _ _ __ ___ | __ )___ / _ __ 
| |_) | || |_| '_ \| |  _  |_ \      |  \| | | | | '_ ` _ \|  _ \ |_ \| '__|
|  _ <|__   _| | | | |_| |___) |     | |\  | |_| | | | | | | |_) |__) | |   
|_| \_\  |_| |_| |_|\____|____/      |_| \_|\__,_|_| |_| |_|____/____/|_|   
                                                                                                                                        

''')



def crat():


    number = int(input('\nGive me the renge Number #Like [916 ,922 ,938 ,910  ...] : '))
    
    if (1000 > number > 99):
        files = input('\nGive me the name file #Like [exp.txt] : ')
        file = files.split('.')
        if_1 = 1
        
        if (file[1]=='txt'):
            text = open (files, mode='a+')
            if_2 = 1

        else:
            print('\nThe file name is incorrect #Example [s.txt ,num.txt]')

    else:
        print('\nThis number not in the range :D ')

    if (if_1==if_2):
        print('''
__        __    _ _   
\ \      / /_ _(_) |_ 
 \ \ /\ / / _` | | __|
  \ V  V / (_| | | |_ 
   \_/\_/ \__,_|_|\__|

''')
        for x in range(0, 9999999):
            n = int("98{}0000000".format(number))
            n = n + x
            n = ('+{}\n'.format(n))
            text.write(n)
        print ('\nsuccessful created :D \n')
            
    text.close()
crat()
