#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the body of the response
echo $(curl "$1")
