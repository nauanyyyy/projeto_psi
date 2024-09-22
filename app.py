from flask import Flask, render_template, redirect, url_for, request, session
#from login_config import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
#from mail_config import Mail, Message
from flask_mail import Mail, Message
from models import db, User, Resource
from config import Config
import smtplib

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db.init_app(app)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first() #ESTÁ DANDO ERRO NESSA LINHA.
        if user and check_password_hash(user.password, password):
            login_user(user)  # Substituindo session por login_user
            return redirect(url_for('index'))
        else:
            return 'Login inválido'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        # Envio de email após o cadastro
        msg = Message('Bem-vindo ao Sistema', recipients=[email])
        msg.body = 'Obrigado por se registrar!'
        mail.send(msg)

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/manage_resources')
def manage_resources():
    resources = Resource.query.all()
    return render_template('manage_resources.html', resources=resources)

@app.route('/resources')
def list_resources():
    resources = Resource.query.all()  # Obter todos os recursos
    return render_template('manage_resources.html', resources=resources)

@app.route('/resource/<int:id>')
def resource_detail(id):
    resource = Resource.query.get_or_404(id)
    return render_template('resource_detail.html', resource=resource)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)