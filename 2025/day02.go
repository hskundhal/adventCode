package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func (Runner) Day2() {
	file, err := os.Open("input2.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
