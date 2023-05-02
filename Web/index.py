from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')  

@app.route('/descargar')
def descargar():
    return render_template('descargar.html')   

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')   

@app.route('/noticias')
def noticias():
    return render_template('inicio_users_regi.html')   

@app.route('/home')
def homePrincipal():
    return render_template('home.html')   
     

if __name__ == '__main__':
    app.run(port=8000,debug=True)
    
    