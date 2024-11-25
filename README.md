# Weather and Prayer Times Data Project

Этот проект предназначен для получения данных о времени молитвы и погоде для различных регионов Узбекистана и сохранения их в Excel-файл.

## Установка и настройка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/doossee/prayers-and-weather.git
cd prayers-and-weather
```

### 2. Создайте и активируйте виртуальное окружение

Для создания виртуального окружения выполните следующую команду:

```bash
python -m venv venv
```

Активируйте виртуальное окружение:

- **На Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **На macOS и Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Установите зависимости

Убедитесь, что виртуальное окружение активировано, и установите все необходимые зависимости, указанные в `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Запустите проект

После установки зависимостей вы можете запустить основной скрипт проекта:

```bash
python main.py
```

## Как это работает

1. **Получение данных о времени молитвы:** Скрипт использует функцию `get_prayer_times` для получения времени молитвы для Ташкента и форматирует данные для вывода.
2. **Получение данных о погоде:** Скрипт запрашивает данные о погоде для указанных регионов Узбекистана и форматирует их для вывода.
3. **Сохранение в Excel:** Все собранные данные сохраняются в файл `output.xlsx` в текущей рабочей директории.

## Требования

- Python 3.7 или новее
- Установленные библиотеки из `requirements.txt`

## Дополнительная информация

- **API ключ для погоды:** Замените `API_KEY` на ваш собственный ключ API для WeatherAPI в файле `main.py`.
