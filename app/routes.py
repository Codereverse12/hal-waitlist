from flask import render_template, redirect, url_for
from app import app, db
from app.forms import WaitlistForm
import sqlalchemy as sa
from app.models import Subscriber

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = WaitlistForm()
    if form.validate_on_submit():
        subscriber = Subscriber(email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', title="Waitlist", form=form)

@app.route('/success')
def success():
    return render_template('success.html', title="Success")