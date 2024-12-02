package main

import (
	"strconv"
	"strings"
)

func Sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}

func MakeValues(puzzleInput string) []int {
	lines := strings.Split(string(puzzleInput), "\n")
	values := make([]int, len(lines))
	for i, raw := range lines {
		values[i], _ = strconv.Atoi(raw)
	}
	return values
}
