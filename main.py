import re
phone_no = "91 82967 54907"
with open("chat_historyy.txt", encoding="utf-8") as fh:
    text = fh.readlines()
    valid = []
    for i in text:
        if re.search(phone_no, i):
            valid.append(i)

with open(f"search_dates.txt", "w", encoding="utf-8") as fh:
    fh.writelines(valid)
    