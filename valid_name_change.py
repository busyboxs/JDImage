import os
import glob

root_dir = 'D:/7-30/change_name'
pair_dir = os.path.join(root_dir, 'pairs')
trans_dir = os.path.join(root_dir, 'transparent')

pair_names = os.listdir(pair_dir)
trans_name_vaild = [pair_names[i] for i in range(len(pair_names)) if i % 2 == 1]
print(trans_name_vaild)
print(len(trans_name_vaild))

trans_names = os.listdir(trans_dir)
print(trans_names)
print(len(trans_names))

trans_name_txt = os.path.join(root_dir, 'transparent.txt')

i = 0
with open(trans_name_txt, 'r') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        assert trans_names[i] == line.strip(), 'name not same'
        i += 1

# for i in range(len(trans_names)):
#     if not pair_names[i] == trans_names[i]:
#         print(i)


