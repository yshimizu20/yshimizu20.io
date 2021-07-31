from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/words/<string:word>')
def anagram(word):
    anagrams = []
    with open('words.txt', 'r') as f:
        word_list = f.read().splitlines()
        if word.upper() not in word_list:
            return render_template('main.html', word=word, exist=False, anagrams=anagrams)
        for w in word_list:
            if sorted(w) == sorted(word.upper()):
                anagrams.append(w)
    return render_template('main.html', word=word, exist=True, anagrams=anagrams)