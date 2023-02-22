from flask import Flask

app = Flask(__name__)

# primeira pagina
# route 
#funcao
@app.route("/")
def homepage():
    return 'agora vai'




# colocar a pagina no ar
if __name__ == '__main__':
 app.run()
    

