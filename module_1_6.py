my_dict = {'Saga': 2009, 'Crypto':2000, 'Frencys':1993}
print(my_dict)
print(my_dict['Crypto']) #2000 существующий ключ
print(my_dict.get('Scavenger')) #несуществующий ключ None
my_dict.update({'Batman':1972, 'Frog': 3}) #добавлено
x=my_dict.pop('Saga') #удалено и выведено 2009
print(x)
print(my_dict)
my_set = {33,False,"Bubaleh",12,33,52,'Kreyg','Bubaleh'}
print(my_set)
my_set.update([5,72,True]) #добавлено 2 произвольных
my_set.remove('Bubaleh') #удален
print(my_set)
