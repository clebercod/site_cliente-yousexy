from flask import Flask,render_template

app = Flask(__name__)

# primeira pagina
# route 
#funcao
@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')



# colocar a pagina no ar
if __name__ == '__main__':
 app.run()
    



