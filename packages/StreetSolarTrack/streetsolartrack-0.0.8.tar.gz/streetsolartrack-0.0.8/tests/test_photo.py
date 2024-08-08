# test_photo.py
import sys
import os

# 将项目根目录添加到 sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from StreetSolarTrack.utils.photo import Photo

def main():
    # 创建 Photo 实例并读取图像
    photo = Photo('./tests/R-C.jpg')
    print(photo)
    # 显示图像
    photo.show_image()

    # 获取并打印图片大小
    print(f"Image size (width, height): {photo.get_image_size()}")
    
    # 获取并打印文件大小
    print(f"File size (bytes): {photo.get_file_size()}")

if __name__ == "__main__":
    main()
