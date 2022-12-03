package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	puzzleInput := string(bytes)
	fmt.Println("Answer1", Answer1(puzzleInput))
	fmt.Println("Answer2", Answer2(puzzleInput))
}

func Answer1(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	answer := 0
	for i := 0; i < len(values)-1; i++ {
		if values[i] != 0 {
		} else {
		}
	}
	return answer
}

func Answer2(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	answer := 0
	for i := 0; i < len(values)-1; i++ {
		if values[i] != 0 {
		} else {
		}
	}
	return answer
}
