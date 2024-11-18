import os
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

app = QApplication([])
win = QWidget()
win.resize(700, 500)
lb_image = QLabel('редактор фото про ульра хз что')
btn_dir = QPushButton('Папка')
lw_files = QListWidget()

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_flip = QPushButton('Зеркало')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')

row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col2.addWidget(lw_files)
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)


win.show()


workdir = ''
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamelist():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkDir()
    filename = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filename:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamelist())
app.exec()