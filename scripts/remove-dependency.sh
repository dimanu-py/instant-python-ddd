#!/bin/bash

read -p "Dependency to remove: " dependency
read -p "Is $dependency a dev dependency? (y/n): " is_dev
read -p "Does $dependency belong to a group? (y/n): " belongs_to_group

flag=""

if [ "$is_dev" == "y" ]; then
  flag="--dev"
fi

if [ "$belongs_to_group" == "y" ]; then
  read -p "Group name: " group_name
  flag="--group $group_name"
fi

uv remove $flag $dependency