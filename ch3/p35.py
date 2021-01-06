import numpy as np

seed = 1
rng = np.random.default_rng(seed)

# X:= Y^2 + N_X
# Y:= N_Y
# N_X, N_Y \sim N(0,1), iid.

size = 200

NX = rng.normal(size=size)
NY = rng.normal(size=size)

Y = NY
X = Y**2 + NX

Z = np.zeros((size, 2))
Z[:, 0] = X
Z[:, 1] = Y



