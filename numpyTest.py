#!/bin/env python
# numpy library (http://www.numpy.org/)

import numpy as np
m1 = np.array([ [1,2,3],
                [7,3,4] ]); # fixed input
                
# m1 = np.zeros((4,3),int); # initialise matrix
r1 = np.ndim(m1);       # number of dimensions for matrix 1
m, p = np.shape(m1);    # no. of rows in m1 and cols in m1
# use range(0,4) to generate all indices
# use m1[i][j] to lookup an elem

print("Matrix m1 is an ", r1, "-dimensional matrix, of shape ", m, "x", p)
print("Contents:")
print(m1)
