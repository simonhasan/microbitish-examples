# Displaying Strings (BBC micro:bit)

The BBC micro:bit display is a 5×5 matrix of red LEDs. Strings are displayed by either scrolling the characters of the string from right to left or displaying each character individually. In order to display strings the `microbit` module must be imported.

---

###  Displaying Strings (Simplest)

---

> ### `display.scroll(string)`
>
> Display a string scrolling from right to left.

```python
# display-string-microbit1.py
from microbit import *

text = 'Python'

display.scroll(text)
```

![display-string-microbit1](images/display-string-microbit1.gif)

---

> ### `display.show(string)`
>
> Display a string by displaying one character at a time.

```python
# display-string-microbit2.py
from microbit import *

text = 'Python'

display.show(text)
```

![display-string-microbit1](images/display-string-microbit2.gif)

> **NOTE**: The `display.show()` method does not clear the screen by default, leaving the final character on the display.

---

### Displaying Strings (Additional Methods)

---

#### Displaying a String with a Delay 

> ### `display.scroll(string, delay=ms)`
>
> Display a string scrolling from right to left with a delay in milliseconds between each increments. The default is `delay=400`.

```python
# display-string-delay-microbit1.py
from microbit import *

text = 'Python'

display.scroll(text, delay=100)
```

![display-string-delay-microbit1](images/display-string-delay-microbit1.gif)

---

> ### `display.show(string, delay=ms)`
>
> Display a string by displaying one character at a time with a delay in milliseconds between characters. The default is `delay=400`.

```python
# display-string-delay-microbit2.py
from microbit import *

text = 'Python'

display.show(text, delay=100)
```

![display-string-delay-microbit2](images/display-string-delay-microbit2.gif)

---

#### Displaying a String with a Loop

> ### `display.scroll(string, loop=bool)`
>
> Display a string scrolling from right to left with a loop. The default is `loop=False`.

```python
# display-string-loop-microbit1.py
from microbit import *

text = 'Python'

display.scroll(text, loop=True)
```

![display-string-loop-microbit1](images/display-string-loop-microbit1.gif)

---

> ### `display.show(string, loop=bool)`
>
> Display a string by displaying one character in a loop. The default is `loop=False`.

```python
# display-string-loop-microbit1.py
from microbit import *

text = 'Python'

display.scroll(text, loop=True)
```

![display-string-loop-microbit2](images/display-string-loop-microbit2.gif)

---

#### Clearing the Display

> ### `display.scroll(string, clear=bool)`
>
> This is in the API, but does not work as it raises a `TypeError`.

```python
# This will return a TypeError
from microbit import *

text = 'Python'

display.show(text, clear=True)
```

**OUTPUT:**

```
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: extra keyword arguments given
```

---

> ### `display.show(string, clear=bool)`
>
> Display a string by displaying one character clearing the display upon completion. The default is `clear=False`.

```python
# display-string-clear-microbit.py
from microbit import *

text = 'Python'

display.show(text, clear=True)
```

![display-string-clear-microbit](images/display-string-clear-microbit.gif)

