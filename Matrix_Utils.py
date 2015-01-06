#/bin/python
from numpy import *;

def is_matrix_equals(M1,M2):
    if 2 == M1.ndim: 
        if M1.shape != M2.shape:
            return False;
        r,c = M1.shape;
        for i in xrange(r):
            for j in xrange(c):
                if abs(M1[i,j] - M2[i,j]) >= 1e-9:
                    return False;
        return True;
    elif 1 == M1.ndim:
        if M1.shape != M2.shape:
            return False;
        r = M1.shape[0];
        for i in xrange(r):
            if abs(M1[i] - M2[i]) >= 1e-9:
                return False;
        return True;

    else:
        raise Exception("equals_matrix function not support ndim = %d"%(M1.ndim));

def matrix_Ak(A,k): # A_k is the best rank-k approximination to A
    m,n = A.shape;
    if k > min(m,n):
        raise Exception("matrix_Ak requires k <= min(m,n), but m=%d, n=%d, k=%d"%(m,n,k));

    u,d,vt = linalg.svd(A);
    
    Ak = zeros([m,n]);
    for i in xrange(k):
        Ak += dot(u[:,i:i+1],vt[i:i+1,:]) * d[i];
    return Ak;

def matrix_read(filename):
    row = 0;
    col = -1;
    for line in file(filename, "r"):    
        row += 1;
        if -1 == col:
            line = line.strip();
            eles = line.split("\t");
            col  = len(eles);

    m = zeros([row,col]);
    i = 0;
    j = 0;
    for line in file(filename, "r"):
        line = line.strip();
        eles = line.split("\t");
        for j in xrange(len(eles)):
            m[i,j] = float(eles[j]);        
        i += 1;    

    return m;

def matrix_show(M):
    if 2 == M.ndim:
        r,c = M.shape;
        for i in xrange(r):
            for j in xrange(c):
                if (i > 3 and i < r-3) or (j > 3 and j < c - 3):
                    continue;
                elif i == 3 and i < r -3:
                    print " ...\t",;
                elif j == 3 and j < c -3:
                    print " ...\t",;   
                elif M[i,j] >= 0:
                    print " %.3f\t"%M[i,j],
                else:
                    print "%.3f\t"%M[i,j],
            print "";
    elif 1 == M.ndim:
        l = len(M);
        for i in xrange(l):
            if i > 3 and i < l-3:
                continue;
            elif i == 3 and i < l-3:
                print " ...\t",
            elif M[i] >= 0:
                print " %.3f\t"%M[i],
            else:
                print "%.3f\t"%M[i],
        print "";
    else:
        raise Exception("show_matrix not support ndim=%d yet"%M.ndim);

