from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db, login
from utils.models import Users


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/add_user', methods=["POST", "GET"])
@login_required
def add_user():
    if current_user.statuse == "Learner":
        return redirect(url_for('index'))
    if request.method == "POST":
        usernamec = request.form['username']
        passwordc = request.form['password']
        namec = request.form['name']
        subnamec = request.form['subname']
        shoolc = request.form['shool']
        numclassc = request.form['numclass']
        bclassc = request.form['bclass']
        statusec = request.form['statuses']
        if len(usernamec) == 0 or len(passwordc) == 0 or len(namec) == 0 or len(subnamec) == 0 or len(shoolc) == 0 or len(numclassc) == 0 or len(bclassc) == 0 or len(statusec) == 0:
            flash("Одно из полей не заполнено!", "alert-danger")
        else:
            userdb = Users.query.filter_by(username=usernamec).first()
            if userdb != usernamec:
                resultuser = Users(username=usernamec, name=namec, subname=subnamec, shool=shoolc, classs=f"{numclassc} {bclassc}", statuse=statusec)
                resultuser.set_password(passwordc)
                db.session.add(resultuser)
                db.session.commit()
                flash(f"Пользователь {usernamec}, {namec} {subnamec} успешно добавлен в базу данных, ура!", "alert-success")
            else:
                flash(f"Логин {usernamec} уже есть в базе данных!", "alert-danger")
    title = "SDnevnik | Добавление пользователя"
    return render_template("add_user.html", title=title)

@app.route('/add_shool', methods=["POST", "GET"])
@login_required
def add_shool():
    if current_user.statuse == "Learner":
        return redirect(url_for('index'))
    title = "SDnevnik | Добавление пользователя"
    return render_template("add_user.html", title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form['username']).first()
        if user is None or not user.check_password(request.form['password']):
            flash('Неправильный логин или пароль.', category="alert-danger")
            return redirect(url_for('login'))
        login_user(user, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('user', username=request.form["username"])
        return redirect(next_page)
    return render_template('auth.html', title='SDnevnik | Авторизация')

@app.route('/user/<username>')
@login_required
def user(username):
    user = Users.query.filter_by(username=username).first_or_404()
    title = f"SDnevnik | Профиль {user.name} {user.subname}"

    return render_template('profiles.html', user=user, title=title)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))