#https://programmers.co.kr/learn/courses/30/lessons/92334


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

print(solution(id_list, report, k))



from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    report_to_from = defaultdict(set)  # key(id)를 신고한 목록
    report_from_to = defaultdict(set)  # key(id)가 신고한 목록
    for r in report:
        report_from, report_to = r.split(' ')  # 공백을 기준으로 from/to 구분
        report_to_from[report_to].add(report_from)  # report_to를 신고한 목록에 from 추가
        report_from_to[report_from].add(report_to)  # report_from이 신고한 목록에 to 추가

    for _id in id_list:
        cnt = 0
        for r_to in report_from_to[_id]:  # _id가 신고한 목록에서 아이디를 가져옴(r_to)
            if len(report_to_from[r_to]) >= k:  # r_to 신고한 목록의 개수가 k 이상인 경우 cnt++
                cnt += 1
        answer.append(cnt)
    return answer