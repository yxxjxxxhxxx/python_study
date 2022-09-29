from addr.menu import Menu
from addr.dao import Dao
from addr.service import Service

if __name__=='__main__':
    m = Menu(Service(Dao()))
    m.run()