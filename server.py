from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html",row=8,col=8,color1='red',color2='black')

@app.route('/<int:x>')
def boardHeight(x):
    return render_template("index.html",row=x,col=8,color1='red',color2='black')

@app.route('/<int:x>/<int:y>')
def newBoard1(x,y):
    return render_template("index.html",row=x,col=y,color1='red',color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>')
def newBoard2(x,y,color1):
    return render_template("index.html",row=x,col=y,color1=color1,color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def newBoard3(x,y,color1,color2):
    return render_template("index.html",row=x,col=y,color1=color1,color2=color2)

# @app.route('/<int: num1>/<int: num2>/<string: color1>')

if __name__=='__main__':
    app.run(debug=True)