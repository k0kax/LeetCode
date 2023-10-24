def count_elderly_passengers(details):
    count = 0
    for detail in details:
        age = int(detail[11:13])
        if age > 60:
            count += 1
    return count

details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
result = count_elderly_passengers(details)
print(result)