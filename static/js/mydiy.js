
//当前页所在菜单的样式
//var fullpath=window.location.pathname;
//var fullpathsplit=fullpath.split('/');
//var proname=fullpathsplit[1];
//var providerCode=getQueryVariable('providerCode')== false ? '': '-'+getQueryVariable('providerCode');
//var dtlmenu=fullpathsplit[fullpathsplit.length-1].split('.')[0];
//var submenu=dtlmenu.split('-')[0];
//
//$('#'+submenu).addClass(' active ');
//document.getElementById(submenu).getElementsByTagName('ul')[0].style='display: none';
//if($('#'+dtlmenu).html()!=null){
//$('#'+dtlmenu).addClass(' active ');
//}

//当前菜单样式
    var fullpath=window.location.pathname;
	var fullpathsplit=fullpath.split('/');
	var flength = fullpathsplit.length;
	var menuinfo= fullpathsplit[flength-1]
	var submenu=menuinfo.split('-')[0];
	var dtlmenu=menuinfo.split('-')[1];
	$('#'+submenu).addClass(' active open')
	document.getElementById(submenu).getElementsByTagName('ul')[0].style='display:block';
	$('#'+dtlmenu).addClass('active');

//获取当前url的查询参数
function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}

//清空密码重置框
function passwordinfoPopJs() {
	$('#passwordForm-oldpsd').val();
	$('#passwordForm-newpsd').val();
	$('#passwordForm-repsd').val();
}

//设置页面时间空间
setInterval(function () {
    var date = new Date();
    var h = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
    var mm = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
    var s = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
    var time = h + ":" + mm + ":" + s;
    $("#p").html(time);
}, 500);


var returnInfo = $('#returnInfo').text();
if(returnInfo!=null&&$.trim(returnInfo))
{
	 $('#returnInfoLink')[0].click();
}

function addappcheckconfig(appid,appcheckid) {
    $('#appcheckForm').attr("action","./datasyncappcheckeedit");
    $('#appcheckpop').removeAttr("hidden");
    $('#appcheck_id').val("0");
    $('#app_id').removeAttr("disabled");
    //恢复默认选择第一个
    $('#app_id option:first').prop('selected', 'selected');
    $('#appchecktitle').text("");
    $('#checkinfo').text("");
    $('#appid').val("");
    $('#check_object').val("");
    $('#check_logic').val("");
    $('#check_result').val("");
    $('#check_sql').val("");
    //初始化是否使用状态
    $('#check_used_lab_1').click();
    $('#check_used_rad_0').click();
    $('#check_used_lab_0').click();
    $('#check_used_rad_1').click();
    if(appcheckid==""){
        //$('#appckeckid').attr("hidden","hidden");//此项目前不关闭,显示在外
        $('#appchecktitle').text("新建主题检查规则");
    }
    else{
        $('#appchecktitle').text("【"+$('#app_name-'+appid).text()+"】");
        $('#appcheck_id').val(appcheckid);
        $('#app_id').val($('#app_id-'+appid).val());
        $('#app_id').attr("disabled","");
        $('#check_object').val($('#check_object-'+appid+'-'+appcheckid).text());
        $('#check_result').val($('#check_result-'+appid+'-'+appcheckid).text());
        $('#check_logic').val($('#check_logic-'+appid+'-'+appcheckid).text());
        $('#check_sql').val($('#check_sql-'+appid+'-'+appcheckid).text());
        //点击当前的是否使用状态
        var usedlabel=$('#check_used_lab_'+$('#check_used-'+appid+'-'+appcheckid).val());
        var usedradio=$('#check_used_rad_'+$('#check_used-'+appid+'-'+appcheckid).val());
        usedlabel.click();
        usedradio.click();
    }
}


function appcheckedit_check_used(){
    if( 'checked' == $('#check_used_lab_0 span').attr('class') ){
        $('#check_used').val('0');
    }
    if( 'checked' == $('#check_used_lab_1 span').attr('class') ){
        $('#check_used').val('1');
    }
}