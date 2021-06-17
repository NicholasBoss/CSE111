l = 5
w = 5
h = 2

def compute_volume(length, width, height):
    print(l)
    global l
    l = 50
    return length * width * height

volume = compute_volume(l, w, h)

print(volume)

print(l)
