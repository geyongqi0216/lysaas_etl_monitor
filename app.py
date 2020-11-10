from flask import Flask
from flask import render_template
app = Flask(__name__)

# 视图函数 总览页面


@app.route("/")
def index():
    #pendect()
    return render_template('myindex.html', table_name='app_order')


@app.route("/datasync-topic")
def datasync_topic():
    return render_template('datasync-topic.html')


if __name__ == "__main__":
    app.run('127.0.0.1', '8000')




