##Schéma Euler ordre 1
import matplotlib.pyplot as plt
import numpy as np 
def solve_euler_explicit(f, x0, dt, t_max = 100):
    x=np.array(x0)
    t=np.array(0)
    while t[-1]< t_max: #condition de fin
        xj=x[-1]
        tj=t[-1]
        x.append(xj+dt*f(xj))
        t.append(tj+dt)
    return t, x

#teste sur une fonction connue
def f(x):
    return -4*x

les_t, les_x=solve_euler_explicit(f,1, 10**-1)
plt.plot(les_t, les_x)
plt.grid
plt.show()


##Méthode de Heun ordre 2

def solve_heun(f,x0,dt, t_max):
    x=np.array(x0)
    t=np.array(0)
    while t[-1] < t_max:
        xj=x[-1]
        tj=t[-1]
        x_approx=xj+f(xj)*dt
        x.append(xj+(dt/2)*(f(xj)+x_approx))
        t.append(tj+dt)
    return t,x

def f(x):
    return -4*x

les_t, les_x=solve_euler_explicit(f,1, 10**-1)
plt.plot(les_t, les_x)
plt.grid
plt.show()
