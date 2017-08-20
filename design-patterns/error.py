import logging
# try:
#     print('try...')
#     r = 10 / int('1')
#     print 'result:', r
# except ValueError as e:
#     print 'ValueError:', e
# except ZeroDivisionError as e:
#     print 'ZeroDivisionError:', e
# else:
#     print 'no error!'
# finally:
#     print('finally...')
# print('END')


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
        # pass
    return 10 / n

def bar(s):
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


def main():
    try:
        bar(0)
    except Exception as e:
        # print 0
        logging.exception(e)
        # print 1
        # pass


# main()
# foo(0)
bar(0)
print 'END'