
from detect_rectangle import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "C:/Anna/CSE/semester1/ML/projects/P2/"
    input_folder = "RxT_PVVIH_Benin/"

    input_path = path + input_folder
    out_path = path + "RxT_PVVIH_Benin_rect_del1/"

    detect_rectangle(input_path, out_path)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
