from PyQt5.QtWidgets import QListWidgetItem


class StepListWidgetItem(QListWidgetItem):
    def __init__(self, text, id,image_src):
        super().__init__(text)
        self.id= id
        self.name=text
        self.image_src=image_src
