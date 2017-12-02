import getname as getname
from flask import Flask
from flask import render_template,redirect,request,url_for,session
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY']='aRFQWE34hjYUfrgtAfertA'
db = SQLAlchemy(app)


class User(db.Model):
    id=db.Column('id', db.Integer, primary_key=True)
    correo = db.Column(db.String(100))
    usuario = db.Column(db.String(100))
    passwd = db.Column(db.String(100))

    def __init__(self,usuario, passwd,correo):
        self.correo = correo
        self.usuario = usuario
        self.passwd = passwd

@app.route('/',methods=['GET','POST'])
def index():
    """Control de Secion"""
    #Para traer todo se coloca all()
    #consulta = User.query.all()
    #for usu in consulta:
    #    print(usu.usuario, usu.passwd)
    #para filtrar los datos que se quieres traer se utilixa filter
    #consulta2 = db.session.query(User).\
    #    filter(User.usuario == 'jose').first()
    #print(consulta2.id, consulta2.passwd)
    #for usu in consulta2:
    #    print(usu.usuario, usu.passwd)
    #print(consulta[0].usuario)

    if not session.get('logged_in'):
        print('llegue al index')
        return render_template('index.html')
    else:
        if request.method == 'POST':
            print('si debe estar logeado')
            return render_template('index.html')
        nombre = session.get('usuario')
        return render_template('index.html',nombre=nombre)

@app.route('/login',methods=['GET','POST'])
def login():
    """Pasos para el login"""
    #1 este if es para ver si al ingresar a la pagina estoy logiado o no
    if request.method == 'GET':
        return render_template('login.html')
    else:
        correo = request.form['correo']
        pwd = request.form['pwd']
        try:
            data = User.query.filter(User.correo==correo,User.passwd==pwd).first()
            if data is not None:
                session['logged_in'] = True
                session['usuario'] = data.usuario
                print('login debe ser true')
                return redirect(url_for('index'))
            else:
                error = 1
                return  render_template('login.html',error=error)
        except Exception as e:
            print('exception: ',e)
            error = 2
            return render_template('login.html',error=error)

@app.route('/registro',methods=['GET','POST'])
def registro():
    """formulario de registro"""
    if request.method == 'POST':
        nuevo_usuario = User(request.form['user'],request.form['pwd'],request.form['correo'])
        db.session.add(nuevo_usuario)
        db.session.commit()
        return render_template('login.html')
    return render_template('registro.html')

@app.route('/logout',methods = ['GET','POST'])
def logout():
    """Cerrar Sesion"""
    session['logged_in'] = False
    return redirect(url_for('index'))
