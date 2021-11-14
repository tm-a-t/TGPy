import sys


def main():
    cmd = sys.argv[1]
    if cmd == 'run':
        return 'Run'
    else:
        return 'Unknown command'
