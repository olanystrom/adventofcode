package main

import (
	"fmt"
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

type sectionspair struct {
	start1 int
	end1   int
	start2 int
	end2   int
}

func MakeValues(puzzleInput string) []sectionspair {
	lines := strings.Split(string(puzzleInput), "\n")
	values := make([]sectionspair, len(lines))
	for i, raw := range lines {

		if len(raw) > 0 {
			tmp := strings.Split(raw, ",")
			elf1 := strings.Split(tmp[0], "-")
			elf2 := strings.Split(tmp[1], "-")
			tmp2, err := strconv.Atoi(elf1[0])
			if err != nil || tmp2 == 0 {
				fmt.Println("Error:", raw)
			} else {
				values[i].start1 = tmp2
			}
			values[i].start2, _ = strconv.Atoi(elf2[0])
			values[i].end1, _ = strconv.Atoi(elf1[1])
			values[i].end2, _ = strconv.Atoi(elf2[1])
		}
	}
	return values
}
