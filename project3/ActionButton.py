class ActionButton:
    def __init__(self, canvas, x, y, width, height, color, b_type, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.bType = b_type
        self.icon = canvas.create_rectangle(self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2,
                                            self.y + self.height / 2, fill=color, width=5)
        self.textString = text
        self.text = canvas.create_text(self.x, self.y, text=text, width=self.width-10)

    # return if the given coordinates are within the button
    def contains(self, x, y):
        return self.x - self.width / 2 < x < self.x + self.width / 2 and \
               self.y - self.height / 2 < y < self.y + self.height / 2
