"""
Draw the SBML model's network which consists of nodes and reactions.
"""

import matplotlib.pyplot as plt

plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)

ax = plt.axes()

# Draw Reactions
ax.arrow(0,0,0.5,0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')

# Label Reactions
plt.text(0,1,"hello")

# Draw Nodes
plt.text(0-.10,0-.10,"A")
plt.text(0.5+.10, 0.5+.10, "B")

plt.show()



