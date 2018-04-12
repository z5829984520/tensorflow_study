# coding=utf-8
import tensorflow as tf

# 生成[x, y]0矩阵  x代表维度 y代表每个维度里的长度  类似还有tf.ones 1矩阵
a = tf.zeros([2, 10], tf.int32, name="a")

b = tf.constant([[0, 1], [2, 3], [3, 4]], name="b")
# 相同维度和长度的0矩阵 tf.zeros_like(value, dtype=None, name=None, optimize=True)  类似还有tf.ones_like 1矩阵
c = tf.zeros_like(b, name="c")

# 生成一个[x, y] value矩阵
d = tf.fill([2, 3], 8, name="d")

with tf.Session() as sess:
    print sess.run(a)
    print sess.run(c)
    print sess.run(d)

