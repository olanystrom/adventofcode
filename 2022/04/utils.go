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

func MakeValuesSscanf(puzzleInput string) []sectionspair {
	lines := strings.Split(string(puzzleInput), "\n")
	values := make([]sectionspair, len(lines))
	var s1, e1, s2, e2 int
	for i, raw := range lines {
		if len(raw) > 0 {
			fmt.Sscanf(raw, "%d-%d,%d-%d", &s1, &e1, &s2, &e2)
			values[i].start1 = s1
			values[i].start2 = s2
			values[i].end1 = e1
			values[i].end2 = e2
		}
	}
	return values
}
