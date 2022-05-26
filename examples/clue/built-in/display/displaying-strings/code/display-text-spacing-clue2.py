# display-string-spacing-clue2.py
from adafruit_clue import clue

text = 'Python'

clue_display = clue.simple_text_display(title=text)
clue_display[1].text = 'Red'
clue_display[1].color = clue.RED
clue_display[2].text = 'Orange'
clue_display[2].color = clue.ORANGE
clue_display[4].text = 'Yellow'
clue_display[4].color = clue.YELLOW
clue_display[8].text = 'Green'
clue_display[8].color = clue.GREEN
clue_display[16].text = 'Blue'
clue_display[16].color = clue.BLUE
clue_display.show()



