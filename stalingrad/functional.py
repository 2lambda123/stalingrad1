from tensor import Tensor

def relu(x: Tensor):
  x.data = np.maximum(x, 0.0)