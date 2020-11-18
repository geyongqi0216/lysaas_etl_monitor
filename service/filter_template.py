import datetime
from flask import session, request, url_for
from werkzeug.utils import redirect


def login_filter():
    isallow = False
    ue = session.get("user.effective")
    if ue is not None and ue > str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        session['user.effective'] = (datetime.datetime.now() + datetime.timedelta(minutes=int(30))).strftime("%Y-%m-%d %H:%M:%S")
        isallow = True
    else:
        fullpath = request.path
        pathsp = fullpath.split("/")
        allowvisit = {"etlmonitor": {"forget", "register", "login", "do_login"}, "static": {}}
        allowlist = allowvisit.get(pathsp[1])
        if allowlist is not None:
            if len(allowlist) > 0:
                for page in allowlist:
                    if len(pathsp)>2 and pathsp[2] == page:
                        isallow = True
            else:
                isallow = True
    if not isallow:
        return redirect(url_for('login'))
