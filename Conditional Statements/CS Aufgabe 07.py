# if else Lösung
status = int(input('Bitte Statuscode eingeben: '))
if status == 200:
	print('OK')
elif status == 201:
	print('Accepted')
elif status == 400:
	print('Bad Request')
elif status == 401 or status == 403:
	print('Connection Refuseder')
elif status == 502:
	print('Bad Request')
else:
	print('Falsche Eingabe')
	
 
# match case Lösung
match status:
		case 200:
				print('OK')
		case 201:
				print('Accepted')
		case 400:
				print('Bad Request')
		case 401:
				print('Connection Refuseder')
		case 403:
				print('Connection Refuseder')
		case	502:
				print('Bad Request')
		case other:
				print('Falsche Eingabe')
