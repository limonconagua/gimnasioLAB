from flask import Flask, render_template, url_for
import random
app = Flask(__name__, static_folder='static')

logos_lic = [
    "/static/logoLAB.png",
    "/static/logoLH.png",
    "/static/logoMMR.png",
    "/static/logoIN.png",
    "/static/logoVC.png"
]

@app.route('/')
def index():
    iconobaquet = url_for('static', filename='baquet_icon.png')
    iconofutbal = url_for('static', filename='futbal.png')
    iconovoley = url_for('static', filename='voley.png')
    iconoface = url_for('static', filename='iconoface.png')
    logoLAB = url_for('static', filename='logoLAB.png')
    fondo_index = url_for('static',  filename='fondo_index.jpg')

    return render_template('index.html', iconobaquet=iconobaquet, iconofutbal=iconofutbal, iconovoley=iconovoley, iconoface=iconoface, logoLAB=logoLAB, fondo_index=fondo_index)

@app.route('/futsal')
def futsal():
    iconobaquet = url_for('static', filename='baquet_icon.png')
    iconofutbal = url_for('static', filename='futbal.png')
    iconovoley = url_for('static', filename='voley.png')
    canchafutsal = url_for('static', filename='cancha_futsal.png')
    iconoface = url_for('static', filename='iconoface.png')
    logoLAB = url_for('static', filename='logoLAB.png')
    flecha_about = url_for('static', filename='flecha_about.png')
    imagenes_aleatorias = random.sample(logos_lic, 1)
    return render_template('futsal.html', iconobaquet=iconobaquet, iconofutbal=iconofutbal, iconovoley=iconovoley, canchafutsal=canchafutsal, iconoface=iconoface, logoLAB=logoLAB, flecha_about=flecha_about, imagenes=imagenes_aleatorias)

@app.route('/basquet')
def basquetball():
    iconobaquet = url_for('static', filename='baquet_icon.png')
    iconofutbal = url_for('static', filename='futbal.png')
    iconovoley = url_for('static', filename='voley.png')
    canchabasquet = url_for('static', filename='cancha_basquet.png')
    iconoface = url_for('static', filename='iconoface.png')
    logoLAB = url_for('static', filename='logoLAB.png')
    flecha_about = url_for('static', filename='flecha_about.png')
    imagenes_aleatorias = random.sample(logos_lic, 1)
    return render_template('basket.html', iconobaquet=iconobaquet, iconofutbal=iconofutbal, iconovoley=iconovoley,canchabasquet=canchabasquet, iconoface=iconoface, logoLAB=logoLAB, flecha_about=flecha_about, imagenes=imagenes_aleatorias)

@app.route('/voley') 
def voli():
    iconobaquet = url_for('static', filename='baquet_icon.png')
    iconofutbal = url_for('static', filename='futbal.png')
    iconovoley = url_for('static', filename='voley.png')
    iconoface = url_for('static', filename='iconoface.png')
    logoLAB = url_for('static', filename='logoLAB.png')
    flecha_about = url_for('static', filename='flecha_about.png')
    imagenes_aleatorias = random.sample(logos_lic, 1)
    return render_template('voley.html', iconobaquet=iconobaquet, iconofutbal=iconofutbal, iconovoley=iconovoley, iconoface=iconoface, logoLAB=logoLAB, flecha_about=flecha_about, imagenes=imagenes_aleatorias)

@app.route('/about')
def about():
    iconobaquet = url_for('static', filename='baquet_icon.png')
    iconofutbal = url_for('static', filename='futbal.png')
    iconovoley = url_for('static', filename='voley.png')
    iconoface = url_for('static', filename='iconoface.png')
    logoLAB = url_for('static', filename='logoLAB.png')
    flecha_about = url_for('static', filename='flecha_about.png')
    return render_template('about.html', iconobaquet=iconobaquet, iconofutbal=iconofutbal, iconovoley=iconovoley, iconoface=iconoface, logoLAB=logoLAB, flecha_about=flecha_about)

if  __name__ == '__main__':
    app.run(debug=True)
