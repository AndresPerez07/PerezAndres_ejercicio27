import numpy as np
import matplotlib.pyplot as plt

nums = [0.0001, 0.001, 0.01, 0.1, 0.3, 0.4, 0.5, 0.8, 0.9, 1.0]

fig = plt.figure(figsize=(10,15))
x = np.linspace(0,40,100)

ax = fig.add_subplot(1,1,1)
ax.plot(x,np.exp(-0.1*x), label="analitica")
for i in range(10):
    data_exp = np.loadtxt("euler_exp_{}.txt".format(i))
    ax.plot(data_exp[:,0], data_exp[:,1], label="$dt\ =\ {}$".format(nums[i]))

ax.set_title("Euler explicit scheme")
ax.legend()

plt.savefig("soluciones_euler_exp.png")
plt.close()

fig2 = plt.figure(figsize=(10,15))
ax = fig2.add_subplot(1,1,1)
ax.plot(x,np.exp(-0.1*x), label="analitica")
for i in range(10):
    data_imp = np.loadtxt("euler_imp_{}.txt".format(i))

    ax.plot(data_imp[:,0], data_imp[:,1], label="$dt\ =\ {}$".format(nums[i]))

ax.set_title("Euler implicit scheme")
ax.legend()

plt.savefig("soluciones_euler_imp.png")
plt.close()
