#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the body of the response
if [ $(curl -I "$1" | grep 'HTTP' | awk '{print$2}') == 200 ]; then echo $(curl "$1"); fi
