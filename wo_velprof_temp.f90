program main

    real, dimension (:), allocatable :: X, Y, Z, VX, VY, VZ
    real, dimension (:), allocatable :: zc, vl, avl
    integer, dimension (:), allocatable :: NID, NTYP, NM
    real :: stv, L, rc, v, ct, ke, temp, vv, vva, bs, x_s, x_e, dx
    integer :: I, IJ, J, K, P, NDUMP, NS, NB, NP, ts, CL, NC, MA, MB, F, SN, bn, x_len

    L  = 40
    NB = 3*(L**3)
    CL = 301
    VF = 1

    NC = 190
    NP = CL*NC

    NS = NB - NP

    MA = 1
    MB = 1

    NDUMP = 100
    SN = 1

    bs = 1

    bn = L/bs

    bn = int(bn)+1


    !print *, bn

    allocate (X(NB), Y(NB), Z(NB), VX(NB), VY(NB), VZ(NB), NM(NB), NID(NB), NTYP(NB))

    allocate (zc(bn), vl(bn), avl(bn))


    open (unit = 10, file = 'shear.lammpstrj')
    open (unit = 8, file = 'av_temp_v10.dat')

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

    ke = 0
    temp = 0

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

    DO K = 1, NB

    vv = 0

    stv = 0

    stv = Z(K)*0.25
! 0.25 is the srate
    !print *, stv

    vv = (VX(K)-stv)**2 +  (VY(K))**2 + (VZ(K))**2
        ke = ke + vv

    end do


!    print *, ke

    temp = ke/(NB*3)

    !print *, temp

    write (8, *) ts, temp

    END DO


    close(8)
    close(10)


end program main


