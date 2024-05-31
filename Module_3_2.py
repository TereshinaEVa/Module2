def Section(n = 10):
    print('-' * n, '//', '-' * n)
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params('пять', 8)
print_params(b = 25)
print_params(c = [1,2,3])

Section()

values_list = ['one', 2.5, [4, 5]]
values_dict = {'a': 45, 'b': False, 'c': 'The end'}

print_params(*values_list)
print_params(**values_dict)

Section()

values_list_2 = [42.0, 'is' ]
print_params(*values_list_2, 42)