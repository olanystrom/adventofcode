package main

import (
	"strings"
)

func MakeValues(puzzleInput string) []string {
	lines := strings.Split(string(puzzleInput), "\n")
	return lines
}
