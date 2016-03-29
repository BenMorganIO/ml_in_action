# Numpy Examples

from numpy import *

random_array = random.rand(4, 4)
# array([[ 0.19388939,  0.19277884,  0.59986524,  0.03905984],
#        [ 0.10509243,  0.17752127,  0.38273379,  0.46309031],
#        [ 0.40639618,  0.69309673,  0.57234602,  0.74387191],
#        [ 0.06731941,  0.8979966 ,  0.61127765,  0.77631404]])

random_matrix = mat(random_array)
# matrix([[ 0.19388939,  0.19277884,  0.59986524,  0.03905984],
#         [ 0.10509243,  0.17752127,  0.38273379,  0.46309031],
#         [ 0.40639618,  0.69309673,  0.57234602,  0.74387191],
#         [ 0.06731941,  0.8979966 ,  0.61127765,  0.77631404]])

inverse_random_matrix = random_matrix.I
# matrix([[ 0.11846198, -1.4125783 ,  3.12719878, -2.15983614],
#         [ 0.10683393, -2.98519428,  0.50744603,  1.28912621],
#         [ 1.68977154,  1.2470436 , -1.17839566,  0.30023858],
#         [-1.4643956 ,  2.59366477,  0.06971528, -0.25216755]])

identity_matrix = inverse_random_matrix * random_matrix
# matrix([[  1.00000000e+00,  -3.05311332e-16,  -5.55111512e-17,
#           -4.44089210e-16],
#         [  1.11022302e-16,   1.00000000e+00,   2.22044605e-16,
#            0.00000000e+00],
#         [  5.55111512e-17,   0.00000000e+00,   1.00000000e+00,
#            0.00000000e+00],
#         [ -3.81639165e-17,   2.77555756e-17,   4.16333634e-17,
#            1.00000000e+00]])
