from PassengerInfo_one import *
import csv
class Show:
    def show_tkt(self):
        all_info = []
        with open('passenger.csv', 'r+', newline='') as f:
            r = csv.reader(f)
            data = list(r)
            id = int(input('Enter your booking id: '))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        all_info.append(j)
                    break
                #print(all_info)

        print(f'-'*65)
        print(f"{' '*15} WELCOME TO GREEN LINE BUS TRAVELS {' '*15}")
        print(f'{" "*13} {"="*36} {" "*15}')
        print(f"{' '*2 }E-ticket:\n{' '*2}Tangail Address \t\t\t : New bus tarminal ")
        print(f"{' '*2 }Phone \t\t\t\t : 00881798918267 ")
        print(f"{'_'*65}\n")
        print(f"{' '*2}Departure:{' '*25} {all_info[3]}\n")
        print(f"{' '*2}Destination:{' '*23} {all_info[4]}\n")
        print(f"{' '*2}Booking ID:{' '*24} {all_info[0]}\n")
        print(f"{' '*2}Passenger Name:{' '*20} {all_info[1]}\n")
        print(f"{' '*2}Number of Passenger:{' '*15} {all_info[2]}\n")
        print(f"{' '*2}Date of Booking:{' '*19} {all_info[5]}\n")
        print(f"{' '*2}Seat Number:{' '*23} {all_info[6]}\n")
        print(f"{' '*2}Bus Type:{' '*26} {all_info[7]}\n")
        print(f"{' '*2}Bus Fare:{' '*26} {all_info[8]}\n")
        print(f'-'*65)

