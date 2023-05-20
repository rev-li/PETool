from PEAnalyze import *
from Tools.scripts.ndiff import *

if __name__ == '__main__':
    content = ReadFile()
    ImageDosHeader = Image_Dos_Header()  # 创建用来接受dos头的对象
    e_lfanew = ImageDosHeader.GetNToffset(content)  # 获取程序开始的地址
    # print(e_lfanew)
    # Read_IMAGE_FILE_HEADER(e_lfanew, content)
    # Read_IMAGE_NT_HEADERS(e_lfanew, content)
