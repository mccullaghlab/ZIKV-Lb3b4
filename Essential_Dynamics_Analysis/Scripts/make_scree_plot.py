


In [33]: fix, ax = plt.subplots(1,1)                                                                                                                                                                               

In [34]: plt.plot(nEigval,eigval[:,0],'-b')                                                                                                                                                                        
Out[34]: [<matplotlib.lines.Line2D at 0x7f9a8a1402d0>]

In [35]: plt.xlabel('Component Number',size=20)                                                                                                                                                                    
Out[35]: Text(0.5, 0, 'Component Number')

In [36]: plt.ylabel('Eigenvalue',size=20)                                                                                                                                                                          
Out[36]: Text(0, 0.5, 'Eigenvalue')

In [37]: plt.savefig('temp.png',dpi=600,transparent=True)                                                                                                                                                          

In [38]: plt.tight_layout()                                                                                                                                                                                        

In [39]: plt.savefig('temp.png',dpi=600,transparent=True)                                                                                                                                                          

In [40]: 44*3                                                                                                                                                                                                      
Out[40]: 132

In [41]: axins = inset_axes(ax,width='65%',height='65%')                                                                                                                                                           

In [42]: plt.plot(nEigval[:10],eigval[:10,0],'-bo')                                                                                                                                                                
Out[42]: [<matplotlib.lines.Line2D at 0x7f9a8a120b90>]

In [43]: plt.ylim((0,200))                                                                                                                                                                                         
Out[43]: (0, 200)

In [44]: plt.savefig('temp.png',dpi=600,transparent=True)                                                                                                                                                          

In [45]: plt.savefig('SCREE_plot.png',dpi=600,transparent=True)
