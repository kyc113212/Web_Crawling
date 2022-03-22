# format사용법, 요즘은 f''를 더 많이 사용한다

ivalue = 12312312323
fvalue = 323.32523
f2value = 891723981723981233.223

str1 = '정수값 : %d, 실수값 : %f' % (ivalue, fvalue)
print(str1)

str2 = '정수값 : {0}, 실수값 :  {1}'.format(ivalue, fvalue)
print(str2)

# 왼쪽정렬을 하려면 :<10처럼 오른쪽 기준은 <를 제외하면 된다
# 실수값을 표현하고 싶다면 .2f로 표현가능하다.
str3 = '정수값 : {:<10}, 실수값 : {:10.2f}'.format(ivalue, fvalue)
print(str3)

# 천단위로 끊는것
print('{:,.3f}'.format(f2value))

# value뒤에 : 추가하고 ,을 넣으면 1000단위로 콤마 넣어주는 것, : 뒤에 .3f와 같이 표시하면 실수형 자릿수표시
# format에 대한 약식형태
str4 = f'정수값 :{ivalue}, 실수값:{fvalue}'
print(str4)

str5 = f'정수값 :{ivalue:<10}, 실수값:{fvalue:<10}'
print(str5)

str6 = f'정수값 :{ivalue:,}, 실수값:{f2value:,.3f}'
print(str6)