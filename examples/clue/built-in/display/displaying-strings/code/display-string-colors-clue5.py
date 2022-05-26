from adafruit_clue import clue

text = 'Python'

clue_display = clue.simple_text_display(title=text)
clue_display[0].text = text
clue_display[0].color = clue.RED
clue_display[1].text = text
clue_display[1].color = clue.GREEN
clue_display[2].text = text
clue_display[2].color = clue.BLUE
clue_display.show()




