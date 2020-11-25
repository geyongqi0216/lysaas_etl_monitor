from flask import request, render_template
from dao.AppCheckDao import selCheckByAppId, selCheckApp, insCheckInfo, updCheckById
from domain.appCheckDomain import AppCheckBean, AppCheckEntity, AppCheckInsBean, AppCheckUpdBean, AppIdNameBean
from enum import Enum


class ReturnInfoEnum:
    class Edit(Enum):
        upd_error = '编辑失败'
        upd_success = '编辑成功'

    class Add(Enum):
        ins_success = '添加成功'
        ins_error = '添加失败'


# 添加check信息
def addCheckInfo():
    # 从前端中获取数据
    check_object = request.form.get('check_object')   # 获取主题名称
    app_id = request.form.get('app_id')     # 获取主题id
    check_used = request.form.get('check_used')     # 获取是否有效
    check_logic = request.form.get('check_logic')   # 获取检查项目
    check_result = request.form.get('check_result')     # 获取逻辑说明
    check_sql = request.form.get('check_sql')   # 获取执行SQL
    appcheckinsbean = AppCheckInsBean(check_object, app_id, check_used, check_logic, check_result, check_sql)
    result = insCheckInfo(appcheckinsbean)
    if result == 1:
        return render_template('datasync-appcheck.html', errorInfo=ReturnInfoEnum.Add.ins_seccess.value)
    return render_template('datasync-appcheck.html', errorInfo=ReturnInfoEnum.Add.ins_error.value)


# 修改check信息
def editCheckById():
    # 从前端中获取数据
    appcheackid = request.form.get('appcheackid')   # 获取检查项目id
    check_object = request.form.get('check_object')  # 获取主题名称
    app_id = request.form.get('app_id')     # 获取主题id
    check_used = request.form.get('check_used')  # 获取是否有效
    check_logic = request.form.get('check_logic')   # 获取检查项目
    check_result = request.form.get('check_result')     # 获取逻辑说明
    check_sql = request.form.get('check_sql')   # 获取执行SQL
    appcheckupdbean = AppCheckUpdBean(appcheackid, check_object, app_id, check_used, check_logic, check_result, check_sql)
    result = updCheckById(appcheckupdbean)
    if result == 1:
        return render_template('datasync-appcheck.html', errorInfo=ReturnInfoEnum.Edit.upd_seccess.value)
    return render_template('datasync-appcheck.html', errorInfo=ReturnInfoEnum.Edit.upd_error.value)


# 查询所有check信息
def getCheckInfo():
    appchecklist = []
    # 查询所有主题信息
    appCheckInfoList = selCheckApp()
    # 循环所有主题信息
    for appCheckInfo in appCheckInfoList:
        # 根据主题信息查询t_check所有详情信息
        appidnamebean = AppIdNameBean(appCheckInfo[0], appCheckInfo[1])
        checklist = selCheckByAppId(appidnamebean)
        appcheckdetaillist = []
        # 循环此主题t_check详情信息
        for check in checklist:
            appcheckentity = AppCheckEntity(check[0], check[1], check[2], check[3], check[4], check[5], check[6], check[7])
            appcheckdetaillist.append(appcheckentity)
        # 将主题信息和相对的详情信息打包成对象
        appcheck = AppCheckBean(appidnamebean.app_id, appidnamebean.app_name, appcheckdetaillist)
        # 传进最后appchecklist中
        appchecklist.append(appcheck)
    return appchecklist


if __name__ == '__main__':
    appchecklist = getCheckInfo()
    print(appchecklist)
    for i in appchecklist:
        print(i.app_name, i.app_id)
        for each in i.checkdetaillist:
            print(each.id, each.check_object, each.app_id, each.app_name, each.check_used, each.check_logic, each.check_result, each.check_sql)
