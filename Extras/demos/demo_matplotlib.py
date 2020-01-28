import matplotlib.pyplot as plt


def get_ratio():
    """
    """
    axes = plt.gca()
    t = axes.transAxes.transform([(0, 0), (1, 1)])
#    print("t: ", type(t), ", ", len(t), ", ", t, ", ", t[1,1], ", ", t[0,1])
#    print("dpi: ", axes.get_figure().get_dpi())
    ratio = float(axes.get_figure().get_dpi() / (t[1,1] - t[0,1]) / 72.)*100.
    
    return ratio

fig = plt.figure()
axes = plt.gca()

print()
print("fig size: ", fig.get_size_inches())
print("dpi: ", fig.get_dpi())
t = axes.transAxes.transform([(0, 0), (1, 1)])
print("t: ", t )
print("t diff: ", (t[1,1] - t[0,1]) )
ratio = get_ratio()
print("ratio: ", ratio)
print()
print()
fig.set_size_inches(10,10)
print("fig size: ", fig.get_size_inches())
print("dpi: ", fig.get_dpi())
t = axes.transAxes.transform([(0, 0), (1, 1)])
print("t: ", t)
print("t diff: ", (t[1,1] - t[0,1]) )
ratio = get_ratio()
print("ratio: ", ratio)
print()
print()
fig.set_dpi(144)
print("fig size: ", fig.get_size_inches())
print("dpi: ", fig.get_dpi())
t = axes.transAxes.transform([(0, 0), (1, 1)])
print("t: ", t)
print("t diff: ", (t[1,1] - t[0,1]) )
ratio = get_ratio()
print("ratio: ", ratio)
print()
print()
