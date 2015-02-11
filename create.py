# -*- coding: utf-8 -*-

#xlrd 为第三方依赖库，提供对excel表格的支持
import xlrd
import json

string_header = '''# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import redirect
import json
import time
import json
import datetime
import mcpack.mcpack as mcpack

app= Flask(__name__)
'''


string_footer = '''
if __name__ == '__main__':
        app.run(host="0.0.0.0",port=%s, threaded=True, debug=False)
'''

string_route = '''
@app.route('%s',methods=['POST','GET'])
'''

string_func_1 = '''
def processing_%s():
        try:
            unpack = json.loads(request.data)
        except:
            print 'json_decode_error'
        try:
            unpack = mcpack.loads(request.data)
        except:
            print 'mcpack_decode_error'
        sig = 0
'''

string_func_2 ='''
        %s = request.form['%s']
        if(%s != '%s'):
            sig = 1
        else:
            pass
'''

string_func_2_unpack ='''
        request_params = json.loads('%s')
        if(request_params == unpack):
            sig = 0
        else:
            sig = 1
        
'''

string_func_3 = '''
        ret = %s
%s
        if(sig == 0):
            return ret
        else:
            return %s.dumps({'status':0})
'''

#这里对一站式做了个兼容，返回值返回请求参数中的id值
string_func_4 = '''
        try:
            if(%s):
                ret = %s
                if(unpack.has_key('id')):
                    ret['id'] = unpack['id']
                ret = %s.dumps(ret)
        except:
            pass
'''

#处理接口文档excel
data = xlrd.open_workbook('api.xls')
table = data.sheets()[0]
api_list = {}

#不处理标题行
for i in range(1,table.nrows):
    api_data = table.row_values(i)
    #print api_data
    if(api_list.has_key(api_data[0])):
        api_list[api_data[0]].append({'input':api_data[1],'output':api_data[2],'ret_pack':api_data[3],'req_pack':api_data[4],'action':api_data[0]})
    else:
        api_list[api_data[0]]=[]
        api_list[api_data[0]].append({'input':api_data[1],'output':api_data[2],'ret_pack':api_data[3],'req_pack':api_data[4],'action':api_data[0]})
      
for action in api_list.keys():
    print action

#写入python脚本头部
file_script = open('mock_server.py','w+')
file_script.write(string_header)

count = 0

for action in api_list.keys():
    
    #写入action，支持post和get
    file_script.write(string_route%(action))

    #写入处理函数，对请求包头进行解析（目前尝试mcpack和json解包，失败跳过）
    file_script.write(string_func_1%(count))

    #不同参数返回不同的返回值
    default_return = 'json.dumps({"status":0})'
    string_return = ''

    #处理不同的传入参数，进入不同的if语句
    for branch in api_list[action]:
        
        #对请求参数进行处理
        try:
            params = json.loads(branch['input'])
        except:
            params = {'status':0}
            print 'No input'
        test_string = ''
        
        #普通http请求
        if(branch['req_pack'] == 'http'):
            for key in params.keys():
                test_string += "\"%s\" == request.form['%s'] and "%(params[key],key)
            test_string += 'True'
            
        #处理需要解包的请求参数条件
        elif(branch['req_pack'] == 'unpack'):
            for key in params.keys():
                if(type(params[key]) == type(u'') or type(params[key]) == type('')):
                    test_string += "'%s' == unpack['%s'] and "%(params[key],key)
                else:
                    test_string += "%s == unpack['%s'] and "%(params[key],key)
            test_string += 'True'
        
        #不需要对请求参数进行处理
        elif(branch['req_pack'] == 'noparams'):
            default_return = '%s.dumps(%s)'%(branch['ret_pack'],branch['output'])

        #如果返回类型不是无参数，需要进入if语句，生成if语句
        if(branch['req_pack'] != 'noparams'):
            try:
                string_return += string_func_4%(test_string,branch['output'],branch['ret_pack'])
                del test_string
            except:
                pass
    
    #对返回值进行处理，默认返回json格式
    file_script.write('\t#对返回值进行处理，mcpack打包和json打包')
    file_script.write(string_func_3%(default_return,string_return,'json'))

    count += 1
    

#写入python脚本尾部，端口默认8708
port = 8708
file_script.write(string_footer%(port))
file_script.close()
