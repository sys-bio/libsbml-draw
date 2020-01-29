from matplotlib.patches import BoxStyle, FancyBboxPatch
from matplotlib import pyplot as plt

def get_length(pts_needed):
    
    dxy = pts_needed/72 # inches

    print()
    tmp_x = ax.transData.transform([(0,0), (1,1)])
    print("pixels tmp: ", tmp_x)
    tx = (tmp_x[1,0] - tmp_x[0,0])/540  # 1 unit in display coords
    print("pixels per libs coord x: ", tx)
        
    tmp_y = ax.transData.transform([(0,0), (1,1)])
    ty = (tmp_y[1,1] - tmp_y[0,1])/520  # 1 unit in display coords
    print("pixels per libs coord y: ", ty)

    tmp = 1/ty  # 1 pixel in display coords
    print("libs coord/pixel", tmp)

    length_data_coords = tmp*dxy*ax.get_figure().get_dpi()  # shift pixels in display coords
    #print("libs coord/pixel * inch * pixel/inch: ", tmp)
    print(f"length libs coords for {pts_needed}", length_data_coords)
    print()

    return length_data_coords

def get_node_patch(node_center_x, node_center_y):

    width = get_length(12*5)
    height = get_length(12*1)
    
    node_patch = FancyBboxPatch(
            [node_center_x-width/2, node_center_y-height/2],
            width,
            height,
            edgecolor="blue",
            facecolor="lightblue",
            linewidth=1,
            boxstyle=BoxStyle("round", pad=0.4, rounding_size=.8),
            mutation_scale=10
            )
        
    return node_patch    


fig = plt.figure()
#fig.set_dpi(1200)

print("fig dims: ", fig.get_figwidth(), fig.get_figheight())
print("fig dpi: ", fig.get_dpi())



ax = plt.gca()

node_centers = [(0, 500), (0, 0), (500, 0),  (500, 500)] 


for x, y in node_centers:
    ax.add_patch(get_node_patch(x, y))


for x, y in node_centers:
    plt.text(x,
             y,
            "NodeX",
            fontsize=12,
            color="black",
            horizontalalignment="center",
            verticalalignment="center")


plt.axis("off")

plt.axis("tight")

plt.axis("equal")

plt.show()

