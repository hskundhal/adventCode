package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	pos := 50
	paswd := 0
	prevpos := false
	//quotient := 0
	file, err := os.Open("2025/input1.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		if pos == 0 {
			prevpos = true
		} else {
			prevpos = false
		}
		if strings.HasPrefix(line, "L") {
			numStr := strings.TrimPrefix(line, "L")
			num, err := strconv.Atoi(numStr)
			paswd += num / 100
			num = num % 100
			if err == nil {
				pos -= num
				if pos < 0 {
					pos += 100
					if !prevpos && pos != 0 {
						paswd += 1
					}
				}
			}
		} else if strings.HasPrefix(line, "R") {
			numStr := strings.TrimPrefix(line, "R")
			num, err := strconv.Atoi(numStr)
			paswd += num / 100
			num = num % 100

			if err == nil {
				pos += num
				if pos >= 100 {
					pos -= 100
					if !prevpos && pos != 0 {
						paswd += 1
					}
				}
			}

		}

		if pos == 0 {
			paswd += 1
		}
		fmt.Println(line, " ", pos, " ", paswd)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error scanning file:", err)
	}
}
