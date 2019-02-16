# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:01:37 2019

@author: nrhaw
"""

import matplotlib.pyplot as plt

plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)

size=4

plt.gcf().set_size_inches(size, size)
 
plt.xticks([])
plt.yticks([])

max_text_size = size * 12
min_text_size = size
label_text_size = size * 2.5

ax = plt.gca()

#plt.arrow(x_pos, y_pos, x_scale * length, y_scale * length,
#          fc=fc, ec=ec, alpha=alpha, width=width,
#          head_width=head_width, head_length=head_length,
#          **arrow_params)

#plt.text(x, y, label, size=label_text_size, ha='center', va='center',
#                 color=labelcolor or fc)

ax = plt.axes()
ax.arrow(0,0,0.5,0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')

plt.text(0,1,"hello")
plt.text(0-.10,0-.10,"A")
plt.text(0.5+.10, 0.5+.10, "B")

#size = 4
#plt.figure(figsize=(size, size))

#make_arrow_plot(d, display=display, linewidth=0.001, edgecolor=None,
#                    normalize_data=scaled, head_starts_at_zero=True, size=size)

#plt.show()

plt.show()

