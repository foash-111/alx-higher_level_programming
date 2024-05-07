#!/bin/bash
#a Bash script must send a POST request with the contents of a file, passed with the filename as the second argument of the script.
curl -s -X POST "@$2" $1
