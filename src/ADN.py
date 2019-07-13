class ADN:
    @staticmethod
    def isMutant(bases):
        if not bases:
            return False
        N = len(bases[0])
        MIN_LENGHT = 4
        if N < MIN_LENGHT:
            return False

        m = int(N/2)
        counth = 0;countv = 0; i=0
        while i < N :
            j =0
            hor = 1
            vert = 1
            while j < N:
                if j+1 < N :
                    #check horizontal
                    if bases[i][j] == bases[i][j+1] :
                    #print('%s:%s == %s:%s'%(j,bases[i][j],j+1,bases[i][j+1]))
                        hor = hor + 1
                    else:
                        if hor >= MIN_LENGHT :
                            counth = counth + 1
                        hor = 1
                    #check vertical
                    if bases[j][i] == bases[j+1][i] :
                        print('%s:%s == %s:%s'%(j,bases[j][i],j+1,bases[j+1][i]))
                        vert = vert + 1
                    else:
                        if vert >= MIN_LENGHT :
                            countv = countv + 1
                        vert = 1
                j = j + 1
            i = i +1
        print('counth:%s countv:%s'%(counth,countv))

        return False