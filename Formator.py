import os
import sys

from utils.file_manage_utils import delete_images_from_target_folder, copy_images_to_target_folder
from utils.file_name_utils import get_target_image_name

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

source_images_names = os.listdir(path=file_resource)

if image_to_replace_name == "-c":
    for source_image in source_images_names:
        new_name = get_target_image_name(source_image)
        copy_images_to_target_folder(
            source_images_name=source_image,
            target_image_name=new_name,
            size_to_fold_dict=size_to_fold_dict,
            source_path=file_resource,
            target_path=file_final,
        )

else:
    delete_images_from_target_folder(
        target_folder_path=file_final,
        image_to_replace_name=image_to_replace_name,
        size_to_fold_dict=size_to_fold_dict
    )

    for el in source_images_names:
        copy_images_to_target_folder(
            source_images_name=el,
            target_image_name=image_to_replace_name,
            size_to_fold_dict=size_to_fold_dict,
            source_path=file_resource,
            target_path=file_final,
        )
