from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        estado = request.form['estado']
        estado = estado.lower()
        cidade = request.form['cidade']
        cidade = cidade.lower()
        url = f'https://www.cptec.inpe.br/{estado}/{cidade}'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        element = soup.find(class_ = 'bloco-previsao d-flex flex-column text-center') 
        temperatures = element.select('label')
        normallist = []
        for i in temperatures: 
            q = (f"{i}")
            normallist.append(q[31:34])
        max_temp = normallist[0]
        min_temp = normallist[1]
        return render_template('/searcher.html', max_temp=max_temp, min_temp = min_temp, cidade=cidade, estado=estado)
    else:
        return render_template('index.html')

app.route('/searcher.html', methods=["GET", "POST"])
def searcher():
    if request.method == "POST":
        return render_template('/')
    else:
        return render_template('/searcher.html')

if __name__ == ("__main__"):
    app.run(debug=True)