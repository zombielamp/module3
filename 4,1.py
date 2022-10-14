import json

login = input('Введите логин')
passwd = input('Введите пароль')

with open ('register.json', 'w') as f:
		json.dump(login, f)
		json.dump(passwd, f)

def register(login, passwd):
	print (login, passwd)

register(login,passwd)