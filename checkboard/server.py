from operator import index
from time import time
from flask import Flask, render_template 

#----------------------------1-halloworld

app = Flask(__name__)    
# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/<color>')
def checkboard(color):
    col = f"style = 'background-color: {color}; '"
    return render_template("index.html",boardx=8,boardy=8,flag=1,col=col)

@app.route('/<int:boardx>')
def checkboardby8(boardx):
    boardx=int(boardx/2)
    col = f"style = 'background-color: blue; '"
    return render_template("index.html",boardx=boardx,boardy=boardx,flag=0,col=col)


@app.route('/<int:boardx>/<int:boardy>')
def checkboarddef(boardx,boardy):
    col = f"style = 'background-color: blue; '"
    return render_template("index.html",boardx=int(boardx),boardy=int(boardy),flag=0,col=col)



@app.route('/ali/<int:age>')
def chechyourage(age): 
    col = f"style = 'background-color: blue; '"
    return render_template("index.html",boardx=int(age),boardy=int(age),flag=0,col=col)

if __name__=="__main__":   
    app.run(debug=True)    

