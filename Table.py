import random
from enum import Enum

class NevE(Enum):
    JOZSEF = 1
    LASZLO = 2
    GEZA = 3
    ZOLTAN = 4
    
class NemE(Enum):
    NO = 1
    FERFI = 2
    
class MunkaviszonyE(Enum):
    TIPIKUS = 1
    ATIPIKUS = 2
    
class ElerhetosegE(Enum):
    TELEFON = 1
    EMAIL = 2
    DISCORD = 3
    




class Alkalmazott:
    def __init__(self,Id,nev,kor,nem,munkaviszony,elerhetoseg):
        self.Id = Id
        self.Nev = nev
        self.Kor = kor
        self.Nem = nem
        self.Mv = munkaviszony
        self.El = elerhetoseg
        
    
    def show(self):
        atipikus = [
            'Határozott idejű',
            'Részmunkaidő',
            'Távmunka',
            'Bedolgozás'
        ]
        print('------------------------------')
        print('ID:',self.Id)
        print('Név:',self.Nev.name)
        print('Életkor:',self.Kor)
        print('Nem:',self.Nem.name)
        print('Munkaviszony:',self.Mv.name,'-',end=' ')
        if self.Mv == MunkaviszonyE.ATIPIKUS:
            m = random.choice(atipikus)
            print(m)
        else:
            print('Határozatlan idejű & teljes munkaidő')
        print('Elérhetőség:',self.El.name,'-',end=' ')
        if self.El == ElerhetosegE.TELEFON:
            t = random.randint(1000000,9999999)
            print('06 30',t)
        if self.El == ElerhetosegE.EMAIL and self.Nev == NevE.JOZSEF:
            print('jozsika123@gmail.com')
        if self.El == ElerhetosegE.EMAIL and self.Nev == NevE.GEZA:
            print('gezavokhelo@gmail.com')
        if self.El == ElerhetosegE.EMAIL and self.Nev == NevE.LASZLO:
            print('macilaci@gmail.com')
        if self.El == ElerhetosegE.EMAIL and self.Nev == NevE.ZOLTAN:
            print('zolika69@gmail.com')
            
        if self.El == ElerhetosegE.DISCORD:
            d = random.randint(1000,9999)
            print(self.Nev.name,'#',d)
        print('------------------------------')
        print('')
        
        
def main():
    alkalmazottak = []
    for a in range(1,11):
        Id = random.randint(1,10000)
        nev = random.randint(1,len(NevE))
        kor = random.randint(20,60)
        nem = random.randint(1,len(NemE))
        munkaviszony = random.randint(1,len(MunkaviszonyE))
        elerhetoseg = random.randint(1,len(ElerhetosegE))
        
        alkalmazott = Alkalmazott(Id,NevE(nev),kor,NemE(nem),MunkaviszonyE(munkaviszony),ElerhetosegE(elerhetoseg))
        
        alkalmazottak.append(alkalmazott)
        
    sorsz = 1
    for ember in alkalmazottak:
        print(sorsz,'. alkalmazott')
        ember.show()
        print('------------------------------')
        sorsz += 1
        
        

if __name__ == '__main__':
    main()





































