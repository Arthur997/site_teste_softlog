from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/painel")
def painel():
    return render_template('painel.html')

@app.route("/form-cliente")
def form_cliente():
    return render_template('form-cliente.html')

@app.route("/form-filial")
def form_filial():
    return render_template('form-filial.html')

@app.route("/form-empresa")
def form_empresa():
    return render_template('form-empresa.html')

if __name__ == "__main__":
    app.run()



