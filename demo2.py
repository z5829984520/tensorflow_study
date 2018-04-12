# coding=utf-8
import tensorflow as tf

# 简单的TensorFlow计算方式 每定义一个计算在TensorFlow里都看做一个节点

# 定义一些数据
x = 2
y = 3

# 加法
op1 = tf.add(x, y)

# 乘法(旧版本的TensorFlow用的是tf.mul)
op2 = tf.multiply(x, y)

# 幂次方(op2的op1次方)
op3 = tf.pow(op2, op1)

with tf.Session() as sess:
    op3 = sess.run(op3)
    print(op3)
