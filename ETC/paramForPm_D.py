from urllib import parse
import os

# 인쇄 파라미터
b = 'ccode=68487&user_id=wnahd1208&ym_insa=2019&ty_form=srst0104&key_closes=&da_make=20230712&index=0&report_data={"ty_disk": "0", "nm_userid": "acacac", "add_saaddr": "강원 춘천시 남면 버들1길 8", "da_reportm": "", "nm_krname": "가가가", "da_accbegind": "01", "nm_trade": "테스트", "tel_com1": "02", "no_social": "8808081337635", "tel_com": "0262333000", "cd_lawcom": "4211040024", "nm_lawcom2": "", "ty_mediation": "2", "da_reportd": "", "da_accendd": "31", "key_taxoffice": 46,"no_manage1": "T", "cd_taxoffcom": "221", "add_saaddr2": "", "tel3_charger": "123", "nm_charger": "123", "no_mediation": "0002", "qt_disk": "0.00", "tel_com3": "3000", "no_manage3": "1", "tel_charger": "123123123", "no_biz": "1111111119", "file_pw": "", "em_taxoffice": "asasas@naver.com", "id_hometax": "sdasd", "tel_com2": "6233", "ty_report": "1", "da_reporty": "", "tel1_charger": "123", "em_dtem": "", "da_accendy": "2023", "str_4_1_1": "4159025625", "da_birth": "19880808", "da_accbeginy": "2023", "da_accbeginm": "01", "cel_dtem2": "1234", "cel_dtem3": "1111", "zip_com": "24468 ", "add_saaddr1": "강원 춘천시 남면 버들1길 8", "db_date": "20230712", "no_master": "T12311", "ty_united": "2", "cd_lawcom2": "", "da_accendm": "12", "ty_intro": 1,"no_corpor": "8808081337634", "str_3_99_99": "421104454272", "cel_dtem1": "010", "nm_chargedept": "123", "nm_taxoff": "춘천", "nm_laware": "", "key_laware": 4095,"com_end": "", "cd_laware": "4211040024", "tel2_charger": "123", "no_manage2": "1231"}&ty_report=1&cnt_com=1&ty_module=4&form_code=K101000&fg_declare=80&dt_supply=&ty_date=&ym_end=&ty_er_report=&ym_pay=&da_begin=20230101&da_end=20231231&hometax_userid=acacac&gubun_com=80&type=1&cno=68487&timestamp=1689128944'
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