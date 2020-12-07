program main

    real, dimension (:), allocatable :: X, Y, Z, VX, VY, VZ
    real, dimension (:), allocatable :: zc, vl, avl
    integer, dimension (:), allocatable :: NID, NTYP, NM
    real :: L, rc, v, ct, vv, vva, bs, x_s, x_e, dx
    integer :: I, IJ, J, K, P, NDUMP, NS, NB, NP, ts, CL, NC, MA, MB, F, SN, bn, x_len

    L  = 20
    NB = 3*(L**3)
    CL = 301
    VF = 1

    NC = 190
    NP = CL*NC

    NS = NB - NP

    MA = 1
    MB = 1

    NDUMP = 6000
    SN = 5000

    bs = 1

    bn = L/bs

    bn = int(bn)+1


    !print *, bn

    allocate (X(NB), Y(NB), Z(NB), VX(NB), VY(NB), VZ(NB), NM(NB), NID(NB), NTYP(NB))

    allocate (zc(bn), vl(bn), avl(bn))


    x_e = 10
    x_s = -10
    x_len = 21

    !dx = (x_e - x_s) / (x_len - 1)
    dx = 1
    zc(1:x_len) = [(x_s + ((i-1)*dx), i = 1, x_len)]

    !print *, zc

    avl = 0

    open (unit = 10, file = 'shear.lammpstrj')
    open (unit = 8, file = 'av_vel_prof_vx.dat')

    Do IJ = 1, SN

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

    !DO P = 1, NDUMP - SN

    DO P = 1, NDUMP - SN

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

    DO I = 1, NB
    read(10, *) NM(I), NID(I), NTYP(I), X(I), Y(I), Z(I), VX(I), VY(I), VZ(I), D1, D2, A1, A2, A3, C1, C2, C3
    END DO

    vl = 0

    DO J = 1, bn

    vv = 0
    ct = 0

    DO K = 1, NB
    IF ((Z(K).LT.zc(J+1)) .AND. (Z(K).GE.zc(J))) THEN
        vva = 0
        vva = VX(K)
        vv = vv + vva
        ct = ct + 1
    END IF
    END DO

    !print *, vv

    vv = vv/ct

    !print *, vv

    vl(J) = vv

    END DO

    !print *, vl

    avl = avl + vl

    END DO

    avl = avl/(NDUMP - SN)


    DO J = 1, bn

    write(8, *) zc(J), avl(J)

    END DO


    close(8)
    close(10)


end program main
