#!/home/rbdavid/bin/python
# ----------------------------------------
# USAGE:

# ----------------------------------------
# PREAMBLE:

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation

plt.rc('axes', axisbelow=True)

original_unbiased_projected_data_file = sys.argv[1]
new_unbiased_projected_data_file = sys.argv[2]
#equilib_index = int(sys.argv[3])

xlim = (-28.5, 20.5)
ylim = (-8.0, 15.0)
hexbin_extent = (-28.5, 20.5,-8.0, 15.0)
gridsize = 200
plot_title_string = 'Apo Unbiased Trajectory Data\nProjected onto Apo Unbiased Eigenvecs.'
#plot_title_string = 'ssRNA All Unbiased Sampling\nProjected onto Apo Unbiased Eigenvecs.'
#plot_title_string = r'ssRNA$_{1-2}$ All Unbiased Sampling' + '\nProjected onto Apo Unbiased Eigenvecs.'

#### 
# Plotting unbiased trajectory data projected onto the first two eigenvectors of unbiased trajectory in which the transition is observed
####

original_unbiased_projected_data = np.loadtxt(original_unbiased_projected_data_file)#[100000:]
new_unbiased_projected_data = np.loadtxt(new_unbiased_projected_data_file)#[100000:]

figure,ax = plt.subplots()

image = plt.hexbin(original_unbiased_projected_data[:,0],original_unbiased_projected_data[:,1],bins='log',gridsize=gridsize,extent=hexbin_extent,mincnt=1,alpha=0.5,cmap='gray_r',linewidths=0.,vmax=3.5)        #alpha=0.25,gray_r,marginals=True
image = plt.hexbin(new_unbiased_projected_data[:,0],new_unbiased_projected_data[:,1],bins='log',gridsize=gridsize,extent=hexbin_extent,mincnt=1,cmap='inferno_r',linewidths=0.,vmax=3.5)        #cmap='Spectral_r'
plt.xlim(xlim)
plt.ylim(ylim)
ax.set_aspect('equal')
plt.xlabel('Projection onto PC 1',size=12)
plt.ylabel('Projection onto PC 2',size=12)
plt.title(plot_title_string,size=14)
plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
#cb = plt.colorbar(image,spacing='uniform',extend='max')
cb = plt.colorbar(image,spacing='uniform')
cb.set_label('Log of Counts')
plt.tight_layout()
plt.savefig('unbiased_sampling.spectral_hexmap.png',dpi=600,transparent=True)
plt.close()

