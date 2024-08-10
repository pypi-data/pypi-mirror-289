# MIT License

# Copyright (c) 2024 dechin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("-i", help="Set the input record file path.")
parser.add_argument("-ic", help="Set the cv index of input record file.")
parser.add_argument("-ib", help="Set the bias index of input record file.")
parser.add_argument("-o", help="Set the output FES file path.")
parser.add_argument("-sigma", help="Sigma value when calculating FES.")

args = parser.parse_args()

input_name = args.i
output_name = args.o
cv_index = np.array([int(x) for x in args.ic.split(',')], dtype=np.int32)
bias_index = int(args.ib)
sigma = float(args.sigma)

def read_out(file_name, idx=0, hat_lines=1, max_size=None, dlm=None):
    """ Read data from output files. """
    with open(file_name, 'r') as file:
        if max_size is None:
            lines = file.readlines()[hat_lines:]
        else:
            lines = file.readlines()[hat_lines: hat_lines + max_size]
    if isinstance(idx, int):
        cv = []
        for line in lines:
            l = line.strip()
            if dlm is None:
                cv.append(float(l.split()[idx]))
            else:
                cv.append(float(l.split(dlm)[idx]))
        cv = np.array(cv)
        return cv
    elif isinstance(idx, list):
        cv = []
        for line in lines:
            l = line.strip()
            cv_i = []
            for i in idx:
                if dlm is None:
                    cv_i.append(float(l.split()[i]))
                else:
                    cv_i.append(float(l.split(dlm)[i]))
            cv.append(cv_i)
        cv = np.array(cv)
        return cv
    else:
        raise ValueError("The data type of idx only support int and list.")

def save_fes(file_name, Z):
    """ Save the FES values. """
    np.savetxt(file_name, Z, delimiter=',')
