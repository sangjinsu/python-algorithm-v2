N = int(input())
end = 1
depth = 1
while N > end:
    end += depth * 6
    depth += 1

print(depth)
