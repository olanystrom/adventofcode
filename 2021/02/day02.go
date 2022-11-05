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

type valueStruct struct {
	direction string
	amount    int
}

func Answer1(puzzleInput string) int {
	values := makeValues(puzzleInput)
	horizontal := 0
	depth := 0

	for _, value := range values {
		switch value.direction {
		case "forward":
			horizontal += value.amount
		case "down":
			depth += value.amount
		case "up":
			depth -= value.amount
		}
	}
	return depth * horizontal
}

func Answer2(puzzleInput string) int {
	values := makeValues(puzzleInput)
	horizontal := 0
	depth := 0
	aim := 0

	for _, value := range values {
		switch value.direction {
		case "forward":
			horizontal += value.amount
			depth += value.amount * aim
		case "down":
			aim += value.amount
		case "up":
			aim -= value.amount
		}
	}
	return depth * horizontal
}

func makeValues(puzzleInput string) []valueStruct {
	lines := strings.Split(string(puzzleInput), "\n")
	values := make([]valueStruct, len(lines))
	for i, raw := range lines {
		parts := strings.Split(raw, " ")
		values[i].direction = parts[0]
		values[i].amount, _ = strconv.Atoi(parts[1])
	}
	return values
}
