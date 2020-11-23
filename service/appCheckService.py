from flask import request
from dao.AppCheckDao import selCheckByAppid, selCheckAppid, insCheckInfo, updCheckById
from domain.appCheckDomain import AppCheckBean, AppCheckDetailBean, AppCheckInsBean, AppCheckUpdBean


def addCheckInfo():
    # 从前端中获取数据
    check_object = request.form.get('check_object')    # 获取主题名称
    app_id = request.form.get('app_id')     # 获取主题id
    check_logic = request.form.get('check_logic')   # 获取检查项目
    check_result = request.form.get('check_result')     # 获取逻辑说明
    check_sql = request.form.get('check_sql')   # 获取执行SQL
    check_info = AppCheckInsBean(check_object, app_id, check_logic, check_result, check_sql)
    insCheckInfo(check_info)
    return


def editCheckById():
    # 从前端中获取数据
    appcheackid = request.form.get('appcheackid')   # 获取检查项目id
    check_object = request.form.get('check_object')  # 获取主题名称
    app_id = request.form.get('app_id')     # 获取主题id
    check_logic = request.form.get('check_logic')   # 获取检查项目
    check_result = request.form.get('check_result')     # 获取逻辑说明
    check_sql = request.form.get('check_sql')   # 获取执行SQL
    check_info = AppCheckUpdBean(appcheackid, check_object, app_id, check_logic, check_result, check_sql)
    updCheckById(check_info)
    return


def getCheckInfo():
    appchecklist = []
    # 查询所有主题信息
    appCheckInfoList = selCheckAppid()
    # 循环所有主题信息
    for appCheckInfo in appCheckInfoList:
        # 根据主题信息查询t_check所有详情信息
        checkList = selCheckByAppid(appCheckInfo[0])
        appCheckDetaillist = []
        # 循环此主题t_check详情信息
        for check in checkList:
            appCheckDetail = AppCheckDetailBean(check[0], check[1], check[2], check[3], check[4], check[5], check[6], check[7])
            appCheckDetaillist.append(appCheckDetail)
        # 将主题信息和相对的详情信息打包成对象
        appcheck = AppCheckBean(appCheckInfo[0], appCheckInfo[1], appCheckDetaillist)
        # 传进最后appchecklist中
        appchecklist.append(appcheck)
    return appchecklist


if __name__ == '__main__':
    appchecklist = getCheckInfo()
    for appcheck in appchecklist:
        print(appcheck.app_id,appcheck.app_name,appcheck.checkdetaillist)
