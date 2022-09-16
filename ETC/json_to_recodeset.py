# postgresql - json_to_recordset 문자열 표현
# [{}, {}] 형태 한줄로 표현
# 내부 스트링 키 밸류 값은 " "
# [] 문자열은 '' 으로 마지막에 감싸주기

a = '[{"ym_insa": "2022", "ym_rvrs": "202209", "fg_pay": "1", "dt_pay": "20220915", "cd_emp": "1", "dt_payment": "20220915", "cd_bank": "088", "no_bnkacct": "110333445566", "nm_bnkowner": "박사원", "el_gubun": "1", "el_title": "상신", "el_key": "5000", "transfer_status": "1", "rl_pay": "1000"}]'
print(a)


b = '[{"ym_insa": "2022", "ym_rvrs": "202209", "fg_pay": "1", "dt_pay": "20220915", "cd_emp": "1", "dt_payment": "20220915", "cd_bank": "088", "no_bnkacct": "110333445566", "nm_bnkowner": "박사원", "el_gubun": "1", "el_title": "상신", "el_key": "5000", "transfer_status": "1", "rl_pay": "1000"},{"ym_insa": "2022", "ym_rvrs": "202209", "fg_pay": "1", "dt_pay": "20220915", "cd_emp": "2", "dt_payment": "20220915", "cd_bank": "088", "no_bnkacct": "110333445566", "nm_bnkowner": "이사원", "el_gubun": "1", "el_title": "상신", "el_key": "5000", "transfer_status": "1", "rl_pay": "500"}]'
print(b)