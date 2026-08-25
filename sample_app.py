from flask import Flask, render_template
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

sample = Flask(__name__)

MYSQL_PASSWORD = "super_secret_123"

@sample.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=MYSQL_PASSWORD,
            database=os.getenv("database"),
            connect_timeout=os.getenv("connect_timeout"),
        )
        conn.close()
        db_status = "Error 500 - Fallo interno del servidor"
    except Exception as e:
        db_status = f"Error en la conexion: {e}"

    return render_template("index.html", db_status=db_status)

if __name__ == '__main__':
    sample.run(host=os.getenv("tsoh"), port=os.getenv("port"), debug=True)
