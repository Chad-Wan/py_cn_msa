import os
import subprocess
import platform
from PySide6.QtWidgets import QFileDialog, QMessageBox

# 函数功能：查找当前文件夹中，文件名包含<pattern>的文件
# 如果当前文件夹中包含目录，则返回所有的目录名字
# 输入:
#   root_path: 想要搜寻的目标文件夹
#   pattern: 文件名需要包含字符串
# 输出:
#   remained_folders: 当前文件中存在的子文件夹路径
#   final_files: 当前文件夹中，文件名中包含<pattern>的文件路径
def find_files_with_certain_patterns(root_path: str, pattern: str):
    items = os.listdir(os.path.expanduser(root_path))
    remained_folders = []
    final_files = []
    for item in items:
        current_path = os.path.expanduser(os.path.join(root_path, item))
        if os.path.isdir(current_path):
            remained_folders.append(current_path)
        elif os.path.isfile(current_path) and pattern in item:
            final_files.append(current_path)
    return remained_folders, final_files

# 函数功能：查找当前文件夹中"和子文件夹中"，文件名包含<pattern>的文件
# 输入:
#   root_path: 想要搜寻的目标文件夹
#   pattern: 文件名需要包含字符串
# 输出:
#   final_files: 当前文件夹中，文件名中包含<pattern>的文件路径
def find_all_subfiles_with_certain_patterns(root_path: str, pattern: str):
    remained_folders = []
    final_files = []
    print(root_path)
    current_path = os.path.abspath(os.path.expanduser(root_path))
    current_folders, current_files = find_files_with_certain_patterns(current_path, pattern)

    remained_folders.extend(current_folders)
    final_files.extend(current_files)

    while len(remained_folders) > 0:
        current_folders, current_files = find_files_with_certain_patterns(remained_folders.pop(), pattern)
        remained_folders.extend(current_folders)
        final_files.extend(current_files)
        # print(remained_folders)

    final_files.sort()
    return final_files

# 函数功能：查找当前文件夹中"和子文件夹中"，所有.ui文件. 并在同级目录生成对应的python类
# 输入:
#   root_path: 想要搜寻的目标文件夹
#   pattern: 文件名需要包含字符串
# 输出:
#   final_files: 当前文件夹中，文件名中包含<pattern>的文件路径
def recreate_all_ui_classes(root_path: str):
    all_ui_files = find_all_subfiles_with_certain_patterns(root_path, u".ui")
    os_name = platform.system()
    if os_name.lower() == 'windows':
        print("当前操作系统为 Windows")
    elif os_name.lower() == 'linux':
        print("当前操作系统为 Linux")
    else:
        print(f"当前操作系统为 {os_name}")

    # print(all_ui_files)
    if os_name.lower() == 'linux':
        for ui_file in all_ui_files:
            ui_path_list = ui_file.split("/")
            # print(ui_path_list)
            ui_name = ui_path_list.pop()
            ui_location = '/'.join(ui_path_list)
            command = "pyside6-uic " + ui_file + " > " + ui_location + '/' + ui_name.replace('.ui', '.py')
            # print(command)
            result = subprocess.run(command, shell=True)
            if result.returncode == 0:
                print(ui_name.replace('.ui', '.py') + " has been recreated")
            else:
                print(ui_name.replace('.ui', '.py') + " generation failed")

    elif os_name.lower() == 'windows':
        for ui_file in all_ui_files:
            ui_path_list = ui_file.split("\\")
            # print(ui_path_list)
            ui_name = ui_path_list.pop()
            ui_location = '\\'.join(ui_path_list)

            command = "pyside6-uic " + ui_file + " > " + ui_location + '/' + ui_name.replace('.ui', '.py')
            # print(command)
            result = subprocess.run(command, shell=True)
            if result.returncode == 0:
                print(ui_name.replace('.ui', '.py') + " has been recreated")
            else:
                print(ui_name.replace('.ui', '.py') + " generation failed")

def browser_to_file(file_format: str):
    file_path, filter_str = QFileDialog.getOpenFileName(
        parent=None,
        caption="请选择数据文件",
        dir=".",
        filter="{} File(*.{});;All Files (*.*)".format(file_format, file_format)
    )
    if file_path and os.path.isfile(file_path):
        return file_path
    else:
        QMessageBox.information(
            None,
            "错误",
            f"选择的目标路径非法！")
        return None


def browser_to_folder():
    folder_path = QFileDialog.getExistingDirectory(
        parent=None,
        caption="选择文件夹",
        dir=".")
    if folder_path and os.path.isdir(folder_path):
        return folder_path
    else:
        QMessageBox.information(
            None,
            "错误",
            f"选择的目标路径非法！")
        return None

def str2float(s: str):
    try:
        return float(s)
    except ValueError:
        return s

def float2str(f: float):
    return str(f)

def read_file(file_path: str):
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()
    return lines

# print(find_all_subfiles_with_certain_patterns("..", ".ui"))
# recreate_all_ui_classes("..")