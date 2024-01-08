from PyQt5.QtWidgets import QDialog
from Window.UI.Ui_AboutWindow import Ui_AboutWindow

ABOUT_INFO = """软件名称：PETool
软件版本：1.0.0.0
软件作者：Rev Li

识别类型：32位PE文件;64位PE文件;超小畸形PE文件.

查看功能：文件基本信息;文件结构解析;
          DOS头;文件头;可选头;目录表;区段表;
          导入表;调试信息表;绑定导入表等.

计算功能：[时间戳/日历时间]转换;[VA/RVA/RAW]转换.

作者留言：该工具永久免费,无需注册,绿色无广告插件.

发现BUG欢迎来信：xxxx@163.com.

查看更新：
https://github.com/rev-li/PETool
"""

class AboutWindow(QDialog, Ui_AboutWindow):
    def __init__(self, app):
        super(AboutWindow, self).__init__(app.mainWindow)
        self.app = app
        self.setupUi(self)
        self.textBrowser.setText(ABOUT_INFO)
        self.setModal(True)