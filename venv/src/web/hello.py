# hello.py
import time
import json
def application(environ, start_response):
    # start_response('200 OK', [('Content-Type', 'text/html')])
    # data = {"name":"fei","time":time.ctime()}
    # # return [b'<h1>Hello, web!</h1>']
    # jsonStr = json.dumps(data)
    # print(jsonStr)
    # returnStr = b'<h1>Hello, web!</h1>'
    # return jsonStr
    # 构造响应体，以可迭代字符串形式封装
    response_body = 'The request method was %s' % environ['REQUEST_METHOD']

    # HTTP 响应码及消息
    status = '200 OK'

    # 提供给客户端的响应头.
    # 封装成list of tuple pairs 的形式:
    # 格式要求：[(Header name, Header value)].
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]

    # 将响应码/消息及响应头通过传入的start_reponse回调函数返回给server
    start_response(status, response_headers)

    # 响应体作为返回值返回
    # 注意这里被封装到了list中.
    return [response_body]