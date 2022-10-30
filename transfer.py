def date_trans(date):
    date_res = date.split('/')
    i = 0
    while i < len(date_res):
        # res.append(int(date_res[i]))
        date_res[i] = int(date_res[i])

        i += 1
    if len(date_res) <3:
        return "Not a value date"
    if date_res[2] < 23:
        date_res[2] += 2000
    if date_res[2] <100 and date_res[2] >=23:
        date_res[2] += 1900
    if date_res[0] > 12 or date_res[0]<= 0:
        if date_res[1] < 31:
            return f"Not a valued date.Did you mean to import {date_res[1]}/{date_res[0]}/{date_res[2]}"
        return "Not a value date"
    if date_res[1] > 31:
        return "Not a value date"
    if date_res[0] == 2 and date_res[2] % 4 == 0:
        if date_res[1] > 29:
            return "Not a value date"

    return f"{date_res[1]:02d}" + "-" + f"{date_res[0]:02d}" + "-" + f"{date_res[2]:02d}"


if __name__ == "__main__":
    x = "15/3/25"
    y = date_trans(x)
    print(y)
