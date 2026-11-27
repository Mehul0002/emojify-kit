# emojify-kit

Write **:name:** in your text and it will be replaced with an emoji.
For example, `:earth:` becomes 🌍.

---

## 1. Install

Open your terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
pip install git+https://github.com/Mehul0002/emojify-kit.git
```

---

## 2. Use it in your code

Add this line at the top of your Python file:

```python
from emojify_kit import emojify
```

Then pass your text to `emojify()` wherever you want emojis:

```python
from emojify_kit import emojify

print(emojify("Look at the earth :earth:"))
```

Output:
```
Look at the earth 🌍
```

---

## 3. What each syntax does

| You write | Output |
|---|---|
| `:earth:` | 🌍 |
| `:laugh:` | 😂 |
| `happy` (plain word) | `happy 😀` |

More examples:

```python
from emojify_kit import emojify

print(emojify("That was so funny :laugh:"))
# That was so funny 😂

print(emojify("I am happy today"))
# I am happy 😀 today
```

---

## 4. Add your own emoji (optional)

```python
from emojify_kit import add_emoji, emojify

add_emoji("python", "🐍")
print(emojify("I love :python:"))
# I love 🐍
```

---

## 5. Run from the terminal

```bash
python -m emojify_kit "Look at the earth :earth:"
```

Output:
```
Look at the earth 🌍
```

---

## Common problems

**The emoji is not shown, and `:earth:` appears as plain text**
That name is not in the emoji list. Open `emojify_kit/core.py`, find `EMOJI_MAP`, and add the name there.

**On Windows, emojis show as squares (□) or question marks (?)**
Run this command in the terminal, then run your program again:
```bash
chcp 65001
```

**The `pip` command is not found**
Try `pip3` instead, and check that Python is installed correctly.

---

## Quick steps for any new project

1. Run `pip install git+https://github.com/Mehul0002/emojify-kit.git` in the terminal.
2. Add `from emojify_kit import emojify` to your Python file.
3. Write `:name:` in your text and pass it to `emojify("...")`.
4. Run your file with `python your_file.py`.
