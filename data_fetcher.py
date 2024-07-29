import requests
from datetime import datetime, timedelta
from hijri_converter import convert

def get_prayer_times(region):
    response = requests.get(f"https://islomapi.uz/api/present/week?region={region}")
    data = response.json()

    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow_date_str = tomorrow.strftime('%d/%m/%Y')

    for day in data:
        if day['date'].startswith(tomorrow_date_str):
            return day['times']

    raise ValueError(f"Prayer times for {tomorrow_date_str} not found in the API response.")

def get_weather_data(api_key, city):
    response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no")
    data = response.json()

    if 'error' in data:
        raise ValueError(f"Error getting weather data: {data['error']['message']}")

    return data['forecast']['forecastday'][0]['day']

def get_hijri_year(date):
    hijri_date = convert.Gregorian(date.year, date.month, date.day).to_hijri()
    return hijri_date.year

def format_prayer_times(times, hijri_year, tomorrow):
    months_uz = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
    months_ru = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    months_en = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    date_str_uz = f"Namoz {hijri_year}-yil. {tomorrow.day}-{months_uz[tomorrow.month-1]}"
    date_str_ru = f"Намаз {hijri_year}-йил. {tomorrow.day}-{months_ru[tomorrow.month-1]}"
    date_str_en = f"Prayer {hijri_year}. {months_en[tomorrow.month-1]} {tomorrow.day}"

    text_uz = f"{date_str_uz} Tong - {times['tong_saharlik']}, Quyosh - {times['quyosh']}, Peshin - {times['peshin']}, Asr - {times['asr']}, Shom - {times['shom_iftor']}, Xufton - {times['hufton']}."
    text_ru = f"{date_str_ru} Фаджр - {times['tong_saharlik']}, Восход - {times['quyosh']}, Зухр - {times['peshin']}, Аср - {times['asr']}, Магриб - {times['shom_iftor']}, Иша - {times['hufton']}."
    text_en = f"{date_str_en}, Fajr - {times['tong_saharlik']}, Ishraq - {times['quyosh']}, Dhuhr - {times['peshin']}, Asr - {times['asr']}, Maghrib - {times['shom_iftor']}, Isha - {times['hufton']}."

    return text_uz, text_ru, text_en

def format_weather_data(weather_data, tomorrow):
    temp_day = weather_data['maxtemp_c']
    temp_night = weather_data['mintemp_c']

    date_str_uz = f"{tomorrow.day}-{tomorrow.strftime('%B').lower()}"
    date_str_ru = f"{tomorrow.day}-{tomorrow.strftime('%B').lower()}"
    date_str_en = f"{tomorrow.strftime('%B')} {tomorrow.day}"

    text_uz = f"{date_str_uz} havo o'zgarib turadi. Kunduzi harorat +{temp_day} daraja kechasi +{temp_night} daraja bo'lishi kutilmoqda"
    text_ru = f"{date_str_ru} havo o'zgarib turadi. Kunduzi harorat +{temp_day} daraja kechasi +{temp_night} daraja bo'lishi kutilmoqda"
    text_en = f"{date_str_en} is changing weather. During the day, temperatures are expected to be +{temp_day} degrees At night +{temp_night} degrees"

    return text_uz, text_ru, text_en
