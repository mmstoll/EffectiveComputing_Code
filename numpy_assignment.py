# Effective Computing Coding Assignment

import numpy as np
import sys, os
import pickle

# sys.path.append(os.path.abspath('../shared'))
import my_module as mymod
from importlib import reload
reload(mymod)

# make sure the output directory exists
this_dir = os.path.abspath('.').split('/')[-1]
# this_parent = os.path.abspath('.').split('/')[-2]
out_dir = './' + this_dir + '_output/'
print('Creating ' + out_dir + ', if needed')
mymod.make_dir(out_dir)

print('\nCreate a 1-D array from a [list]:')
a = np.array([1,4,9,16,25,36,49,64,81,100])
print(a)

print('\nCreate a 1-D array taking the square root of array a:')
b = np.sqrt(a)
print(b)

print('\nReturn an array (from array a) whose values are limited to 10 and 50:')
c = np.clip(a,10,50)
print(c)

print('\nFind the index of the maximum value in array a:')
d = np.argmax(a)		
print(d)

print('\nCreate a 2-D array from a [list]:')
aa = np.array(np.arange(15)).reshape((5,3))
bb = np.array(np.arange(12)).reshape((2,6))
print('\n2-D arrays of different shapes:')
print('\naa =')
print(aa)
print('\nbb =')
print(bb)

print('\nView all the values in the third row')
print(aa[2, :]) #row 3 corresponds with index value = 2

print('\nChange the value of the number in row 3, column 2 to 15')
aa[2,1] = 15
print(aa)


# Pickle dump array aa
out_fn = out_dir + 'pickled_array.p'
pickle.dump(aa, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
r = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary

print('\nThe shape of the loaded object is')
print(r.shape)
