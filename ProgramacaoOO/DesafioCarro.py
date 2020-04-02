class Carro:
    def __init__(self, velMax):
        self.velMax = velMax
        self.velAtual = 0

    def acelerar(self, delta):
        maxima = self.velMax
        nova = self.velAtual + delta
        self.velAtual = nova if nova <= maxima else maxima
        return self.velAtual



    def frear(self, delta):
        nova = self.velAtual - delta
        self.velAtual = nova if nova >= 0 else 0
        return self.velAtual
        

c1 = Carro(220)

for _ in range(35):
    print(c1.acelerar(8))


for _ in range(10):
    print(c1.frear(30))




