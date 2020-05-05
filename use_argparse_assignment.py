"""
Code to test passing command line arguments to a program using the 
argparse module.

This is a helpfule technique for making code that runs both on your
laptop and on a remote machine - where you might tell it to process
a larger pile of data.

Usage from the linux command line:
python use_argparse -a 'hello' -b 6 -v True

Usage from the ipython command line:
run use_argparse -a 'hello' -b 6 -v True

NOTE: it does not matter which order you pass the arguments in.

NOTE: to pass a NEGATIVE NUMBER as an argument you have to enclose it in quotes, with a space before the minus sign:
run use_argparse -c " -108.77"

"""

# imports
import argparse

# def boolean_string(s):
#     # this function helps with getting Boolean input
#     if s not in ['False', 'True']:
#         raise ValueError('Not a valid boolean string')
#     return s == 'True' # note use of ==

# create the parser object
parser = argparse.ArgumentParser()

# NOTE: argparse will throw an error if:
#     - a flag is given with no value
#     - the value does not match the type
# and if a flag is not given it will be filled with the default.
parser.add_argument('-a', '--a_string', default='stranger', type=str) #input your name
parser.add_argument('-m', '--integer_m', default=1, type=int) #input your birth month
parser.add_argument('-d', '--integer_d', default=1, type=int) #input your birth day
parser.add_argument('-y', '--integer_y', default=2000, type=int) #input your birth year
# parser.add_argument('-m', '--float_c', default=1.5, type=float)
# parser.add_argument('-y', '--verbose', default=True, type=boolean_string)
# Note that you assign a short name and a long name to each argument.
# You can use either when you call the program, but you have to use the
# long name when getting the values back from "args".

# get the arguments
args = parser.parse_args()
months = ['Not a real month','January','February','March','April','May','June','July','August','September','October','November','December']
# print(months)

# output
month_name = months[args.integer_m]
if args.integer_m == 0:
	print('This is not a valid birthday month')
elif args.integer_m != 0:
	print('\nHello, '+ args.a_string)
	print('\nYour birthday is:')
	print(month_name,args.integer_d,args.integer_y)



