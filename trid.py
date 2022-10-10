import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, required=True,
                    help='输入文件路径')
args  = parser.parse_args()


base_dir = os.path.dirname(os.path.abspath(__file__))
file_dir = os.path.abspath(args.f)
file_name = file_dir.split("\\")[-1]

# 1.复制文件到trid文件夹下
shutil.copy(file_dir, base_dir)
 
# 2.开始
os.chdir(base_dir)
os.system(f"trid.exe {file_name}")
os.remove(file_name)
os.system("pause")