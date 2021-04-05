def get_image_size_descriptor(full_image_name: str):
    part_after_dog = full_image_name.split("@")[1]
    return part_after_dog.replace(".png", "")


def get_target_image_name(source_file_name: str):
    return source_file_name.split("@")[0]
