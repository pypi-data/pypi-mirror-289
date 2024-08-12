import sys

from .MemeGenerator import save_meme_to_disk


def h():
    print("Usage: memician <template> <path> <*args> <*options>")
    sys.exit()

def main(args):
    if len(args) <= 2:
        h()
    try:
        print("running newest version")
        args = args[1:]
        template = args[0]
        path = args[1]
        save_meme_to_disk(template, path, args[2:])
    except ValueError as e:
        print(str(e))
        h()
    except FileNotFoundError:
        print("No such directory: " + path)