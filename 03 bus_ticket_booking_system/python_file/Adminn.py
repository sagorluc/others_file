import csv
class Admin:
    def __init__(self) -> None:
        self.user_name = None
        self.password = None

    def admin_registration(self):
        print(f"\n{'-'*15} ADMIN REGISTRATION {'-'*13}\n")

        with open('admin_credential.csv', 'w', newline='') as f:
            w = csv.writer(f)
            self.user_name = input('Enter admin name: ')
            self.password =  input("Enter admin password: ")

            # saveing data into database
            w.writerow([self.user_name, self.password])
            print('Admin Registration Successfull \n')
            #print(f"{'-'*65}")

    def admin_login(self):
        store_data = [] #list for storing data and retrieving from adminCredential.csv file
        with open('admin_credential.csv', 'r+', newline='') as f:
            r = csv.reader(f)
            #print(r)
            data = list(r)

            for i in data:
                for j in i:
                    store_data.append(j)

            #print(store_data)

        while True:
            print(f'{"-"*15} ADMID LOGIN {"-"*15}\n')
            self.user_name = input('Enter admin user name: ')
            self.password =  input('Enter user password: ')

            if self.user_name == str(store_data[0]) and self.password == str(store_data[1]):
                print()
                print('Admin login successfull')
                break
            else:
                print('Please enter correct username and password')
            print()
        print(f'{"-"*65}')



