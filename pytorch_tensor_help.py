import torch
import numpy as np

# PyTorch Examples

# Create Tensor (three attributes: shape, dtype, device <- (cpu/gpu))
data = [[1,2],[3,4]]
data_tensor = torch.tensor(data)
#   or
data_np = np.array(data)
data_np_tensor = torch.from_numpy(data_np)

#   From another tensor
data_zeros_tensor = torch.zeros_like(data_tensor)
data_random_tensor = torch.rand_like(data_tensor, dtype=torch.float)
'''
print(f"Normal: \n {data_tensor}\n")
print(f"Numpy: \n {data_np_tensor}\n")
print(f"Zeroes: \n {data_zeros_tensor}\n")
print(f"Random: \n {data_random_tensor}\n")
'''

# You can define a shape and fill it
shape = (3,4)
t_rand = torch.rand(shape)
print(f"Random: \n {t_rand}\n")


# We want to move our tensor to the GPU if possible (FASTER)
tensor=t_rand
if torch.cuda.is_available():
    tensor = t_rand.to('cuda')

# NumPy Slicing and Indexing
#  : = all
# ... = print horizontal
print("Last Col printed horizontal: \n", tensor[...,-1])

# Join tensors with .cat or .stack
tensor_tensor = torch.cat([tensor, tensor], dim=1)
tensor_tensor2 = torch.cat([tensor, tensor], dim=0)
print(".cat dim=1: \n",tensor_tensor)
print(".cat dim=0: \n",tensor_tensor2)

# matrix multiplication (needs transposition if same dimensions)
#   all three ways end up with same result
mm1 = tensor @ tensor.T
mm2 = tensor.matmul(tensor.T) 
mm3 = torch.rand_like(tensor) # create answer tensor
mm3 = torch.matmul(tensor, tensor.T)

# element wise multiplication (doesn't need transposition)
#   all three ways end up with same result
em1 = tensor * tensor
em2 = tensor.mul(tensor)
em3 = torch.rand_like(tensor)
em3 = torch.mul(tensor, tensor)

# convert to python numerical value
sum_tensor = tensor.sum()
sum_tensor_item = sum_tensor.item()
print("Sum Tensor: ",sum_tensor_item)



# In place operations (+=,\=, etc.)
# add a _ suffix to ex. copy() -> copy_()
print("Before: \n",em1)
em1.add_(0.69)
print(".add_(0.69) \n",em1)


# Link to numpy
numpy_tensor = tensor.numpy()
#   From here on out, any changes to the tensor, will change the numpy array
n = np.ones(5)
t = torch.from_numpy(n)
#   From here on out, any changes to the numpy array, will change the tensor