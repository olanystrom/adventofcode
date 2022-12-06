package main

import (
	"os"
	"testing"
)

func TestAnswer1(t *testing.T) {
	bytes, _ := os.ReadFile("test.txt")
	stacks := []string{" ", "ZN", "MCD", "P"}
	puzzleTest := string(bytes)
	answer := Answer1(puzzleTest, stacks)
	if answer != "CMZ" {
		t.Errorf("Answer1(TEST) = %s, want CMZ", answer)
	}
}

func TestAnswer2(t *testing.T) {
	bytes, _ := os.ReadFile("test.txt")
	puzzleTest := string(bytes)
	stacks := []string{" ", "ZN", "MCD", "P"}
	answer := Answer2(puzzleTest, stacks)
	if answer != "MCD" {
		t.Errorf("Answer2(TEST) = %s, want MCD", answer)
	}
}

func BenchmarkAnswer1(b *testing.B) {
	bytes, _ := os.ReadFile("input.txt")
	puzzleTest := string(bytes)
	for i := 0; i < b.N; i++ {
		stacks := []string{" ", "DTWFJSHN", "HRPQTNBG", "LQV", "NBSWRQ", "NDFTVMB", "MDBVHTR", "DBQJ", "DNJVRZHQ", "BNHMS"}
		_ = Answer1(puzzleTest, stacks)
	}
}

// func BenchmarkAnswer2(b *testing.B) {
// 	bytes, _ := os.ReadFile("input.txt")
// 	puzzleTest := string(bytes)
// 	for i := 0; i < b.N; i++ {
// 		_ = Answer2(puzzleTest)
// 	}
// }
