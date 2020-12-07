program main

    real, dimension (:), allocatable :: X, Y, Z, VX, VY, VZ, RG_L, REE, RG, SQR, ASQR, AVRG, AVREE, MSD
    real, dimension (:), allocatable :: MSDP, Dm, Cm
    real, dimension (:,:), allocatable :: D0, COM
    real, dimension (:, :), allocatable :: MSDall, ffcor, allcor
    integer, dimension (:), allocatable :: NID, NTYP, NM
    real :: DIFF, L, rc, v, comx, comy, comz
    real :: avkap, num, t1, t2, rcut, VF, CX0, CY0, CZ0
    real :: AVL1, AVL2, AVL3, TAVL1, TAVL2, TAVL3, hh, NPV
    integer :: I, K, P, PP, MM, NDUMP, NS, NB, NP, ts, KK, LL, CL, NC, MA, MB, gg

    CALL CPU_TIME(ti)

    L  = 100
    NB = 3*(L**3)
    CL = 301
    VF = 1

    NPV = CL
    NC =  190

    NP = CL*NC

    NS = NB - NP

    MA = 1
    MB = 1

    NDUMP = 41

    CX0 = 0
    CY0 = 0
    CZ0 = 0

    allocate (COM(3,NC), RG(NC), REE(NC), SQR(NC))
    allocate (allcor(3, NC*CL), ffcor(3, NC*CL), MSDall(NDUMP, NC*CL))
    allocate (ASQR(NDUMP), RG_L(CL), AVRG(NDUMP), AVREE(NDUMP))
    allocate (MSD(NDUMP), D0(3,NC), MSDP(NC))
    allocate (X(CL), Y(CL), Z(CL), NM(CL), NID(CL), NTYP(CL))
    allocate (Dm(NC), Cm(NC))

    open (unit = 10, file = 'FN1')
    open (unit = 18, file = 'RG_FN2')
    open (unit = 20, file = 'MSD_FN3')

    DO 16 K = 1, NDUMP

    COM(:,:) = 0

    read(10, *)
    read(10, *) ts
    read(10, *)
    read(10, *)
    read(10, *)
    read(10, *)
    read(10, *)
    read(10, *)
    read(10, *)


    print *, 'Evaluating time step: ', ts


    DO I = 1, NS
    read(10, *) F1, F2, F3
    IF (F3.EQ.1) THEN
        print *, 'this is not a solvent'
    END IF
    END DO

    gg = 1
    DO 25 KK = 1, NC
    DO LL = 1, CL
    read(10, *) NM(LL), NID(LL), NTYP(LL), A1, A2, A3, B1, B2, B3, D1, D2, X(LL), Y(LL), Z(LL), C1, C2, C3

    IF (K.EQ.1) THEN
        ffcor(1,gg) = X(LL)
        ffcor(2,gg) = Y(LL)
        ffcor(3,gg) = Z(LL)
    END IF
    allcor(1,gg) = X(LL)
    allcor(2,gg) = Y(LL)
    allcor(3,gg) = Z(LL)
    gg = gg + 1
    END DO

    COM(1,KK) = SUM(X)/CL
    COM(2,KK) = SUM(Y)/CL
    COM(3,KK) = SUM(Z)/CL

    RGC = 0

    DO LL = 1, CL
    RG_L(LL) = ((X(LL) - COM(1, KK))**2 + (Y(LL) - COM(2, KK))**2 + (Z(LL) - COM(3, KK))**2)
    END DO

    RG(KK) = sum(RG_L)/(CL)

    IF (K.EQ.1) THEN
        D0 = COM
        Dm(KK) = sqrt(COM(1, KK)**2 + COM(2, KK)**2 + COM(3, KK)**2)
        t1 = ts
    END IF

    IF (K.EQ.2) THEN
        t2 = ts
    END IF

    Cm(KK) = sqrt(COM(1, KK)**2 + COM(2, KK)**2 + COM(3, KK)**2)

!    print *, d0(1, KK), d0(2, KK), d0(3, KK)
    MSDP(KK) = ((COM(1, KK) - D0(1, KK))**2 + (COM(2, KK) - D0(2, KK))**2 + (COM(3, KK) - D0(3, KK))**2)

25 continue

    MSD(K) = SUM(MSDP)/NC
    ASQR(K) = sum(SQR)/NC
    AVRG(K) = sum(RG)/NC
    AVREE(K) = sum(REE)/NC


    write (18, *) ts, AVRG(K)
    write (20, *) ts, MSD(K)

16 continue


    close(18)
    close(10)
    close(20)
end program main

    
