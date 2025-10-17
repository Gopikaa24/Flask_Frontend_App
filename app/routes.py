from flask import Blueprint, render_template, redirect, url_for, request, flash

main = Blueprint('main', __name__)

# In-memory data storage
users = []

@main.route('/')
def index():
    return render_template('index.html', users=users)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user_id = len(users) + 1
        users.append({'id': user_id, 'name': name, 'email': email})
        flash('User added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create.html')

@main.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        flash('User not found!', 'danger')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        flash('User updated successfully!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('update.html', user=user)

@main.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    flash('User deleted successfully!', 'danger')
    return redirect(url_for('main.index'))
