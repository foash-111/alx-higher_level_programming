#!/bin/bash
#a Bash script must send a POST request with the contents of a file, passed with the filename as the second argument of the script.
curl -s -d "@$2" $1
