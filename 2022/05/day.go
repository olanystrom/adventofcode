package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	bytes, _ := os.ReadFile("input.txt")
	puzzleInput := string(bytes)
	stacks := []string{" ", "DTWFJSHN", "HRPQTNBG", "LQV", "NBSWRQ", "NDFTVMB", "MDBVHTR", "DBQJ", "DNJVRZHQ", "BNHMS"}
	fmt.Println("Answer1", Answer1(puzzleInput, stacks))
	stacks = []string{" ", "DTWFJSHN", "HRPQTNBG", "LQV", "NBSWRQ", "NDFTVMB", "MDBVHTR", "DBQJ", "DNJVRZHQ", "BNHMS"}
	fmt.Println("Answer2", Answer2(puzzleInput, stacks))
}

func Answer1(puzzleInput string, stacks []string) string {
	values := MakeValues(puzzleInput)
	answer := ""
	for i := 0; i < len(values); i++ {
		tmp := strings.Fields(values[i])
		amount, _ := strconv.Atoi(tmp[1])
		from, _ := strconv.Atoi(tmp[3])
		to, _ := strconv.Atoi(tmp[5])
		// fmt.Println(i, values[i], ":", tmp[1], tmp[3], tmp[5], ":", stacks)
		for j := 0; j < amount; j++ {
			item := stacks[from][len(stacks[from])-1]
			stacks[from] = stacks[from][0 : len(stacks[from])-1]
			stacks[to] += string(item)
		}
		// fmt.Println(i, values[i], ":", tmp[1], tmp[3], tmp[5], ":", stacks)
	}
	for a := range stacks {
		// fmt.Println(a, stacks[a], len(stacks[a]))
		if len(stacks[a]) > 0 {
			answer += string(stacks[a][len(stacks[a])-1])
		}
	}
	return answer[1:len(answer)]
}

func Answer2(puzzleInput string, stacks []string) string {
	values := MakeValues(puzzleInput)
	answer := ""
	for i := 0; i < len(values); i++ {
		tmp := strings.Fields(values[i])
		amount, _ := strconv.Atoi(tmp[1])
		from, _ := strconv.Atoi(tmp[3])
		to, _ := strconv.Atoi(tmp[5])
		// fmt.Println(i, values[i], ":", tmp[1], tmp[3], tmp[5], ":", stacks)
		item := stacks[from][len(stacks[from])-amount : len(stacks[from])]
		stacks[from] = stacks[from][0 : len(stacks[from])-amount]
		stacks[to] += string(item)
		// fmt.Println(i, values[i], ":", tmp[1], tmp[3], tmp[5], ":", stacks)
	}
	for a := range stacks {
		// fmt.Println(a, stacks[a], len(stacks[a]))
		if len(stacks[a]) > 0 {
			answer += string(stacks[a][len(stacks[a])-1])
		}
	}
	return answer[1:len(answer)]
}
