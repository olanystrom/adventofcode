package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	bytes, _ := os.ReadFile("input.txt")
	puzzleInput := string(bytes)
	fmt.Println("Answer1", Answer1(puzzleInput))
	fmt.Println("Answer2", Answer2(puzzleInput))
}

func uniq(data string) bool {
	for a := range data {
		if strings.Count(data, string(data[a])) > 1 {
			return false
		}
	}
	return true
}

func Answer1(puzzleInput string) int {
	values := strings.Split(string(puzzleInput), "\n")
	line := values[0]
	answer := 0
	buffer := line[0:4]
	for i := 4; i < len(line); i++ {
		// fmt.Println(i, buffer)
		buffer = fmt.Sprintf("%s%s", buffer[1:], string(line[i]))
		if uniq(buffer) {
			answer = i + 1
			break
		}
	}
	return answer
}

func Answer2(puzzleInput string) int {
	values := strings.Split(string(puzzleInput), "\n")
	line := values[0]
	answer := 0
	buffer := line[0:14]
	for i := 4; i < len(line); i++ {
		// fmt.Println(i, buffer)
		buffer = fmt.Sprintf("%s%s", buffer[1:], string(line[i]))
		if uniq(buffer) {
			answer = i + 1
			break
		}
	}
	return answer
}
