import numpy as np
from src.utils import *
from src.blocks import *
from src.layers import *
import tensorflow as tf
from matplotlib import pyplot as plt

# model = FeatureExtractor(weights=None)
# x = tf.random.normal((1, 96, 96, 3))
# y = model(x)
# print(y.shape)

# pos_encoding = positional_encoding(36, 256)
# plt.pcolormesh(pos_encoding[0], cmap='RdBu')
# plt.xlabel('Depth')
# plt.xlim((0, 256))
# plt.ylabel('Position')
# plt.colorbar()
# plt.title('Positional Encoding Test')
# plt.show()


def test_scaled_dot_product_attention(q, k, v):
    temp_out, temp_attn = scaled_dot_product_attention(q, k, v)
    print('Attention weights are:')
    print(temp_attn)
    print('Output is:')
    print(temp_out)


np.set_printoptions(suppress=True)
temp_k = tf.constant([[10, 0, 0],
                      [0, 10, 0],
                      [0, 0, 10],
                      [0, 0, 10]], dtype=tf.float32)
temp_v = tf.constant([[1, 0],
                      [10, 0],
                      [100, 5],
                      [1000, 6]], dtype=tf.float32)
temp_q = tf.constant([[0, 10, 0]], dtype=tf.float32)
test_scaled_dot_product_attention(temp_q, temp_k, temp_v)
temp_q = tf.constant([[0, 0, 10]], dtype=tf.float32)
test_scaled_dot_product_attention(temp_q, temp_k, temp_v)
temp_q = tf.constant([[10, 10, 0]], dtype=tf.float32)
test_scaled_dot_product_attention(temp_q, temp_k, temp_v)
temp_q = tf.constant([[0, 0, 10], [0, 10, 0], [10, 10, 0]], dtype=tf.float32)
test_scaled_dot_product_attention(temp_q, temp_k, temp_v)
