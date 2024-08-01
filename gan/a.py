from __future__ import absolute_import
from __future__ import print_function

import sys
import os

import nngen as ng


# data types
act_dtype = ng.int16
weight_dtype = ng.int16
bias_dtype = ng.int16
scale_dtype = ng.int16

# input
input_layer = ng.placeholder(dtype=act_dtype,
                             shape=(1, 32, 32, 3),  # N, H, W, C
                             name='input_layer')

# layer 0: conv2d (with bias and scale (= batchnorm)), relu, max_pool
w0 = ng.variable(dtype=weight_dtype,
                 shape=(64, 3, 3, 3),  # Och, Ky, Kx, Ich
                 name='w0')
b0 = ng.variable(dtype=bias_dtype,
                 shape=(w0.shape[0],), name='b0')
s0 = ng.variable(dtype=scale_dtype,
                 shape=(w0.shape[0],), name='s0')

a0 = ng.conv2d(input_layer, w0,
               strides=(1, 1, 1, 1),
               bias=b0,
               scale=s0,
               act_func=ng.relu,
               sum_dtype=ng.int64)

a0p = ng.max_pool_serial(a0,
                         ksize=(1, 2, 2, 1),
                         strides=(1, 2, 2, 1))

# layer 1: conv2d, relu, reshape
w1 = ng.variable(weight_dtype,
                 shape=(64, 3, 3, a0.shape[-1]),
                 name='w1')
b1 = ng.variable(bias_dtype,
                 shape=(w1.shape[0],),
                 name='b1')
s1 = ng.variable(scale_dtype,
                 shape=(w1.shape[0],),
                 name='s1')

a1 = ng.conv2d(a0p, w1,
               strides=(1, 1, 1, 1),
               bias=b1,
               scale=s1,
               act_func=ng.relu,
               sum_dtype=ng.int64)

a1r = ng.reshape(a1, [1, -1])

# layer 2: full-connection, relu
w2 = ng.variable(weight_dtype,
                 shape=(256, a1r.shape[-1]),
                 name='w2')
b2 = ng.variable(bias_dtype,
                 shape=(w2.shape[0],),
                 name='b2')
s2 = ng.variable(scale_dtype,
                 shape=(w2.shape[0],),
                 name='s2')

a2 = ng.matmul(a1r, w2,
               bias=b2,
               scale=s2,
               transposed_b=True,
               act_func=ng.relu,
               sum_dtype=ng.int64)

# layer 3: full-connection, relu
w3 = ng.variable(weight_dtype,
                 shape=(10, a2.shape[-1]),
                 name='w3')
b3 = ng.variable(bias_dtype,
                 shape=(w3.shape[0],),
                 name='b3')
s3 = ng.variable(scale_dtype,
                 shape=(w3.shape[0],),
                 name='s3')

# output
output_layer = ng.matmul(a2, w3,
                         bias=b3,
                         scale=s3,
                         transposed_b=True,
                         name='output_layer',
                         sum_dtype=ng.int64)

import numpy as np

w0_value = np.random.normal(size=w0.length).reshape(w0.shape)
w0_value = np.clip(w0_value, -5.0, 5.0)
w0_value = w0_value * (2.0 ** (weight_dtype.width - 1) - 1) / 5.0
w0_value = np.round(w0_value).astype(np.int64)
w0.set_value(w0_value)

b0_value = np.random.normal(size=b0.length).reshape(b0.shape)
b0_value = np.clip(b0_value, -5.0, 5.0)
b0_value = b0_value * (2.0 ** (weight_dtype.width - 1) - 1) / 5.0 / 100.0
b0_value = np.round(b0_value).astype(np.int64)
b0.set_value(b0_value)

s0_value = np.ones(s0.shape, dtype=np.int64)
s0.set_value(s0_value)

w1_value = np.random.normal(size=w1.length).reshape(w1.shape)
w1_value = np.clip(w1_value, -5.0, 5.0)
w1_value = w1_value * (2.0 ** (weight_dtype.width - 1) - 1) / 5.0
w1_value = np.round(w1_value).astype(np.int64)
w1.set_value(w1_value)

b1_value = np.random.normal(size=b1.length).reshape(b1.shape)
b1_value = np.clip(b1_value, -5.0, 5.0)
b1_value = b1_value * (2.0 ** (weight_dtype.width - 1) - 1) / 5.0 / 100.0
b1_value = np.round(b1_value).astype(np.int64)
b1.set_value(b1_value)

s1_value = np.ones(s1.shape, dtype=np.int64)
s1.set_value(s1_value)

w2_value = np.random.normal(size=w2.length).reshape(w2.shape)
w2_value = np.clip(w2_value, -5.0, 5.0)
w2_value = w2_value * (2.0 ** (weight_dtype.width - 1) - 1) / 5.0
w2_value = np.round(w2_value).astype(np.int64)
w2.set_value(w2_value)

b2_value = np.random.normal(size=b2.length).reshape(b2.shape)
b2_value = np.clip(b2_value, -5.0, 5.0)
b2_value = b2_value * (2.0 ** (weight_dtype.width - 1) - 1) / 5.0 / 100.0
b2_value = np.round(b2_value).astype(np.int64)
b2.set_value(b2_value)

s2_value = np.ones(s2.shape, dtype=np.int64)
s2.set_value(s2_value)

w3_value = np.random.normal(size=w3.length).reshape(w3.shape)
w3_value = np.clip(w3_value, -5.0, 5.0)
w3_value = w3_value * (2.0 ** (weight_dtype.width - 1) - 1) / 5.0
w3_value = np.round(w3_value).astype(np.int64)
w3.set_value(w3_value)

b3_value = np.random.normal(size=b3.length).reshape(b3.shape)
b3_value = np.clip(b3_value, -5.0, 5.0)
b3_value = b3_value * (2.0 ** (weight_dtype.width - 1) - 1) / 5.0 / 100.0
b3_value = np.round(b3_value).astype(np.int64)
b3.set_value(b3_value)

s3_value = np.ones(s3.shape, dtype=np.int64)
s3.set_value(s3_value)

# conv2d, matmul
# par_ich: parallelism in input-channel
# par_och: parallelism in output-channel
# par_col: parallelism in pixel column
# par_row: parallelism in pixel row
# cshamt_out: right shift amount after applying bias/scale

par_ich = 2
par_och = 2
cshamt_out = weight_dtype.width + 1

a0.attribute(par_ich=par_ich, par_och=par_och,
             cshamt_out=weight_dtype.width + 1)
a1.attribute(par_ich=par_ich, par_och=par_och,
             cshamt_out=weight_dtype.width + 1)
a2.attribute(par_ich=par_ich, par_och=par_och,
             cshamt_out=weight_dtype.width + 1)
output_layer.attribute(par_ich=par_ich, par_och=par_och,
                       cshamt_out=weight_dtype.width + 1)

# max_pool
# par: parallelism in in/out channel

par = par_och

a0p.attribute(par=par)

input_layer_value = np.random.normal(size=input_layer.length).reshape(input_layer.shape)
input_layer_value = np.clip(input_layer_value, -5.0, 5.0)
input_layer_value = input_layer_value * (2.0 ** (input_layer.dtype.width - 1) - 1) / 5.0
input_layer_value = np.round(input_layer_value).astype(np.int64)

eval_outs = ng.eval([output_layer], input_layer=input_layer_value)
output_layer_value = eval_outs[0]

print(output_layer_value)

silent = False
axi_datawidth = 32

# to Veriloggen object
# targ = ng.to_veriloggen([output_layer], 'hello_nngen', silent=silent,
#                        config={'maxi_datawidth': axi_datawidth})

# to IP-XACT (the method returns Veriloggen object, as well as to_veriloggen)
targ = ng.to_ipxact([output_layer], 'hello_nngen', silent=silent,
                    config={'maxi_datawidth': axi_datawidth})
print('# IP-XACT was generated. Check the current directory.')

# to Verilog HDL RTL (the method returns a source code text)
# rtl = ng.to_verilog([output_layer], 'hello_nngen', silent=silent,
#                    config={'maxi_datawidth': axi_datawidth})

# to memory image:
# on a real FPGA platform, this image will be used as a part of the model definition.
param_filename = 'hello_nngen.npy'
chunk_size = 64

param_data = ng.export_ndarray([output_layer], chunk_size)
np.save(param_filename, param_data)

# If you don't check the RTL behavior, exit here.
# print('# Skipping RTL simulation. If you simulate the RTL behavior, comment out the next line.')
# sys.exit()

