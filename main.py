from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversao_moeda', methods=['POST'])
def converter_moeda():
    valor = float(request.form['valor'])

    conversao = valor / 6.44

    return render_template('index.html', conversao = conversao)

if __name__ == '__main__':
    app.run(debug=True)