input1="""Some
text."""
input2="""package main

import "fmt"

func main() {
    queue := make(chan string, 2)
    queue <- "one"
    queue <- "twoO"
    close(queue)
    for elem := range queue {
        fmt.Println(elem)
    }
}"""


def transpose(text):
    lines = text.splitlines()
    lens = [len(line) for line in lines]
    longest = max(lens)
    for i in xrange(len(lines)):
        spaces = longest-lens[i]
        if spaces > 0:
            lines[i]+=' '*(spaces)
    output=''
    curindex=0
    for i in xrange(longest):
        for line in lines:
            output+=line[curindex]
        if curindex<longest-1:
            output+='\n'
            curindex+=1
    return output

if __name__ == "__main__":
    print transpose(input1)
    print transpose(input2)
