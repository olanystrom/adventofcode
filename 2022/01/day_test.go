package main

import (
	"io/ioutil"
	"testing"
)

func TestAnswer1(t *testing.T) {
	bytes, _ := ioutil.ReadFile("test.txt")
	puzzleTest := string(bytes)
	answer := Answer1(puzzleTest)
	if answer != 24000 {
		t.Errorf("Answer1(TEST) = %d, want 24000", answer)
	}
}

func TestAnswer2(t *testing.T) {
	bytes, _ := ioutil.ReadFile("test.txt")
	puzzleTest := string(bytes)
	answer := Answer2(puzzleTest)
	if answer != 45000 {
		t.Errorf("Answer2(TEST) = %d, want 45000", answer)
	}
}
