package main

import (
	"flag"
	"fmt"
	"os"
	"reflect"
)

type Runner struct{}

func main() {
	d := flag.String("d", "", "Day to run (e.g., 1,2)")
	flag.Parse()

	if *d == "" {
		fmt.Println("Please specify a valid day to run using -d <name> (e.g., -d 1)")
		return
	}
	funcName := "Day" + *d

	runner := Runner{}
	method := reflect.ValueOf(&runner).MethodByName(funcName)

	if !method.IsValid() {
		fmt.Printf("Method '%s' not found. Make sure it is defined on Runner struct.\n", funcName)
		os.Exit(1)
	}

	fmt.Printf("Running %s...\n", funcName)
	method.Call(nil)
}
