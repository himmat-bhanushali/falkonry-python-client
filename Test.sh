#!/usr/bin/env bash

for file in test/*
  do
    if [[ $file == *".py"* ]]; then
      cmd python "$file"
    fi
  done