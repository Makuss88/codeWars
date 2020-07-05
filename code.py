import numpy


def halving_sum(n):
    result = 0
    while n >= 1:
        result += n
        n = n // 2
    return result


def capitalize(s):
    res = ''
    for a in range(len(s)):
        if a % 2 == 0:
            res += (s[a].upper())
        else:
            res += s[a]
    res2 = res.swapcase()
    result = [res, res2]
    return result


def solve(n):
    if n % 10 != 0:
        return -1
    count = 0
    flag = True
    while flag:
        if n - 500 >= 0:
            n -= 500
            count += 1
            continue
        elif n - 200 >= 0:
            n -= 200
            count += 1
            continue
        elif n - 100 >= 0:
            n -= 100
            count += 1
            continue
        elif n - 50 >= 0:
            n -= 50
            count += 1
            continue
        elif n - 20 >= 0:
            n -= 20
            count += 1
            continue
        elif n - 10 >= 0:
            n -= 10
            count += 1
            continue
        else:
            flag = False

    return count


def greet(name):
    return 'Hello {}'.format(name.title())


def row_sum_odd_numbers(n):
    begin = 1
    for i in range(n):
        begin = begin + 2 * i

    count = []
    for i in range(n):
        count.append(begin)
        begin = begin + 2

    return sum(count)


def get_sum(a, b):
    if a == b:
        return a

    # if a > b: zamiana dwoch zmiennych
    #     test = a
    #     a = b
    #     b = test

    if a > b: a, b = b, a

    sum = 0
    for g in range(a, b + 1):
        sum = sum + g

    return sum


def days_represented(trips):
    l = []
    for i in trips:
        for j in range(i[0], i[1] + 1):
            l.append(j)
    result = set(l)
    return len(result)


def solve2(a, b):
    str = '2357111317192329313741434753596167717379838997101103107109113127131137139149151157163167173179181191193197' \
          '1992112232272292332392412512572632692712772812832933073113133173313373473493533593673733793833893974014094' \
          '1942143143343944344945746146346747948749149950350952152354154755756356957157758759359960160761361761963164' \
          '1643647653659661673677683691701709719727733739743751757761769773787797809811821823827829839853857859863877' \
          '8818838879079119199299379419479539679719779839919971009101310191021103110331039104910511061106310691087109' \
          '1109310971103110911171123112911511153116311711181118711931201121312171223122912311237124912591277127912831' \
          '2891291129713011303130713191321132713611367137313811399140914231427142914331439144714511453145914711481148' \
          '3148714891493149915111523153115431549155315591567157115791583159716011607160916131619162116271637165716631' \
          '6671669169316971699170917211723173317411747175317591777178317871789180118111823183118471861186718711873187' \
          '7187918891901190719131931193319491951197319791987199319971999200320112017202720292039205320632069208120832' \
          '0872089209921112113212921312137214121432153216121792203220722132221223722392243225122672269227322812287229' \
          '3229723092311233323392341234723512357237123772381238323892393239924112417242324372441244724592467247324772' \
          '5032521253125392543254925512557257925912593260926172621263326472657265926632671267726832687268926932699270' \
          '7271127132719272927312741274927532767277727892791279728012803281928332837284328512857286128792887289729032' \
          '9092917292729392953295729632969297129993001301130193023303730413049306130673079308330893109311931213137316' \
          '3316731693181318731913203320932173221322932513253325732593271329933013307331333193323332933313343334733593' \
          '3613371337333893391340734133433344934573461346334673469349134993511351735273529353335393541354735573559357' \
          '1358135833593360736133617362336313637364336593671367336773691369737013709371937273733373937613767376937793' \
          '7933797380338213823383338473851385338633877388138893907391139173919392339293931394339473967398940014003400' \
          '7401340194021402740494051405740734079409140934099411141274129413341394153415741594177420142114217421942294' \
          '2314241424342534259426142714273428342894297432743374339434943574363437343914397440944214423444144474451445' \
          '7446344814483449345074513451745194523454745494561456745834591459746034621463746394643464946514657466346734' \
          '6794691470347214723472947334751475947834787478947934799480148134817483148614871487748894903490949194931493' \
          '3493749434951495749674969497349874993499950035009501150215023503950515059507750815087509951015107511351195' \
          '1475153516751715179518951975209522752315233523752615273527952815297530353095323533353475351538153875393539' \
          '9540754135417541954315437544154435449547154775479548355015503550755195521552755315557556355695573558155915' \
          '6235639564156475651565356575659566956835689569357015711571757375741574357495779578357915801580758135821582' \
          '7583958435849585158575861586758695879588158975903592359275939595359815987600760116029603760436047605360676' \
          '0736079608960916101611361216131613361436151616361736197619962036211621762216229624762576263626962716277628' \
          '7629963016311631763236329633763436353635963616367637363796389639764216427644964516469647364816491652165296' \
          '5476551655365636569657165776581659966076619663766536659666166736679668966916701670367096719673367376761676' \
          '3677967816791679368036823682768296833684168576863686968716883689969076911691769476949695969616967697169776' \
          '9836991699770017013701970277039704370577069707971037109712171277129715171597177718771937207721172137219722' \
          '9723772437247725372837297730773097321733173337349735173697393741174177433745174577459747774817487748974997' \
          '5077517752375297537754175477549755975617573757775837589759176037607762176397643764976697673768176877691769' \
          '977037717772377277741775377577759778977937817782378297841785378677873787778797883790179077919'

    return str[a: a + b]


def solution(digits):
    result = int(digits[0:5])

    for i in range(len(digits) - 4):
        res = int(digits[i:5 + i])
        if res > result:
            result = res

    return result


def multiples(m, n):
    result = []
    for i in range(m):
        result.append(n * (i + 1))
    return result


def split_in_parts(s, part_length):
    result = ''

    for i in range(0, len(s), part_length):
        result += s[i:i + part_length] + ' '

    return result


def my_languages(results):
    dic = {}

    for k, v in results.items():
        if results[k] >= 60:
            dic[k] = v

    result = [k for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True)]

    return result


def digits(n):
    return len(str(n))


def hydrate(drink_string: str):
    total = 0
    res = drink_string.replace('and ', ', ').split(', ')

    for i in res:
        total += int(i[0:1])
    if total == 1:
        return "1 glass of water"
    else:
        return str(total) + ' glasses of water'


def positive_sum(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i
    return result


def add_letters(*letters):
    if not letters:
        return 'z'

    import string
    alfa = list(string.ascii_lowercase)
    suma = 0

    dic = {}
    count = 1
    for i in alfa:
        dic[i] = count
        count += 1

    for i in letters:
        suma += (dic[i])

    while suma > 26:
        suma -= 26

    for k, v in dic.items():
        if v == suma:
            return k


# możliwość skorzystania z funkcji ord(), gdzie zamienia litere na numerek, np ord('a') ==== 97
def encrypt_this(text):
    if len(text) == 0:
        return ''

    import string
    alfa = list(string.ascii_letters)
    # print(alfa)
    dic = {}
    count = 97
    for i in alfa:
        dic[i] = count
        if i == 'z':
            count = 64
        count += 1
    # print(dic)
    txt = text.split(' ')
    enc = []
    for i in txt:

        first_letter = dic[i[0:1]]
        if len(i) == 1:
            full = str(first_letter)
        elif len(i) == 2:
            full = str(first_letter) + i[-1]
        elif len(i) == 3:
            full = str(first_letter) + i[-1] + i[1]
        else:
            full = str(first_letter) + i[-1] + i[2:-1] + i[1]

        enc.append(full)

    encrypt = " ".join(enc)
    return encrypt


def london_city_hacker(journey):
    tube = 2.40
    bus = 1.50
    total_cost = 0.00
    count = 0
    for link in journey:
        if isinstance(link, str):
            total_cost += tube
            count = 0
        else:
            if count == 0:
                total_cost += bus
                count += 1
            else:
                count = 0
    return '£{:.2f}'.format(total_cost)


def find_screen_height(width: int, ratio: str) -> str:
    r = ratio.split(':')
    height = int(r[1]) * width / int(r[0])
    return str(width) + "x" + str(int(height))


def get_count(input_str: str) -> int:
    num_vowels = 0
    char = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(input_str)):
        if input_str[i].lower() in char:
            num_vowels += 1
    return num_vowels


def in_asc_order(arr: list):
    copy = arr.copy()
    arr.sort()
    if copy == arr:
        return True
    else:
        return False


def bombelkowe(arr):
    for i in range(len(arr)):
        sort = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sort = True
        print(arr)
        # if not sort:
        #     break
    return arr


# trwa za długo...
def squer(n):
    sqr = [-0.1]
    j = 20800
    for i in range(j):
        sqr.append(i ** 2)

    for i in range(j):
        if n + sqr[i] in sqr:
            return sqr[i]
    return -1


def initials(name: str) -> str:
    nameList = name.split()
    result = ''
    for n in range(len(nameList) - 1):
        result += nameList[n][0].upper() + "."
    result += nameList[::-1][0].title()
    return result


def largest_pair_sum(numbers):
    a = sorted(numbers, reverse=True)
    return a[0] + a[1]


def capitalize(s: str, ind: list) -> str:
    lis = list(s)

    for i in range(len(lis)):
        if i in ind:
            lis[i] = lis[i].upper()

    return ''.join(lis)


def prod_int_part(n):  # n the integer to be partitioned in products

    if n % 2 == 1:
        return [0, []]

    count = 0
    lis = []

    return [(1), [(2)]]  # (1) - Amount of different products equals to n
    # (2) - List of list - products that have maximum length sorted


def posNeg(arr):
    pos = []
    neg = []
    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        elif arr[i] < 0:
            neg.append(-arr[i])
    if len(pos) > len(neg):
        a = list(filter(lambda x: x not in neg, pos))
        return a[0]
    elif len(pos) < len(neg):
        a = list(filter(lambda x: x not in pos, neg))
        return -a[0]


def reverse_bits(n):
    bins = bin(n)[2:]
    rever = str(bins)[::-1]
    return int(rever, 2)
    # return int(str(bin(n)[2:])[::-1], 2)


def any_odd(x):
    z = str(bin(x))[2:][::-1]
    answer = False
    for i in range(0, len(z)):
        if z[i] == "1" and i % 2 == 1:
            answer = True
    return answer


def move_zeros(array):
    string = []
    index = []

    for i in range(len(array)):
        if type(array[i]) == 'str':
            continue
        else:
            string.append(str(array[i]))

    for i in range(len(string)):
        if string[i] == '0':
            index.append(i)

    arr = numpy.array(array)
    new_arr = numpy.delete(arr, index)
    new = numpy.ndarray.tolist(new_arr)

    for i in range(len(index)):
        new.append(0)

    return new


def change(x: float) -> int:
    return int(x)


def solving_string(str: str) -> bool:
    if len(str) == 1:
        return True

    res = ''.join(sorted(str))

    for i in range(0, len(res) - 1):
        if ord(res[i]) + 1 != ord(res[i + 1]):
            return False

    return True


print(solving_string('b'))

# # TODO do zrobienia
# def move_zeros2(array):
#
#     zero = []
#     for x in array:
#         if x == 0 and type(x) != bool:
#             zero.append(x)
#     print(zero)
#
#
# move_zeros2(["a", 1.0, 0.0, False, 0, 1,  [], ])
