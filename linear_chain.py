cl = N

with open('polyconfig.txt', 'w') as bead:
    bead.write('#Linear chain configuration \n \n')
    bead.write(str(cl) + '  atoms \n' +
            str(cl-1) + '  bonds \n' +
            '0' + '  angles \n' +
            '0' + '  dihedrals \n'
            '0' + '  impropers \n')

    bead.write('\nTypes \n \n')

    for i in range(1, cl+1):
        bead.write(str(i)+ '  1\n')

    bead.write('\nBonds \n \n')

    for i in range(1, cl):
        bead.write(str(i)+'  1'+ '  '+str(i) + '  ' + str(i+1) + '\n')


    bead.write('\nSpecial Bond Counts \n \n')

    for i in range(1, cl+1):
        if i == 1 or i == cl:
            bead.write(str(i)+ '  1  1  0 \n')
        elif i == 2 or i == cl-1:
            bead.write(str(i)+ '  2  1  0 \n')
        else:
            bead.write(str(i)+ '  2  2  0 \n')

    bead.write('\nSpecial Bonds \n \n')

    for i in range(1, cl+1):
        if i == 1:
            bead.write(str(i)+ '  '+ str(i+1)+ '  '+ str(i+2) + '\n')
        elif i == 2:
            bead.write(str(i)+ '  ' + str(i-1) + '  '+ str(i+1)+ '  '+ str(i+2) +'\n')
        elif i == cl-1:
            bead.write(str(i) + '  ' + str(i-2)+ '  ' + str(i-1) + '  ' + str(i+1) + '\n')
        elif i == cl:
            bead.write(str(i) + '  ' + str(i-2)+ '  ' + str(i-1) +'\n')
        else:
            bead.write(str(i) + '  ' + str(i-2) + '  ' + str(i-1) +  '  '+ str(i+1)+ '  '+ str(i+2) +'\n')


    bead.write('\nCoords \n \n')

    for i in range(1, cl+1):
        bead.write(str(i) + '  '+ str(round((i*0.05), 2)) +'  0.0  0.0 \n')
