class Member:
    def __init__(self, id='', pwd='', name='', email=''):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def __str__(self):
        return self.id+ ' / '+self.pwd+' / '