from urllib import *

def talk(text):
    head='http://www.tuling123.com/openapi/api?key=2aceb1c3b3e94bd2bceebe031d8e23ca&info='
    tail='&userid=105118'
    rs = urlopen(head+quote(text.encode('utf-8'))+tail)
    data = rs.read()
    result=data[23:len(data)-2]
    return result