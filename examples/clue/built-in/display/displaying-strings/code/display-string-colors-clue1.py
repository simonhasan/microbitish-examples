from adafruit_clue import clue

text = 'Python'

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

colors = (red, orange, yellow, green, blue, purple)

display = clue.simple_text_display(title=text, colors=colors)
display[0].text = text
display[1].text = text
display[2].text = text
display[3].text = text
display[4].text = text
display[5].text = text
display.show()

