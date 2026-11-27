import re

EMOJI_MAP = {
    # English
    "happy": "😀", "smile": "😊", "love": "❤️", "heart": "❤️",
    "sad": "😢", "angry": "😡", "laugh": "😂", "funny": "🤣",
    "cool": "😎", "sleep": "😴", "tired": "😫", "surprised": "😲",
    "birthday": "🎂", "party": "🥳", "fun": "🎉", "celebrate": "🎉",
    "food": "🍔", "pizza": "🍕", "coffee": "☕", "tea": "🍵",
    "music": "🎵", "dog": "🐶", "cat": "🐱", "sun": "☀️",
    "moon": "🌙", "night": "🌃", "rain": "🌧️", "fire": "🔥",
    "star": "⭐", "good": "👍", "bad": "👎", "win": "🏆",
    "money": "💰", "code": "💻", "python": "🐍", "book": "📚",
    "car": "🚗", "travel": "✈️", "work": "💼", "thanks": "🙏",
    "hello": "👋", "hi": "👋", "bye": "👋", "fast": "⚡",
    "idea": "💡", "success": "✅",
    "world": "🌍", "earth": "🌍", "globe": "🌍",
    # Hinglish / Hindi (roman)
    "khush": "😊", "pyar": "❤️", "dukh": "😢", "gussa": "😡",
    "hasi": "😂", "chai": "☕", "khana": "🍛", "dost": "🤝",
    "shukriya": "🙏", "namaste": "🙏", "neend": "😴", "paisa": "💰",
    "mazaa": "🎉", "jaldi": "⚡",
}

_SUFFIXES = ("ness", "ing", "ed", "es", "s", "ly")

# Pehle :name: pattern check hota hai, phir normal words
_TOKEN_RE = re.compile(r":([A-Za-z_]+):|\w+", re.UNICODE)


def get_emoji(word):
    """Ek word ka emoji return karta hai, nahi mila to None."""
    if not word:
        return None
    key = str(word).lower()
    if key in EMOJI_MAP:
        return EMOJI_MAP[key]
    for suffix in _SUFFIXES:
        if key.endswith(suffix) and len(key) - len(suffix) >= 3:
            base = key[: -len(suffix)]
            if base in EMOJI_MAP:
                return EMOJI_MAP[base]
    return None


def emojify(text):
    """
    Text ko process karta hai:
    - :earth:  -> 🌍  (sirf emoji, word ki jagah)
    - world    -> world 🌍  (word ke baad emoji)
    - :xyz:    -> agar map mein nahi hai to waise hi rehta hai
    """
    if text is None:
        return ""

    def _replace(match):
        shortcode = match.group(1)
        if shortcode is not None:
            # :name: wala case
            emoji = EMOJI_MAP.get(shortcode.lower())
            return emoji if emoji else match.group(0)

        # Normal word wala case
        word = match.group(0)
        emoji = get_emoji(word)
        return f"{word} {emoji}" if emoji else word

    return _TOKEN_RE.sub(_replace, str(text))


def add_emoji(word, emoji):
    """Runtime mein naya word-emoji pair add karta hai."""
    if word and emoji:
        EMOJI_MAP[str(word).lower()] = str(emoji)
