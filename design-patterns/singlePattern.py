class OnlyOne(object):
    class __OnlyOne(object):
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    # def __init__(self, arg):
    #     if not OnlyOne.instance:
    #         OnlyOne.instance = OnlyOne.__OnlyOne(arg)
    #     else:
    #         OnlyOne.instance.val = arg

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __new__(cls, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
        return OnlyOne.instance


class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg
        print 1
    def __str__(self):
        return self.val



# a = Borg()
# x = Singleton(1)
# y = Singleton(2)
# y.age = 35
# print 2


# all instances are the same instance: __instance
#
class SingleTone(object):
    __instance = None
    def __new__(cls, arg):
        if not SingleTone.__instance:
            SingleTone.__instance = object.__new__(cls)
        SingleTone.__instance.val = arg
        return SingleTone.__instance