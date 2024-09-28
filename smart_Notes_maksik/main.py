from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()
window.setWindowTitle("Smart Notes")
window.resize(800,600)
window.move(0,0)
window.setStyleSheet("background-color : rgb(235.231,255); font-size: 15px")

text_editor = QTextEdit()
text_editor.setPlaceholderText("Введіть текс замтки.<3")

list_widget_1 = QListWidget() 
list_widget_2 = QListWidget() 

text_searcher = QLineEdit()
text_searcher.setPlaceholderText("Введи текс ...")

tag_searcher = QLineEdit()
tag_searcher.setPlaceholderText("Введи тег ...")


make_note = QPushButton()
make_note.setText("Створи заміку")

delete_note = QPushButton()
delete_note.setText("Видалити заміку")

save_note = QPushButton()
save_note.setText("Зберегти замітку")

searcher_fore_text = QPushButton()
searcher_fore_text.setText("Шукати за текстом")

searcher_fore_tag = QPushButton()
searcher_fore_tag.setText("Шукати за тегом")

add_to_note = QPushButton()
add_to_note.setText("Додати тег до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setText("Відкріпити тег від замтки")

convert_to_txt = QPushButton()
convert_to_txt.setText("Конвертувати до txt формату")

action_theme_btn = QPushButton()
action_theme_btn.setText("Змінити тему")

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(make_note)
row2.addWidget(delete_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)


col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)

col2.addWidget(QLabel("Список тегів:"))
col2.addWidget(list_widget_2)
col2.addWidget(QLabel("Пошук данних:"))
col2.addWidget(tag_searcher)
col2.addWidget(text_searcher)
col2.addLayout(row2)

col2.addWidget(searcher_fore_tag)
col2.addWidget(searcher_fore_text)
col2.addWidget(convert_to_txt)
col2.addWidget(action_theme_btn)

layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

window.setLayout(layout_note)

window.show()
app.exec_()