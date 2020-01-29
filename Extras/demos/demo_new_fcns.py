
# void gf_layout_alignToOrigin(gf_layoutInfo* l, double pad_x, double pad_y)

# This is the function we were talking about yesterday to align the 
# bounding box to the origin. You can use the x & y padding if you need to 
# to offset the lower left corner from the origin. Please let me know if 
# you have any problems with this function.


# gf_writeSBMLwithLayout and gf_getSBMLwithLayoutStr, which is just a 0 or 
# 1 integer value that controls whether the library will use the 
# previously set transformed coordinates or not (1 means to use them)
#
# 1 means that the fitToWindow coordinates will be written.
# 