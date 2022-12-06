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

func MakeValues(puzzleInput string) []string {
	lines := strings.Split(string(puzzleInput), "\n")
	values := make([]string, 0, len(lines))
	for _, raw := range lines {
		if strings.Contains(raw, "move") {
			values = append(values, raw)
		}
	}
	return values
}
