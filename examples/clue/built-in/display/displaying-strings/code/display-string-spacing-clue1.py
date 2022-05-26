# display-string-spacing-clue1.py
from adafruit_clue import clue

text = 'Python'

clue_display = clue.simple_text_display(title=text)
clue_display[1].text = text
clue_display[2].text = text
clue_display[4].text = text
clue_display[8].text = text
clue_display[16].text = text
clue_display.show()




