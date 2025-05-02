from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # Define models
    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(200), nullable=False)
        tasks = db.relationship('Task', backref='user', lazy=True)

    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(120), nullable=False)
        description = db.Column(db.String(300))
        due_date = db.Column(db.String(20))
        status = db.Column(db.String(20), default='pending')
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Routes
    @app.route('/')
    def home():
        return redirect(url_for('login'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if User.query.filter_by(username=username).first():
                flash('Username already exists')
                return redirect(url_for('register'))
            hashed_pw = generate_password_hash(password)
            user = User(username=username, password=hashed_pw)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please log in.')
            return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('dashboard'))
            flash('Invalid credentials')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/dashboard')
    @login_required
    def dashboard():
        tasks = Task.query.filter_by(user_id=current_user.id).all()
        return render_template('dashboard.html', tasks=tasks)

    @app.route('/task', methods=['POST'])
    @login_required
    def add_task():
        title = request.form['title']
        description = request.form.get('description', '')
        due_date = request.form.get('due_date', '')
        task = Task(title=title, description=description, due_date=due_date, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('dashboard'))

    @app.route('/task/<int:task_id>/update', methods=['POST'])
    @login_required
    def update_task(task_id):
        task = Task.query.get_or_404(task_id)
        if task.user_id != current_user.id:
            return "Unauthorized", 403
        task.title = request.form['title']
        task.description = request.form.get('description', '')
        task.due_date = request.form.get('due_date', '')
        task.status = request.form.get('status', task.status)
        db.session.commit()
        return redirect(url_for('dashboard'))

    @app.route('/task/<int:task_id>/delete', methods=['POST'])
    @login_required
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        if task.user_id != current_user.id:
            return "Unauthorized", 403
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('dashboard'))

    return app
