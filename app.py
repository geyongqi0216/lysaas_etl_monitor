import os
from flask import Flask, render_template, redirect, session

from service.appCheckService import getAppCheckList, editAppCheck
from service.pandectService import pandect_topic, pandect_table
from service.userManageService import editUserPsw, doLogin
from service.filterTemplateService import login_filter

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route("/")
def root():
    return redirect('/etlmonitor/index')


@app.route("/etlmonitor")
def default():
    return redirect('/etlmonitor/index')


@app.route("/etlmonitor/index")
def index():
    # return render_template('myindex.html')
    return redirect('/etlmonitor/datasynctopic')


@app.route("/etlmonitor/login")
def login():
    return render_template('login.html')


@app.route("/etlmonitor/do_login", methods=['GET', 'POST'])
def do_login():
    return doLogin()


@app.route("/etlmonitor/newpwd", methods=['GET', 'POST'])
def newpwd():
    return editUserPsw()


@app.route("/etlmonitor/logout")
def logout():
    session.clear()
    return render_template('login.html')


@app.route("/etlmonitor/datasynctopic")
def datasync_topic():
    return render_template('datasync-topic.html', topiclist=pandect_topic())


@app.route("/etlmonitor/datasynctable")
def datasync_table():
    return render_template('datasync-table.html', tablelist=pandect_table())


@app.route("/etlmonitor/datasyncappcheck")
def datasync_appcheck():
    return render_template('datasync-appcheck.html', appchecklist=getAppCheckList())


@app.route("/etlmonitor/datasyncappcheckeedit", methods=['GET', 'POST'])
def datasync_appcheckedit():
    return editAppCheck()


# @app.before_request
# def do_filter():
#     return login_filter()


# 添加过滤器，未登陆状态或登陆超时自动进入登陆页面
app.add_template_filter(login_filter, 'login_filter')
if __name__ == "__main__":
    app.run('0.0.0.0', '8000')
