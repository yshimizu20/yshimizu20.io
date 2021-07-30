from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'Choose Adventure'
    text = 'Choose the stage you want to play'

    choices = [
        ('level1', 'Moon'),
        ('level2', 'Mars'),
    ]

    return render_template('template.html', title=title, text=text, choices=choices)

@app.route('/moon')
def level1():
    title = 'You fly to the moon...'
    text = 'Suddenly, you are thrown out of the spaceship.'

    choices = [
        ('fix', 'Run back to the spaceship'),
        ('explore', 'Explore the planet')
    ]

    return render_template('template.html', title=title, text=text, choices=choices)

@app.route('/failure')
def run_away():
    title = 'No oil'
    text = 'Mission failed.'
    choices = []

    return render_template('template.html', title=title, text=text, choices=choices)

@app.route('/complete')
def run_away2():
    title = 'Clear'
    text = 'Mission complete!'
    choices = []

    return render_template('template.html', title=title, text=text, choices=choices)

@app.route('/fix')
def fix():
    title = 'Fix spaceship'
    text = 'The oil tank is broken and oil is flowing out.'
    choices = [
        ('run_away', 'Fly back with broken tank'),
        ('explore', 'Explore the planet to find something to fix the tank')
    ]
    return render_template('template.html', title=title, text=text, choices=choices)

@app.route('/explore')
def explore():
    title = 'Explore the planet'
    text = 'You found some clay on the hill.'
    choices = [
        ('fix2', 'Might lead to a significant academic discovery. Bring some with you to the spaceship'),
        ('fix', 'It might be dangerous. Don\'t touch it and return to the spaceship')
    ]
    return render_template('template.html', title=title, text=text, choices=choices)

@app.route('/fix2')
def fix2():
    title = 'Fix spaceship'
    text = 'You return to the spaceship and the oil tank is broken and oil is flowing out.'
    choices = [
        ('run_away', 'Fly back with broken tank'),
        ('run_away2', 'Use the clay to fix the tank'),
    ]
    return render_template('template.html', title=title, text=text, choices=choices)

@app.route('/mars')
def level2():
    title = 'Mars quest'
    text = 'The level2 quest has not been released yet.'
    choices = []

    return render_template('template.html', title=title, text=text, choices=choices)
