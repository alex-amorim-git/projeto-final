from flask import Flask, request, jsonif
app = Flask(__name__)

@app.get("/")
def ola_mundo():
    return("Olá mundo")

if __name__ == '__main__':
    app.run()
