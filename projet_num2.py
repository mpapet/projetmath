##Schéma Euler ordre 1
import matplotlib.pyplot as plt
def solve_euler_explicit(f, x0, dt):
    x=[x0]
    t=[0]
    while t[-1]<10**2: #condition de fin
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

def solve_heun(f,x0,dt):
    x=[x0]
    t=[0]
    while t[-1] <10**2:
        xj=x[-1]
        tj=t[-1]
        x_appprox=xj+f(xj)*dt
        x.append(xj+(dt/2)*(f(xj)+x_approx))
        t.append(tj+dt)
    return t,x

def f(x):
    return -4*x

les_t, les_x=solve_euler_explicit(f,1, 10**-1)
plt.plot(les_t, les_x)
plt.grid
plt.show()
