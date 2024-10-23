import os
from fastapi import UploadFile


def check_image_size(image: UploadFile, kb_size_limit: int):
    image.file.seek(0, 2)  
    file_size_kbytes = image.file.tell()/1024 
    image.file.seek(0)
    return file_size_kbytes <= kb_size_limit


def get_image_filepath(image_name: str, image_type: str):
    print(os.path.dirname(__file__))
    file_path_jpeg = os.path.dirname(__file__) + "/../../images/" + image_type + "/" + image_name + ".jpeg"
    file_path_png = os.path.dirname(__file__) + "/../../images/" + image_type + "/" + image_name + ".png"
    file_path_default = os.path.dirname(__file__) + "/../../images/" + image_type + "/default.jpg"
    if os.path.exists(file_path_jpeg):
        return file_path_jpeg
    if os.path.exists(file_path_png):
        return file_path_png
    
    return file_path_default


def save_image(image: UploadFile, image_name: str, image_type: str):
    file_path = os.path.dirname(__file__) + "/../../images/" + image_type + "/" + image_name + "." + image.content_type.split("/")[-1]
    with open(file_path, 'wb') as f:
        f.write(image.file.read())