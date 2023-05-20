MZ = b'MZ'
E_LFANEW = b'\x00\x00\x00\x00'


def ByteToHex(bytes):
    return hex(int.from_bytes(bytes, "little"))[2:]


def LitToBig(bytes):
    ans = ""
    for i in reversed(bytes):
        if i < 10:
            ans += '0'
        ans += hex(i)[2:4]
    return ans.upper()


def Machine_CODE(NT_File_Machine):
    switcher = {
        b'0': "Unknown Machine",
        b'\x4c\x01': "Intel 386(Intel x86)",
        b'\x62\x01': "MIPS little-endian",
        b'\x60\x01': "MIPS big-endian",
        b'\x66\x01': "MIPS little-endian",
        b'\x68\x01': "MIPS little-endian",
        b'\x69\x01': "MIPS little-endian WCE v2",
        b'\x84\x01': 'Alpha_AXP',
        b'\xf0\x01': "IBM PowerPC Little-Endian",
        b'\xa2\x01': "SH3 little-Endian",
        b'\xa4\x01': "SH3E little-Endian",
        b'\xa6\x01': "SH4 little-Endian",
        b'\xc0\x01': "ARM little-Endian",
        b'\xc2\x01': "THUMB",
        b'\x00\x02': "Intel 64",
        b'\x66\x02': "MIPS",
        b'\x66\x03': "MIPS",
        b'\x66\x04': "MIPS",
        b'\x84\x02': "ALPHA64",
    }
    return switcher.get(NT_File_Machine, "Nothing")


dict_Characteristics = [b"\x01\x00", b"\x02\x00", b"\x04\x00", b"\x08\x00", b"\x10\x00", b"\x20\x00", b"\x80\x00",
                        b"\x00\x01",
                        b"\x00\x02", b"\x00\x04", b"\x00\x08", b"\x00\x10", b"\x00\x20", b"\x00\x40", b"\x00\x80"]


def Characteristics(Character):
    switcher = {
        b"\x01\x00": "重定位信息被移除",
        b"\x02\x00": "是可执行文件",  # .exe
        b"\x04\x00": "行号被移除",
        b"\x08\x00": "定位符号被移除",
        b"\x10\x00": "主动调整工作台",
        b"\x20\x00": "高地址警告",
        b"\x80\x00": "处理机的低位字节是相反的",
        b"\x00\x01": "32位机器",
        b"\x00\x02": ".DBG的调试信息被移除",
        b"\x00\x04": "如果映像文件在可移动媒体中，则先复制到交换文件后再运行",
        b"\x00\x08": "如果映像文件在网络中，则复制到交换文件后才运行",
        b"\x00\x10": "是系统文件",
        b"\x00\x20": "是DLL文件",
        b"\x00\x40": "文件只能运行在单处理器上",
        b"\x00\x80": "处理机的高位字节是相反的",
    }
    return switcher.get(Character, "")


def ReadFile():
    with open(".\\HelloWorld.exe", mode="rb") as file:
        if file == None:
            print("源文件打开出错啦！！")
        else:
            # print("开始读取PE文件的二进制格式内容...")
            content = file.read()
            # print(content)
            # print("二进制格式内容读取完毕，正在关闭文件...")
            file.close()
            # print("关闭成功^_^")
    return content


def IsDos(cont):
    e_magic = cont[:2]
    # print("e_magic = ", e_magic)
    # print("是否DOS文件 :", end=" ")
    if e_magic != MZ:
        # print("e_magic = ", e_magic)
        # print("否")
        exit(-1)
    else:
        # print("是")
        pass


# def GetPeFileStart():
#     e_lfanew = cont[60:64]
#     if e_lfanew == E_LFANEW:
#         exit(-1)
#     else:
#         print("PE文件开始地址 :", ByteToHex(e_lfanew).upper())
#         return e_lfanew


def Character(character_offset, content):
    print("文件属性  : ")
    character = content[character_offset:character_offset + 2]
    # character先变为int数值
    character = int.from_bytes(character, "little")
    for c in dict_Characteristics:
        # c先变为int数值
        c = int.from_bytes(c, "little")
        tmp = character & c
        # print("char : ",character.to_bytes(2,"little"))
        # print("tmp : ",tmp.to_bytes(2,"little"))
        # print("c :", c.to_bytes(2,"little"))
        if tmp == c:
            # 在这里传入时转为临时的bytes类型
            print("           ", Characteristics(tmp.to_bytes(2, "little")))
            character = character ^ c
        else:
            continue


def IsPE(Offset, Signature):
    print("是否PE文件  : ", end=" ")
    if Signature == b'PE\x00\x00':
        print("是")
    else:
        print("否")


def Read_IMAGE_NT_HEADERS(e_lfanew, content):
    NT_offset = int.from_bytes(e_lfanew, "little")
    # PE
    IsPE(NT_offset, content)
    # FileHeader NT头：文件头
    print("----------------------- IMAGE_NT_HEADERS -------------------------")
    Machine_offset = NT_offset + 4
    machine = content[Machine_offset:Machine_offset + 2]
    print("运行平台  :", Machine_CODE(machine))
    NumOfSections_offset = NT_offset + 6
    NumOfSections = int.from_bytes(content[NumOfSections_offset:NumOfSections_offset + 2], "little")
    # print("NumOfSections_offset = ", NumOfSections_offset)
    print("节区数量  : ", NumOfSections)
    # SOOH:SizeOfOptionalHeader
    print("可选头长度: ", end=" ")
    SOOH_offset = NT_offset + 20
    SOOH = int.from_bytes(content[SOOH_offset:SOOH_offset + 2], "little")
    # print("SizeOfOptionalHeader = ", SOOH)
    print(SOOH)
    # Characteristics
    Character(NT_offset + 22, content)
    # Image_Optional_Header
    # print("---------------------IMAGE_OPTIONAL_HEADER------------------------")
    # IMAGE_OPTIONAL_HEADER_Offset: IOH_offset
    IOH_offset = NT_offset + 24
    Read_Image_Optional_Header(IOH_offset, content)


class Image_Dos_Header:
    def __init__(self, content):
        # print("----------------Image_Dos_Header------------------")
        self.e_magic = LitToBig(content[0:2])
        self.e_cblp = LitToBig(content[2:4])
        self.e_cp = LitToBig(content[4:6])
        self.e_crlc = LitToBig(content[6:8])
        self.e_cparhdr = LitToBig(content[8:10])
        self.e_minalloc = LitToBig(content[10:12])
        self.e_ss = LitToBig(content[12:14])
        self.e_sp = LitToBig(content[14:16])
        self.e_csum = LitToBig(content[16:18])
        self.e_ip = LitToBig(content[20:22])
        self.e_cs = LitToBig(content[22:24])
        self.e_lfarlc = LitToBig(content[24:26])
        self.e_res = LitToBig(content[26:34])
        self.e_oemid = LitToBig(content[34:36])
        self.e_oeminfo = LitToBig(content[38:40])
        self.e_res2 = LitToBig(content[40:60])
        self.e_lfanew = LitToBig(content[60:64])

    def GetNToffset(self, content):
        e_lfanew = content[60:64]
        return int.from_bytes(e_lfanew, "little")


class IMAGE_FILE_HEADER:
    def __init__(self, e_lfanew, content):
        self.Signature = LitToBig(content[e_lfanew: e_lfanew + 4])
        self.Machine = LitToBig(content[e_lfanew + 4: e_lfanew + 6])
        self.NumberOfSections = LitToBig(content[e_lfanew + 6: e_lfanew + 8])
        self.TimeDateStamp = LitToBig(content[e_lfanew + 8: e_lfanew + 12])
        self.PointerToSymbolTable = LitToBig(content[e_lfanew + 12: e_lfanew + 16])
        self.NumberOfSymbols = LitToBig(content[e_lfanew + 16: e_lfanew + 20])
        self.SizeOfOptionalHeader = LitToBig(content[e_lfanew + 20: e_lfanew + 22])
        self.Characteristics = LitToBig(content[e_lfanew + 22: e_lfanew + 24])


def Read_Image_Optional_Header(IOHbase, content):
    magic = content[IOHbase:IOHbase + 2]
    # print("magic:", magic)
    if magic == b'\x0b\x01':
        print("---------------------IMAGE_OPTIONAL_HEADER32----------------------")
    elif magic == b'\x0b\x02':
        print("---------------------IMAGE_OPTIONAL_HEADER64----------------------")
    # AddressOfEntryPoint
    AddrOfEntryPoint = content[IOHbase + 16: IOHbase + 20]
    print("程序入口点地址(EP) :   ", ByteToHex(AddrOfEntryPoint).upper())
    # Image_Base
    Image_Base = content[IOHbase + 28: IOHbase + 32]
    print("Image_Base :        ", ByteToHex(Image_Base))
    # SectionalAlignment
    SectionalAlignment = content[IOHbase + 32: IOHbase + 36]
    print("SectionalAlignment :", ByteToHex(SectionalAlignment))
    # FileAlignment
    FileAlignment = content[IOHbase + 36: IOHbase + 40]
    print("FileAlignment :     ", ByteToHex(FileAlignment))
    # SizeOfImage
    SizeOfImage = content[IOHbase + 56: IOHbase + 60]
    print("SizeOfImage :       ", ByteToHex(SizeOfImage).upper())
    # SizeOfHeader
    SizeOfHeader = content[IOHbase + 60: IOHbase + 64]
    print("SizeOfHeader :      ", ByteToHex(SizeOfHeader))

    # Subsystem
    print("Subsystem :         ", end=" ")
    Subsystem = content[IOHbase + 68: IOHbase + 70]
    Subsystem = int.from_bytes(Subsystem, "little")
    if Subsystem == 1:
        print("系统驱动文件")
    elif Subsystem == 2:
        print("窗口应用程序")
    elif Subsystem == 3:
        print("控制台应用程序")

    # NumberOfRvaAndSizes
    NumberOfRvaAndSizes = content[IOHbase + 92: IOHbase + 96]
    print("NumberOfRvaAndSizes:", ByteToHex(NumberOfRvaAndSizes).upper())

    # DataDirectory
    # TODO
    # DataDirectory = content[IOHbase + 96 : IOHbase + 160]
    # print("DataDirectory :", hex(int.from_bytes(DataDirectory, "little")))
    # VirtualAddress = DataDirectory[:4]
    # Size = DataDirectory[4:8]
    # print("VirtualAddress :", hex(int.from_bytes(VirtualAddress, "little")))
    # print("Size :", hex(int.from_bytes(Size, "little")))


def GetCreateTime():
    pass


def GetAccessTime():
    pass


def GetModiTime():
    pass
