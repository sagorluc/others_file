import requests # request to other website
from bs4 import BeautifulSoup
from tkinter import Tk, Label # open up new window popup
from PIL import ImageTk,Image # add image 

url = 'https://weather.com/weather/today/l/61bd7e707adfd50a808d53fb1379b839c9b6e3022c1d20164b00efa0f6b4c824'

master = Tk()
master.title('Weather App')
master.config(bg='white')

img = Image.open('weather_img.png')
resize_img = img.resize((150,150))
photo_img = ImageTk.PhotoImage(resize_img)

def get_weather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1',class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find('span', class_='CurrentConditions--tempValue--MHmYY').text
    weather_prediction = soup.find('div', class_='CurrentConditions--phraseValue--mZC_p').text
    total_degree = soup.find('div', class_='CurrentConditions--tempHiLoValue--3T1DG').text
    #print(temperature)
    
    location_label.config(text= location)
    temperature_label.config(text= temperature)
    weather_prediction_label.config(text= weather_prediction)
    total_degree_label.config(text= total_degree)
    
    # update weather after some time or second
    temperature_label.after(60000, get_weather)
    master.update()
    
    
    
location_label = Label(master, font=('calibri bold',20), bg='white')
location_label.grid(row=0, sticky='N', padx=100)

temperature_label = Label(master, font=('calibri bold',80), bg='white')
temperature_label.grid(row=1, sticky='W', padx=40)

Label(master, image = photo_img, bg='white').grid(row=1, sticky='E')

weather_prediction_label = Label(master, font=('calibri, bold',15), bg='white')
weather_prediction_label.grid(row=2, sticky='W', padx=40)

total_degree_label = Label(master, font=('calibri 20',15), bg='white')
total_degree_label.grid(row=3, sticky='W', padx=40)

get_weather()
master.mainloop()
