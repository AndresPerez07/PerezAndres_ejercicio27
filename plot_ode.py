import numpy as np
import matplotlib.pyplot as plt


nums = [0.0001, 0.001, 0.01, 0.1, 0.3, 0.4,0.5,0.8,0.9, 1.0]

fig = plt.figure(figsize=(10,15))
x = np.linspace(0,4,100)

for i in range(10):
    data_exp = np.loadtxt("euler_exp_{}.txt".format(i))

    ax = fig.add_subplot(5,2,i+1)
    ax.plot(data_exp[:,0], data_exp[:,1], label="euler_explicit")
    ax.plot(x,np.exp(-x), label="analitica")
    ax.set_title("$\omega\ *\ dt\ =\ {}$".format(nums[i]))
    ax.legend()

plt.savefig("soluciones_euler_exp.png")
plt.close()

fig2 = plt.figure(figsize=(10,15))
x = np.linspace(0,4,100)

for i in range(10):
    data_imp = np.loadtxt("euler_imp_{}.txt".format(i))

    ax = fig2.add_subplot(5,2,i+1)
    ax.plot(data_imp[:,0], data_imp[:,1], label="euler_implicit")
    ax.plot(x,np.exp(-x), label="analitica")
    ax.set_title("$\omega\ *\ dt\ =\ {}$".format(nums[i]))
    ax.legend()

plt.savefig("soluciones_euler_imp.png")
plt.close()
