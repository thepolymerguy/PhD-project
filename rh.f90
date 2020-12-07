program main

    real, dimension (:), allocatable :: X, Y, Z, Rh, AVRh
    integer, dimension (:), allocatable :: NID, NTYP, NM
    real :: L, Rij_v, Rij
    integer :: sn, I, K, P, PP, MM, NDUMP, NS, NB, NP, ts, KK, LL, CL, NC, MA, MB, gg

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

    sn = 3

    CX0 = 0
    CY0 = 0
    CZ0 = 0

    allocate (Rh(NC), AVRh(NDUMP))
    allocate (X(CL), Y(CL), Z(CL), NM(CL), NID(CL), NTYP(CL))

    open (unit = 10, file = 'eq.lammpstrj')
    open (unit = 18, file = 'rh_N_301_lin_a_25.dat')

    do P = 1, sn
    read(10, *)
    read(10, *) ts
    read(10, *)
    read(10, *)
    read(10, *)
    read(10, *)
    read(10, *)
    read(10, *)
    read(10, *)

    print *, 'Skipping time step: ', ts

    DO I = 1, NB
    read(10, *)
    END DO

    END DO

    DO 16 K = 1, NDUMP-sn

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

    DO KK = 1, NC
    Rij = 0

    DO LL = 1, CL
    read(10, *) NM(LL), NID(LL), NTYP(LL), A1, A2, A3, B1, B2, B3, D1, D2, X(LL), Y(LL), Z(LL), C1, C2, C3
    END DO

    DO II = 1, CL-1
    DO JJ = II + 1, CL

    Rij_v = 0

    Rij_v = (sqrt((X(II) - X(JJ))**2 + (Y(II) - Y(JJ))**2 + (Z(II) - Z(JJ))**2))**(-1)

    Rij = Rij + Rij_v

    END DO
    END DO

    Rh(KK) = (Rij)


    write (18, *) (CL*CL*((Rh(KK)**(-1))))

    END DO

    !AVRh(K) = sum(Rh)/NC

    !write (18, *) ts, AVRh(K)
16 continue


    close(18)
    close(10)
end program main
