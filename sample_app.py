from flask import Flask, render_template
import pymysql

sample = Flask(__name__)

@sample.route("/")
def home():
    try:
        # Vamos a intentar conectarnos a la BD
        conn = pymysql.connect(
            host="servidor-bd-ejemplo",
            user="root",
            password="sena123",
            database="adso_db_ejemplo",
            connect_timeout=3
		)
        conn.close()
        db_status= "Conexion exitosa a la BD!"
    except Exception as e:
        db_status = f"Error en la conexion: {e}"

    return render_template("index.html", db_status=db_status)

if __name__ == '__main__':
    sample.run(host="0.0.0.0", port=5050, debug=True)
