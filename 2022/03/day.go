package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const scoreIndex string = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	puzzleInput := string(bytes)
	fmt.Println("Answer1", Answer1(puzzleInput))
	fmt.Println("Answer2", Answer2(puzzleInput))
}

// 7510 not the right answer; your answer is too low.

func Answer1(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	answer := 0
	match := 0
	ascore := 0
	for i := 0; i < len(values)-1; i++ {
		// fmt.Printf("%s %s\n", values[i].first, values[i].second)
		for j := 0; j < len(values[i].first); j++ {
			match = strings.Index(values[i].second, string(values[i].first[j]))
			if match > -1 {
				ascore = strings.Index(scoreIndex, string(values[i].first[j]))
				answer += ascore
				// fmt.Println(i, string(values[i].first[j]), ascore)
				break
			}
		}
	}
	return answer
}

// 1784 not the right answer; your answer is too low.
// 2743 is to low
func Answer2(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	answer := 0
	var first string
	var second string
	var third string
	ascore := 0

	for i := 0; i < len(values)-1; i += 3 {
		first = values[i].whole
		second = values[i+1].whole
		third = values[i+2].whole
		for j := 0; j < len(first); j++ {
			if strings.Contains(second, string(first[j])) {
				if strings.Contains(third, string(first[j])) {
					ascore = strings.Index(scoreIndex, string(first[j]))
					answer += ascore
					// fmt.Println(i, i+1, i+2, string(first[j]), ascore)
					break
				}
			}
		}
	}
	return answer
}
