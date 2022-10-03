def solution(today, terms, privacies):
    today = today.replace(".", "")
    answer = []
    for i, v in enumerate(privacies):
        delete_days = 0
        year = int(v[:4])
        month = int(v[5:7])
        day = v[8:10]
        for t in terms:
            if t[0] == v[-1]:
                mid = t[1:]
                plus_year = divmod(int(mid), 12)[0]
                plus_month = divmod(int(mid), 12)[1]
                if month + plus_month > 12:
                    month = month + plus_month - 12
                    plus_year += 1
                else:
                    month = month + plus_month
                if len(str(month)) == 1:
                    month = '0' + str(month)
                delete_days = str(year + plus_year) + str(month) + day
            else:
                continue
        if int(delete_days) <= int(today):
            answer.append(i+1)

    return answer

privacies = ["2021.05.02A", "2021.07.01B", "2022.02.19C", "2022.02.20C"]

print(solution('20220519', ["A6", "B12", "C3"], privacies))



def solution(today, terms, privacies):
    today = today.replace(".", "")
    answer = []
    for i, v in enumerate(privacies):
        delete_days = 0
        year = int(v[:4])
        month = int(v[5:7])
        day = v[8:10]
        for t in terms:
            if t[0] == v[-1]:
                mid = t[1:]
                plus_year = divmod(int(mid), 12)[0]
                plus_month = divmod(int(mid), 12)[1]
                if month + plus_month > 12:
                    month = month + plus_month - 12
                    plus_year += 1
                else:
                    month = month + plus_month
                if len(str(month)) == 1:
                    month = '0' + str(month)
                delete_days = str(year + plus_year) + str(month) + day
            else:
                continue
        if int(delete_days) <= int(today):
            answer.append(i+1)

    return answer