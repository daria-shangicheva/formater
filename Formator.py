import os
import shutil
import sys

file_resource = sys.argv[1]
file_final = sys.argv[2]
image_to_replace_name = sys.argv[3]

size_to_fold_dict = {
    '1x': 'drawable-mdpi',
    '1.5x': 'drawable-hdpi',
    '2x': 'drawable-xhdpi',
    '3x': 'drawable-xxhdpi',
    '4x': 'drawable-xxxhdpi'
}

if image_to_replace_name is not None:

    for el in size_to_fold_dict:
        if not os.access(file_final + size_to_fold_dict.get(el), os.F_OK):
            os.mkdir(file_final + size_to_fold_dict.get(el))

    images_names = os.listdir(path=file_resource)

    for el in size_to_fold_dict:
        if not os.access(file_final + size_to_fold_dict.get(el), os.F_OK):
            os.mkdir(file_final + size_to_fold_dict.get(el))

    for el in size_to_fold_dict:
        os.remove(file_final + size_to_fold_dict[el] + "\\" + image_to_replace_name + ".png")

    for el in images_names:
        if el != image_to_replace_name:
            new_rep = size_to_fold_dict.get(el.split("@")[1][:-4])
            copy_path = file_final + new_rep + '\\' + image_to_replace_name + ".png"
            shutil.copy(file_resource + el, copy_path)
            print(copy_path)

    else:
        for el in size_to_fold_dict:
            if not os.access(file_final + size_to_fold_dict.get(el), os.F_OK):
                os.mkdir(file_final + size_to_fold_dict.get(el))

        images_names = os.listdir(path=file_resource)

        for el in images_names:
            new_name = el.split("@")[0]
            if el != new_name:
                new_rep = size_to_fold_dict.get(el.split("@")[1][:-4])
                copy_path = file_final + new_rep + '/' + new_name + ".png"
                shutil.copy(file_resource + el, copy_path)
                print(copy_path)
