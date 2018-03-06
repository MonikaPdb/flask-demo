# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 18:00:58 2018

@author: monik
"""


#specialni promena, co ukaze jmeno aktualniho modulu, to __ __ 
# bude to v kazde flaskove aplikaci

#set FLASK_APP=hello.py - neco se serverem
#set FLASK_DEBUG=1 - chci pustit ladici rezim, co zjednodusuje vyvoj te stranky
#flask run

#problem: SyntaxError: Non-UTF-8 code starting with '\x90' in file C:\Users\monik\Anaconda3\Scripts\flask.exe 
#on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
#vyreseno pres to, ze jsem vyhodila diakritiku z kodu

#vyhodilo mi to tohle:
 #Debugger is active!
 #Debugger PIN: 334-413-854
 #Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 #a zkopirovala jsem si adresu do prohlizece, a tam bylo Mi-PYT! 
 
 #spoustim to nakonec pres >python -m flask run protoze ten nahore mi nefungoval kvuli encoding
 
#UDELAM CHYBU DO KODU
#1/0 A KDYZ TO PROJEDU, TAK MI TO HODI CHYBOVE HLASKY NA TE WEBOVE STRANCE

#FLASK DEBUG
#na strance muzu v jednotlivych castich kodu poustet konzoli - pres tu ikonku terminalu, kde musim zadat
#pin, co mam v logu v cmd

#pokud to vypnu v cmd prikazem ctrl+c tak se mi ta stranka s textem nenacte
#pak zase spustim pomoci >python -m flask run
 
#ono je to vlastne cele takovy server, ta adresa v url je server + nejake nase veci dole - v tech lomitkach


from flask import Flask, url_for, render_template


app = Flask(__name__)

@app.template_filter('cap')
def capitalize(word):
    return word[0].upper() + word[1:]


@app.route('/')
def index():
    return 'Hello PyLadies!'

# musi tam byt jmeno funcke, v mem pripade hi :}
# external mi ukaze celou tu adresu
# kykoliv budeme chtit vytvorit adresu v ramci stranek, pouzijte funkci url_for, nestrkat tam jen tak tu adresu
    # protoze pak se to zmeni a bude z toho bordeeeel
@app.route('/url/')
def url():
    return url_for('hello', name='Monca', count=3, _external=True)

# chci dalsi stranku, co najdu na adrese http://127.0.0.1:5000/hello/
@app.route('/hello/')
#def hello():
 #   return 'Tadadada!' - Pokud to bude zakrizkovane, tak mi to bude obsluhovat oboji, musim, ale nastavit defaultni jmeno - zde word

# dynamicka cesta, muzu menit tu polozku, co mam v <name> - v tom name nesmi mit kupodivu lomitko
# html dokument musi byt ve slozce templates, slozka musi vyt ve stejnem adresari jako tenhle dokument
# go back home me hodi na /hello/
 #capitalzie proto, aby me to zdravilo pekne
@app.route('/hello/<name>/')
@app.route('/hello/<name>/<int:count>/')
def hello(name=None, count = 1):
    return  render_template('hello.html', name=name)


# pro staticke soubory - css, obrazky nemusim psat slozite veci, dam si ty soubory do specialniho adresar static a 
# flask mi sam ty obrazky dam


