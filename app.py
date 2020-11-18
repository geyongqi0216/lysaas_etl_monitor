from flask import Flask, render_template, request, redirect, session, url_for
from service.pandect import *
app = Flask(__name__)
app.debug = True  # 自动重启
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'

# 视图函数 总览页面

USERS = {
    1: {'name': '大白', 'age': '18', 'gender': '男', 'text': '非常可爱'},
    2: {'name': '小白', 'age': '20', 'gender': '男', 'text': '非常暖'},
    3: {'name': '张三', 'age': '21', 'gender': '女', 'text': '天下第一美'},
    4: {'name': '王五', 'age': '20', 'gender': '女', 'text': '帝国理工宅女'},
}


@app.route('/')
def hello():
    return render_template('login.html')


@app.route('/detail/<int:nid>', methods=['GET'])  # 动态url传入一个值
def detail(nid):
    user = session.get('user_info')
    if not user:
        url = url_for('l1')  # 根据别名生成url
        return redirect(url)
    info = USERS[nid]
    return render_template('detail.html', info=info)  # html 文件放在templates文件夹


@app.route('/login', methods=['GET', 'POST'], endpoint='l1')  # endpoint 表示别名
def login():
    get_login()


@app.route('/register_go', methods=['GET', 'POST'])
def enroll_go():
    return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])
def enroll():
    get_register()


@app.route('/register_ok', methods=['GET', 'POST'])
def enroll_ok():
    return render_template('login.html')


@app.route('/index', methods=['GET', 'POST'], endpoint='l2')
def index():
    user = session.get('user_info')
    if user is None:
        return redirect('/login')  # 跳转到登录页
    return render_template('index.html', user_dict=USERS)


# @app.route("/")
# def root():
#     return redirect('/etlmonitor/index')

@app.route("/etlmonitor")
def default():
    return redirect('/etlmonitor/index')


@app.route("/etlmonitor/index")
def index():
    return render_template('myindex.html')


@app.route("/etlmonitor/datasync-topic")
def datasync_topic():
    return render_template('datasync-topic.html', topiclist=pandect_topic())


@app.route("/etlmonitor/datasync-table")
def datasync_table():
    return render_template('datasync-table.html', tablelist=pandect_table())


if __name__ == "__main__":
    app.run('0.0.0.0', '8000')




