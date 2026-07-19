
import numpy as np


# 计算两个向量的内积
def get_dot(vec_a,vec_b):
    if len(vec_a) != len(vec_b):
        raise ValueError('维度必须相同')
    dot_sum = 0
    for a,b in zip(vec_a,vec_b):# zip() 等于 (1,2)(2,1) a=1 b=2 二次 a=2 b=1
        dot_sum += a * b
    
    return dot_sum
# 计算向量的模长 vec = (a,b) a*a + b*b
def get_norm(vec):
    norm_sum = 0
    for v in vec:
        norm_sum += v * v
    return np.sqrt(norm_sum) # 根号

# 计算两个向量的相似度 2个向量的点积 除两个向量的模长的乘积
def get_similar(vec_a,vec_b):
    resulf = get_dot(vec_a,vec_b) / (get_norm(vec_a) * get_norm(vec_b))
    return resulf


vac_a = [0.5,0.5]
vac_b = [0.7,0.7]
vac_c = [0.7,0.5]
vac_d = [-0.6,0.5]

print('ab:',get_similar(vac_a,vac_b))
print('ac:',get_similar(vac_a,vac_c))
print('ad:',get_similar(vac_a,vac_d))






