# SetUp libs
- ```python -m venv ./.venv```
- ```.\.venv\Scripts\activate.bat```
- ```pip install --upgrade pip```
- ```pip install -r requirements.txt```

# Run Code
- ```.\.venv\Scripts\activate.bat```
- ```python main.py```

# Build requirements.txt
- ```.\.venv\Scripts\activate.bat```
- ```pip freeze > requirements.txt```

# Run QT Designer
- ```.\.venv\Scripts\activate.bat```
- ```C:\Users\j-ssr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyqt5-tools designer```
## Convert to design.py
- ```.\.venv\Scripts\activate.bat```
- ```C:\Users\j-ssr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyuic5 ./components/GUI/design.ui -o ./components/GUI/design.py```

# Build app to share
- ```C:\Users\j-ssr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller --noconfirm --onefile --windowed  "./main.py"```