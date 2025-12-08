package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
    "strconv"
)

func main(){

    var r1 int64 = 0
    var r2 int64 = 0
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    line := scanner.Text()
    lines := strings.Split(line, ",") 
    for _, temp := range lines {
        LR := strings.Split(temp,"-")
        L, _ := strconv.ParseInt(LR[0], 10, 64)
        R, _ := strconv.ParseInt(LR[1], 10, 64)
        for n:=L; n<R+1; n++ {
            s := strconv.FormatInt(n,10)
            if p1(s) { r1+=n }
            if p2(s) { r2+=n }
        }
    }
    fmt.Println("res1/", r1)
    fmt.Println("res2/", r2)
}

func p2(s string)bool{

    l := len(s)
    for ll := 1; ll < l/2+1; ll++ {
        if l % ll == 0 {
            tt := l/ll
            ok := true
            sub := s[:ll]
            for i:=0; i<tt; i++ {
                if sub != s[i * ll : (i+1) * ll] {
                    ok = false
                    break
                }
            }
            if ok {
                return true
            }
        }
    }
    return false
}

func p1(s string)bool{

    l := len(s)
    if l % 2 == 0 {
        return s[:l/2] == s[l/2:]
    }
    return false
}

