from PEAnalyze import *
from Tools.scripts.ndiff import *

if __name__ == '__main__':
    content = ReadFile()
    e_lfanew = GetPeFileStart(content)
    ISH = Image_Section_Header(e_lfanew, content)
    print(ISH.Name_str)

    # print(e_lfanew)
    # Read_IMAGE_FILE_HEADER(e_lfanew, content)
    # Read_IMAGE_NT_HEADERS(e_lfanew, content)
