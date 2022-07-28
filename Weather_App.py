from distutils.sysconfig import customize_compiler
from email.utils import localtime
from tkinter.font import BOLD
from tkinter.tix import IMAGE
import requests
from datetime import datetime
import time
import tkinter
import customtkinter
from PIL import ImageTk, Image


WeatherApp = customtkinter.CTk()
WeatherApp.geometry(f"{975}x{600}")
WeatherApp.resizable(False, False)
WeatherApp.title("Weather")
WeatherApp.iconbitmap("C:/Digital Creations/Coding Projects/Weather_App/icon.ico")
customtkinter.set_appearance_mode("dark")
WeatherApp.configure(bg="#13233C")

WeatherApp.grid_rowconfigure(0, weight =1)
WeatherApp.grid_columnconfigure(1, weight = 1)


#Functions
country_to_abbrev = {
    
    "Andorra": "AD",
    "United Arab Emirates": "AE",
    "Afghanistan": "AF",
    "Antigua and Barbuda": "AG",
    "Anguilla": "AI",
    "Albania": "AL",
    "Armenia": "AM",
    "Angola": "AO",
    "Antarctica": "AQ",
    "Argentina": "AR",
    "American Samoa": "AS",
    "Austria": "AT",
    "Australia": "AU",
    "Aruba": "AW",
    "Åland Islands": "AX",
    "Azerbaijan": "AZ",
    "Bosnia and Herzegovina": "BA",
    "Barbados": "BB",
    "Bangladesh": "BD",
    "Belgium": "BE",
    "Burkina Faso": "BF",
    "Bulgaria": "BG",
    "Bahrain": "BH",
    "Burundi": "BI",
    "Benin": "BJ",
    "Saint Barthélemy": "BL",
    "Bermuda": "BM",
    "Brunei Darussalam": "BN",
    "Bolivia (Plurinational State of)": "BO",
    "Bonaire, Sint Eustatius and Saba": "BQ",
    "Brazil": "BR",
    "Bahamas": "BS",
    "Bhutan": "BT",
    "Bouvet Island": "BV",
    "Botswana": "BW",
    "Belarus": "BY",
    "Belize": "BZ",
    "Canada": "CA",
    "Cocos (Keeling) Islands": "CC",
    "Congo, Democratic Republic of the": "CD",
    "Central African Republic": "CF",
    "Congo": "CG",
    "Switzerland": "CH",
    "Côte d'Ivoire": "CI",
    "Cook Islands": "CK",
    "Chile": "CL",
    "Cameroon": "CM",
    "China": "CN",
    "Colombia": "CO",
    "Costa Rica": "CR",
    "Cuba": "CU",
    "Cabo Verde": "CV",
    "Curaçao": "CW",
    "Christmas Island": "CX",
    "Cyprus": "CY",
    "Czechia": "CZ",
    "Germany": "DE",
    "Djibouti": "DJ",
    "Denmark": "DK",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Algeria": "DZ",
    "Ecuador": "EC",
    "Estonia": "EE",
    "Egypt": "EG",
    "Western Sahara": "EH",
    "Eritrea": "ER",
    "Spain": "ES",
    "Ethiopia": "ET",
    "Finland": "FI",
    "Fiji": "FJ",
    "Falkland Islands (Malvinas)": "FK",
    "Micronesia (Federated States of)": "FM",
    "Faroe Islands": "FO",
    "France": "FR",
    "Gabon": "GA",
    "United Kingdom of Great Britain and Northern Ireland": "GB",
    "Grenada": "GD",
    "Georgia": "GE",
    "French Guiana": "GF",
    "Guernsey": "GG",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greenland": "GL",
    "Gambia": "GM",
    "Guinea": "GN",
    "Guadeloupe": "GP",
    "Equatorial Guinea": "GQ",
    "Greece": "GR",
    "South Georgia and the South Sandwich Islands": "GS",
    "Guatemala": "GT",
    "Guam": "GU",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Hong Kong": "HK",
    "Heard Island and McDonald Islands": "HM",
    "Honduras": "HN",
    "Croatia": "HR",
    "Haiti": "HT",
    "Hungary": "HU",
    "Indonesia": "ID",
    "Ireland": "IE",
    "Israel": "IL",
    "Isle of Man": "IM",
    "India": "IN",
    "British Indian Ocean Territory": "IO",
    "Iraq": "IQ",
    "Iran (Islamic Republic of)": "IR",
    "Iceland": "IS",
    "Italy": "IT",
    "Jersey": "JE",
    "Jamaica": "JM",
    "Jordan": "JO",
    "Japan": "JP",
    "Kenya": "KE",
    "Kyrgyzstan": "KG",
    "Cambodia": "KH",
    "Kiribati": "KI",
    "Comoros": "KM",
    "Saint Kitts and Nevis": "KN",
    "Korea (Democratic People's Republic of)": "KP",
    "Korea, Republic of": "KR",
    "Kuwait": "KW",
    "Cayman Islands": "KY",
    "Kazakhstan": "KZ",
    "Lao People's Democratic Republic": "LA",
    "Lebanon": "LB",
    "Saint Lucia": "LC",
    "Liechtenstein": "LI",
    "Sri Lanka": "LK",
    "Liberia": "LR",
    "Lesotho": "LS",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Latvia": "LV",
    "Libya": "LY",
    "Morocco": "MA",
    "Monaco": "MC",
    "Moldova, Republic of": "MD",
    "Montenegro": "ME",
    "Saint Martin (French part)": "MF",
    "Madagascar": "MG",
    "Marshall Islands": "MH",
    "North Macedonia": "MK",
    "Mali": "ML",
    "Myanmar": "MM",
    "Mongolia": "MN",
    "Macao": "MO",
    "Northern Mariana Islands": "MP",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Montserrat": "MS",
    "Malta": "MT",
    "Mauritius": "MU",
    "Maldives": "MV",
    "Malawi": "MW",
    "Mexico": "MX",
    "Malaysia": "MY",
    "Mozambique": "MZ",
    "Namibia": "NA",
    "New Caledonia": "NC",
    "Niger": "NE",
    "Norfolk Island": "NF",
    "Nigeria": "NG",
    "Nicaragua": "NI",
    "Netherlands": "NL",
    "Norway": "NO",
    "Nepal": "NP",
    "Nauru": "NR",
    "Niue": "NU",
    "New Zealand": "NZ",
    "Oman": "OM",
    "Panama": "PA",
    "Peru": "PE",
    "French Polynesia": "PF",
    "Papua New Guinea": "PG",
    "Philippines": "PH",
    "Pakistan": "PK",
    "Poland": "PL",
    "Saint Pierre and Miquelon": "PM",
    "Pitcairn": "PN",
    "Puerto Rico": "PR",
    "Palestine, State of": "PS",
    "Portugal": "PT",
    "Palau": "PW",
    "Paraguay": "PY",
    "Qatar": "QA",
    "Réunion": "RE",
    "Romania": "RO",
    "Serbia": "RS",
    "Russia": "RU",
    "Rwanda": "RW",
    "Saudi Arabia": "SA",
    "Solomon Islands": "SB",
    "Seychelles": "SC",
    "Sudan": "SD",
    "Sweden": "SE",
    "Singapore": "SG",
    "Saint Helena, Ascension and Tristan da Cunha": "SH",
    "Slovenia": "SI",
    "Svalbard and Jan Mayen": "SJ",
    "Slovakia": "SK",
    "Sierra Leone": "SL",
    "San Marino": "SM",
    "Senegal": "SN",
    "Somalia": "SO",
    "Suriname": "SR",
    "South Sudan": "SS",
    "Sao Tome and Principe": "ST",
    "El Salvador": "SV",
    "Sint Maarten (Dutch part)": "SX",
    "Syrian Arab Republic": "SY",
    "Eswatini": "SZ",
    "Turks and Caicos Islands": "TC",
    "Chad": "TD",
    "French Southern Territories": "TF",
    "Togo": "TG",
    "Thailand": "TH",
    "Tajikistan": "TJ",
    "Tokelau": "TK",
    "Timor-Leste": "TL",
    "Turkmenistan": "TM",
    "Tunisia": "TN",
    "Tonga": "TO",
    "Turkey": "TR",
    "Trinidad and Tobago": "TT",
    "Tuvalu": "TV",
    "Taiwan, Province of China": "TW",
    "Tanzania, United Republic of": "TZ",
    "Ukraine": "UA",
    "Uganda": "UG",
    "United Kingdom": "UK",
    "United States Minor Outlying Islands": "UM",
    "United States of America": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Holy See": "VA",
    "Saint Vincent and the Grenadines": "VC",
    "Venezuela (Bolivarian Republic of)": "VE",
    "Virgin Islands (British)": "VG",
    "Virgin Islands (U.S.)": "VI",
    "Viet Nam": "VN",
    "Vanuatu": "VU",
    "Wallis and Futuna": "WF",
    "Samoa": "WS",
    "Yemen": "YE",
    "Mayotte": "YT",
    "South Africa": "ZA",
    "Zambia": "ZM",
    "Zimbabwe": "ZW",
}

def getCurrentWeather():
    currentWeatherCondition = jsonData['current']['condition']['text']
    currentTemp = int(jsonData['current']['temp_c'])
    currentLowTemp = int(jsonData['forecast']['forecastday'][0]['day']['mintemp_c'])
    currentHighTemp = int(jsonData['forecast']['forecastday'][0]['day']['maxtemp_c'])

    return currentWeatherCondition, currentTemp, currentLowTemp, currentHighTemp

def getDailyForecast (dailyHighTemp, dailyLowTemp, conditionList):
    for i in range(0,3):
        dailyHighTemp.append(int(jsonData['forecast']['forecastday'][i]['day']['maxtemp_c']))
        dailyLowTemp.append(int(jsonData['forecast']['forecastday'][i]['day']['mintemp_c']))
        conditionList.append(jsonData['forecast']['forecastday'][i]['day']['condition']['text'])

def getHourlyForecast (hourlyTemps, hourlyConditions, iconUneditedLinks, hourlyTimes):
    localTime = jsonData['location']['localtime'][11] + jsonData['location']['localtime'][12]
    
    if (localTime[1] == ":"):
        localHour = int(localTime[0])
    else:
        localHour = int(localTime)

    i = 0
    while (localHour + i < 24 and i < 7):
        hourlyTemps.append(int(jsonData['forecast']['forecastday'][0]['hour'][localHour + i]['temp_c']))
        hourlyConditions.append(jsonData['forecast']['forecastday'][0]['hour'][localHour + i]['condition']['text'])
        iconUneditedLinks.append(jsonData['forecast']['forecastday'][0]['hour'][localHour + i]['condition']['icon'])
        hourlyTimes.append(jsonData['forecast']['forecastday'][0]['hour'][localHour + i]['time'])
        i += 1

    if (localHour + i >= 24):
        for j in range (0, 7 - i):
            hourlyTemps.append(int(jsonData['forecast']['forecastday'][1]['hour'][(24 - localHour - i) + j]['temp_c']))
            hourlyConditions.append(jsonData['forecast']['forecastday'][1]['hour'][(24 - localHour - i) + j]['condition']['text'])
            iconUneditedLinks.append(jsonData['forecast']['forecastday'][1]['hour'][(24 - localHour - i) + j]['condition']['icon'])
            hourlyTimes.append(jsonData['forecast']['forecastday'][1]['hour'][(24 - localHour - i) + j]['time'])

def getWeatherIconPath(iconLink):
    #Get code --> determine if it's day or night --> build icon path 

    #Get code
    code = (iconLink[len(iconLink) - 7] + iconLink[len(iconLink) - 6] + iconLink[len(iconLink) - 5])

    #Night or day?
    if (iconLink[len(iconLink) - 9] == "t"):
        timeOfDay = 'night'
    else:
        timeOfDay = 'day'

    #icon path
    iconPath = "C:/Digital Creations/Coding Projects/Weather_App/Weather Icons/weather/64x64/"+timeOfDay+"/"+code+".png"

    return iconPath

def militaryto12HourTime (hourlyTime):
    number = int(hourlyTime[11] + hourlyTime[12])

    if (number < 12 and number > 0):
        time = str(number) + " AM"
    elif(number == 0):
        time = "12 AM"
    elif(number == 12):
        time = "12 PM"
    else:
        time = str(number - 12) + " PM"
    
    return time


def configureLabels(city, currentWeatherCondition, currentTemp, currentLowTemp, 
                    currentHighTemp, dailyHighTemp, dailyLowTemp, conditionList, 
                    hourlyTemps, hourlyConditions, hourlyTimes):
    
    #Current Weather Labels
    CurrentWeatherLabel.configure(text = "Current Weather - " + city.upper())
    LocationLabel.configure(text = city.upper() + " , " + country_to_abbrev[jsonData['location']['country']])
    CurrentTempLabel.configure(text = str(currentTemp) + "°")
    CurrentConditionLabel.configure(text = currentWeatherCondition.capitalize())
    CurrentHighLabel.configure(text = "H: " + str(currentHighTemp) + "°")
    CurrentLowLabel.configure(text = "L: " + str(currentLowTemp) + "°")

    #Daily Weather Labels
    TodayLabel.configure(text = "Today")
    TodayTempLabel.configure(text = "H: " + str(dailyHighTemp[0]) + "° L: " + str(dailyLowTemp[0]) + "°")
    TodayConditionLabel.configure(text = conditionList[0])

    Day2Label.configure(text = time.strftime('%A', time.localtime(jsonData['forecast']['forecastday'][1]['hour'][0]['time_epoch'])))
    Day2TempLabel.configure(text = "H: " + str(dailyHighTemp[1]) + "° L: " + str(dailyLowTemp[1]) + "°")
    Day2ConditionLabel.configure(text = conditionList[1])

    Day3Label.configure(text = time.strftime('%A', time.localtime(jsonData['forecast']['forecastday'][2]['hour'][0]['time_epoch'])))
    Day3TempLabel.configure(text = "H: " + str(dailyHighTemp[2]) + "° L: " + str(dailyLowTemp[2]) + "°")
    Day3ConditionLabel.configure(text = conditionList[2])

    #Hourly Weather Labels
    Hour1Label.configure(text = " NOW ")
    Hour1TempLabel.configure(text = str(hourlyTemps[0]) + "°")
    Hour1ConditionLabel.configure(text = hourlyConditions[0])
        
    Hour2Label.configure(text = militaryto12HourTime(hourlyTimes[1]))
    Hour2TempLabel.configure(text = str(hourlyTemps[1]) + "°")
    Hour2ConditionLabel.configure(text = hourlyConditions[1])
        
    Hour3Label.configure(text = militaryto12HourTime(hourlyTimes[2]))
    Hour3TempLabel.configure(text = str(hourlyTemps[2]) + "°")
    Hour3ConditionLabel.configure(text = hourlyConditions[2])
        
    Hour4Label.configure(text = militaryto12HourTime(hourlyTimes[3]))
    Hour4TempLabel.configure(text = str(hourlyTemps[3]) + "°")
    Hour4ConditionLabel.configure(text = hourlyConditions[3])
      
    Hour5Label.configure(text = militaryto12HourTime(hourlyTimes[4]))
    Hour5TempLabel.configure(text = str(hourlyTemps[4]) + "°")
    Hour5ConditionLabel.configure(text = hourlyConditions[4])
        
    Hour6Label.configure(text = militaryto12HourTime(hourlyTimes[5]))
    Hour6TempLabel.configure(text = str(hourlyTemps[5]) + "°")
    Hour6ConditionLabel.configure(text = hourlyConditions[5])
        
    Hour7Label.configure(text = militaryto12HourTime(hourlyTimes[6]))
    Hour7TempLabel.configure(text = str(hourlyTemps[6]) + "°")
    Hour7ConditionLabel.configure(text = hourlyConditions[6])
def configureImages(iconUneditedLinks):
    #Image Settings - CurrentImageLabel
        currentIconLink = jsonData['current']['condition']['icon']
        img1 = Image.open(getWeatherIconPath(currentIconLink))
        img1Resized = img1.resize((125,125), Image.ANTIALIAS)
        img1Final = ImageTk.PhotoImage(img1Resized)
        CurrentImageLabel.configure(image = img1Final)
        CurrentImageLabel.img = img1Final

        #Image Settings - TodayImageLabel
        TodayIconLink = jsonData['forecast']['forecastday'][0]['day']['condition']['icon']
        img2 = Image.open(getWeatherIconPath(TodayIconLink))
        img2Resized = img2.resize((100,100), Image.ANTIALIAS)
        img2Final = ImageTk.PhotoImage(img2Resized)
        TodayImageLabel.configure(image = img2Final)
        TodayImageLabel.img = img2Final

        #Image Settings - Day2ImageLabel
        Day2IconLink = jsonData['forecast']['forecastday'][1]['day']['condition']['icon']
        img3 = Image.open(getWeatherIconPath(Day2IconLink))
        img3Resized = img3.resize((100,100), Image.ANTIALIAS)
        img3Final = ImageTk.PhotoImage(img3Resized)
        Day2ImageLabel.configure(image = img3Final)
        Day2ImageLabel.img = img3Final

        #Image Settings - Day3ImageLabel
        Day3IconLink = jsonData['forecast']['forecastday'][2]['day']['condition']['icon']
        img4 = Image.open(getWeatherIconPath(Day3IconLink))
        img4Resized = img4.resize((100,100), Image.ANTIALIAS)
        img4Final = ImageTk.PhotoImage(img4Resized)
        Day3ImageLabel.configure(image = img4Final)
        Day3ImageLabel.img = img4Final

        #Image Settings - Hour1ImageLabel
        Hour1IconLink = iconUneditedLinks[0]
        img5 = Image.open(getWeatherIconPath(Hour1IconLink))
        img5Resized = img5.resize((100,100), Image.ANTIALIAS)
        img5Final = ImageTk.PhotoImage(img5Resized)
        Hour1ImageLabel.configure(image = img5Final)
        Hour1ImageLabel.img = img5Final

        #Image Settings - Hour2ImageLabel
        Hour2IconLink = iconUneditedLinks[1]
        img6 = Image.open(getWeatherIconPath(Hour2IconLink))
        img6Resized = img6.resize((100,100), Image.ANTIALIAS)
        img6Final = ImageTk.PhotoImage(img6Resized)
        Hour2ImageLabel.configure(image = img6Final)
        Hour2ImageLabel.img = img6Final
        
        #Image Settings - Hour3ImageLabel
        Hour3IconLink = iconUneditedLinks[2]
        img7 = Image.open(getWeatherIconPath(Hour3IconLink))
        img7Resized = img7.resize((100,100), Image.ANTIALIAS)
        img7Final = ImageTk.PhotoImage(img7Resized)
        Hour3ImageLabel.configure(image = img7Final)
        Hour3ImageLabel.img = img7Final
        
        #Image Settings - Hour4ImageLabel
        Hour4IconLink = iconUneditedLinks[3]
        img8 = Image.open(getWeatherIconPath(Hour4IconLink))
        img8Resized = img8.resize((100,100), Image.ANTIALIAS)
        img8Final = ImageTk.PhotoImage(img8Resized)
        Hour4ImageLabel.configure(image = img8Final)
        Hour4ImageLabel.img = img8Final

        #Image Settings - Hour5ImageLabel
        Hour5IconLink = iconUneditedLinks[4]
        img9 = Image.open(getWeatherIconPath(Hour5IconLink))
        img9Resized = img9.resize((100,100), Image.ANTIALIAS)
        img9Final = ImageTk.PhotoImage(img9Resized)
        Hour5ImageLabel.configure(image = img9Final)
        Hour5ImageLabel.img = img9Final

        #Image Settings - Hour6ImageLabel
        Hour6IconLink = iconUneditedLinks[5]
        img10 = Image.open(getWeatherIconPath(Hour6IconLink))
        img10Resized = img10.resize((100,100), Image.ANTIALIAS)
        img10Final = ImageTk.PhotoImage(img10Resized)
        Hour6ImageLabel.configure(image = img10Final)
        Hour6ImageLabel.img = img10Final

        #Image Settings - Hour7ImageLabel
        Hour7IconLink = iconUneditedLinks[6]
        img11 = Image.open(getWeatherIconPath(Hour7IconLink))
        img11Resized = img11.resize((100,100), Image.ANTIALIAS)
        img11Final = ImageTk.PhotoImage(img11Resized)
        Hour7ImageLabel.configure(image = img11Final)
        Hour7ImageLabel.img = img11Final


def getWeatherEntry(WeatherWidget):
    #get data from API
    apiKey = "7dbaac7437644c84af623913222707"
    city = CitySearchEntry.get()
    apiLink = "http://api.weatherapi.com/v1/forecast.json?key="+apiKey+"&q="+city+"&days=3&aqi=no&alerts=no"
    response = requests.get(apiLink)
    
    global jsonData 
    jsonData = response.json()
    

    if (response.status_code != 200):
        LocationLabel.configure(text = "Invalid City: " + city.upper())
    else: 
        #Current Weather Related

        currentWeatherCondition = getCurrentWeather()[0]
        currentTemp = getCurrentWeather()[1]
        currentLowTemp = getCurrentWeather()[2]
        currentHighTemp = getCurrentWeather()[3]
            
        #Daily Forecast Related
        dailyHighTemp = []
        dailyLowTemp = []
        conditionList = []
        
        getDailyForecast(dailyHighTemp, dailyLowTemp, conditionList)

        #Hourly Forecast Related
        hourlyTemps = []
        hourlyConditions = []
        iconUneditedLinks = []
        hourlyTimes = []

        getHourlyForecast(hourlyTemps, hourlyConditions, iconUneditedLinks, hourlyTimes)

        #Configuring labels and images
        configureLabels(city, currentWeatherCondition, currentTemp, currentLowTemp, 
                        currentHighTemp, dailyHighTemp, dailyLowTemp, conditionList, 
                        hourlyTemps, hourlyConditions, hourlyTimes)
        configureImages(iconUneditedLinks)
def getWeatherButton():
    getWeatherEntry(WeatherApp)




#Frames
currentWeatherFrame = customtkinter.CTkFrame(master = WeatherApp, 
                                             width = 405,
                                             height = 270,
                                             corner_radius= 15, 
                                             fg_color= "#2F455E"
                                             )
currentWeatherFrame.grid(row=1, column=0, columnspan=1, padx = 10, pady=10)

DailyForecastFrame = customtkinter.CTkFrame(master = WeatherApp, 
                                             width = 405,
                                             height = 270,
                                             corner_radius= 15, 
                                             fg_color = "#2F455E"
                                             )
DailyForecastFrame.grid(row=1, column=1, columnspan = 2, padx=10, pady=10)

HourlyForecastFrame = customtkinter.CTkFrame(master = WeatherApp, 
                                             width = 830,
                                             height = 240,
                                             corner_radius= 15, 
                                             fg_color = "#2F455E"
                                             )
HourlyForecastFrame.grid(row=2,column = 0, columnspan=3, padx=10, pady=10)

#Labels
LocationLabel = customtkinter.CTkLabel(master=WeatherApp, 
                                        text="", 
                                        text_font = ("Calibri", 22), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 500)
LocationLabel.grid(row=0, column=0, columnspan = 1)

CurrentWeatherLabel = customtkinter.CTkLabel(master = currentWeatherFrame,text=" Current Weather ", 
                                        text_font = ("Calibri", 15, BOLD), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 150, height = 25)
CurrentWeatherLabel.place(relx=0.5, anchor = tkinter.N)

CurrentTempLabel = customtkinter.CTkLabel(currentWeatherFrame, text = "", 
                                        text_font = ("Calibri", 30), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE",
                                        width = 100
                                            )
CurrentTempLabel.place(x = 30, y = 55)
CurrentConditionLabel = customtkinter.CTkLabel(currentWeatherFrame, text = "", 
                                        text_font = ("Calibri", 20), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100
                                            )
CurrentConditionLabel.place(x = 150, y = 65)
CurrentHighLabel = customtkinter.CTkLabel(currentWeatherFrame, text = "", 
                                        text_font = ("Calibri", 20), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100
                                            )
CurrentHighLabel.place(x = 30, y = 150)
CurrentLowLabel = customtkinter.CTkLabel(currentWeatherFrame, text = "", 
                                        text_font = ("Calibri", 20), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100
                                            )
CurrentLowLabel.place(x = 150, y = 150)
CurrentImageLabel = customtkinter.CTkLabel(master = currentWeatherFrame,
                                        text="", 
                                        text_font = ("Calibri", 20), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE",
                                        width = 125, height = 125)
CurrentImageLabel.place(x=270, y=100)
DailyForecastLabel = customtkinter.CTkLabel(master = DailyForecastFrame,text=" Daily Forecast ", 
                                        text_font = ("Calibri", 15, BOLD), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 150, height = 25 )
DailyForecastLabel.place(relx=0.5, anchor = tkinter.N)

TodayLabel = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
TodayLabel.place(x=35, y=55)
TodayTempLabel = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
TodayTempLabel.place(x=35, y=95)

TodayConditionLabel = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
TodayConditionLabel.place(x=35, y=135)
TodayImageLabel = customtkinter.CTkLabel(master = DailyForecastFrame,
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
TodayImageLabel.place(x=35, y=162)

Day2Label = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Day2Label.place(x=150, y=55)
Day2TempLabel = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Day2TempLabel.place(x=150, y=95)
Day2ConditionLabel = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Day2ConditionLabel.place(x=150, y=135)
Day2ImageLabel = customtkinter.CTkLabel(master = DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Day2ImageLabel.place(x=150, y=162)

Day3Label = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Day3Label.place(x=265, y=55)
Day3TempLabel = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Day3TempLabel.place(x=265, y=95)
Day3ConditionLabel = customtkinter.CTkLabel(DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Day3ConditionLabel.place(x=265, y=135)
Day3ImageLabel = customtkinter.CTkLabel(master = DailyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Day3ImageLabel.place(x=265, y=162)

HourlyForecastLabel = customtkinter.CTkLabel(master = HourlyForecastFrame,text=" Hourly Forecast ", 
                                        text_font = ("Calibri", 15, BOLD), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 150, height = 25 )
HourlyForecastLabel.place(relx=0.5, anchor = tkinter.N)

Hour1Label = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour1Label.place(x=35, y=35)
Hour1TempLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour1TempLabel.place(x=35, y=75)

Hour1ConditionLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour1ConditionLabel.place(x=35, y=105)
Hour1ImageLabel = customtkinter.CTkLabel(master = HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Hour1ImageLabel.place(x=35, y=135)

Hour2Label = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour2Label.place(x=150, y=35)
Hour2TempLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour2TempLabel.place(x=150, y=75)

Hour2ConditionLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour2ConditionLabel.place(x=150, y=105)
Hour2ImageLabel = customtkinter.CTkLabel(master = HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Hour2ImageLabel.place(x=150, y=135)

Hour3Label = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour3Label.place(x=260, y=35)
Hour3TempLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour3TempLabel.place(x=260, y=75)

Hour3ConditionLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour3ConditionLabel.place(x=260, y=105)
Hour3ImageLabel = customtkinter.CTkLabel(master = HourlyForecastFrame,
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Hour3ImageLabel.place(x=260, y=135)

Hour4Label = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour4Label.place(x=370, y=35)
Hour4TempLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour4TempLabel.place(x=370, y=75)

Hour4ConditionLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour4ConditionLabel.place(x=370, y=105)
Hour4ImageLabel = customtkinter.CTkLabel(master = HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Hour4ImageLabel.place(x=370, y=135)

Hour5Label = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour5Label.place(x=480, y=35)
Hour5TempLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour5TempLabel.place(x=480, y=75)

Hour5ConditionLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour5ConditionLabel.place(x=480, y=105)
Hour5ImageLabel = customtkinter.CTkLabel(master = HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Hour5ImageLabel.place(x=480, y=135)

Hour6Label = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour6Label.place(x=590, y=35)
Hour6TempLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour6TempLabel.place(x=590, y=75)

Hour6ConditionLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour6ConditionLabel.place(x=590, y=105)
Hour6ImageLabel = customtkinter.CTkLabel(master = HourlyForecastFrame,
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Hour6ImageLabel.place(x=590, y=135)

Hour7Label = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 12), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour7Label.place(x=700, y=35)
Hour7TempLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour7TempLabel.place(x=700, y=75)
Hour7ConditionLabel = customtkinter.CTkLabel(HourlyForecastFrame, 
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100)
Hour7ConditionLabel.place(x=700, y=105)
Hour7ImageLabel = customtkinter.CTkLabel(master = HourlyForecastFrame,
                                        text="", 
                                        text_font = ("Calibri", 10), 
                                        bg_color = "#2F455E", 
                                        text_color = "#EDF6FE", 
                                        width = 100, height = 100)
Hour7ImageLabel.place(x=700, y=135)

#Entrys
CitySearchEntry = customtkinter.CTkEntry(master=WeatherApp, 
                                        placeholder_text="Enter City", 
                                        width = 275
                                        )
CitySearchEntry.grid(row = 0, column = 1, padx = 10, pady= 10)
CitySearchEntry.bind('<Return>', getWeatherEntry)

#Buttons
SearchButton = customtkinter.CTkButton(master=WeatherApp, 
                                        text="Search", 
                                        width = 100, 
                                        command=getWeatherButton)
SearchButton.grid(row = 0, column = 2, padx = 10, pady = 10)







WeatherApp.mainloop()
