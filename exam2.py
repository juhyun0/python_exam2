print("1. 다음 중에서 틀린 것을 모두 고르세요.")
print("  1) 리스트는 변경이 가능한 자료형이다.\n  2) 튜플은변경이 가능한 자료형이다.\n  3) 딕셔너리의 키는 변경이 불가능한 자료형을 사용해야 한다.\n  4) 문자열은 변경이 가능한 자료형이다.")
print(" 답 : 2), 3)") 

print("")

print("2. 다음 코드에서 a는 어떤 결과를 갖게 될까요?")
print(">>>a=[1,2,3]\n>>>a.append(4)\n>>>a")
a=[1,2,3]
a.append(4)
print(a)

print("")

print("3. 다음 코드에서 a는 어떤 결과를 갖게 될까요?")
print(">>>a=[1,2,3,4,5]\n>>>a.pop(2)")
a=[1,2,3,4,5]
a.pop(2)
print(a)

print("")

print("4. 다음 중 올바른 튜플 선언이 아닌 것은 무엇입니까?")
print("  1)a=1,2,3,4,5\n  2)a=1,\n  3)a=(1,2,3,4,5)\n  a=[1,2,3,4,5]")
print(" 답 : 2), 3)")

print("")

print("5. 다음 코드에서 city, latitude, longitude의 값은 무엇입니까?")
print(" >>> city, latitude, longitude = 'Seoul', 37.541, 126.986")
city, latitude, longitude = 'Seoul', 37.541, 126.986
print(city)
print(latitude)
print(longitude)

print("")

print("6. 다음 코드에서 잘못된 부분을 찾아 설명하세요.")
print(" >>> a=(1,2,3)\n >>>a[0]=7\n >>>print(a[0])")
print(" 답 : a[0]=7")

print("")

print("7.다음과 같은 실행 결과를 갖는 dic 객체를 선언하는 코드를 작성하세요.")
print(" >>>dic {'애플': 'www.apple.com', '파이썬': 'www.python.org', '마이크로소프트': 'www.microsoft.com'")
dic={}
dic['파이썬']='www.python.org'
dic['애플']='www.apple.com'
dic['마이크로소프트']='www.microsoft.com'
print(dic)
print(" 답 : \n<dic={}\n dic['파이썬']='www.python.org'\n dic['애플']='www.apple.com'\n dic['마이크로소프트']='www.microsoft.com'>")



