# Установка библиотек и зависимостей
- ```python -m venv ./.venv```
- ```.\.venv\Scripts\activate.bat```
- ```pip install --upgrade pip```
- ```pip install -r requirements.txt```

# Запуск кода
- ```.\.venv\Scripts\activate.bat```
- ```python main.py```

# Заполнить файл зависимостей
- ```.\.venv\Scripts\activate.bat```
- ```pip freeze > requirements.txt```

# Запуск QT Designer
- ```.\.venv\Scripts\activate.bat```
- ```pyqt5-tools designer```
## Конвертирование to design.py
- ```.\.venv\Scripts\activate.bat```
- ```pyuic5 ./components/GUI/design.ui -o ./components/GUI/design.py```

# Собрать приложение в .exe
- ```pyinstaller --noconfirm --onefile --windowed  "./main.py"```