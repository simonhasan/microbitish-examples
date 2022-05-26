from adafruit_clue import clue

text = 'Python'

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors = (red, green, blue,)

clue_display = clue.simple_text_display(title=text, colors=colors)
clue_display[0].text = text
clue_display[1].text = text
clue_display[2].text = text
clue_display[3].text = text
clue_display[4].text = text
clue_display[5].text = text
clue_display.show()


