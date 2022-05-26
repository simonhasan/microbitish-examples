# 0.0.0: Displaying a String

## 0.0.0.1: Adafruit CLUE TODO

---

ENTER INTRO

---

### <a name="disp-str-clue"></a>Display a String

The simplest way to display a string using an Adafruit CLUE is to use the `print()` function. The OLED display mirrors the REPL.

> #### `print(string)`

```python
from adafruit_clue import clue

text = 'Python'

print(text)
```

<img src="C:\Users\sjema\OneDrive\Documents\GitHub\microbitish-examples\examples\00-built-in\0.00-display\images\display-string-clue1.jpg" alt="display-string-clue1" style="zoom:18%;" />

```
Adafruit CircuitPython x.x.x on YYYY-
MM-DD; Clue n
code.py output:
Python

Code done running.
```



> #### [`simple_text_display(title=None, title_color=(255, 255, 255), title_scale=1, text_scale=1, font=None, colors=None)`](https://docs.circuitpython.org/projects/clue/en/latest/api.html#adafruit_clue.Clue.simple_text_display)

```python
from adafruit_clue import clue

text = 'Python'

clue.simple_text_display(text).show()
```

<img src="C:\Users\sjema\OneDrive\Documents\GitHub\microbitish-examples\examples\00-built-in\0.00-display\images\display-string-clue2.jpg" alt="display-string-clue2" style="zoom:18%;" />

```python

```

