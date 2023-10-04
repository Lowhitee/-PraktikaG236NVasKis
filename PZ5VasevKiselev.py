import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

def f(x):
    return np.sum(np.sin(5*np.cos(x)/2))

def grad_f(x):
    return -(5*np.sin(x)*np.cos((5*np.cos(x))/2))/2


def grad_descent_2d(f, grad_f, lr, num_iter=100, x0=None):
    if x0 is None:
        x0 = np.random.random(2)

    history = []

    curr_x = x0.copy()
    for iter_num in range(num_iter):
        entry = np.hstack((curr_x, f(curr_x)))
        history.append(entry)

        curr_x -= lr * grad_f(curr_x)

    return np.vstack(history)

steps = grad_descent_2d(f, grad_f, lr=0.1, num_iter=20)

path = []

X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-3, 3, 100))

fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

zs = np.array([f(np.array([x,y]))
              for x, y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)


ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, zorder=2)

ax.plot(xs=steps[:, 0], ys=steps[:, 1], zs=steps[:, 2],
        marker='.', markersize=2, zorder=3,
        markerfacecolor='y', lw=1, c='black')

ax.set_zlim(-5, 5)
ax.view_init(elev=60)
plt.show()