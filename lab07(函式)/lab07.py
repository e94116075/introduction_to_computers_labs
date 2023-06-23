class Animal():
    def __init__(self, weight, mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        pass
    def walk(self):
        pass
    def bath(self):
        pass
class Dogs(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight,mood)
    def feed(self):
        self.weight+=0.2
        self.mood+=1
    def walk(self):
        self.weight-=0.2
        self.mood+=2
    def bath(self):
        self.mood-=2
    def printf(self, n_feed, n_walk, n_bath):
        for i in range(n_feed):
          Dogs.feed(self)
        for i in range(n_walk):
          Dogs.walk(self)
        for i in range(n_bath):
          Dogs.bath(self)
        print("狗狗現在的體重=",self.weight,"心情",self.mood) 

class Cats(Animal):
    def __init__(self, weight, mood):
       super().__init__(weight,mood)
    def feed(self):
        self.weight+=0.1
        self.mood+=1
    def walk(self):
        self.weight-=0.1
        self.mood-=1
    def bath(self):
        self.mood-=2
    def printf(self, n_feed, n_walk, n_bath):
        for i in range(n_feed):
          Cats.feed(self)
        for i in range(n_walk):
          Cats.walk(self)
        for i in range(n_bath):
          Cats.bath(self)
        print("貓貓現在的體重=",round(self.weight,2),"心情",self.mood) #...請接續完成

dog = Dogs(4.8, 65) 
dog.printf(18, 10, 4) 

cat = Cats(8.2, 60) 
cat.printf(40, 7, 1) 
