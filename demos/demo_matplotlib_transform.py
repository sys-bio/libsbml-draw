import matplotlib.pyplot as plt
# import matplotlib.transforms as transforms

fig, ax = plt.subplots()

fig_multiplier = 2

fig.set_figheight(fig_multiplier*fig.get_figheight())
fig.set_figwidth(fig_multiplier*fig.get_figwidth())

x = [0, 1]
y = [0, 0]

plt.axis("equal")

ax.plot(x, y)

ax.plot([0,0], [0,1])

dy = 12/72

#i = 1  # 1 for dy
#i = 0  # 0 for dx

tmp = ax.transData.transform([(0,0), (1,1)])
print("pixels tmp: ", tmp)
tx = tmp[1,0] - tmp[0,0]  # 1 unit in display coords
print("pixels per data coord x: ", tx)
ty = tmp[1,1] - tmp[0,1]  # 1 unit in display coords
print("pixels per data coord y: ", ty)
tmp = 1/ty  # 1 pixel in display coords
print("data coord/pixel", tmp)
tmp = tmp*dy*ax.get_figure().get_dpi()  # shift pixels in display coords

print("data coord/pixel * inch * pixel/inch: ", tmp)


ax.plot(x, y)

ax.annotate("", [0,tmp], [1,tmp],
            size = 10,
            arrowprops = dict(arrowstyle = '<|-|>'))



plt.text(0.0, 0, "hello", fontsize=12)
plt.text(0.1, 0, "hello", fontsize=14)
plt.text(0.2, 0, "hello", fontsize=16)
plt.text(0.3, 0, "hello", fontsize=18)
plt.text(0.4, 0, "hello", fontsize=20)
plt.text(0.5, 0, "hello", fontsize=22)
plt.text(0.6, 0, "hello", fontsize=24)



plt.show()

