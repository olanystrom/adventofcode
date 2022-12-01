package main

import (
	"fmt"
	"io/ioutil"
	"sort"
)

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	puzzleInput := string(bytes)
	fmt.Println("Answer1", Answer1(puzzleInput))
	fmt.Println("Answer2", Answer2(puzzleInput))
}

func Answer1(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	maxelf := 0
	celf := 0
	for i := 0; i < len(values)-1; i++ {
		if values[i] != 0 {
			celf += values[i]
		} else {
			if celf > maxelf {
				maxelf = celf
			}
			celf = 0
		}
	}
	return maxelf
}

func Answer2(puzzleInput string) int {
	values := MakeValues(puzzleInput)

	celf := 0
	maxelf := make([]int, 0)
	for i := 0; i < len(values)-1; i++ {
		if values[i] != 0 {
			celf += values[i]
		} else {
			maxelf = append(maxelf, celf)
			celf = 0
		}
	}
	maxelf = append(maxelf, celf)
	sort.Ints(maxelf)
	// sort.Slice(maxelf, func(i, j int) bool {
	// 	return maxelf[i] < maxelf[j]
	// })
	// fmt.Printf("%v", maxelf[len(maxelf)-3:])
	return Sum(maxelf[len(maxelf)-3:])
}
