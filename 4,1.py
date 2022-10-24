import json

name = [input('Введите логин ')]
password = [input('Введите пароль ')]
with open('reg.json', 'w') as f:
	json.dump(name, f)
	json.dump(password, f)


def register(login, passwd):
	if login in name:
		if passwd in password:
			print(name, password)

print(name, password)
