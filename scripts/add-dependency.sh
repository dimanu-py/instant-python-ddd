#!/bin/bash

read -p "Dependency to install: " dependency
read -p "Do you want to install $dependency as a dev dependency? (y/n): " is_dev
read -p "Do you want to install the $dependency inside a group? (y/n): " add_to_group

flag=""

if [ "$is_dev" == "y" ]; then
  flag="--dev"
fi

if [ "$add_to_group" == "y" ]; then
  read -p "Group name: " group_name
  flag="--group $group_name"
fi

uv add $flag $dependency