import site, os
def add_to_path():
    this_dir = os.path.dirname(__file__)
    up_one = os.path.dirname(this_dir)
    src_dir = os.path.join(up_one, 'src')
    pkg_dir = os.path.join(src_dir, 'python')
    site.addsitedir(pkg_dir)
