from tkinter import *
import os
from PIL import ImageTk, Image

# main screen
master = Tk()
master.title('Banking app')

#=========================START REGISTRATION AREA=================
def finish_register():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_account = os.listdir()
    #print(all_account)
    
    if name == '' or age == '' or gender == '' or password == '':
        notif.config(fg='red', text='All fields required *')
        return
    else:
        print('Good to go mate')
        
    for name_check in all_account:
        if name == name_check:
            notif.config(fg='red', text='Account already exits')
            return
        else:
            new_file = open(name, 'w')
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('0') # remove the empty string
            new_file.close()
            notif.config(fg='green', text='Account has been successfully') 
    
# function
def register():
    
    # variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    
    # this one will make another window open
    register_screen = Toplevel(master)
    register_screen.title('Register')

    # label
    Label(register_screen, text='Please enter your details to below register', font='calibri,12').grid(row=0, sticky=N, pady=10)
    Label(register_screen, text='Name', font='calibri,12').grid(row=1, sticky=W)
    Label(register_screen, text='Age', font='calibri,12').grid(row=2, sticky=W)
    Label(register_screen, text='Gender', font='calibri,12').grid(row=3, sticky=W)
    Label(register_screen, text='Password', font='calibri,12').grid(row=4, sticky=W)
    notif = Label(register_screen,font='calibri,12')
    notif.grid(row=6, sticky=N, pady=10)
    
    # Entries taking input
    Entry(register_screen, textvariable= temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable= temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable= temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable= temp_password, show='*').grid(row=4, column=0)
    
    Button(register_screen, text='Register', command= finish_register, font=('calibri,12')).grid(row=5, sticky=N, pady=10)

#======================START LOGIN AREA============================ 

def login_session():
    global login_name
    login_name = login_temp_name.get()
    login_password = login_temp_password.get()
    all_login_account = os.listdir()
                  
    for name in all_login_account:
        if name == login_name:
            file = open(name, 'r')
            file_data = file.read()
            file_data = file_data.split('\n')
            password = file_data[1] # 1 number position got password
           
            # Account dashboard
            if login_password == password:
                login_sereec.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Dashboard')
                
                # labels
                Label(account_dashboard, text='Account Dashboard', font=('calibri,12')).grid(row=0, sticky=N, pady=15)
                Label(account_dashboard, text='Welcome'+ ' ' + name, font=('calibri,12')).grid(row=1, sticky=N, pady=5)
                
                # button
                Button(account_dashboard, text='Personal Details', font=('calibri,12'), width=30, command= personal_details).grid(row=2, sticky=N, padx=10)
                Button(account_dashboard, text='Deposit', font=('calibri,12'), width=30, command= deposit).grid(row=3, sticky=N, padx=10)
                Button(account_dashboard, text='Withdraw', font=('calibri,12'), width=30, command= withdraw).grid(row=4, sticky=N, padx=10)
                Label(account_dashboard).grid(row=5, sticky=N, pady=10)
                return
            
            else:
                login_notif.config(fg='red', text='Wrong password')
                return
    login_notif.config(fg='red', text='No account found')
#======================END LOGIN SESSION FUNCTION CODE===============

#======================START DEPOSIT FUNCTION CODE===================
def deposit():
    global amount
    global deposit_notif
    global current_balance_label
    
    amount = StringVar()
    
    file = open(login_name, 'r')
    file_data = file.read()
    file_data = file_data.split()
    user_balance = file_data[4]
    
    # deposit screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposit')
    
    # label
    Label(deposit_screen, text='Deposit Details', font=('calibri,12')).grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposit_screen, text='Current balance: tk- '+ user_balance, font=('calibri,12'))
    current_balance_label.grid(row=1, sticky=W, padx=10)
    Label(deposit_screen, text='Amount: ', font=('calibri,12')).grid(row=2, sticky=W, padx=10)

    deposit_notif = Label(deposit_screen, font=('calibri,12'))
    deposit_notif.grid(row=4, sticky=N, pady=5) 
    
    # Entries takeing input
    Entry(deposit_screen, textvariable= amount, font=('calibri,12'), width=15).grid(row=2, column=1)
    Button(deposit_screen, text='Finish', font=('calibri,12'), width=5, command= finish_deposit).grid(row=3,sticky=W, pady=10)
    
def finish_deposit():
    if amount.get() == '':
        deposit_notif.config(fg='red', text='Amount required')
        return 
        
    if float(amount.get()) <= 0:
        deposit_notif.config(fg='red', text='Amount can not be negetive and zero')
        return
    
    file = open(login_name, 'r+') # read and write mood
    file_data = file.read()
    details = file_data.split('\n')
    current_balance = details[4] # fourth position in the list
    
    update_balance = current_balance
    update_balance = float(update_balance) + float(amount.get())
    
    file_data      = file_data.replace(current_balance, str(update_balance)) # replace the balance in the file data
    
    # update all the data in the file
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()   
    
    current_balance_label.config(fg='green', text='Current balance: ' + str(update_balance))
    deposit_notif.config(fg='green', text='Balance Updated') 
    
#========================END DIPOSIT FUNCTION CODE====================   

#========================START WITHDRAW FUNCTION CODE=============
def withdraw():
    pass

#========================END WITHDRAW FUNCTION CODE================

#========================START PERSONAL DETAILS HERE===============

def personal_details():
    
    # variables
    file = open(login_name, 'r')
    file_data = file.read()
    file_data = file_data.split('\n')
    #print(file_data)
    user_name = file_data[0]
    user_age = file_data[2]
    user_gender = file_data[3]
    user_balance = file_data[4]
    #print(user_name, user_age, user_gender, user_balance)
    
    # personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title('Personal Details')
    
    # labels
    Label(personal_details_screen, text= 'Personal Details', font=('calibri,12')).grid(row=0, sticky=N, pady=10)
    Label(personal_details_screen, text= 'Name: '+user_name, font=('calibri,12')).grid(row=1, sticky=W, padx=10)
    Label(personal_details_screen, text= 'Age: '+user_age, font=('calibri,12')).grid(row=2, sticky=W, padx=10)
    Label(personal_details_screen, text= 'Gender: '+user_gender, font=('calibri,12')).grid(row=3, sticky=W, padx=10)
    Label(personal_details_screen, text= 'Balance: tk-'+user_balance, font=('calibri,12')).grid(row=4, sticky=W, padx=10)

                # END PERSONAL DETAILS FUNCTION
            #======================================
def login():
    global login_temp_name
    global login_temp_password
    global login_notif
    global login_sereec
    
    login_temp_name = StringVar()
    login_temp_password = StringVar()
    
    # login screen
    login_sereec = Toplevel(master)
    login_sereec.title('Log-in')
    
    # label
    Label(login_sereec, text='Enter your username and password to login', font=('calibri,12')).grid(row=0,sticky=N, pady=10)
    Label(login_sereec, text='Username', font=('calibri,12')).grid(row=1,sticky=W, pady=10)
    Label(login_sereec, text='Password', font=('calibri,12')).grid(row=2,sticky=W, pady=10)
    login_notif = Label(login_sereec, font=('calibri,12'))
    login_notif.grid(row=4, sticky=N, pady=10)
    # Entries to take input
    Entry(login_sereec, textvariable= login_temp_name, font=('calibri,12'),width=15).grid(row=1, column=0)
    Entry(login_sereec, textvariable= login_temp_password,show='*', font=('calibri,12'), width=15).grid(row=2, column=0)
    
    Button(login_sereec, text='Login', command= login_session, font=('calibri,12'), width=10).grid(row=3, sticky=N, pady=10)
 
#======================END LOGIN FUNCTION CODE=====================   

#======================IMPORTING AREA================================  
    
# import image
img = Image.open('img_box2.png')
resize_img = img.resize((150,150))
photo_img = ImageTk.PhotoImage(resize_img)

# labels
Label(master, text='Custom banking beta', font=('calibri',14)).grid(row=0, sticky=N, pady=10)
Label(master, text='The most secure bank you have useing', font=('calibri',12)).grid(row=1, sticky=N)
Label(master, image=photo_img).grid(row=2, sticky=N, pady= 15)


# Button
Button(master, text='Registration', font=('calibri,12'), width=20, command=register).grid(row=3, sticky=N)
Button(master, text='Login', font=('calibri,12'), width=20, command=login).grid(row=4, sticky=N, pady=10)

master.mainloop()
