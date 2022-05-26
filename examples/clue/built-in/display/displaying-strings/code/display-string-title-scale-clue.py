from adafruit_clue import clue

text = 'Python'

clue_display = clue.simple_text_display(title=text, title_scale=2)
clue_display[0].text = text
clue_display[1].text = text
clue_display[2].text = text
clue_display[3].text = text
clue_display[4].text = text
clue_display.show()
