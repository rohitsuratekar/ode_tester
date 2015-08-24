#ODE Function
from parameter_values import parameter_values
m2 = parameter_values()


def ode_function(y, t, test, test2):
	#print test+test2
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
