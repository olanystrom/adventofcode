package main

import (
	"strings"
)

func Sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

type GameInput struct {
	elf string
	you string
}

func MakeValues(puzzleInput string) []GameInput {
	lines := strings.Split(string(puzzleInput), "\n")
	values := make([]GameInput, len(lines))
	for i, raw := range lines {
		if len(raw) > 0 {
			tmp := strings.Split(raw, " ")
			values[i].elf = tmp[0]
			values[i].you = tmp[1]
		}
	}
	return values
}
