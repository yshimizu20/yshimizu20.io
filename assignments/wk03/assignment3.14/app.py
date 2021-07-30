from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    title = 'Choose Adventure'
    text = 'Choose the stage you want to play'

    choices = [
        ('level1', 'Moon'),
        ('level2', 'Mars'),
    ]

    img_path = url_for('static', filename='img1.jpeg')

    return render_template('template.html', title=title, text=text, choices=choices, img_path=img_path)

@app.route('/moon')
def level1():
    title = 'You fly to the moon...'
    text = 'Suddenly, you are thrown out of the spaceship.'

    choices = [
        ('fix', 'Run back to the spaceship'),
        ('explore', 'Explore the planet')
    ]

    img_path = url_for('static', filename='img2.jpeg')

    return render_template('template.html', title=title, text=text, choices=choices, img_path=img_path)

@app.route('/failure')
def run_away():
    title = 'No oil'
    text = 'Mission failed.'
    choices = []

    img_path = url_for('static', filename='img3.jpeg')

    return render_template('template.html', title=title, text=text, choices=choices, img_path=img_path)

@app.route('/complete')
def run_away2():
    title = 'Clear'
    text = 'Mission complete!'
    choices = []

    img_path = url_for('static', filename='img4.jpeg')

    return render_template('template.html', title=title, text=text, choices=choices, img_path=img_path)

@app.route('/fix')
def fix():
    title = 'Fix spaceship'
    text = 'The oil tank is broken and oil is flowing out.'
    choices = [
        ('run_away', 'Fly back with broken tank'),
        ('explore', 'Explore the planet to find something to fix the tank')
    ]

    img_path = url_for('static', filename='img5.jpeg')

    return render_template('template.html', title=title, text=text, choices=choices, img_path=img_path)

@app.route('/explore')
def explore():
    title = 'Explore the planet'
    text = 'You found some clay on the hill.'
    choices = [
        ('fix2', 'Might lead to a significant academic discovery. Bring some with you to the spaceship'),
        ('fix', 'It might be dangerous. Don\'t touch it and return to the spaceship')
    ]

    img_path = url_for('static', filename='img6.jpeg')

    return render_template('template.html', title=title, text=text, choices=choices, img_path=img_path)

@app.route('/fix2')
def fix2():
    title = 'Fix spaceship'
    text = 'You return to the spaceship and the oil tank is broken and oil is flowing out.'
    choices = [
        ('run_away', 'Fly back with broken tank'),
        ('run_away2', 'Use the clay to fix the tank'),
    ]

    img_path = url_for('static', filename='img7.jpeg')

    return render_template('template.html', title=title, text=text, choices=choices, img_path=img_path)

@app.route('/mars')
def level2():
    title = 'Mars quest'
    text = 'The level2 quest has not been released yet.'
    choices = []

    img_path = url_for('static', filename='img1.jpeg')

    return render_template('template.html', title=title, text=text, choices=choices, img_path=img_path)
