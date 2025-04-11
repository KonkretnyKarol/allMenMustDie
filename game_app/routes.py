from flask import Blueprint, render_template, redirect, url_for, flash
from game_app import db, bcrypt
from game_app.models import User
from game_app.forms import RegistrationForm, LoginForm, ChangePasswordForm
from flask_login import login_user, logout_user, login_required, current_user
from game_app.models import Village

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required  # Add this decorator to ensure only logged-in users can see villages
def home():
    villages = Village.query.filter_by(owner_id=current_user.id).all()
    print(villages)
    return render_template('home.html', villages=villages)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        # Create a first village for the user
        village_name = f"{user.username}'s village"
        village = Village(name=village_name, owner_id=user.id)
        db.session.add(village)
        db.session.commit()
        
        flash('Account created successfully, and your first village has been created!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        flash('Invalid email or password', 'danger')
    return render_template('login.html', form=form)

@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))

@main_bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, form.current_password.data):
            hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            current_user.password = hashed_password
            db.session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Current password is incorrect', 'danger')
    return render_template('change_password.html', form=form)
