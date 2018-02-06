#키-값

dic={}
dic['파이썬']='www.python.org'
dic['마이크로소프트']='www.microsoft.com'
dic['애플']='www.apple.com'
print(dic['파이썬'])
print(dic['마이크로소프트'])
print(dic['애플'])

print("")

print(dic)

print(dic.keys()) #키
print(dic.values()) #값
print(dic.items()) #전체 목록

print("")

#in dic.keys() <= 키 목록 안에 있는지
print('애플' in dic.keys()) 
print('사과' in dic.keys()) 
print("")

#in dic.values() <= 값 목록 안에 있는지
print('www.microsoft.com' in dic.values()) 

print("")

#삭제할 키-값
dic={'애플': 'www.apple.com', '파이썬': 'www.python.org', '마이크로소프트': 'www.microsoft.com'}
print(dic.pop('애플'))
print(dic)

#다 지우기
dic.clear()
print(dir)
