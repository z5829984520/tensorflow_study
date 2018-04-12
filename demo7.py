# coding=utf-8
import tensorflow as tf

# TensorFlow多维度数据计算当数据维度不同时候默认向最多维度的数据补全计算

a = tf.constant([2, 3], name="a")
b = tf.constant([[0, 1], [2, 3]], name="b")

x = tf.add(a, b, name="add")
y = tf.multiply(a, b, name="mul")

with tf.Session() as sess:
    print sess.run(x), sess.run(y)
    writer = tf.summary.FileWriter('./graphs1', sess.graph)
    writer.close()