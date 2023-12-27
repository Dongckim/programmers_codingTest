import sys
sys.stdin = open("input.txt", "rt")

print(len(sys.stdin.read().split()))