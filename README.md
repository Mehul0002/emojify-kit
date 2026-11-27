# emojify-kit

Apne text mein **:naam:** likho, to uski jagah emoji aa jayega.
Jaise `:earth:` likhoge to 🌍 aayega.

---

## 1. Install kaise karein

Terminal (Command Prompt / PowerShell / Terminal) kholo aur ye command chalao:

```bash
pip install git+https://github.com/YOUR_USERNAME/emojify-kit.git
```

> `YOUR_USERNAME` ki jagah apna GitHub username likho.

---

## 2. Code mein kaise use karein

Apni Python file mein sabse upar ye line likho:

```python
from emojify_kit import emojify
```

Phir jahan bhi text mein emoji chahiye, wahan `emojify()` ke andar text do:

```python
from emojify_kit import emojify

print(emojify("Aaj mai :earth: dekh raha hoon"))
```

Output:
```
Aaj mai 🌍 dekh raha hoon
```

---

## 3. Kaun sa syntax kya karta hai

| Aap likhoge | Output |
|---|---|
| `:earth:` | 🌍 |
| `:hasi:` | 😂 |
| `happy` (plain word) | `happy 😀` |

Ek aur example:

```python
from emojify_kit import emojify

print(emojify("Aaj mai :hasi: kar raha hoon"))
# Aaj mai 😂 kar raha hoon

print(emojify("I am happy today"))
# I am happy 😀 today
```

---

## 4. Apna khud ka emoji add karna (optional)

```python
from emojify_kit import add_emoji, emojify

add_emoji("python", "🐍")
print(emojify("I love :python:"))
# I love 🐍
```

---

## 5. Terminal se seedha chalana

```bash
python -m emojify_kit "Aaj mai :earth: dekh raha hoon"
```

Output:
```
Aaj mai 🌍 dekh raha hoon
```

---

## Common problems

**Emoji ki jagah `:earth:` hi dikh raha hai**
Us naam ka emoji list mein nahi hai. `emojify_kit/core.py` kholo aur `EMOJI_MAP` mein wo naam add karo.

**Windows par emoji square box (□) ya `?` dikh raha hai**
Terminal mein ye command chalao, phir dobara run karo:
```bash
chcp 65001
```

**`pip` command nahi mil rahi**
`pip3` try karo, ya Python sahi se install hai ya nahi check karo.

---

## Kisi bhi naye project mein use karne ke steps (short mein)

1. Terminal mein `pip install git+https://github.com/YOUR_USERNAME/emojify-kit.git` chalao.
2. Apni Python file mein `from emojify_kit import emojify` likho.
3. Text ke andar `:naam:` likho aur `emojify("...")` mein pass karo.
4. File run karo: `python apni_file.py`
