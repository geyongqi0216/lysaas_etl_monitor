from flask import Flask
from flask import render_template
from flask import redirect,url_for
from service.pandect import *
app = Flask(__name__)

# 视图函数 总览页面


@app.route("/etlmonitor")
def default():
    return redirect('/etlmonitor/index')

@app.route("/etlmonitor/index")
def index():
    #pendect()
    return render_template('myindex.html', table_name='app_order')


@app.route("/etlmonitor/datasync-topic")
def datasync_topic():
    date=pandect()
    print(date.topicname[0])
    topiclist = []
    topiclist.append(date)
    return render_template('datasync-topic.html',topiclist=topiclist)

@app.route("/etlmonitor/datasync-table")
def datasync_table():
    return render_template('datasync-table.html')


if __name__ == "__main__":
    app.run('127.0.0.1', '8000')




