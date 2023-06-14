from tkinter import *
import os
from PIL import ImageTk, Image

# main screen
master = Tk()
master.title('Banking app')

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

def login():
    print('This is a login page')

# import image
img = Image.open('img_box.png')
resize_img = img.resize((150,150))
photo_img = ImageTk.PhotoImage(resize_img)

# labels
Label(master, text='Custom banking beta', font=('calibri',14)).grid(row=0, sticky=N, pady=10)
Label(master, text='The most secure bank you have useing', font=('calibri',12)).grid(row=1, sticky=N)
Label(master, image=photo_img).grid(row=2, sticky=N, pady= 15)


# Button
Button(master, text='Registration', font=('calibri,12'), width=20, command=register()).grid(row=3, sticky=N)
Button(master, text='Login', font=('calibri,12'), width=20, command=login()).grid(row=4, sticky=N, pady=10)

master.mainloop()
