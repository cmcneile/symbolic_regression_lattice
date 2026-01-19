import math

#
#
def extrap3(x,p):
    """
    Fit model p[0]  + p[1] * x + p[2] * x**2

    """
    res = []

    for i,point in enumerate(x):
        tmp_ = p['a'][0] * (1 + p['a'][1]*(point) + p['a'][2]*(point)**2  )
        res.append( tmp_ )

    return res

def extrap3_rat(x,p):
    """
    Fit model (p[0]  + p[1] * x)/( 1 + p[2] * x**2 )

    """
    res = []

    for i,point in enumerate(x):
        tmp_ = p['a'][0] * (1 + p['a'][1]*(point))/ (1 + p['a'][2]*(point)**2  )
        res.append( tmp_ )

    return res



def extrap5(x,p):
    """
    Fit model p[0]  + p[1] * x + p[2] * x**2+ p[3]*x**3 + p[4]*x**4

    """
    res = []

    for i,point in enumerate(x):
        tmp_ = p['a'][0]  + p['a'][1]*(point) + p['a'][2]*(point)**2 + p['a'][3]*(point)**3  + p['a'][4]*(point)**4
        res.append( tmp_ )

    return res

