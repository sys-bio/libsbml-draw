    def __computeFigureSize(self, box_padding_multiplier=1.15):
        """Computes the estimated figure size in inches required so that the
        node boxes are large enough to contain the node name.

        Args:
            box_padding_multiplier (float): makes the box 5% wider than the
            text length

        Returns: tuple(float, float)
        """

        length_longest_node_name = 0
        node_with_longest_name = None
        for node in self.__network.nodes.values():
            if len(node.name) > length_longest_node_name:
                length_longest_node_name = len(node.name)
                node_with_longest_name = node

        length_of_one_font_point_inches = 1/72
        length_of_node_name_inches = (length_longest_node_name *
                                      node_with_longest_name.font_size *
                                      length_of_one_font_point_inches)

        max_x_in_network = max([n.center.x
                               for n in self.__network.nodes.values()])

        min_x_in_network = min([n.center.x
                               for n in self.__network.nodes.values()])

        figure_width_data_units = max_x_in_network - min_x_in_network

        fig_width_inches = (length_of_node_name_inches*box_padding_multiplier *
                            figure_width_data_units /
                            node_with_longest_name.width)

#        default_matplotlib_h_w_ratio = 4.8/6.4  # inches

        fig_height_inches = fig_width_inches

#        fig_height_inches = max(fig_width_inches/
#                                node_with_longest_name.font_size,
#                                default_matplotlib_h_w_ratio*fig_width_inches)

        # print("max x", max_x_in_network, "min x", min_x_in_network)
        # print("fig width", figure_width_data_units)
        # print("fig width inches", fig_width_inches)
        # print("fig height inches", fig_height_inches)

        return (fig_width_inches, fig_height_inches)
