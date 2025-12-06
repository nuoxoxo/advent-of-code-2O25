package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

func main(){

    r1 := 0
    r2 := 0
    i := 50
    j := i
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan(){
        line := scanner.Text()
        d := line[0]
        n, _ := strconv.Atoi(line[1:])
        lr := 1
        if d == 'L' {
            lr = -1
        }
        i += n*lr
        i %= 100
        if i == 0 {
            r1++
        }
        // p2
        for k:=0;k<n;k++ {
            j += lr
            j %= 100
            if j == 0 {
                r2++
            }
        }
    }
    fmt.Println("res1/", r1)
    fmt.Println("res2/", r2)
}

