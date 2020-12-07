cl = 151 #total chain length
nc = 3 #number of arms
def star():
    with open('polyconfig.txt', 'w') as bead:
        bead.write('#3 branched star chain configuration \n \n')
        bead.write(str(cl) + '  atoms \n' +
                str(cl-1) + '  bonds \n' +
                '0' + '  angles \n' +
                '0' + '  dihedrals \n'
                '0' + '  impropers \n')

        bead.write('\nTypes \n \n')

        for i in range(1, cl+1):
            bead.write(str(i)+ '  1\n')

        bead.write('\nBonds \n \n')

        bl = 1 + (cl-1)/nc

        kl = bl + (cl-1)/nc

        for i in range(1, cl):
            if i < kl:
                bead.write(str(i)+'  1'+ '  '+str(i) + '  ' + str(i+1) + '\n')
            elif i == kl:
                bead.write(str(i)+'  1'+ '  '+str(int(bl)) + '  ' + str(i+1) + '\n')
            elif i > kl:
                bead.write(str(i)+'  1'+ '  '+str(i) + '  ' + str(i+1) + '\n')


        bead.write('\nSpecial Bond Counts \n \n')

        for i in range(1, cl+1):
            if i == 1 or i == (((cl-1)/3)*2)+1 or i == cl:
                bead.write(str(i)+ '  1  0  0 \n')
            elif i == bl:
                bead.write(str(i)+ '  3  0  0 \n')
            else:
                bead.write(str(i)+ '  2  0  0 \n')

        bead.write('\nSpecial Bonds \n \n')


        for i in range(1, cl+1):
            if kl+1 == cl:
                if i == 1 :
                    bead.write(str(i)+ '  '+ str(i+1) + '\n')
                elif i == (1+((cl-1)/3)*2):
                    bead.write(str(i) + '  ' + str(i-1) +'\n')
                elif i == bl:
                    bead.write(str(i) + '  ' + str(i-1)+ '  ' + str(i+1) +  '  ' + str(int(kl+1)) +'\n')
                elif i == kl+1:
                    bead.write(str(i) + '  ' + str(int(bl)) +'\n')
                else:
                    bead.write(str(i) + '  ' + str(i-1) +  '  '+ str(i+1) +'\n')
            else:
                if i == 1 :
                    bead.write(str(i)+ '  '+ str(i+1) + '\n')
                elif i == cl or i == (1+((cl-1)/3)*2):
                    bead.write(str(i) + '  ' + str(i-1) +'\n')
                elif i == bl:
                    bead.write(str(i) + '  ' + str(i-1)+ '  ' + str(i+1) +  '  ' + str(int(kl+1)) +'\n')
                elif i == kl+1:
                    bead.write(str(i) + '  ' + str(int(bl))+ '  ' + str(i+1) +'\n')
                else:
                    bead.write(str(i) + '  ' + str(i-1) +  '  '+ str(i+1) +'\n')


        bead.write('\nCoords \n \n')

        for i in range(1, cl+1):
            if i <= (1+((cl-1)/3)*2):
                bead.write(str(i)+'  '+str(round((i*0.05), 2)) + '  0.0  0.0 \n')
            else:
                bead.write(str(i)+'  '+ str(round((bl*0.05), 2)) + '  ' + str(((i-(1+((cl-1)/3)*2))*0.05)) + '  0.0\n')


star()
