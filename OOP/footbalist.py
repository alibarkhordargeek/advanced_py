from random import randint

class Ensan:
    def __init__(self, esm):
        self.esm = esm

    def get_esm(self):
        print('%s' %self.esm)

class Futbalist(Ensan):
    A = list()
    B = list()

    def rndm(self):
        j = randint(1, 2)
        if j == 1:
            Futbalist.A.append(self.esm)
        elif j == 2:
            Futbalist.B.append(self.esm)

    def get_esm(self):
        if self.esm in Futbalist.A:
            tm = 'A'
        elif self.esm in Futbalist.B:
            tm = 'B'
        print('%s %s' %(self.esm, tm))


hosein = Futbalist('hosein')
hosein.rndm()
hosein.get_esm()

maziar = Futbalist('maziar')
maziar.rndm()
maziar.get_esm()

akbar = Futbalist('akbar')
akbar.rndm()
akbar.get_esm()

nima = Futbalist('nima')
nima.rndm()
nima.get_esm()

mahdi = Futbalist('mahdi')
mahdi.rndm()
mahdi.get_esm()

farhad = Futbalist('farhad')
farhad.rndm()
farhad.get_esm()

mohamad = Futbalist('mohamad')
mohamad.rndm()
mohamad.get_esm()

khashayar = Futbalist('khashayar')
khashayar.rndm()
khashayar.get_esm()

milad = Futbalist('milad')
milad.rndm()
milad.get_esm()

mostafa = Futbalist('mostafa')
mostafa.rndm()
mostafa.get_esm()

amin = Futbalist('amin')
amin.rndm()
amin.get_esm()

saiid = Futbalist('saiid')
saiid.rndm()
saiid.get_esm()

pooya = Futbalist('pooya')
pooya.rndm()
pooya.get_esm()

poria = Futbalist('poria')
poria.rndm()
poria.get_esm()

reza = Futbalist('reza')
reza.rndm()
reza.get_esm()

ali = Futbalist('ali')
ali.rndm()
ali.get_esm()

bahzad = Futbalist('bahzad')
bahzad.rndm()
bahzad.get_esm()

soheil = Futbalist('soheil')
soheil.rndm()
soheil.get_esm()

behrooz = Futbalist('behrooz')
behrooz.rndm()
behrooz.get_esm()

shahrooz = Futbalist('shahrooz')
shahrooz.rndm()
shahrooz.get_esm()

saman = Futbalist('saman')
saman.rndm()
saman.get_esm()

mohsen = Futbalist('mohsen')
mohsen.rndm()
mohsen.get_esm()