from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scr_system.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

class ChangeRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Routes
@app.route('/')
def index():
    change_requests = ChangeRequest.query.all()
    return render_template('index.html', change_requests=change_requests)

@app.route('/new', methods=['GET', 'POST'])
def new_request():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        user_id = 1  # Assuming the user ID for now

        new_request = ChangeRequest(title=title, description=description, priority=priority, user_id=user_id)
        db.session.add(new_request)
        db.session.commit()
        flash('Change request submitted successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('new_request.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
