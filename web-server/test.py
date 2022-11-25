import requests

response = requests.get('http://localhost:8080/',verify=False)
# print(response.status_code)
# print("src=\"https://wp-p.info/reps/html-biginner/img/sample.jpg\"" in response.text)
flag = True

if response.status_code == 200:
    pass
else:
    flag = False
if "src=\"https://wp-p.info/reps/html-biginner/img/sample.jpg\"" in response.text:
    pass
else:
    flag = False

if flag:
    print("ok")
else:
    print("error")
