from datetime import datetime

'''
# opcja numer 1


def say_something():
    print("Hello ziomek!!")


def disable_at_night(func, start, meta):

    def wrapper():
        if start <= datetime.now().hour < meta:
            func()
        else:
            print('nie czas dla ziomków')
    return wrapper


disable_at_night(say_something)()

'''

"""
# opcja numer 2
def disable_at_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 24:
            func()
        else:
            print('nie czas dla ziomków')

    return wrapper


@disable_at_night
def say_something():
    print("Hello ziomek!!")


say_something()

"""

"""
# opcja numer 3 jeszcze jedna funkcja
def run_olny_time(_from, _to):
    def disable_at_night(func):
        def wrapper():
            if _from <= datetime.now().hour < _to:
                func()
            else:
                print('nie czas dla ziomków')

        return wrapper

    return disable_at_night


@run_olny_time(7, 24)
def say_something():
    print("Hello ziomek!!")


say_something()

"""

"""
def log_before_and_after(func):
    def wrapper():
        print("before")
        result = func()
        print("after")
        return result

    return wrapper


def run_only_between(_from=7, _to=22):
    def real_decorator(func):
        def wrapper():
            if _from <= datetime.now().hour < _to:
                func()
            else:
                print('nie czas dla ziomków')

        return wrapper

    return real_decorator


@log_before_and_after
@run_only_between(7, 22)
def say_something():
    print("Hello ziomek!!")


say_something()
"""