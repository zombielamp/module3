import json

data = {'login': 'paswd'}
with open('reg.json', 'a') as f:
	json.dump(data, f)

def register(login, psswd):
	with open('reg.json', 'r') as f:
		data = json.load(f)
	if login in data.keys():
		print('Данный логин уже существует. Придумайте новый логин.')
	else:
		data[login] = psswd
		with open('reg.json', 'w') as f:
			json.dump(data,f)
		print(' Регистрация прошла успешно!')
		

def login_function(login, psswd):
	with open('reg.json', 'r') as f:
		data = json.load(f)
	if login in data.keys():
		if psswd == data[login]
		with open('reg.json', 'w') as f:
			json.dump(data,f)
		print('Добро пожаловать!')
	else:
		print('Неверный логин или пароль')
