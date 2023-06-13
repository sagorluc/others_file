# 1. passenger: input name and num_of_passenger
# 2. departure location
# 3. destination location 
# 4. date
# 5. seat functionality
# 6. bus type: ac/ no_ac and fare 

# csv file add

import csv
class Passenger:
    def __init__(self) -> None:
        self.passenger_name = None
        self.number_of_passenger = None 
        self.departure = None
        self.destination = None
        self.date_time = None
        self.seat_number = None
        self.bus_type = None
        self.bus_fare = None
        self.auto_increment = 1 # booking id
        self.count_col = 0

    def get_passenger_info(self):
        self.passenger_name = input('Enter your name: ')
        self.number_of_passenger = int(input('How many passenger of you: '))

        # departure start from here
        print('1. Tangail')
        print('2. Ghatail')
        print('3. Modupur')
        print('4. Kalihati')
        print('5. Exit')

        depart_input = int(input('Enter your departure choice: ')) 
        if depart_input == 5:
            exit()
        elif depart_input == 1:
            self.departure = 'Tangail'
        elif depart_input == 2:
            self.departure = 'Ghatail'
        elif depart_input == 3:
            self.departure = 'Modupur'
        elif depart_input == 4:
            self.departure = 'Kalihati'
        else:
            print('Please enter valid input! and try agein')

        # departure end here

        # detination start form here
        print('1. Dhaka')
        print('2. Gazipur')
        print('3. Chitaggong')
        print('4. Cumilla')
        print('5. Exit')

        self.desti_input = int(input('Enter your destination choice: '))

       
        if self.desti_input == 5:
            exit()
        elif self.desti_input == 1:
            self.destination = 'Dhaka'
        elif self.desti_input == 2:
            self.destination = 'Gazipur'
        elif self.desti_input == 3:
            self.destination = 'Chitaggong'
        elif self.desti_input == 4:
            self.destination = 'Cumilla'
        else:
            print('Please enter valid input! and try agein')


        # dete input here
        self.date_input = input('Enter your date like(dd-mm-yyyy): ')
        self.date_time = self.date_input

        # seat functionality start form here

        print('[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]')
        print('[11]__[12]__[13]__[14]__[15]__[16]__[17]__[18]__[19]__[20]')
        print('[21]__[22]__[23]__[24]__[25]__[26]__[27]__[28]__[29]__[30]')

        self.number_of_seat = [Empty for Empty in range(1,31)]
        #print(number_of_seat)
        self.seat_list = []

        while True:
            self.seat_input = int(input('Enter your seat number: '))
            if self.seat_input <= 30:
                    if self.seat_input in self.number_of_seat:
                        self.seat_list.append(self.seat_input)
                        del self.number_of_seat[self.seat_input + 1]
                        count = len(self.number_of_seat)
                    else:
                        print('Ticket already booked')
                    print('Do you want to take more seat (yes/no): ')
                    self.more_input = input('Choice yes or no: ')
                    if self.more_input == 'yes':
                        pass
                    else:
                        break
            else:
                print('Please enter the valid seat number')

        # seat functionality end here

        # bus type start from here
        print('Choice the type of bus(Ac or Non AC)')
        print('1. AC bus fare = 800 TK.')
        print('2. Non AC bus fare = 550 TK.')
    
        bus = int(input('Enter the type of bus: '))
        if bus == 1:
            self.bus_type = 'AC bus'
            self.bus_fare = self.number_of_passenger * 800
        elif bus == 2:
            self.bus_type = 'Non AC bus'
            self.bus_fare = self.number_of_passenger * 550

        # booking seat end
#=================================================================
        # saveing passenger data in csv file
#=================================================================

class Passenger_data_csv(Passenger):
    def save_info(self):
        try:
            with open('Passenger.csv', 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)
                #print(data)
                for i in data:
                    self.auto_increment += 1
                    for j in i:
                        self.count_col += 1
                    print()
                print('Number of racord are found in databased', self.auto_increment)
        except:
            print('file not found')
        finally:
            with open('Passenger_data.csv','a+',newline="") as f:
                w = csv.writer(f)
                w.writerow([self.auto_increment, self.passenger_name, self.number_of_passenger, self.departure, self.destination, self.date_time, self.seat_list, self.bus_type, self.bus_fare])
                print()
                print('Data save successfully\n')


# pa = Passenger_data_csv()
# pa.get_passenger_info()
# pa.save_info()





            

            









