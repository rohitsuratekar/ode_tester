#May 2015
#Testing ODE function

import math
import initial_conditions
from ode_function import ode_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib
#matplotlib.use('TkAgg') #For interactive plots
from parameter_values import parameter_values
m2 = parameter_values()

v1 = m2[0]
v2 = m2[1]
v2i = m2[2]
v3 = m2[3]
v3i = m2[4]
v4 = m2[5]
v5 = m2[6]
v5i = m2[7]
v6 = m2[8]
v7 = m2[9]
v8 = m2[10]
k1 = m2[11]
k2 = m2[12]
k2i = m2[13]
k3 = m2[14]
k3i = m2[15]
k4 = m2[16]
k5 = m2[17]
k5i = m2[18]
k6 = m2[19]
k7 = m2[20]
k8 = m2[21]



for i in np.linspace(0.01, 0.05, 100):
    v4 = i

    def ode_function(y, t):
        pmpi = y[0]
        pi4p = y[1]
        pip2 = y[2]
        dag  = y[3]
        pmpa = y[4]
        erpa = y[5]
        cdpdag=y[6]
        erpi = y[7]
        # the model equations
        f_pmpi = (v1*erpi)/(k1 + erpi) + (v2i*pi4p)/(k2i + pi4p) - (v2*pmpi)/(k2 + pmpi)
        f_pi4p = (v2*pmpi)/(k2 + pmpi) + (v3i*pip2)/(k3i + pip2) - (v2i*pi4p)/(k2i + pi4p) - (v3*pi4p)/(k3 + pi4p)
        f_pip2 = (v3*pi4p)/(k3 + pi4p) - (v3i*pip2)/(k3i + pip2) - (v4*pip2)/(k4 + pip2)
        f_dag =  (v4*pip2)/(k4 + pip2) + (v5i*pmpa)/(k5i + pmpa) - (v5*dag)/(k5 + dag)
        f_pmpa = (v5*dag)/(k5 + dag)   - (v5i*pmpa)/(k5i + pmpa) - (v6*pmpa)/(k6 + pmpa)
        f_erpa = (v6*pmpa)/(k6 + pmpa) - (v7*erpa)/(k7 + erpa)
        f_cdpdag = (v7*erpa)/(k7 + erpa) - (v8*cdpdag)/(k8 + cdpdag)
        f_erpi = (v8*cdpdag)/(k8 + cdpdag) - (v1*erpi)/(k1 + erpi)
        return [f_pmpi, f_pi4p, f_pip2, f_dag, f_pmpa, f_erpa, f_cdpdag, f_erpi]



    y0 = initial_conditions.initial_conditions_vector()     # initial condition vector
    time_coord = initial_conditions.time_conditions()
    t  = np.linspace(time_coord[0], time_coord[1], 10000)   # time grid
    soln = odeint(ode_function, y0, t)

    pPMPI = soln[:, 0]
    pPI4P = soln[:, 1]
    pPIP2 = soln[:, 2]
    pDAG= soln[:, 3]
    pPMPA= soln[:, 4]
    pERPA= soln[:, 5]
    pCDPDAG= soln[:, 6]
    pERPI= soln[:, 7]

    all_concentrations_main = soln[-1,:]  #Get all final concentrations
    total_concentration_main = sum(all_concentrations_main)  #Total Concentration

    cPMPI = all_concentrations_main[0]
    cPI4P = all_concentrations_main[1]
    cPIP2 = all_concentrations_main[2]
    cDAG= all_concentrations_main[3]
    cPMPA= all_concentrations_main[4]
    cERPA= all_concentrations_main[5]
    cCDPDAG= all_concentrations_main[6]
    cERPI= all_concentrations_main[7]

    other_than_erpi = [ cPMPI, cPI4P, cPIP2, cDAG, cPMPA, cERPA, cCDPDAG ]
    total_pi = cPMPI + cERPI
    total_pa = cPMPA + cERPA
    other_than_cdpdag = [ total_pa, total_pi, cPI4P, cPIP2 ]


    j1 = [i1 for i1 in all_concentrations_main if i1 < 0 ] #Checking for negative values
    j2 = [i2 for i2 in other_than_erpi if i2 > cERPI ] #Checking Values greater than ERPI
    j3 = [i3 for i3 in other_than_cdpdag if i3 < cCDPDAG ] #Checking Values less than CDPDAG

    penalty_error = 0

    if len(j1) == 0:
        penalty_error = penalty_error -400
    if 481 < total_concentration_main < 484:
        penalty_error = penalty_error -0
    if len(j2) == 0:
        penalty_error = penalty_error -10
    if len(j3) == 0:
        penalty_error = penalty_error -5

    #Error checking
    rpip2=cPIP2/(cERPI+cPMPI) #Should be 0.05
    rpi4p=cPI4P/(cERPI+cPMPI)  #Should be 0.05
    rpa= (cPMPA+cERPA)/(cERPI+cPMPI) #Should be 0.167
    rdag= (cDAG)/(cERPI+cPMPI) #Should be 0.008

    error_from_pip2 = (math.fabs(rpip2-0.05))/0.05
    error_from_pi4p = (math.fabs(rpi4p-0.05))/0.05
    error_from_pa = (math.fabs(rpa-0.167))/0.167
    error_from_dag = (math.fabs(rdag-0.008))/0.008

    ferror = error_from_pip2 + error_from_pi4p + error_from_pa + error_from_dag
    #Adding Penalty Error
    ferror = ferror + 415 + penalty_error
    #print ferror
    efh2 = open('xyz.txt','a')
    efh2.write("%.3f\t%.3f\t%.3f\n" % (i,ferror,cPIP2))
    efh2.close()
