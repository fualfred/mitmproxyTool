# coding =utf-8
import os
from mitmproxy import http
import json





def request(flow: http.HTTPFlow):
    pass

def response(flow: http.HTTPFlow):
    print(flow.request.pretty_url)
    if flow.request.path == '/cloud/v2/deviceManaged/bypassV2':
        request_data = flow.request.get_text()
        # print(request_data)
        method = json.loads(request_data)['payload']['method']
        if method == 'getHumidifierStatus1':
            print("拦截到了请求，函数是"+ method)
            response_data = json.loads(flow.response.get_text())
            response_data['result']['result']['humidity'] = 98
            flow.response.set_text(json.dumps(response_data))
        else:
            pass
    
if __name__ == "__main__":
    file_path = __file__  #取当前文件路径
    cmd = "mitmweb -s" + file_path  #cmd窗口命令:mitmweb -s  脚本路径
    os.system(cmd)    #运行cmd命令
 