import json

login = {'Login' : input('Введите логин ')}
passwd = {'Password' : input('Введите пароль ')}

with open ('register.json', 'w') as f:
	json.dump(login, f)
	json.dump(passwd, f)

def register(login, passwd):
	with open ('register.json', 'r') as f:
		login = json.load(f)
		passwd = json.load(f)

	print (login, passwd)
