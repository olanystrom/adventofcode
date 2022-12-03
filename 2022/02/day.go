package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	bytes, _ := ioutil.ReadFile("input.txt")
	puzzleInput := string(bytes)
	fmt.Println("Answer1", Answer1(puzzleInput))
	// fmt.Println("Answer2", Answer2(puzzleInput))
}

func Answer1(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	answer := 0
	score := 0
	for i := 0; i < len(values)-1; i++ {
		winner := 0
		winner = compareHands(values[i].elf, values[i].you)
		score = strings.Index(" XYZ", values[i].you)
		// fmt.Printf("You: %s, Elf: %s, Winner: %d, Score1: %d\n", values[i].you, values[i].elf, winner, score)
		if winner == 0 {
			score += 3
		} else if winner == -1 {
			score += 6
		}
		answer += score
	}
	return answer
}

func compareHands(elf string, you string) int {

	// A for Rock, B for Paper, and C for Scissors
	// Rock defeats Scissors  A > C
	// Scissors defeats Paper C > B
	// Paper defeats Rock B > A

	you = strings.Replace(you, "X", "A", 1)
	you = strings.Replace(you, "Y", "B", 1)
	you = strings.Replace(you, "Z", "C", 1)
	switch elf {
	case "A":
		if you == "C" {
			return 1
		} else if you == "B" {
			return -1
		} else {
			return 0
		}
	case "B":
		if you == "A" {
			return 1
		} else if you == "C" {
			return -1
		} else {
			return 0
		}
	case "C":
		if you == "B" {
			return 1
		} else if you == "A" {
			return -1
		} else {
			return 0
		}
	}
	return 0
}

// Anyway, the second column says how the round needs to end:
// X means you need to lose,
// Y means you need to end the round in a draw
// Z means you need to win. Good luck!"

func Answer2(puzzleInput string) int {
	values := MakeValues(puzzleInput)
	answer := 0
	for i := 0; i < len(values)-1; i++ {
		if values[i] != 0 {
		} else {
		}
	}
	return answer
}
