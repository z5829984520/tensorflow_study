# coding=utf-8
import tensorflow as tf

# 一个视图绑定一个session视图

g = tf.Graph()

with g.as_default():
    a = 3
    b = 5

    x = tf.add(a, b)

sess = tf.Session(graph=g)
print sess.run(x)
