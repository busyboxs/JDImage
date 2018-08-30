from util import *

root_dir = 'D:/7-31/'
origin_dir = root_dir + 'origin'
trans_dir = root_dir + 'transparent'

origin_list = get_name_list(origin_dir)
trans_list = get_name_list(trans_dir)

valid_index(origin_list, trans_list)
