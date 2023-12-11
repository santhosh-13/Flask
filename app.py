from flask import Flask,redirect,url_for

## WSGI Application
app=Flask(__name__)
## this is decorator it will define how many urls are there in that
@app.route('/')
def welcome():
    return 'Hi all.I am learning Flask'
@app.route('/success/<int:score>')
def success(score):
    return "i has passed with"+ str(score)
@app.route('/failed/<int:score>')
def failed(score):
    return "i have failed with"+ str(score)
@app.route('/results/<int:marks>')
def results(marks):
    res=""
    if(marks<30):
        res='failed'
    else:
        res='success'
    return redirect(url_for(res,score=marks))



if __name__=='__main__':
    app.run(debug=True)



