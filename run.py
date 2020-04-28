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

@app.route("/form-veiculo")
def form_veiculo():
    return render_template('form-veiculo.html')

@app.route("/form-banco")
def form_banco():
    return render_template('form-banco.html')

@app.route("/form-agencia")
def form_agencia():
    return render_template('form-agencia.html')

@app.route("/form-conta-corrente")
def form_conta_corrente():
    return render_template('form-conta-corrente.html')

@app.route("/form-conta-caixa")
def form_conta_caixa():
    return render_template('form-conta-caixa.html')

    

if __name__ == "__main__":
    app.run()



