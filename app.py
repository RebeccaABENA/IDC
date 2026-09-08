from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        # L'hôte correspond au nom du conteneur MySQL sur le réseau exonet
        connection = mysql.connector.connect(
            host='ma-bdd',
            database='mysql', # Base de données système présente par défaut
            user='root',
            password='root'
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            return f"<h1>Hello, World !</h1><p>Succès : Connecté à MySQL version {db_info} !</p>"
            
    except Error as e:
        return f"<h1>Erreur de connexion</h1><p>Impossible de joindre la base de données : {e}</p>"
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__== "__main__":
    app.run(host='0.0.0.0', port=5000)