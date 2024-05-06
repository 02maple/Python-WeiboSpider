import re

from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)
app.secret_key = 'hi,secretKey'

from views.page import page
from views.user import user
app.register_blueprint(page.pb)
app.register_blueprint(user.ub)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/<path:path>')
def catch_all(path):
    return render_template('404.html')

@app.before_request
def before_request():
    pat = re.compile(r'^static')
    # 静态目录文件，不做处理
    if re.search(pat, request.path):
        return
    elif request.path == '/user/login' or request.path == '/user/register':
        return
    elif session.get('username'):
        return
    return redirect('/user/login')



if __name__ == '__main__':
    app.run()
