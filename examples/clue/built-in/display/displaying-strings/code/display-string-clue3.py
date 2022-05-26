import board
import terminalio
from adafruit_display_text import label

text = 'Python'
text_area = label.Label(terminalio.FONT, text=text)
text_area.x = 10
text_area.y = 10
board.DISPLAY.show(text_area)