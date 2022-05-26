# display-string-clue2.py
from adafruit_clue import clue

text = 'Python'

display = clue.simple_text_display(text)
display.show()
