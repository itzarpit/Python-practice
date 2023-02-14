from flask import Flask
app=Flask(__name__)

@app.route('/')
def MainPage():
    return ("Satus : Main Page is Working")



from Controller import*