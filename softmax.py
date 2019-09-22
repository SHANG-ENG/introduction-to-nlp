import numpy as np

def softmax(scores):
    return np.exp(scores) / sum(np.exp(scores))


scores = np.array([3,1,0.2])

print(softmax(scores))
print(softmax(scores*10))
print(softmax(scores/10))

#offset=[]
#for step in range(3001):
#    offset.append((step*128)%1000)
