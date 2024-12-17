import sys

def main():
    argv = sys.argv
    argc = len(argv)
    if argc == 2:
        print(int(argv[1]) ** 2)
        sys.exit(0)
    if argc == 3:
        print(int(argv[1]) * int(argv[2]))
        sys.exit(0)
    print(f"usage: \npython3 {argv[0]} <v1> <v2>(optional)\n")
    sys.exit(1)

main()