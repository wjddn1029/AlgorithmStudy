from urllib import parse
import os

# 인쇄 파라미터
b = 'ym_rvrsfrom=202301&ym_rvrsto=202304&ym_payfrom=202301&ym_payto=202304&fg_report=0&cnt_chasu=1&ty_report=1&psingogu_3=0&psingogu_4=0&yn_bakrequest=0&cno=35547&ccode=biz202011020000311&user_id=we0303&gisu=7&ym_insa=2023&wehago_s=189340565519984773375979618847077222425&oldview=0&yn_empty=0&yn_exceptelec=0&yn_na=0&yn_privacy=0&yn_printtaildate=0&yn_printtailpage=0&yn_sealprinting=0'
# 포스트맨 용 파라미터 변환
b = b.replace("=", ':').replace('&','\n').replace('%2C', ',').replace('?','\n')

# 아스키코드 문자열 한글 변환
print(parse.unquote(b))
c = '%EC%A0%84%ED%91%9C2'
print(c)
d = parse.unquote(c)
print(d)
a = []



print(print(os.getcwd()))