import os
import shutil
from typing import Dict

from utils.file_name_utils import get_image_size_descriptor


def delete_images_from_target_folder(
        target_folder_path: str,
        image_to_replace_name: str,
        size_to_fold_dict: Dict[str, str]
):
    for el in size_to_fold_dict:
        remove_file_path = target_folder_path + size_to_fold_dict[el] + "\\" + image_to_replace_name + ".png"
        if os.access(remove_file_path, os.F_OK):
            os.remove(remove_file_path)


def copy_images_to_target_folder(
        source_images_name: str,
        target_image_name: str,
        size_to_fold_dict: Dict[str, str],
        source_path: str,
        target_path: str,
):
    if source_images_name != target_image_name:
        new_rep = size_to_fold_dict.get(get_image_size_descriptor(source_images_name))
        copy_path = target_path + new_rep + '\\' + target_image_name + ".png"
        shutil.copy(source_path + source_images_name, copy_path)
        print(copy_path)
    else:
        raise Exception("You need delete image before past! Image to delete: %s", el)
