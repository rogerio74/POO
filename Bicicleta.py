class Bicicleta:
    #Atributos
  def __init__(self):
    self.veloc_atual=0
    self.veloc_max=30
    self.altura_cela=0
    self.altura_max=5
    self.calibragem_pneus=0
    self.calibragem_max = 30
    # métodos

    def pedalar(self):
        if self.veloc_atual+1 <= self.veloc_max:
            self.veloc_atual+=1

        return self.veloc_atual



    def frear(self):
        self.veloc_atual-=1
        print("velocidade atual:", self.veloc_atual)

    def regular_cela(self,valor):
        self.altura_cela=valor
        print("altura atual da cela: {} cm ".format(self.altura_cela))

    def calibrar_pneus(self,valor):
        self.calibragem_pneus=valor
        print("calibragem atual dos pneus: {} libras".format(self.calibragem_pneus))


    def main():
        b = Bicicleta()
        b.pedalar()

# criação dos objetos

minha_bicicleta = Bicicleta()
minha_bicicleta.peso=10
minha_bicicleta.altura=100
minha_bicicleta.cor='amarela'
minha_bicicleta.aro = 29
minha_bicicleta.regular_cela(5)
minha_bicicleta.calibrar_pneus(25)
minha_bicicleta.pedalar()
minha_bicicleta.pedalar()
minha_bicicleta.frear()
minha_bicicleta.frear()
print("Cor:",minha_bicicleta.cor)
print("Aro:",minha_bicicleta.aro)
