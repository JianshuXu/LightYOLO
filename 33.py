import os

# 定义文件夹路径
image_folder = 'C:/Users\Darre\Desktop\yolov8FORCOCO\dataset\images/train'  # 替换为实际的图片文件夹路径
txt_folder = 'C:/Users\Darre\Desktop\yolov8FORCOCO\dataset\labels/train'      # 替换为实际的txt文件夹路径

# 获取文件夹中的文件名（不包括扩展名）
image_files = {os.path.splitext(f)[0] for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))}
txt_files = {os.path.splitext(f)[0] for f in os.listdir(txt_folder) if os.path.isfile(os.path.join(txt_folder, f))}

# 找到在图片文件夹中但不在txt文件夹中的文件名
files_to_delete = image_files - txt_files

# 删除这些文件
for file_name in files_to_delete:
    image_path = os.path.join(image_folder, file_name + '.jpg')  # 假设图片文件的扩展名为.jpg
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f'Removed {image_path}')
    else:
        print(f'File {image_path} not found.')

print('Deletion process completed.')
