import sys

n = int(sys.stdin.readline())
text = sys.stdin.readline()

color = {"B": 0, "R": 0}

color[text[0]] += 1

for i in range(1, n):
    if text[i] != text[i-1]:
        color[text[i]] += 1

min_col = min(color["B"], color["R"]) + 1
print(min_col)