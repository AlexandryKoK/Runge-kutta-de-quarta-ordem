import numpy as np
import math


def du1(t,u10,u20):
    return u20

def du2(t,u10,u20):
    return -32.17/2 * u10
    #return np.exp(2*t)*np.sin(t) - 2*u10 + 2*u20


#print('u1_0 =')
#u1 = float(raw_input())

u1 = np.pi / 6

#print('u2_0 =')
#u2 = float(raw_input())

u2 = 0

print('Passos=')
h = float(raw_input())

def rungekutta(u1,u2,h):
    t0=0
    for i in range(1,21):
        u10=u1
        u20=u2
        k11 = h*du1(t0,u10,u20)
        #print(k11)
        k12 = h*du2(t0,u10,u20)
        #print(k12)
        k21 = h*du1(t0 + 0.5*h, u10 + 0.5*k11, u20 + 0.5*k12)
        #print(k21)
        k22 = h*du2(t0+0.5*h, u10 + 0.5*k11, u20 + 0.5*k12)
        #print(k22)
        k31 = h*du1(t0 + 0.5*h,u10 + 0.5*k12, u20 + 0.5*k22)
        #print(k31)
        k32 = h*du2(t0+0.5*h, u10 + 0.5*k21, u20 + 0.5*k22)
        #print(k32)
        k41 = h*du1(t0, u10 + 0.5*k31, u20 + k32)
        #print(k41)
        k42 = h*du2(t0+h, u10 + k31, u20 + k32)
        #print(k42)
        u1 = u10 + (1.0 / 6.0)*(k11 + 2 * k21 + 2 * k31 + k41)
        u2 = u20 + (1.0 / 6.0)*(k12 + 2 * k22 + 2 * k32 + k42) 
        t0 = t0 + h
    print(u1)
    print(u2)
        
    

rungekutta(u1,u2,h)

