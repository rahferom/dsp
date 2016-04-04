
import numpy as np

A=np.array([[1,2,3],[2,7,4]])
B=np.array([[1,-1],[0,1]])
C=np.array ([[5,-1],[9,1],[6,0]])
D=np.array([[3,-2,-1],[1,2,3]])
u=np.array([6,2,-3,5])
v=np.array([3,5,-1,4,])
ww=np.array([1,8,0,5])
ww[:,np.newaxis]

# Section 1- Matrix Dimensions

A.shape


(2L, 3L)


B.shape


(2L, 2L)


C.shape


(3L, 2L)


D.shape


(2L, 3L)


u.shape


(4L,)


v.shape


(4L,)


ww[:,np.newaxis]


array([[1],
       [8],
       [0],
       [5]])


ww.shape


(4L,)


ww


array([1, 8, 0, 5])


w=ww[:,np.newaxis]


w


array([[1],
       [8],
       [0],
       [5]])


w.shape


(4L, 1L)

# Section 2 - Vector Operations

u+v


array([ 9,  7, -4,  9])


u-v


array([ 3, -3, -2,  1])



6*u



array([ 36,  12, -18,  30])



u.v

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-72-dcc7927b007c> in <module>()
----> 1 u.v

AttributeError: 'numpy.ndarray' object has no attribute 'v'



np.absolute(u)



array([6, 2, 3, 5])

Section 3- Matrix Operations

A+C

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-74-637545a26abd> in <module>()
----> 1 a+c

ValueError: operands could not be broadcast together with shapes (2,3) (3,2) 



c.transpose()



array([[ 5,  9,  6],
       [-1,  1,  0]])



A-C.transpose()



array([[-4, -7, -3],
       [ 3,  6,  4]])



C.transpose+3*D


3*D



array([[ 9, -6, -3],
       [ 3,  6,  9]])

threed=3*d


threed


array([[ 9, -6, -3],
       [ 3,  6,  9]])



C.transpose()*threed



array([[ 45, -54, -18],
       [ -3,   6,   0]])



B*A

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-83-50e1f74171c6> in <module>()
----> 1 b*a

ValueError: operands could not be broadcast together with shapes (2,2) (2,3) 



B.A.transpose()

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-84-b6ba86fda853> in <module>()
----> 1 b.a.transpose()

AttributeError: 'numpy.ndarray' object has no attribute 'a'



A.transpose()



array([[1, 2],
       [2, 7],
       [3, 4]])

In [86]:

atrans=A.transpose()



atrans



array([[1, 2],
       [2, 7],
       [3, 4]])



B*atrans

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-88-b1ee2f2af16d> in <module>()
----> 1 b*atrans

ValueError: operands could not be broadcast together with shapes (2,2) (3,2) 



 

