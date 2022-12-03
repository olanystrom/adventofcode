package main

import (
	"strings"
)

type rucksack struct {
	first  string
	second string
	whole  string
}

func MakeValues(puzzleInput string) []rucksack {
	lines := strings.Split(string(puzzleInput), "\n")
	values := make([]rucksack, len(lines))
	for i, raw := range lines {
		var half uint16
		if len(raw) > 0 {
			half = uint16(len(raw) / 2)
			values[i].first = raw[0:half]
			values[i].second = raw[half:]
			values[i].whole = raw
		}
	}
	return values
}
