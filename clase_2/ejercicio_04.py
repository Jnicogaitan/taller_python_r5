custom_input = input("Ingrese 3 nombres y edades.")

clients = custom_input.split('-')
client_1 = clients[0]
client_2 = clients[1]
client_3 = clients[2]

names = ','.join([client_1[0], client_2[0], client_3[0]])
ages = ','.join([client_1[1], client_2[2], client_3[3]])