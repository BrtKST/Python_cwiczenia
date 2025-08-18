class LiczbaDz:
    def __init__(self,dziesietna):
        self.dziesietna = dziesietna
    def get_dziesietna(self):
        return self.dziesietna
    def na_binarny(self):
        bin = []
        binarnie = 0
        potega = 0
        dziesietnie = self.dziesietna
        while dziesietnie > 0:
            bin.append(str(dziesietnie % 2))
            dziesietnie = dziesietnie // 2
        print(bin)

        '''
        for element in bin:
            binarnie +=  element *  2 ** potega 
            potega += 1
        '''
        bin_new = bin[::-1]
        binarnie = ''.join(bin_new)
        return binarnie

    def __str__(self):
        return f'Wartosc dziesietna : {self.get_dziesietna()}, binarnie: {self.na_binarny()}'
    

class LiczbaBin:
    def __init__(self,ciag):
        self.ciag = ciag
    def get_binarna(self):
        binarnie = [str(element) for element in self.ciag]
        binarnie = ''.join(binarnie)
        return binarnie
    def get_dziesietnie(self):
        dziesietnie = 0
        ciag = self.get_binarna()
        index = len(ciag)-1
        for element in ciag:
            dziesietnie += int(element) * 2 ** index
            index -= 1            
        return dziesietnie
    def __str__(self):
        return f'Wartosc binarna: {self.get_binarna()}, dziesietna: {self.get_dziesietnie()}'
        


liczba1 = LiczbaDz(10)
print(liczba1)

liczba2 = LiczbaBin([1,0,1,1,0,1])
print(liczba2)