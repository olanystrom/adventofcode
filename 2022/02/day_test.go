package main

import (
	"io/ioutil"
	"testing"
)

func TestAnswer1(t *testing.T) {
	bytes, _ := ioutil.ReadFile("test.txt")
	puzzleTest := string(bytes)
	answer := Answer1(puzzleTest)
	if answer != 15 {
		t.Errorf("Answer1(TEST) = %d, want 15", answer)
	}
}

func TestAnswer2(t *testing.T) {
	bytes, _ := ioutil.ReadFile("test.txt")
	puzzleTest := string(bytes)
	answer := Answer2(puzzleTest)
	if answer != 12 {
		t.Errorf("Answer2(TEST) = %d, want 12", answer)
	}
}

func BenchmarkAnswer1(b *testing.B) {
	bytes, _ := ioutil.ReadFile("test.txt")
	puzzleTest := string(bytes)
	for i := 0; i < b.N; i++ {
		_ = Answer1(puzzleTest)
	}
}

func BenchmarkAnswer2(b *testing.B) {
	bytes, _ := ioutil.ReadFile("test.txt")
	puzzleTest := string(bytes)
	for i := 0; i < b.N; i++ {
		_ = Answer2(puzzleTest)
	}
}
