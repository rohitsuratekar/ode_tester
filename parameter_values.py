#Parameter Values
original_parameters = open("test_para.txt", 'r')
m1 = original_parameters.read().split()
def parameter_values():
	v1 = m1[0]
	v1=float(v1)
	v2 = m1[1]
	v2=float(v2)
	v2i =v2i = m1[2]
	v2i=float(v2i)
	v3 = m1[3]
	v3=float(v3)
	v3i =m1[4]
	v3i=float(v3i)
	v4 = m1[5]
	v4=float(v4)
	v5 = m1[6]
	v5=float(v5)
	v5i =m1[7]
	v5i=float(v5i)
	v6 = m1[8]
	v6=float(v6)
	v7 = m1[9]
	v7=float(v7)
	v8 = m1[10]
	v8=float(v8)
	k1 = m1[11]
	k1 = float (k1)
	k2 = m1[12]
	k2 = float (k2)
	k2i = m1[13]
	k2i = float (k2i)
	k3 = m1[14]
	k3 = float (k3)
	k3i = m1[15]
	k3i = float (k3i)
	k4 = m1[16]
	k4 = float (k4)
	k5 = m1[17]
	k5 = float (k5)
	k5i = m1[18]
	k5i = float (k5i)
	k6 = m1[19]
	k6 = float (k6)
	k7 = m1[20]
	k7 = float (k7)
	k8 = m1[21]
	k8 = float (k8)
	return [v1,v2,v2i,v3,v3i,v4,v5,v5i,v6,v7,v8,k1,k2,k2i,k3,k3i,k4,k5,k5i,k6,k7,k8]
