from PassengerInfo_one import *
from Show_ticket import *
from Adminn import Admin
global var 
def main():

    print(f'\n{" "*15} WELCOME TO GREEN LINE BUS TRAVEL {" "*15}')
    print(f'{" "*14}{"="*37}{" "*15}')

    print('1. Admin Registration')
    print('2. Admin Login')
    var = int(input('Enter your choice: '))

    ad = Admin()
    if var == 1:
        ad.admin_registration()
    if var == 2:
        ad.admin_login()

    print('1. Passenger Registration')
    print('2. Show Ticket')

    var = int(input('Enter your choice: '))

    if var == 1:
        pas = Passenger_data_csv()
        pas.get_passenger_info()
        pas.save_info()
    if var == 2:
        tic = Show()
        tic.show_tkt()

    # pas = Passenger()
    # pas.get_passenger_info()
    # s = Show()
    # s.show_tkt()
    # a = Admin()
    # a.admin_registration()
    # a.admin_login()
    



if __name__ == '__main__':
    main()