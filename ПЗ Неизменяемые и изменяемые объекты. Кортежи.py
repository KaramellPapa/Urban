immutable_var = 73, 64, not True, 'Vitalis'
print(immutable_var)
# immutable_var[1] = 774 #Кортеж не поддерживает обращение по элементам. Не является изменяемым.
# print(immutable_var) #Кортеж не поддерживает обращение по элементам. Не является изменяемым.
mutable_list = [222, 333, True, 'Kavabanga!']
print(mutable_list)
mutable_list[0] = 3
mutable_list[1] = 16
mutable_list[2] = False
mutable_list[3] = 'Pizza'
print(mutable_list)