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
        counth = 0;countv = 0;countobl1 = 0;countobl2 = 0; i=0
        while i < N :
            j =0
            hor = 1;vert = 1
            obli11 = 1;obli12 = 1
            obli21 = 1;obli22 = 1
            while j < N:
                #check valid char
                #if(bases[i][j] != 'A' and bases[i][j] != 'T' and bases[i][j] != 'C' and bases[i][j] != 'G'):
                #    return False

                #check horizontal
                if j+1 < N and bases[i][j] == bases[i][j+1] :
                    #print('%s:%s == %s:%s'%(j,bases[i][j],j+1,bases[i][j+1]))
                    hor = hor + 1
                else:
                    if hor >= MIN_LENGHT :
                        counth = counth + 1
                    hor = 1
                #check vertical
                if j+1 < N and bases[j][i] == bases[j+1][i] :
                    print('i:%s %s:%s == %s:%s'%(i,j,bases[j][i],j+1,bases[j+1][i]))
                    vert = vert + 1
                else:
                    if vert >= MIN_LENGHT :
                        countv = countv + 1
                    vert = 1

                #check oblicua \
                if j+i+1 < N and bases[j][j+i] == bases[j+1][j+i+1]:
                    #print('i:%s  %s,%s:%s == %s,%s:%s'%(i,j,j+i,bases[j][j+i],j+1,j+i+1,bases[j+1][j+i+1]))
                    obli11 = obli11 + 1
                else:
                    if obli11 >= MIN_LENGHT :
                        countobl1 = countobl1 + 1
                    obli11 = 1
                if j+i>j and j+i+1 < N and bases[j+i][j] == bases[j+i+1][j+1]:
                    #print('i:%s  %s,%s:%s == %s,%s:%s'%(i,j,j+i,bases[j][j+i],j+1,j+i+1,bases[j+1][j+i+1]))
                    obli12 = obli12 + 1
                else:
                    if obli12 >= MIN_LENGHT :
                        countobl1 = countobl1 + 1
                    obli12 = 1

                #check oblicua /
                if N-1-j+i < N and j+1 < N and bases[j][N-1-j+i] == bases[j+1][N-1-j+i-1]:
                    #print('i:%s  %s,%s:%s == %s,%s:%s'%(i,j,j+i,bases[j][j+i],j+1,j+i+1,bases[j+1][j+i+1]))
                    obli21 = obli21 + 1
                else:
                    if obli21 >= MIN_LENGHT :
                        countobl2 = countobl2 + 1
                    obli21 = 1
                if i > 0 and N-1-j-i-1 >= 0 and j+1 < N and bases[j][N-1-j-i] == bases[j+1][N-1-j-i-1]:
                    #print('i:%s  %s,%s:%s == %s,%s:%s'%(i,j,j+i,bases[j][j+i],j+1,j+i+1,bases[j+1][j+i+1]))
                    obli22 = obli22 + 1
                else:
                    if obli22 >= MIN_LENGHT :
                        countobl2 = countobl2 + 1
                    obli22 = 1
                if counth+countv+countobl1+countobl2 > 1 :
                    return True
                j = j + 1
            i = i +1
        print('counth:%s countv:%s countobl1:%s countobl2:%s'%(counth,countv,countobl1,countobl2))

        return False