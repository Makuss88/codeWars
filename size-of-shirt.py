def sort_shirt(size: list):
    dic = {}

    for i in range(len(size)):
        if size[i] == 'M':
            dic[size[i]] = 0

        elif size[i][-1] == 'S':
            dic[size[i]] = -len(size[i])

        elif size[i][-1] == 'L':
            dic[size[i]] = +len(size[i])

    dic2 = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}

    return list(dic2.keys())


print(sort_shirt(['XXXXXXXXXXL', 'M', 'S', 'L', 'XXXXXXXXXXXXXXS', 'XL', 'XXXXS', 'XXS']))
