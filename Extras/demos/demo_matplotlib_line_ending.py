import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.close()
plt.plot([1,2],[0,4], 'w')
ax = plt.gcf().axes[0]

polygons = {\
        '|':np.array([[0,0],[0,1],[0.1,1],[0.1,-1],[0,-1],[0,0]], dtype=float),
        'arrow1':np.array([[0,0],[0,1],[-1,2],[3,0],[-1,-2],[0,-1],[0,0]], dtype=float),
        'arrow2':np.array([[0,0],[-1,1],[0,2],[3,0],[0,-2],[-1,-1],[0,0]], dtype=float),
        }

orig = (1.1,2.)
target = (2.,2.5)
shrinkA = 0.
shrinkB = 0.

xyA = polygons.get("arrow1")
xyB = polygons.get("arrow2")

kwargsA = dict( lw=1., ec='k', fc='gray' )
kwargsB = dict( lw=1., ec='k', fc='b' )

polA = patches.Polygon( xyA, **kwargsA )
polB = patches.Polygon( xyB, **kwargsB )

#polA, polB = patchesAB( '|', 'arrow1', orig, target, 20.,1.,60.,60.,
#                        kwargsA, kwargsB, shrinkA, shrinkB )
#ax.add_patch(polA)

ax.add_patch(polA)
ax.add_patch(polB)

ax.annotate('arrow1', xy=target, xycoords='data',
             xytext=orig, textcoords='data',
             arrowprops=dict(arrowstyle='-', patchA=polA, patchB=polB,
                 lw=1., shrinkA=shrinkA, shrinkB=shrinkB, relpos=(0.,0.),
                 mutation_scale=1.))

ax.annotate('arrow2', xy=target, xycoords='data',
             xytext=orig, textcoords='data',
             arrowprops=dict(arrowstyle='-', patchA=polA, patchB=polB,
                 lw=1., shrinkA=shrinkA, shrinkB=shrinkB, relpos=(0.,0.),
                 mutation_scale=1.))

plt.autoscale()
plt.xlim(1.,2.2)
plt.ylim(0.5,4)
plt.show()