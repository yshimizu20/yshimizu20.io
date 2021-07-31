from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/fizzbuzz/<int:n>')
def fizzbuzz(n):
    numbers = []
    for i in range(1,n+1):
        if i%15 == 0:
            numbers.append('fizzbuzz')
        elif i%3 == 0:
            numbers.append('fizz')
        elif i%5 == 0:
            numbers.append('buzz')
        else:
            numbers.append(i)

    return render_template('main.html', n=n, numbers=numbers)