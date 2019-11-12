import numpy as np
import matplotlib.pyplot as plt
#%%
nums = [0.1,0.01,1]

fig = plt.figure(figsize=(10,10))
x = np.linspace(0,4,100)
for i in range (3):
    data_exp = np.loadtxt("euler_exp_{}.txt".format(i))
    data_imp = np.loadtxt("euler_imp_{}.txt".format(i))

    ax = fig.add_subplot(3,1,i+1)
    ax.plot(data_exp[:,0],data_exp[:,1], label="Euler_Explicit")
    ax.plot(data_imp[:,0],data_imp[:,1], label="Euler_Implicit")
    ax.plot(x,np.exp(-x), label = "Analitica")
    ax.set_title("$\omega\ *\ dt\ =\ {}$".format(nums[i]))
    ax.legend()

    plt.savefig("Soluciones_euler.png")
    plt.close()
#%%
prueba = np.arange(0.1,1.1,0.1)

fig2 = plt.figure(figsize=(10,15))

for i in range (10):
    data_exp = np.loadtxt("muere_exp_{}.txt".format(i))
    data_imp = np.loadtxt("muere_imp_{}.txt".format(i))

    ax = fig2.add_subplot(5,2,i+1)
    ax.plot(data_exp[:,0],data_exp[:,1], label="Euler_Explicit")
    ax.plot(data_imp[:,0],data_imp[:,1], label="Euler_Implicit")
    ax.plot(x,np.exp(-x), label = "Analitica")
    ax.set_title("$\omega\ *\ dt\ =\ {}$".format(prueba[i]))
    ax.legend()

    plt.savefig("Exp_muere_euler.png")
    plt.close()
#%%
