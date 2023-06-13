
from Library_managment import Library
def main():
    lib = Library(['Mina-Raju','Python','Bangladesh','The Rad Mulana'],'IKRA')
    while True:
        print(f'{"*"*10} CHIOSE THE NUMBER  {"*"*10} \n')
        print('1. display book')
        print('2. lend book')
        print('3. add book')
        print('4. return book')
        print('5. exit')
        user_input = input('Enter your choice: ')

        # if user_input not in ['1','2','3','4','5']:
        #     print('Please enter a valid option: ')
        #     continue
            
        # else:
        #     user_input = int(user_input)

        if user_input == 5:
           exit() # break

        elif user_input == 1:
           lib.display_book()

        elif user_input == 2:
             book_name = input('Enter book name: ')
             user_name = input('Enter user name: ')
             
             lib.lend_book(book_name, user_name)

        elif user_input == 3:
            name = input('Enter book name: ')
            lib.add_book(name)

        elif user_input == 4:
             book_name = input('Enter book name: ')
             lib.return_book(book_name)

        else:
            print('Invalid key pressed')

        print('(Q) for exist and (C) for continue')
        q_input = ''
        while q_input != 'Q' and q_input != 'c' and q_input != 'C' and q_input != 'c':
            q_input = input('Enter choice: ')

            if q_input == 'Q' and q_input == 'q':
                exit()
            elif q_input == 'C' and q_input == 'c':
                continue
            else:
                print('Wrong press!try agein')

    
           

   
    # lib.display_book()
    # lib.add_book('5. shadinotar uttor bangladesh')
    # lib.return_book('Mina-Raju')

    # lib.lend_book('sagor','the fiz')
    # lib.display_book()




if __name__ == '__main__':
    main()
