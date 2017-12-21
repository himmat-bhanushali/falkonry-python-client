#!/usr/bin/env bash

for file in test/*
do
  if [[ $file == *".py"* ]]; then
    exec python "$file"
  fi
done