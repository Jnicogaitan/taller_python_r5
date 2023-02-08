input_text = input('ingrese nombre y edad, separado por guion ')
clients_name = []
age = []

split_text = input_text.split('-')

for client in split_text:
    data = client.strip().split(' ')
    clients_name.append(data[0])
    age.append(data[1])

print(','.join(clients_name))
print(','.join(age))


