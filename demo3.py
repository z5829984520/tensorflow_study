# coding=utf-8

import tensorflow as tf

# 这里解释了TensorFlow懒运行思想

x = 2
y = 3

op1 = tf.add(x, y)

op2 = tf.multiply(x, y)

# 此节点在TensorFlow运行时候不会执行
useless = tf.multiply(x, op1)

op3 = tf.pow(op2, op1)

with tf.Session() as sess:
    op3 = sess.run(op3)
    print(op3)
