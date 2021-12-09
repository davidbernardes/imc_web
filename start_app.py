import os
import webbrowser

os.system("start cmd /c python app.py")
webbrowser.open('http://127.0.0.1', new=0)
os.system("cd frontend\imc\dist && python server.py")
