import sys
from .core import emojify


def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        try:
            text = input("Text likho: ")
        except (EOFError, KeyboardInterrupt):
            print()
            return
    print(emojify(text))


if __name__ == "__main__":
    main()
