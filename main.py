import os
import pandas as pd
from datetime import datetime, timedelta
from data_fetcher import get_prayer_times, get_weather_data, get_hijri_year, format_prayer_times, format_weather_data

# API ключ и регионы
API_KEY = 'ad0bd7f6b3504657810200310242907'
REGIONS = [
    'Tashkent,Uzbekistan',
    'Andijan,Uzbekistan',
    'Bukhara,Uzbekistan',
    'Jizzakh,Uzbekistan',
    'Fergana,Uzbekistan',
    'Gulistan,Uzbekistan',
    'Karshi,Uzbekistan',
    'Namangan,Uzbekistan',
    'Navoi,Uzbekistan',
    'Nukus,Uzbekistan',
    'Samarkand,Uzbekistan',
    'Termez,Uzbekistan',
    'Urgench,Uzbekistan'
]

latitude = 41.2995
longitude = 69.2401
timezone = 5

# Получить завтрашнюю дату
tomorrow = datetime.now() + timedelta(days=1)

# Получить время молитвы на завтра
prayer_times = get_prayer_times(latitude, longitude, timezone)

# Получить хиджрийский год на завтра
hijri_year = get_hijri_year(tomorrow)

# Отформатировать время молитвы
text_uz_prayer, text_ru_prayer, text_en_prayer = format_prayer_times(prayer_times, hijri_year, tomorrow)

# Инициализировать словарь данных
data = {
    'id': [],
    'Текст UZ': [],
    'Текст RU': [],
    'Текст EN': [],
    'Дата на отправку': [],
    'Статус': []
}

# Добавить данные для молитв
data['id'].extend(range(1, 6))
data['Текст UZ'].extend([text_uz_prayer] * 5)
data['Текст RU'].extend([text_ru_prayer] * 5)
data['Текст EN'].extend([text_en_prayer] * 5)
data['Дата на отправку'].extend([tomorrow.strftime('%Y%m%d')] * 5)
data['Статус'].extend([1] * 5)

# Получить данные о погоде для каждого региона
weather_data = {}
for region in REGIONS:
    weather_data[region] = get_weather_data(API_KEY, region)

# Отформатировать данные о погоде и добавить их в словарь
for idx, region in enumerate(REGIONS):
    formatted_weather = format_weather_data(weather_data[region], tomorrow)
    data['id'].append(int(len(data['id']) + 8) + 1)
    data['Текст UZ'].append(formatted_weather[0])
    data['Текст RU'].append(formatted_weather[1])
    data['Текст EN'].append(formatted_weather[2])
    data['Дата на отправку'].append(tomorrow.strftime('%Y%m%d'))
    data['Статус'].append(1)

# Создать DataFrame
df = pd.DataFrame(data)

# Получить текущую рабочую директорию
current_directory = os.getcwd()
output_path = os.path.join(current_directory, 'output.xlsx')

# Сохранить в Excel
df.to_excel(output_path, index=False)

print(f"Data saved to {output_path}")
