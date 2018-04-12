# coding=utf-8
import tensorflow as tf

# 使用TensorFlow生成可视化视图

a = tf.constant(2, name="a")
b = tf.constant(3, name="b")

x = tf.add(a, b, name="add")


with tf.Session() as sess:
    print sess.run(x)
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    writer.close()


# 生成了可是视图后在终端中使用 $ tensorboard --logdir="./graphs" --port 6066
