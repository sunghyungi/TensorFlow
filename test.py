import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = tf.constant(1234)
b = tf.constant(5000)
c = tf.constant(3000)
add_op = a + b * c
add_op2 = (a + b) * c
sess = tf.Session()
res1 = sess.run(add_op)
res2 = sess.run(add_op2)
print(res1)
print(res2)