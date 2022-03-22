str1 = '    python      '
print('*',str1,'*')
print('*',str1.strip(),'*')
print('*',str1.rstrip(),'*')
print('*',str1.lstrip(),'*')

str2 = ',python,.'
# ,하고 .를 없애는 것도 가능하다
# 특정한 문자열을 없애는 것도 가능
print(str2.strip(',.'))