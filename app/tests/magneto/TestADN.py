from magneto.ADN import ADN;
class TestADN:
    def testEnunciadoNoMutante(self):
        data = {"dna":["ATGCGA","CAGTGC","TTATTT","AGACGG","GCGTCA","TCACTG"]}
        assert False == ADN.isMutant(data['dna'])
    def testEnunciadoMutante(self):
        data = {"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}
        assert True == ADN.isMutant(data['dna'])
    def testEjemploMutante(self):
        data = {"dna":["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}
        assert True == ADN.isMutant(data['dna'])
    def testHorizontal(self):
        data = {"dna":["AAAAAAAAAA","TTTTTTTTTT","CCCCCCCCCC","GGGGGGGGGG","AAAAAAAAAA","TTTTTTTTTT","CCCCCCCCCC","GGGGGGGGGG","AAAAAAAAAA","TTTTTTTTTT"]}
        assert True == ADN.isMutant(data['dna'])
    def testVertical(self):
        data = {"dna":["ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT","ATCGATCGAT"]}
        assert True == ADN.isMutant(data['dna'])
    def testDiagonal1(self):
        data = {"dna":["ATCGATCGAT","TATCGATCGA","CTATCGATCG","GCTATCGATC","AGCTATCGAT","TAGCTATCGA","CTAGCTATCG","GCTAGCTATC","AGCTAGCTAT","TAGCTAGCTA"]}
        assert True == ADN.isMutant(data['dna'])
    def testDiagonal2(self):
        data = {"dna":["TAGCTAGCTA","AGCTAGCTAT","GCTAGCTATC","CTAGCTATCG","TAGCTATCGA","AGCTATCGAT","GCTATCGATC","CTATCGATCG","TATCGATCGA","ATCGATCGAT"]}
        assert True == ADN.isMutant(data['dna'])

    def testNull(self):
        assert False == ADN.isMutant(None)
    def testEmpty(self):
        assert False == ADN.isMutant([])
    def testMin(self):
        data = {"dna":["ATG","CAG","TTA","AGA","GCG","TCA"]}
        assert False == ADN.isMutant(data['dna'])