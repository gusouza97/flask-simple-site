from flask import Flask, render_template

app = Flask(__name__)

# Paginas no Flask
# route -> link que sera aberto no seu site
# funcao -> o que vc quer exibir naquela pagina
# template

@app.route("/")
def homepage():
    # Retornando uma mensagem no navegador, quando acessa a rota
    return render_template("homepage.html")

@app.route("/contato")
def contatos():
    # Retornando os contatos
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# Colocando site no ar
if __name__ == "__main__":
    # Esse debug é importante para atualizar o site sempre que houver alterações
    app.run(debug=True)