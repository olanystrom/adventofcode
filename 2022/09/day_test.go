package main

import (
	"os"
	"testing"
)

func TestAnswer1(t *testing.T) {
	bytes, _ := os.ReadFile("test.txt")
	puzzleTest := string(bytes)
	answer := Answer1(puzzleTest)
	if answer != 0 {
		t.Errorf("Answer1(TEST) = %d, want 0", answer)
	}
}
func TestAnswer2(t *testing.T) {
	bytes, _ := os.ReadFile("test.txt")
	puzzleTest := string(bytes)
	answer := Answer2(puzzleTest)
	if answer != 0 {
		t.Errorf("Answer2(TEST) = %d, want 0", answer)
	}
}

func BenchmarkAnswer1(b *testing.B) {
	bytes, _ := os.ReadFile("input.txt")
	puzzleTest := string(bytes)
	for i := 0; i < b.N; i++ {
		_ = Answer1(puzzleTest)
	}
}

func BenchmarkAnswer2(b *testing.B) {
	bytes, _ := os.ReadFile("input.txt")
	puzzleTest := string(bytes)
	for i := 0; i < b.N; i++ {
		_ = Answer2(puzzleTest)
	}
}
