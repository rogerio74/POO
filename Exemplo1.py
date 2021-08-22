from unicodedata import normalize


class MinhaFrase:
    texto = None


    def tira_acento(self):
        return normalize('NFKD', self.texto).encode('ASCII', 'ignore').decode('ASCII')


    def contador(self):
        letra ={}
        for letra_texto in self.texto:
            if ord('A') <= ord(letra_texto) <= ord('Z') and (
                letra_texto not in letra):
                letra[letra_texto] = 1
            elif ord('A') <= ord(letra_texto) <= ord('Z') and (
                letra_texto in letra):
                letra[letra_texto] += 1
            elif letra_texto in ",.()!?" and (
                letra_texto not in letra):
                pass
            elif letra_texto in ",.()!?" and (
                letra_texto in letra):
                pass
        return letra


def main():


    f1 = MinhaFrase()
    f1.texto = input("").strip().upper()
    f1.tira_acento()
    print(f1.contador())

if __name__ == "__main__":
    main()