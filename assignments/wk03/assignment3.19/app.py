from flask import Flask, render_template, url_for
import string
app = Flask(__name__)

@app.route('/words/')
def home():
    words = []
    prefix_len = 0
    return render_template('home.html', alphabets=string.ascii_uppercase)

@app.route('/words/<string:prefix>')
def anagram(prefix):
    words = []
    alphabets = []
    prefix_len = len(prefix)
    word_count = 0
    with open('words.txt', 'r') as f:
        word_list = f.read().splitlines()
        if prefix.upper() in word_list:
            is_word=True
        else:
            is_word=False
        for word in word_list:
            if len(word) > prefix_len:
                if word[:prefix_len] == prefix.upper():
                    words.append(word.upper())
                    word_count += 1
                    wd = prefix.upper()+word[prefix_len].upper()
                    if wd not in alphabets:
                        alphabets.append(wd)
    return render_template('main.html', is_word=is_word, prefix=prefix, word_count=word_count, words=words, alphabets=alphabets)