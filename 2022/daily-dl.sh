#!/usr/bin/zsh

mkdir `date +%d`
cp -nv template_day/* `date +%d` 
cd `date +%d`
~/go/bin/aocdl 
# ~/.cargo/bin/aoc d
# ~/.cargo/bin/aoc r
