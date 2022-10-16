import requests, json
from random import randint
model_api = requests.get("https://randomuser.me/api")
json_api = json.loads(model_api.content)


#users
for name_first in json_api["results"]:
    name_first = (name_first["name"]["first"])


for name_last in json_api["results"]:
    name_last = (name_last["name"]["last"])


for gen in json_api["results"]:
    gen = (gen["gender"])


for date_birthday in json_api["results"]:
    date_birthday = (date_birthday["dob"]["date"])
    date_birthday = date_birthday[:4] + '.' + date_birthday[5] + date_birthday[6] + '.' + date_birthday[8] + \
                    date_birthday[9]
    date_birthday = str(date_birthday)


for path_avatar in json_api["results"]:
    path_avatar = (path_avatar["picture"]["large"])


for res_address_street_name in json_api["results"]:
    res_address_street_name = (res_address_street_name["location"]["street"]["name"])


for res_address_street_num in json_api["results"]:
    res_address_street_num = (str(res_address_street_num["location"]["street"]["number"]))


#phones
view_phone = ["home", "jobs"]
view_phone = view_phone[randint(0, len(view_phone)-1)]

for number_phone in json_api["results"]:
    number_phone = (number_phone["phone"])


#email
view_email = ["home", "jobs"]
view_email = view_email[randint(0, len(view_email)-1)]
for email in json_api["results"]:
    email = (email["email"])

