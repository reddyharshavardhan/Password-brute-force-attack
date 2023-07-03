
from flask import *

app= Flask(__name__)

@app.route("/admin")
def admin():
    return 'this is admin'


@app.route("/student")
def student():
    return 'this is student'


@app.route("/staff")
def staff():
    return 'this is staff'
@app.route('/user,name.')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    if name=='school':
        return redirect(url_for('school'))
    if name=='staff':
        return redirect(url_for('staff'))
if __name__== "__main__":
    app.run("127.0.0.1",8080)
