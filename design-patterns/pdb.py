import logging
logging.basicConfig(level=logging.INFO)

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# logging.info('n = %d' % n)
# print(10 / n)


s = '0'
n = int(s)
print(10 / n)

class User:
    _persist_methods = ['get', 'save', 'delete']

    def __init__(self, persister):
        self._persister = persister

    def __getattr__(self, attr):
        if attr in self._persist_methods:
            return getattr(self._persister, attr)

