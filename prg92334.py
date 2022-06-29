def solution(id_list, report, k):
    answer = []
    report_list = {}
    for a in report:
        inv_report = a.split()
        if inv_report[0] not in report_list:
            report_list[inv_report[0]] = [inv_report[1]]
        else:
            if inv_report[1] not in report_list[inv_report[0]]:
                report_list[inv_report[0]].append(inv_report[1])

    whole_list = []
    final = []
    for a in report_list.values():
        whole_list += a
    set_list = set(whole_list)
    
    for a in set_list:
        if whole_list.count(a)>=k:
            final.append(a)
            
    for a in id_list:
        if a not in report_list:
            report_list[a] = "없음"

        
    for a in id_list:
        cnt = 0
        for b in final:
            if b in report_list[a]:
                cnt +=1
        answer.append(cnt)

    return answer