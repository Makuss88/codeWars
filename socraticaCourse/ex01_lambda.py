# lambda:
g = lambda x: x * 3 + 1
# print(g(7))


full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
# print(full_name('        gRzegOrZ', '  MACIborek  '))


scf_list = ['Jagadis Chandra Bose', 'Muhammed Zafar Iqbal', 'José Bento Renato Monteiro Lobato', 'Péter Kuczka',
            'Miguel Ángel Asturias', 'Lawi Tidhar', "Jack Szirak", 'Slawomir Putin',
            'Slawomir Szirak', 'Slawomir Zaden', 'Hugo Szirak']

scf_list.sort(key=lambda name: name.split(' ')[-1])


# print(scf_list)


def quadratic_function(a: int, b: int, c: int):
    '''f(x) = ax^2 + bx + c'''

    return lambda x: a * x ** 2 + b * x + c

# sposob jeden:
# f = quadratic_function(2, 3, -5)
# print(f(2))

# sposob dwa:
# print(quadratic_function(3, 0, 1)(2))


