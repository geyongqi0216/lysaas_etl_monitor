import os
from flask import Flask, render_template, request, redirect, session
from service.filterTemplateService import login_filter
from service.pandectService import pandect_topic, pandect_table
from service.userManageService import get_login, get_update
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route("/")
def root():
    return redirect('/etlmonitor/index')


@app.route("/etlmonitor")
def default():
    return redirect('/etlmonitor/index')


@app.route("/etlmonitor/login")
def login():
    return render_template('login.html')


@app.route("/etlmonitor/logout")
def logout():
    session.clear()
    return render_template('login.html')


@app.route("/etlmonitor/newpwd", methods=['GET', 'POST'])
def newpwd():
    return get_update()


@app.route("/etlmonitor/do_login", methods=['GET', 'POST'])
def do_login():
    if request.method == "POST":
        username = request.form.get('userCode')  # 从表单中获取数据
        password = request.form.get('userPwd')
        print(username)
        print(password)
    return get_login()


@app.route("/etlmonitor/index")
def index():
    # return render_template('myindex.html')
    return render_template('datasync-topic.html', topiclist=pandect_topic())


@app.route("/etlmonitor/datasynctopic")
def datasync_topic():
    return render_template('datasync-topic.html', topiclist=pandect_topic())


@app.route("/etlmonitor/datasynctable")
def datasync_table():
    return render_template('datasync-table.html', tablelist=pandect_table())


@app.before_request
def do_filter():
    return login_filter()


# 添加过滤器，未登陆状态或登陆超时自动进入登陆页面
app.add_template_filter(login_filter, 'login_filter')
if __name__ == "__main__":
    app.run('0.0.0.0', '8485')
