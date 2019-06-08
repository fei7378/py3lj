#!/usr/bin/env python
#coding=utf-8
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('LTAIjCIpztP4nnKf', 'acNkXT5ZDvVp9aFRYuvaNkhIcbYMjD', 'cn-hangzhou')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('RegionId', "cn-hangzhou")
request.add_query_param('PhoneNumbers', "17628067784")
request.add_query_param('SignName', "焕然色彩")
request.add_query_param('TemplateCode', "SMS_166081538")
request.add_query_param('TemplateParam', json.dumps({'name':'fei','type':'僵尸','erro':'nono','time':'123'}))
# request.add_query_param('user', "123")
# request.add_query_param('name', "123")
# request.add_query_param('time', "123")

response = client.do_action(request)

# python2:  print(response)
print(str(response, encoding = 'utf-8'))
