from adafruit_clue import clue

text = 'Python'

colors = (clue.RED,
          clue.ORANGE,
          clue.YELLOW,
          clue.GREEN,
          clue.BLUE,
          clue.PURPLE)

clue_display = clue.simple_text_display(title=text, colors=colors)
clue_display[0].text = text
clue_display[1].text = text
clue_display[2].text = text
clue_display[3].text = text
clue_display[4].text = text
clue_display[5].text = text
clue_display.show()


