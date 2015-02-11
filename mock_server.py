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

@app.route('/json/sms/v3/ReportService/getRealTimeData',methods=['POST','GET'])

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
        ret = json.dumps({"body": {"data": [{"realTimeResultTypes": [{"date": "2014-12-16", "KPIs": [58, 16, 46]}, {"date": "2014-12-17", "KPIs": [81, 89, 58]}, {"date": "2014-12-18", "KPIs": [43, 100, 68]}, {"date": "2014-12-19", "KPIs": [83, 63, 21]}, {"date": "2014-12-20", "KPIs": [33, 46, 39]}, {"date": "2014-12-21", "KPIs": [35, 96, 48]}, {"date": "2014-12-22", "KPIs": [84, 84, 52]}]}]}, "header": {"status": 0, "rquota": 14988, "quota": 3, "oprtime": 0, "oprs": 1, "failures": [], "desc": "success"}})

        try:
            if("1" == request.form['a'] and "fdasfa" == request.form['b'] and True):
                ret = {"body": {"data": [{"realTimeResultTypes": [{"date": "2014-12-16", "KPIs": [58, 16, 46]}, {"date": "2014-12-17", "KPIs": [81, 89, 58]}, {"date": "2014-12-18", "KPIs": [43, 100, 68]}, {"date": "2014-12-19", "KPIs": [83, 63, 21]}, {"date": "2014-12-20", "KPIs": [33, 46, 39]}, {"date": "2014-12-21", "KPIs": [35, 96, 48]}, {"date": "2014-12-22", "KPIs": [84, 84, 52]}]}]}, "header": {"status": 0, "rquota": 14988, "quota": 3, "oprtime": 0, "oprs": 1, "failures": [], "desc": "success"}}
                ret = json.dumps(ret)
        except:
            pass

        try:
            if('wociao' == unpack['ddb'] and 12 == unpack['d'] and True):
                ret = {"body": {"data": [{"realTimeResultTypes": [{"date": "2014-12-16", "KPIs": [58, 16, 46]}, {"date": "2014-12-17", "KPIs": [81, 89, 58]}, {"date": "2014-12-18", "KPIs": [43, 100, 68]}, {"date": "2014-12-19", "KPIs": [83, 63, 21]}, {"date": "2014-12-20", "KPIs": [33, 46, 39]}, {"date": "2014-12-21", "KPIs": [35, 96, 48]}, {"date": "2014-12-22", "KPIs": [84, 84, 52]}]}]}, "header": {"status": 0, "rquota": 14988, "quota": 3, "oprtime": 0, "oprs": 1, "failures": [], "desc": "success"}}
                ret = mcpack.dumps(ret)
        except:
            pass

        if(sig == 0):
            return ret
        else:
            return json.dumps({'status':0})

@app.route('/api/OneService',methods=['POST','GET'])

def processing_1():
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
            if([630152, u'2014-12-16', u'2014-12-22', 1] == unpack['params'] and '2.0' == unpack['jsonrpc'] and 'getBeidouData' == unpack['method'] and True):
                ret = {"jsonrpc": "2.0", "id": 6208783150090698392, "result": {"code": 0, "result": {"5_0": [{"date": "2014-12-16", "clks": 85, "paysum": 97, "shows": 69}, {"date": "2014-12-17", "clks": 68, "paysum": 61, "shows": 90}, {"date": "2014-12-18", "clks": 94, "paysum": 69, "shows": 59}, {"date": "2014-12-19", "clks": 64, "paysum": 81, "shows": 62}, {"date": "2014-12-20", "clks": 74, "paysum": 54, "shows": 50}, {"date": "2014-12-21", "clks": 54, "paysum": 61, "shows": 80}, {"date": "2014-12-22", "clks": 54, "paysum": 90, "shows": 56}], "5": [{"date": "2014-12-16", "clks": 85, "paysum": 97, "shows": 69}, {"date": "2014-12-17", "clks": 68, "paysum": 61, "shows": 90}, {"date": "2014-12-18", "clks": 94, "paysum": 69, "shows": 59}, {"date": "2014-12-19", "clks": 64, "paysum": 81, "shows": 62}, {"date": "2014-12-20", "clks": 74, "paysum": 54, "shows": 50}, {"date": "2014-12-21", "clks": 54, "paysum": 61, "shows": 80}, {"date": "2014-12-22", "clks": 54, "paysum": 90, "shows": 56}]}, "errmsg": ""}}
                ret = mcpack.dumps(ret)
        except:
            pass

        if(sig == 0):
            return ret
        else:
            return json.dumps({'status':0})

if __name__ == '__main__':
        app.run(host="0.0.0.0",port=8708, threaded=True, debug=False)
