
import re 
s1 = '我的手机号是:172766666697,我的qq号是:2822654392,我还有一个手机号是:13530705321'

phonenumber = re.match(r'1[3-9]\d{9}',s1)
phonenumber1 = re.search(r'1[3-9]\d{9}',s1)
phonenumber2 = re.findall(r'1[3-9]\d{9}',s1)

print(phonenumber1.group())

print(phonenumber2)
