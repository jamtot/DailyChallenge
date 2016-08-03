def rektangle(word, x, y):
    wlen=len(word)
    length=wlen*y - (wlen-1)
    width=wlen*x - (wlen-1)
    # continue this

if __name__ == "__main__":
    while True:
        inputs = raw_input().split()
        word=inputs.pop()
        xy = map(int,inputs)
        print rektangle(word, xy[0], xy[1])
