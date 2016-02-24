#! /usr/bin/python

def gcd_bezout(n, m, verbose):
    ri_prec = 0
    ri = max(n, m)
    qi = 0
    ri_next = min(n, m)
    u_prec = 1
    u_next = 0
    v_prec = 0
    v_next = 1

    while(ri_next != 0):
        if(verbose):
            print '{}\t{}\t{}\t{}\t{}\t{}'.format(ri_prec, ri, qi, ri_next, u_next, v_next)
        ri_prec = ri
        ri = ri_next
        qi = ri_prec // ri
        ri_next = ri_prec % ri
        tmp = u_next
        u_next = u_prec - (qi*tmp)
        u_prec = tmp
        tmp = v_next
        v_next = v_prec - (qi*tmp)
        v_prec = tmp
        
    if(verbose):
        print '{}\t{}\t{}\t{}\t{}\t{}'.format(ri_prec, ri, qi, ri_next, u_next, v_next)
    return (ri, (u_prec, v_prec))

def inverse_modulaire(k, nmod):
    res_bezout = gcd_bezout(k,nmod,False)
    if(res_bezout[0] != 1) :
        return 0
    else :
        return (res_bezout[1][1] + nmod) % nmod

def lister_inversibles(n):
    liste_inversibles = list()
    for i in range(1,n):
        inverse = inverse_modulaire(i,n)
        if(inverse != 0):
            liste_inversibles.append(inverse)
    return liste_inversibles

def indicateur_euler(n):
    return len(lister_inversibles(n))
        
print '\n'
i = 5005
k = 1014
res_bezout = gcd_bezout(i,k,True)
print 'GCD(%d,%d) =  %d' % (i,k,res_bezout[0])
print '%d*%d + (%d)*%d = %d' % (res_bezout[1][0], max(i,k), res_bezout[1][1], min(i,k), res_bezout[0])
print inverse_modulaire(3,11)
print lister_inversibles(11)
print indicateur_euler(11)


    
