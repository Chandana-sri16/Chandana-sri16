""" Weather report printing output in a pdf file format"""
import requests
import os
from datetime import datetime
import pytz
from fpdf import FPDF  # importing FPDF for generating pdf

timeZ_Kl = pytz.timezone('Asia/kolkata')
dt_Kl = datetime.now(timeZ_Kl)

count = 1
temp_max = []
wind = []
weather_looking = []
humidity = []
city_names = []
while count <= 5:
        try:
            city_name = input("Enter the city name: ")
            print("fetching info......")
            # declaration of url part, API key and city
            apikey = "47823b480302ab3a6a5f3262798eaef0"
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}' + '&appid=' + f'{apikey}'  # full url
            data = requests.get(url).json()
            city_names.append(city_name)
            temp_max.append(int(data['main']['temp'] - 272.15))  # max temperature
            wind.append(data['wind']['speed'])  # wind speed
            weather_looking.append(data['weather'][0]['main'])  # weather looking like
            humidity.append(data['main']['humidity'])  # humidity
        except KeyError:
            print("City name not found....")
        except IndexError:
            print("List out of range..")
            break
        count += 1
        if count > 5:
            print('PDF ready...')


pdf = FPDF()
pdf.add_page()  # adding a page to the pdf
pdf.set_font('Times', size=12)  # mentioning total letter size and font
current_date = (dt_Kl.strftime('Date:- %d-%m-%y'))
current_time = (dt_Kl.strftime('Time:- %H:%M:%S'))
# text colour
pdf.set_text_color(255, 128, 0)
pdf.cell(198, 10, txt='Weather Report', align='C', ln=1)  # heading
pdf.set_text_color(0, 0, 0)
pdf.cell(300, 8, txt=f"{current_time}", ln=2, align='C')
pdf.cell(300, 8, txt=f"{current_date}", ln=3, align='C')  # today's date will print

pdf.set_text_color(255, 0, 127)
pdf.cell(1, 8, txt=f"City :- {city_names[0]}", ln=4, align='L')  # printing city name
pdf.set_text_color(0, 0, 0)
pdf.cell(10, 8, txt=f"Weather looking like - {weather_looking[0]}", ln=5,align='L')  # how weather looking like
pdf.cell(10, 8, txt=f"Maximum Temperature - {str(temp_max[0])}°C", ln=6, align='L')  # maximum temperature
pdf.cell(10, 8, txt=f"Wind Speed - {str(wind[0])}", ln=7, align='L')  # wind speed
pdf.cell(10, 8, txt=f"Humidity - {str(humidity[0])}", ln=8, align='L')
pdf.cell(10, 8, txt='\n------------------------------------------------------------------------------',align='L', ln=8, border=0.5)

pdf.set_text_color(255, 0, 127)
pdf.cell(1, 8, txt=f"City :- {city_names[1]}", ln=4, align='L')
pdf.set_text_color(0, 0, 0)
pdf.cell(10, 8, txt=f"Weather looking like - {weather_looking[1]}", ln=5,align='L')
pdf.cell(10, 8, txt=f"Maximum Temperature - {str(temp_max[1])}°C", ln=6, align='L')
pdf.cell(10, 8, txt=f"Wind Speed - {str(wind[1])}", ln=7, align='L')
pdf.cell(10, 8, txt=f"Humidity - {str(humidity[1])}", ln=8, align='L')
pdf.cell(10, 8, txt='\n------------------------------------------------------------------------------',align='L', ln=8, border=0.5)

pdf.set_text_color(255, 0, 127)
pdf.cell(1, 8, txt=f"City :- {city_names[2]}", ln=4, align='L')
pdf.set_text_color(0, 0, 0)
pdf.cell(10, 8, txt=f"Weather looking like - {weather_looking[2]}", ln=5,align='L')
pdf.cell(10, 8, txt=f"Maximum Temperature - {str(temp_max[2])}°C", ln=6, align='L')
pdf.cell(10, 8, txt=f"Wind Speed - {str(wind[2])}", ln=7, align='L')
pdf.cell(10, 8, txt=f"Humidity - {str(humidity[2])}", ln=8, align='L')
pdf.cell(10, 8, txt='\n------------------------------------------------------------------------------',align='L', ln=8, border=0.5)

pdf.set_text_color(255, 0, 127)
pdf.cell(1, 8, txt=f"City :- {city_names[3]}", ln=4, align='L')
pdf.set_text_color(0, 0, 0)
pdf.cell(10, 8, txt=f"Weather looking like - {weather_looking[3]}", ln=5,align='L')
pdf.cell(10, 8, txt=f"Maximum Temperature - {str(temp_max[3])}°C", ln=6, align='L')
pdf.cell(10, 8, txt=f"Wind Speed - {str(wind[3])}", ln=7, align='L')
pdf.cell(10, 8, txt=f"Humidity - {str(humidity[3])}", ln=8, align='L')
pdf.cell(10, 8, txt='\n------------------------------------------------------------------------------',align='L', ln=8, border=0.5)

pdf.set_text_color(255, 0, 127)
pdf.cell(1, 8, txt=f"City :- {city_names[4]}", ln=4, align='L')
pdf.set_text_color(0, 0, 0)
pdf.cell(10, 8, txt=f"Weather looking like - {weather_looking[4]}", ln=5,align='L')
pdf.cell(10, 8, txt=f"Maximum Temperature - {str(temp_max[4])}°C", ln=6, align='L')
pdf.cell(10, 8, txt=f"Wind Speed - {str(wind[4])}", ln=7, align='L')
pdf.cell(10, 8, txt=f"Humidity - {str(humidity[4])}", ln=8, align='L')

# weather images for city 1
if weather_looking[0] == 'Smoke' or weather_looking[0] == 'Haze' or weather_looking[0] == 'Mist':
    pdf.image("haze.png", x=80, y=37)
elif weather_looking[0] == "Clouds" or weather_looking[0] == 'Broken clouds' or weather_looking[0] == 'scattered clouds' or weather_looking[0] == 'Few clouds':
    pdf.image("cloudy.png", x=80, y=37)
elif weather_looking[0] == "overcast clouds":
    pdf.image("over.png", x=80, y=37)
elif weather_looking[0] == "Clear":
    pdf.image("clear.png", x=80, y=37)
elif weather_looking[0] == "Rain" or weather_looking[0] == "Drizzle" or weather_looking[0] == "light Rain":
    pdf.image("rainbow.png", x=80, y=37)
elif weather_looking[0] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=80, y=37)
else:
    print(weather_looking[0])

# weather images for city 2
if weather_looking[1] == 'Smoke' or weather_looking[1] == 'Haze' or weather_looking[1] == 'Mist':
    pdf.image("haze.png", x=80, y=87)
elif weather_looking[1] == "Clouds" or weather_looking[1] == 'Broken clouds' or weather_looking[1] == 'scattered clouds' or weather_looking[1] == 'Few clouds':
    pdf.image("cloudy.png", x=80, y=87)
elif weather_looking[1] == "Overcast Clouds":
    pdf.image("over.png", x=80, y=87)
elif weather_looking[1] == "Clear":
    pdf.image("clear.png", x=80, y=87)
elif weather_looking[1] == "Rain" or weather_looking[1] == "Drizzle" or weather_looking[1] == "light Rain":
    pdf.image("rainy.png", x=80, y=87)
elif weather_looking[1] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=80, y=87)
else:
    print("wrong")

# weather images for city 3
if weather_looking[2] == 'Smoke' or weather_looking[2] == 'Haze' or weather_looking[2] == 'Mist':
    pdf.image("haze.png", x=80, y=136)
elif weather_looking[2] == "Clouds" or weather_looking[2] == 'Broken clouds' or weather_looking[2] == 'scattered clouds' or weather_looking[2] == 'Few clouds':
    pdf.image("cloudy.png", x=80, y=136)
elif weather_looking[2] == "Overcast Clouds":
    pdf.image("over.png", x=80, y=136)
elif weather_looking[2] == "Clear":
    pdf.image("clear.png", x=80, y=136)
elif weather_looking[2] == "Rain" or weather_looking[2] == "Drizzle" or weather_looking[2] == "light Rain":
    pdf.image("rainy.png", x=80, y=136)
elif weather_looking[2] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=80, y=136)
else:
    print("wrong")


# weather images for city 4
if weather_looking[3] == 'Smoke' or weather_looking[3] == 'Haze' or weather_looking[3] == 'Mist':
    pdf.image("haze.png", x=80, y=187)
elif weather_looking[3] == "Clouds" or weather_looking[3] == 'Broken clouds' or weather_looking[3] == 'scattered clouds' or weather_looking[3] == 'Few clouds':
    pdf.image("cloudy.png", x=80, y=187)
elif weather_looking[3] == "Overcast Clouds":
    pdf.image("over.png", x=80, y=187)
elif weather_looking[3] == "Clear":
    pdf.image("clear.png", x=80, y=187)
elif weather_looking[3] == "Rain" or weather_looking[3] == "Drizzle" or weather_looking[3] == "light Rain":
    pdf.image("rainy.png", x=80, y=187)
elif weather_looking[3] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=80, y=187)
else:
    print('wrong')


# weather images for city 5
if weather_looking[4] == 'Smoke' or weather_looking[4] == 'Haze' or weather_looking[4] == 'Mist':
    pdf.image("haze.png", x=80, y=235)
elif weather_looking[4] == "Clouds" or weather_looking[4] == 'Broken clouds' or weather_looking[4] == 'scattered clouds' or weather_looking[4] == 'Few clouds':
    pdf.image("cloudy.png", x=80, y=235)
elif weather_looking[4] == "Overcast Clouds":
    pdf.image("over.png", x=80, y=235)
elif weather_looking[4] == "Clear":
    pdf.image("clear.png", x=80, y=235)
elif weather_looking[4] == "Rain" or weather_looking[4] == "Drizzle" or weather_looking[4] == "light Rain":
    pdf.image("rainy.png", x=80, y=235)
elif weather_looking[4] == "Thunderstorm":
    pdf.image("thunderstorm.png", x=80, y=235)
else:
    print('wrong')

pdf.output('weather2.pdf')  # get output in pdf  and the name of the pdf is arithmetic.pdf
os.system('weather2.pdf')
