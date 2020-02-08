# USAGE:

# PREAMBLE:

from plotting_functions import *

data_file = sys.argv[1]
selection_list = sys.argv[2]
system = sys.argv[3]

# ----------------------------------------
# MAIN:

data = np.loadtxt(data_file)
nSteps = data.shape[0]
nEig = data.shape[1]
print('Number of selections: %d, number of steps: %d' %(nEig,nSteps))

time = np.zeros(nSteps)
for i in list(range(nSteps)):
	time[i] = 200 + i*0.002		# units of time in ns; each frame is separated by 0.002 ns 

for i in list(range(nEig)):
	scat_hist(time[:],data[:,i],'k','Time (ns)','Data projected onto Eigenvector %d'%(i+1),'proj_data_time_evol.%02d'%(i),system,x_lim=(200,1300))

