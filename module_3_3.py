def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
#1
print_params('one', 85)
print_params()
print_params(False, c=852)
print_params(b = 25)
print_params(c = [1,2,3])
#2
values_list = [False, 7.7, 'Привет']
values_dict = {'a': 'Пока', 'b': (3, 'Five'), 'c': 99}
print_params(*values_list)
print_params(**values_dict)
#3
values_list_2 = ['Здесь хорошо', (2, 'Two', 3)]
print_params(*values_list_2, 42)