#Inital Conditions
def initial_conditions_vector():
	ipmpi = 17
	ipi4p = 17
  	ipip2 = 17
   	idag  = 2.72
	ipmpa = 39.78
	ierpa = 17
	icdpdag= 1
	ierpi = 323
	return ipmpi, ipi4p, ipip2, idag, ipmpa, ierpa, icdpdag, ierpi

def time_conditions():
	starting_point = 0
	end_point = 50000
	return starting_point, end_point
