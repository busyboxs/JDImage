import os
import sys
import argparse

# use example:
#       1. check one dir : python valid_name_1.py 1 part6_good
#       2. check multi dir. first, you should keep file format like this:
#               |root_dir:
#               |    sub_dir1:
#               |        ****.jpg(png)
#               |    sub_dir2:
#               |        ****.jpg(png)
#               |    ......
#          then run comment: python valid_name_1.py 1 root_dir


def parse_args():
    """
    Parse input arguments,
    """
    parser = argparse.ArgumentParser(description='Valid images')
    parser.add_argument('check_name_length',
                        help='Check true name of image?(true/false)', default=True, type=int)
    parser.add_argument('img_dir', nargs='?', help='Dir to images need to valid',
                        default='data/valid_test', type=str)

    # if len(sys.argv) == 1:
    #     parser.print_help()
    #     sys.exit(1)

    args = parser.parse_args()
    return args


def get_index_from_name(name):
    """img_name format: index_flag_name.suffix, (eg.36802_0_595f3690N4474ba36.jpg)"""
    return name.split('_')[0]


def get_true_name_of_image(img_name):
    """img_name format: index_flag_name.suffix, (eg.36802_0_595f3690N4474ba36.jpg)"""
    return img_name.split('_')[-1].split('.')[0]


def list_minus(list1, list2):
    return [ele for ele in list1 if ele not in list2]


def valid_index(list_raws, list_trans):
    """Valid whether the names of images meet demand:
            1. whether images are pairs, eg. '36797_0_5b1f78cdNf2230d84.jpg' and
               '36797_1_5b3b0b97N6c328efe.png' in same file
            2. whether image true_name meet demand, length of true name is 17. (effect? don't know?)
    """
    not_pair_raws = []
    not_pair_trans = []
    min_length = min(len(list_raws), len(list_trans))  # get min length of two lists to avoid out of range
    j = 0  # list index of raw_list
    k = 0  # list index of transparent list
    for i in range(min_length):
        index_o = get_index_from_name(list_raws[j])
        index_t = get_index_from_name(list_trans[k])
        if index_o < index_t:
            print('{} is not in pairs with others'.format(list_raws[j]))
            not_pair_raws.append(list_raws[j])
            j += 1
            continue
        elif index_o > index_t:
            print('{} is not in pairs with others'.format(list_trans[k]))
            not_pair_trans.append(list_trans[k])
            k += 1
            continue
        j += 1
        k += 1
        # print(index_o, index_t)
        assert index_o == index_t, 'Index are not same.'
    return list_minus(list_raws, not_pair_raws), list_minus(list_trans, not_pair_trans)


def get_sub_dir_list(root_dir):
    sub_dir = []
    for _, dirs, _ in os.walk(root_dir):
        sub_dir.extend(dirs)
        break
    return sub_dir


def get_sub_file_list(root_dir):
    sub_files = []
    for _, _, files in os.walk(root_dir):
        sub_files.extend(files)
        break
    return sub_files


if __name__ == '__main__':
    # for i in range(6, 21):
    args = parse_args()
    imgs_dir = args.img_dir
    check_name_length = args.check_name_length
    sub_dirs = [os.path.join(imgs_dir, path) for path in get_sub_dir_list(imgs_dir)]
    print(sub_dirs)
    if not sub_dirs:
        sub_dirs.append(imgs_dir)
    print(sub_dirs)
    for path in sub_dirs:
        print('Check file dir: {}'.format(path))
        imgs = get_sub_file_list(path)
        raw = [img for img in imgs if img.split('_')[1] == '0']  # get all raw image names
        trans = [img for img in imgs if img.split('_')[1] == '1']  # get all transparent image names
        # raw = sorted(raw)
        # trans = sorted(raw)

        new_raw, new_trans = valid_index(raw, trans)  # valid whether the indices are same

        if check_name_length:
            for raw_, trans_ in zip(new_raw, new_trans):
                if len(get_true_name_of_image(raw_)) != 17 or len(get_true_name_of_image(trans_)) != 17:
                    print(raw_)
                    print(trans_)

        print('done!')
