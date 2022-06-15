from urllib import parse

# 인쇄 파라미터
b = 'iYear=2021&singo=%EC%A0%95%EA%B8%B0%EC%8B%A0%EA%B3%A0&isMagam=false&view_mod=1&ty_report=1&idx=0&cno=53997&ccode=biz202206130000438&user_id=parkdo4&gisu=27&ym_insa=2021&cno_taxnum=32759&yn_empty=0&yn_exceptelec=0&yn_na=0&yn_privacy=0&yn_printtaildate=0&yn_printtailpage=0&yn_sealprinting=0'

# 포스트맨 용 파라미터 변환
b = b.replace("=", ':').replace('&','\n').replace('%2C', ',').replace('?','\n')

# 아스키코드 문자열 한글 변환
print(parse.unquote(b))
c = '%EC%A0%95%EA%B8%B0%EC%8B%A0%EA%B3%A0'
print(c)
d = parse.unquote(c)
print(d)
a = []