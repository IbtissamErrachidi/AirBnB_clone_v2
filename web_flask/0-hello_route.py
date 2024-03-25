#!/usr/bin/python3
"""A Flask web application with its route ('/'):
    display “Hello HBNB!
   => Current file: 0-hello_route.py"""

from flask import Flask

# Création d'une instance de l'application Flask
app = Flask(__name__)


# Définition de la route principale "/"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Lancement de l'application sur 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

