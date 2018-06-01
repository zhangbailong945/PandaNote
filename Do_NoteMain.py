import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog
from Ui_NoteMain import Ui_NoteMain
from PandaNote import Panda_Note_Emoji
class Do_NoteMain(QWidget, Ui_NoteMain):
    
    def __init__(self, parent=None):
        super(Do_NoteMain, self).__init__(parent)
        self.setupUi(self)
        self.saveBtn.clicked.connect(self.saveImage)
    
    def saveImage(self):
        note_Content=self.noteText.toPlainText()
        if(len(note_Content)>10):
            emoji=Panda_Note_Emoji()
            files=QFileDialog.getSaveFileName(self, 'save file', 'c:\\', "Image files (*.png)")
            savePath=files[0]
            emoji.get_note_img(note_Content)
            print(savePath)
            emoji.panda_note_img.save(savePath, 'png')
        else:
            QMessageBox.warning(self, "警告：", "必须输入10个以上日记内容！", QMessageBox.Yes, QMessageBox.Yes)

if __name__=="__main__":
    app=QApplication(sys.argv)
    note_win=Do_NoteMain()
    note_win.show()
    sys.exit(app.exec_())
