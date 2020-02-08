#!/home/rbdavid/bin/python
# ----------------------------------------
# USAGE:

# ----------------------------------------
# PREAMBLE:

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import MultipleLocator

plt.rc('axes', axisbelow=True)

unbiased_collective_variable_data_file = sys.argv[1]
unbiased_collective_variable_index = int(sys.argv[2])
equilib_index = int(sys.argv[3])
unbiased_projected_data_file = sys.argv[4]

# ----------------------------------------
# ANIMATION FUNCTIONS

def init():
        hexmap.set_offsets([[],[]])
        return hexmap

def animate(i):
        plt.cla()
        window = windows_list[i]
        equilib_position = equilib_positions_list[i]
        print i, window, equilib_position
        temp_unbiased_projected_data = np.array([[unbiased_projected_data[j][0],unbiased_projected_data[j][1],j+equilib_index] for j in range(len(unbiased_projected_data)) if unbiased_collective_variable_data_indices[j] == i])

        print len(temp_unbiased_projected_data)

        #if len(temp_projected_data) == 0:
        #        continue

        ax.hexbin(unbiased_projected_data[:,0],unbiased_projected_data[:,1],bins='log',gridsize=200,extent=hex_extent,mincnt=1,alpha=0.5,cmap='gray_r',linewidths=0.,vmin=plotting_vmin,vmax=plotting_vmax)    #,norm=norm_colors
        ax.hexbin(temp_unbiased_projected_data[:,0],temp_unbiased_projected_data[:,1],bins='log',gridsize=200,extent=hex_extent,mincnt=1,cmap='Spectral_r',linewidths=0.,zorder=100,vmin=plotting_vmin,vmax=plotting_vmax) #,norm=norm_colors
        
        plt.xlim(xlim)
        plt.ylim(ylim)
        plt.xlabel('Projection onto PC 1',size=12)
        plt.ylabel('Projection onto PC 2',size=12)
        plt.title('Frames with CV values within %.3f to %.3f $\AA$\nProjected onto Unbiased Eigenvecs.'%(bin_edges[i][0],bin_edges[i][1]),size=14)
        plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
        plt.savefig('window_%02d.unbiased_sampling.hexmap.png'%(window),dpi=600,transparent=True)
        return hexmap

# ----------------------------------------
xlim = (-28.5, 20.5)
ylim = (-8.0, 15.0)
hex_extent = (-28.5, 20.5,-8.0, 15.0)

windows_list = range(40)
dx = 0.375
equilib_positions_list = [3.625 + dx*i for i in windows_list]
print windows_list, equilib_positions_list, dx

# ----------------------------------------
nWindows = len(windows_list)
bin_edges = [[i-dx/2.0,i+dx/2.0] for i in equilib_positions_list]

collective_variable_data = np.loadtxt(unbiased_collective_variable_data_file)[equilib_index:,unbiased_collective_variable_index]    # only grabbing data associated with the biased collective variable space
unbiased_projected_data = np.loadtxt(unbiased_projected_data_file)[:,:2]    # only grabbing first two eigenvector projection values for each frame; will only be plotting in those dimensions
nFrames = len(unbiased_projected_data)
unbiased_collective_variable_data_indices = [int((collective_variable_data[i] - bin_edges[0][0])/dx) for i in range(nFrames)]

fig = plt.figure()
ax = fig.add_subplot(111)
hexmap = ax.hexbin(unbiased_projected_data[:,0],unbiased_projected_data[:,1],bins='log',gridsize=200,extent=hex_extent,mincnt=1,cmap='Spectral_r',linewidths=0.)        #,alpha=0.5,marginals=True
cb = plt.colorbar(hexmap,spacing='uniform',extend='max')
cb.set_label('Log of Counts')
plt.xlim(xlim)
plt.ylim(ylim)
plt.xlabel('Projection onto PC 1',size=14)
plt.ylabel('Projection onto PC 2',size=14)
plt.title('ZIKV Apo (5JRZ) Unbiased Trajectory Data\nProjected onto Unbiased Eigenvecs.',size=16)
plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
plt.tight_layout()
plt.savefig('unbiased_sampling.hexmap.png',dpi=600,transparent=True)
plt.close()

fig = plt.figure()
ax = fig.add_subplot(111)
hexmap = ax.hexbin(unbiased_projected_data[:,0],unbiased_projected_data[:,1],bins='log',gridsize=200,extent=hex_extent,mincnt=1,cmap='Spectral_r',linewidths=0.)        #,alpha=0.5,marginals=True
plt.xlim(xlim)
plt.ylim(ylim)
plt.xlabel('Projection onto PC 1',size=14)
plt.ylabel('Projection onto PC 2',size=14)
plt.title('Unbiased Trajectory Data\nProjected onto Unbiased Eigenvecs.',size=16)
plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
plotting_vmin = np.min(hexmap.get_array())
plotting_vmax = np.max(hexmap.get_array())

#print hexmap.get_array()[0]
print plotting_vmin, plotting_vmax

anim = FuncAnimation(fig,animate,init_func=init,frames=nWindows,interval=1000,repeat=False,blit=False)
anim.save('Unbiased_sampling_Ala230Ca_Ala247Ca.hexmap.mp4',extra_args=['-vcodec','libx264'],bitrate=2500,dpi=600)
plt.close()

#for i in range(nWindows):
#        print 'Working on window', windows_list[i]
#        temp_projected_data = np.array([[unbiased_projected_data[j][0],unbiased_projected_data[j][1],j+equilib_index] for j in range(nFrames) if unbiased_collective_variable_data_indices[j] == i])
#
#        print len(temp_projected_data)
#
#        if len(temp_projected_data) == 0:
#                continue
#
#        plt.hexbin(unbiased_projected_data[:,0],unbiased_projected_data[:,1],bins='log',gridsize=200,extent=hex_extent,mincnt=1,alpha=0.5,cmap='gray_r',linewidths=0.)
#        plt.hexbin(temp_projected_data[:,0],temp_projected_data[:,1],bins='log',gridsize=200,extent=hex_extent,mincnt=1,cmap='Spectral_r',linewidths=0.,zorder=100)
#        plt.xlim(xlim)
#        plt.ylim(ylim)
#        plt.xlabel('Projection onto PC 1',size=12)
#        plt.ylabel('Projection onto PC 2',size=12)
#        plt.title('Frames with CV values within %.2f to %.2f $\AA$\nProjected onto Unbiased Eigenvecs.'%(bin_edges[i][0],bin_edges[i][1]),size=14)
#        plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')
#        plt.tight_layout()
#        plt.savefig('window_%02d.unbiased_sampling.hexmap.png'%(windows_list[i]),dpi=600,transparent=True)
#        plt.close()

