# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import redirect
import json
import time
import json
import datetime
import mcpack.mcpack as mcpack

app= Flask(__name__)

@app.route('/request.ajax',methods=['POST','GET'])

def processing_0():
        try:
            unpack = json.loads(request.data)
        except:
            print 'json_decode_error'
        try:
            unpack = mcpack.loads(request.data)
        except:
            print 'mcpack_decode_error'
        sig = 0
	#对返回值进行处理，mcpack打包和json打包
        ret = json.dumps({"status":0})

        try:
            if("GET/authInfo" == request.form['path'] and True):
                ret = '{"status":200,"data":{"optulevelid":20201,"showRoles":[],"optname":"pmfuqiang","username":"新医","isOperator":true,"ulevelid":10101,"userRoles":[3,5,193],"servertime":1420876491,"company":"太原新医医院","optid":2119562},"errorCode":null}'
        except:
            pass

        try:
            if("GET/entrances/roles" == request.form['path'] and True):
                ret = '{"status":200,"data":{"smartBalanceRemind":true,"tools":[{"title":"优惠积分","name":"point","url":"http://u.baidu.com/ucweb/?module=Accountcenter&controller=Accountmgr&action=main&userid=1000616#/discount/index"},{"title":"商户名片","name":"card","url":"http://u.baidu.com/ucweb/?module=Accountcenter&controller=Accountmgr&action=main&userid=1000616#/businessCard/index"}],"mobileTipsStatus":3,"universal":false,"windowUser":false,"compass":true,"mobileActivity":true,"serviceChat":false},"errorCode":null}'
        except:
            pass

        try:
            if("GET/common/rangeData" == request.form['path'] and {u'startDate': u'2015-01-03', u'isDay': 1, u'endDate': u'2015-01-09', u'appid': 3} == json.loads(request.form['params']) and True):
                ret = '{"status":200,"data":{"3":[{"punish":0.0,"paysum":0,"date":"2015-01-03","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-04","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-05","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-06","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-07","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-08","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-09","clks":0,"shows":0}],"3_0":[{"punish":0.0,"paysum":0,"date":"2015-01-03","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-04","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-05","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-06","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-07","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-08","clks":0,"shows":0},{"punish":0.0,"paysum":0,"date":"2015-01-09","clks":0,"shows":0}]},"errorCode":null}'
        except:
            pass

        try:
            if("GET/common/rangeData" == request.form['path'] and {u'startDate': u'2015-01-03', u'isDay': 1, u'endDate': u'2015-01-09', u'appid': 5} == json.loads(request.form['params']) and True):
                ret = '{"status":200,"data":{"5_0":[{"paysum":0.0,"clks":0,"date":"2015-01-03","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-04","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-05","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-06","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-07","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-08","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-09","shows":0}],"5":[{"paysum":0.0,"clks":0,"date":"2015-01-03","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-04","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-05","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-06","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-07","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-08","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-09","shows":0}]},"errorCode":null}'
        except:
            pass

        try:
            if("GET/common/rangeData" == request.form['path'] and {u'startDate': u'2015-01-03', u'isDay': 1, u'endDate': u'2015-01-09', u'appid': 193} == json.loads(request.form['params']) and True):
                ret = '{"status":200,"data":{"193_0":[{"paysum":0.0,"clks":0,"date":"2015-01-03","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-04","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-05","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-06","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-07","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-08","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-09","shows":0}],"193":[{"paysum":0.0,"clks":0,"date":"2015-01-03","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-04","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-05","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-06","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-07","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-08","shows":0},{"paysum":0.0,"clks":0,"date":"2015-01-09","shows":0}]},"errorCode":null}'
        except:
            pass

        try:
            if("GET/compass/fcAverageData" == request.form['path'] and True):
                ret = '{"status":200,"data":[{"type":0,"tag":0,"shw":4459,"ctr":0.0239,"csm":706.5},{"type":0,"tag":1,"shw":1970,"ctr":0.0065,"csm":95.69},{"type":0,"tag":2,"shw":2488,"ctr":0.0375,"csm":610.79},{"type":1,"tag":0,"shw":13881,"ctr":0.0364,"csm":4586.85},{"type":1,"tag":1,"shw":6067,"ctr":0.0168,"csm":785.03},{"type":1,"tag":2,"shw":7813,"ctr":0.0516,"csm":3801.81},{"type":2,"tag":0,"shw":9317,"ctr":0.0162,"csm":951.91},{"type":2,"tag":1,"shw":3737,"ctr":0.0048,"csm":40.58},{"type":2,"tag":2,"shw":5579,"ctr":0.0239,"csm":911.34}],"errorCode":null}'
        except:
            pass

        try:
            if("GET/compass/otherAverageData" == request.form['path'] and True):
                ret = '{"status":200,"data":[{"type":0,"arvP":0.1599,"prdP":85.25,"jumpP":0.8619,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0},{"type":1,"arvP":0.3334,"prdP":82.27,"jumpP":0.7275,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1},{"type":2,"arvP":0.0516,"prdP":19.4,"jumpP":0.1476,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1}],"errorCode":null}'
        except:
            pass

        try:
            if("GET/compass/fcDayData" == request.form['path'] and True):
                ret = '{"status":200,"data":[{"type":0,"tag":0,"shw":5631,"ctr":0.0204,"csm":586.07,"date":"20141216"},{"type":0,"tag":0,"shw":4905,"ctr":0.0244,"csm":655.15,"date":"20141217"},{"type":0,"tag":0,"shw":4583,"ctr":0.0225,"csm":483.73,"date":"20141218"},{"type":0,"tag":0,"shw":4200,"ctr":0.0232,"csm":475.77,"date":"20141219"},{"type":0,"tag":0,"shw":4340,"ctr":0.026,"csm":525.28,"date":"20141220"},{"type":0,"tag":0,"shw":3460,"ctr":0.0222,"csm":392.19,"date":"20141221"},{"type":0,"tag":0,"shw":3794,"ctr":0.0219,"csm":381.42,"date":"20141222"},{"type":0,"tag":0,"shw":4615,"ctr":0.0219,"csm":554.0,"date":"20141223"},{"type":0,"tag":0,"shw":3282,"ctr":0.02,"csm":380.41,"date":"20141224"},{"type":0,"tag":0,"shw":3746,"ctr":0.0197,"csm":535.66,"date":"20141225"},{"type":0,"tag":0,"shw":4322,"ctr":0.0221,"csm":602.08,"date":"20141226"},{"type":0,"tag":1,"shw":2548,"ctr":0.0059,"csm":97.54,"date":"20141216"},{"type":0,"tag":1,"shw":2448,"ctr":0.0052,"csm":86.3,"date":"20141217"},{"type":0,"tag":1,"shw":2169,"ctr":0.0041,"csm":75.2,"date":"20141218"},{"type":0,"tag":1,"shw":2181,"ctr":0.0082,"csm":106.76,"date":"20141219"},{"type":0,"tag":1,"shw":2160,"ctr":0.0078,"csm":69.58,"date":"20141220"},{"type":0,"tag":1,"shw":1645,"ctr":0.0030,"csm":27.56,"date":"20141221"},{"type":0,"tag":1,"shw":1771,"ctr":0.0124,"csm":133.22,"date":"20141222"},{"type":0,"tag":1,"shw":2038,"ctr":0.0078,"csm":130.99,"date":"20141223"},{"type":0,"tag":1,"shw":1665,"ctr":0.0083,"csm":98.8,"date":"20141224"},{"type":0,"tag":1,"shw":1758,"ctr":0.0051,"csm":66.69,"date":"20141225"},{"type":0,"tag":1,"shw":1959,"ctr":0.0046,"csm":63.97,"date":"20141226"},{"type":0,"tag":2,"shw":3083,"ctr":0.0324,"csm":488.52,"date":"20141216"},{"type":0,"tag":2,"shw":2457,"ctr":0.0434,"csm":568.85,"date":"20141217"},{"type":0,"tag":2,"shw":2414,"ctr":0.0388,"csm":408.51,"date":"20141218"},{"type":0,"tag":2,"shw":2019,"ctr":0.0395,"csm":369.01,"date":"20141219"},{"type":0,"tag":2,"shw":2180,"ctr":0.0439,"csm":455.7,"date":"20141220"},{"type":0,"tag":2,"shw":1815,"ctr":0.0397,"csm":364.61,"date":"20141221"},{"type":0,"tag":2,"shw":2023,"ctr":0.0302,"csm":248.19,"date":"20141222"},{"type":0,"tag":2,"shw":2577,"ctr":0.0329,"csm":423.01,"date":"20141223"},{"type":0,"tag":2,"shw":1617,"ctr":0.0322,"csm":281.6,"date":"20141224"},{"type":0,"tag":2,"shw":1988,"ctr":0.0326,"csm":468.98,"date":"20141225"},{"type":0,"tag":2,"shw":2363,"ctr":0.0368,"csm":538.1,"date":"20141226"},{"type":1,"tag":0,"shw":18668,"ctr":0.0355,"csm":3451.04,"date":"20141216"},{"type":1,"tag":0,"shw":17974,"ctr":0.0362,"csm":3653.09,"date":"20141217"},{"type":1,"tag":0,"shw":17985,"ctr":0.0355,"csm":3329.62,"date":"20141218"},{"type":1,"tag":0,"shw":16974,"ctr":0.0353,"csm":3270.21,"date":"20141219"},{"type":1,"tag":0,"shw":14166,"ctr":0.0361,"csm":3241.51,"date":"20141220"},{"type":1,"tag":0,"shw":16968,"ctr":0.0373,"csm":3437.91,"date":"20141221"},{"type":1,"tag":0,"shw":16882,"ctr":0.0359,"csm":3361.77,"date":"20141222"},{"type":1,"tag":0,"shw":16615,"ctr":0.0355,"csm":3335.09,"date":"20141223"},{"type":1,"tag":0,"shw":13564,"ctr":0.0346,"csm":2817.72,"date":"20141224"},{"type":1,"tag":0,"shw":12750,"ctr":0.0366,"csm":2895.71,"date":"20141225"},{"type":1,"tag":0,"shw":14562,"ctr":0.0353,"csm":3231.82,"date":"20141226"},{"type":1,"tag":1,"shw":8684,"ctr":0.0211,"csm":739.0,"date":"20141216"},{"type":1,"tag":1,"shw":8680,"ctr":0.0209,"csm":788.82,"date":"20141217"},{"type":1,"tag":1,"shw":8955,"ctr":0.0206,"csm":770.89,"date":"20141218"},{"type":1,"tag":1,"shw":8257,"ctr":0.0208,"csm":680.21,"date":"20141219"},{"type":1,"tag":1,"shw":7838,"ctr":0.0219,"csm":663.09,"date":"20141220"},{"type":1,"tag":1,"shw":7895,"ctr":0.0216,"csm":673.86,"date":"20141221"},{"type":1,"tag":1,"shw":8393,"ctr":0.0203,"csm":654.55,"date":"20141222"},{"type":1,"tag":1,"shw":8218,"ctr":0.0204,"csm":668.88,"date":"20141223"},{"type":1,"tag":1,"shw":6118,"ctr":0.0175,"csm":503.27,"date":"20141224"},{"type":1,"tag":1,"shw":4974,"ctr":0.0142,"csm":417.25,"date":"20141225"},{"type":1,"tag":1,"shw":5777,"ctr":0.0131,"csm":449.23,"date":"20141226"},{"type":1,"tag":2,"shw":9984,"ctr":0.0478,"csm":2712.04,"date":"20141216"},{"type":1,"tag":2,"shw":9294,"ctr":0.0505,"csm":2864.27,"date":"20141217"},{"type":1,"tag":2,"shw":9029,"ctr":0.0505,"csm":2558.72,"date":"20141218"},{"type":1,"tag":2,"shw":8716,"ctr":0.0491,"csm":2590.01,"date":"20141219"},{"type":1,"tag":2,"shw":6327,"ctr":0.0535,"csm":2578.4,"date":"20141220"},{"type":1,"tag":2,"shw":9073,"ctr":0.0509,"csm":2764.05,"date":"20141221"},{"type":1,"tag":2,"shw":8488,"ctr":0.0513,"csm":2707.21,"date":"20141222"},{"type":1,"tag":2,"shw":8397,"ctr":0.0505,"csm":2666.2,"date":"20141223"},{"type":1,"tag":2,"shw":7445,"ctr":0.0485,"csm":2314.45,"date":"20141224"},{"type":1,"tag":2,"shw":7775,"ctr":0.0509,"csm":2478.46,"date":"20141225"},{"type":1,"tag":2,"shw":8785,"ctr":0.05,"csm":2782.57,"date":"20141226"},{"type":2,"tag":0,"shw":2398,"ctr":0.0507,"csm":498.23,"date":"20141216"},{"type":2,"tag":0,"shw":2250,"ctr":0.0502,"csm":499.32,"date":"20141217"},{"type":2,"tag":0,"shw":3031,"ctr":0.0394,"csm":482.98,"date":"20141218"},{"type":2,"tag":0,"shw":1969,"ctr":0.0436,"csm":381.5,"date":"20141219"},{"type":2,"tag":0,"shw":2930,"ctr":0.0421,"csm":431.89,"date":"20141220"},{"type":2,"tag":0,"shw":3049,"ctr":0.0384,"csm":540.36,"date":"20141221"},{"type":2,"tag":0,"shw":2637,"ctr":0.0432,"csm":477.72,"date":"20141222"},{"type":2,"tag":0,"shw":2296,"ctr":0.0505,"csm":464.6,"date":"20141223"},{"type":2,"tag":0,"shw":2414,"ctr":0.0381,"csm":408.33,"date":"20141224"},{"type":2,"tag":0,"shw":1568,"ctr":0.0504,"csm":246.72,"date":"20141225"},{"type":2,"tag":0,"shw":2934,"ctr":0.0494,"csm":399.48,"date":"20141226"},{"type":2,"tag":1,"shw":641,"ctr":0.0132,"csm":21.29,"date":"20141216"},{"type":2,"tag":1,"shw":526,"ctr":0.0122,"csm":23.12,"date":"20141217"},{"type":2,"tag":1,"shw":770,"ctr":0.0148,"csm":62.09,"date":"20141218"},{"type":2,"tag":1,"shw":462,"ctr":0.0173,"csm":34.81,"date":"20141219"},{"type":2,"tag":1,"shw":690,"ctr":0.0109,"csm":35.97,"date":"20141220"},{"type":2,"tag":1,"shw":573,"ctr":0.0113,"csm":27.35,"date":"20141221"},{"type":2,"tag":1,"shw":534,"ctr":0.0262,"csm":45.43,"date":"20141222"},{"type":2,"tag":1,"shw":524,"ctr":0.0172,"csm":46.45,"date":"20141223"},{"type":2,"tag":1,"shw":606,"ctr":0.014,"csm":22.37,"date":"20141224"},{"type":2,"tag":1,"shw":484,"ctr":0.0186,"csm":27.28,"date":"20141225"},{"type":2,"tag":1,"shw":861,"ctr":0.0208,"csm":64.73,"date":"20141226"},{"type":2,"tag":2,"shw":1757,"ctr":0.0643,"csm":476.94,"date":"20141216"},{"type":2,"tag":2,"shw":1724,"ctr":0.0617,"csm":476.2,"date":"20141217"},{"type":2,"tag":2,"shw":2261,"ctr":0.0478,"csm":420.89,"date":"20141218"},{"type":2,"tag":2,"shw":1507,"ctr":0.0518,"csm":346.67,"date":"20141219"},{"type":2,"tag":2,"shw":2240,"ctr":0.0518,"csm":395.91,"date":"20141220"},{"type":2,"tag":2,"shw":2476,"ctr":0.0447,"csm":513.02,"date":"20141221"},{"type":2,"tag":2,"shw":2103,"ctr":0.0474,"csm":432.29,"date":"20141222"},{"type":2,"tag":2,"shw":1771,"ctr":0.0604,"csm":418.14,"date":"20141223"},{"type":2,"tag":2,"shw":1808,"ctr":0.0461,"csm":385.95,"date":"20141224"},{"type":2,"tag":2,"shw":1084,"ctr":0.0645,"csm":219.44,"date":"20141225"},{"type":2,"tag":2,"shw":2073,"ctr":0.0612,"csm":334.75,"date":"20141226"}],"errorCode":null}'
        except:
            pass

        try:
            if("GET/compass/otherDayData" == request.form['path'] and True):
                ret = '{"status":200,"data":[{"type":0,"arvP":0.1465,"prdP":69.05,"jumpP":0.9412,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141216"},{"type":0,"arvP":0.1597,"prdP":70.41,"jumpP":0.7894,"sq":0,"lxb":1,"pageCvt":0,"eventCvt":0,"date":"20141217"},{"type":0,"arvP":0.1862,"prdP":95.94,"jumpP":0.9473,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141218"},{"type":0,"arvP":0.1979,"prdP":103.69,"jumpP":0.8,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141219"},{"type":0,"arvP":0.0973,"prdP":63.63,"jumpP":0.909,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141220"},{"type":0,"arvP":0.1429,"prdP":92.73,"jumpP":0.6363,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141221"},{"type":0,"arvP":0.1785,"prdP":102.33,"jumpP":0.8666,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141222"},{"type":0,"arvP":0.1747,"prdP":75.22,"jumpP":0.8888,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141223"},{"type":0,"arvP":0.25,"prdP":131.05,"jumpP":0.7059,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141224"},{"type":0,"arvP":0.1817,"prdP":98.29,"jumpP":0.9286,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141225"},{"type":0,"arvP":0.2292,"prdP":86.44,"jumpP":0.8636,"sq":0,"lxb":0,"pageCvt":0,"eventCvt":0,"date":"20141226"},{"type":1,"arvP":0.3348,"prdP":80.31,"jumpP":0.8381,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141216"},{"type":1,"arvP":0.3186,"prdP":92.2,"jumpP":0.8112,"sq":2,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141217"},{"type":1,"arvP":0.3217,"prdP":84.55,"jumpP":0.7865,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141218"},{"type":1,"arvP":0.3186,"prdP":75.58,"jumpP":0.7073,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141219"},{"type":1,"arvP":0.3143,"prdP":77.93,"jumpP":0.749,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141220"},{"type":1,"arvP":0.3325,"prdP":82.65,"jumpP":0.6894,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141221"},{"type":1,"arvP":0.3411,"prdP":72.86,"jumpP":0.6966,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141222"},{"type":1,"arvP":0.3398,"prdP":83.43,"jumpP":0.6366,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141223"},{"type":1,"arvP":0.3384,"prdP":83.56,"jumpP":0.7024,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141224"},{"type":1,"arvP":0.3364,"prdP":75.62,"jumpP":0.7039,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141225"},{"type":1,"arvP":0.3325,"prdP":84.54,"jumpP":0.6988,"sq":1,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141226"},{"type":2,"arvP":0.1793,"prdP":101.56,"jumpP":0.7871,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141216"},{"type":2,"arvP":0.1372,"prdP":117.3,"jumpP":0.8438,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141217"},{"type":2,"arvP":0.0,"prdP":0.0,"jumpP":0.0,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141218"},{"type":2,"arvP":0.0,"prdP":0.0,"jumpP":0.0,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141219"},{"type":2,"arvP":0.0,"prdP":0.0,"jumpP":0.0,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141220"},{"type":2,"arvP":0.0,"prdP":0.0,"jumpP":0.0,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141221"},{"type":2,"arvP":0.0,"prdP":0.0,"jumpP":0.0,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141222"},{"type":2,"arvP":0.0,"prdP":0.0,"jumpP":0.0,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141223"},{"type":2,"arvP":0.0,"prdP":0.0,"jumpP":0.0,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141224"},{"type":2,"arvP":0.0,"prdP":0.0,"jumpP":0.0,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141225"},{"type":2,"arvP":0.4074,"prdP":52.88,"jumpP":0.437,"sq":0,"lxb":0,"pageCvt":-1,"eventCvt":-1,"date":"20141226"}],"errorCode":null}'
        except:
            pass

        try:
            if("GET/compass/keywords" == request.form['path'] and True):
                ret = '{"status":200,"data":[{"tag":1,"word":"怀孕初期症状","shw":52102},{"tag":2,"word":"阴道炎","shw":324229}],"errorCode":null}'
        except:
            pass

        if(sig == 0):
            return ret
        else:
            return json.dumps({'status':0})

if __name__ == '__main__':
        app.run(host="0.0.0.0",port=8708, threaded=True, debug=False)
