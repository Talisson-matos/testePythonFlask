from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")
    
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/usuario/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)



if __name__=="__main__":
    app.run(debug=True)