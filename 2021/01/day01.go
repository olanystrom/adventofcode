package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	puzzleInput := string(bytes)
	fmt.Println(Answer1(puzzleInput))
	fmt.Println(Answer2(puzzleInput))
}

func Answer1(puzzleInput string) int {
	values := makeValues(puzzleInput)

	count := 0
	for i := 0; i < len(values)-1; i++ {
		if values[i] < values[i+1] {
			count += 1
		}
	}
	return count
}

func Answer2(puzzleInput string) int {
	values := makeValues(puzzleInput)

	count := 0
	for i := 0; i < len(values)-3; i++ {
	}
	return count
}

func makeValues(puzzleInput string) []int {
	lines := strings.Split(string(puzzleInput), "\n")
	values := make([]int, len(lines))
	for i, raw := range lines {
		values[i], _ = strconv.Atoi(raw)
	}
	return values
}
