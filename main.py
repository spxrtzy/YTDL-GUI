from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QProgressBar, QLabel
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtCore import QUrl
from PyQt6.QtCore import QRect
from PyQt6 import uic
import os
import youtube_dl 
 
class UI(QWidget):
    def __init__(self):
        super().__init__()
 
        # loading the ui file with uic module
        uic.loadUi("pls.ui", self)
        self.initUI()
 

    def initUI(self):
        print('Script Loaded')
        self.browsebtn.clicked.connect(self.browse)
        self.downloadbtn.clicked.connect(self.download)

        self.progressBar = QProgressBar(self)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(190, 420, 281, 23))
        self.progressBar.setStyleSheet(u"")

        self.currentprogressstr = ""

        self.currentprogress = QLabel()
        self.currentprogress.setText(self.currentprogressstr)
        self.currentprogress.move(210, 420)

        fullpath = 'ping.mp4'
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(fullpath))
        self.audio_output.setVolume(50)
    
    def browse(self):
        filepath = QFileDialog.getExistingDirectory(self, 'Open File', '/Users')
        self.pathinp.setText(filepath)
        self.filepathstr = self.pathinp.text()
    
    def download(self):

        #retrieve and print
        ytlink = self.linkinp.text()
        savepath = self.pathinp.text()
        customfilename = self.titleinp.text()

        if customfilename == '':
            customfilename = "%(title)s"
        else:
            customfilename = customfilename
        
        print(f"Given Link: [{ytlink}]")
        print(f"Custom file name: [{customfilename}]")
        print(f"Path To Save File [{savepath}]")

        

        #Call 'that' guy 😒

    

        ydl_opts = {
                'outtmpl':savepath + '/' + customfilename + '.%(ext)s',
                'progress_hooks': [self.my_hook],
        }
        

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytlink])

    def my_hook(self, d):
        if d['status'] == 'finished':
                file_tuple = os.path.split(os.path.abspath(d['filename']))
                print("Done downloading {}".format(file_tuple[1]))
        if d['status'] == 'downloading':
            p = d['_percent_str']
            p = p.replace('%','')
            self.progressBar.setValue(int(float(p)))
            print(d['filename'], d['_percent_str'], d['_eta_str'])
            self.currentprogressstr = int(float(p))
            QApplication.processEvents()
        self.player.play()




def CallWin():
    app = QApplication([])
    window = UI()
    window.setGeometry(200, 200, 700, 500)
    window.show()
    app.exec()

CallWin()
