from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

fio = []
for contacts in contacts_list:
    contact = ' '.join(contacts[:3]).split(",")
    organization = contacts[3:-1]
    for con in contact:
       con_split = con.split(), organization
       fio.append(con_split)

regex = r"(\(|)(доб\.?)\s*(\d+)(\)|)"
subst = "\\2\\3"
result = re.sub(regex, subst, str(fio), 0, re.MULTILINE)

regex_2 = r"(\+7|8)?\s*\((\d+)\)\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)"
subst_2 = "\\2-\\3-\\4-\\5"
result_2 = re.sub(regex_2, subst_2, result, 0, re.MULTILINE)
list_result_2 = list(result_2)

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(list_result_2)
