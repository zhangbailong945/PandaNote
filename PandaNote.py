import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from Ui_NoteMain import Ui_NoteMain
from PandaNoteEmoji import Panda_Note_Emoji
class Do_NoteMain(QWidget, Ui_NoteMain):
    
    def __init__(self, parent=None):
        super(Do_NoteMain, self).__init__(parent)
        self.setupUi(self)
        self.noteText.setPlainText("2018年6月2日,多云，室内凉爽，睡到自然醒，美滋滋。但是拨开窗帘一看，外面热得不行。顿时打消出去游玩的念头，还是继续宅吧。冲杯咖啡，打开群。看看有没有老司机看车。发现没一个人开车。emmmm,这个仇今天记下了！")
        self.saveBtn.clicked.connect(self.saveImage)
    
    #生成按钮槽函数
    def saveImage(self):
        note_Content=self.noteText.toPlainText()
        if(len(note_Content)>10):
            emoji=Panda_Note_Emoji()
            files=QFileDialog.getSaveFileName(self, 'save file', 'c:\\', "Image files (*.png)")
            savePath=files[0]
            if(savePath):
                emoji.get_note_img(note_Content)
                emoji.panda_note_img.save(savePath, 'png')
            else:
                QMessageBox.warning(self, "警告：", "请选择图片保存目录和图片名称!", QMessageBox.Yes, QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告：", "必须输入10个以上日记内容！", QMessageBox.Yes, QMessageBox.Yes)

if __name__=="__main__":
    app=QApplication(sys.argv)
    note_win=Do_NoteMain()
    note_win.show()
    sys.exit(app.exec_())
