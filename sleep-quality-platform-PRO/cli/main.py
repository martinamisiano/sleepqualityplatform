
import sys
from core.analyzer import SleepAnalyzer

def load_file(path):
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]

    target = int(lines[0])
    data = [tuple(map(int, l.split())) for l in lines[1:]]
    return target, data


def main():
    if len(sys.argv) != 2:
        print("Usage: python cli/main.py file.txt")
        return

    target, data = load_file(sys.argv[1])
    a = SleepAnalyzer(target, data)

    print("[SONNI]")
    print(a.count_good())

    print("[STATISTICHE]")
    mn, mx, avg = a.stats()
    print(mn)
    print(mx)
    print(avg)

    print("[VALUTAZIONE]")
    for v in a.evaluations():
        print(v)

    print("[DURATE]")
    for t in a.top5():
        print(t)

if __name__ == "__main__":
    main()
