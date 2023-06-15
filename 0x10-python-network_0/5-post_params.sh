#!/bin/bash
# Send POST request to a URL and display the body of the response
curl -sL -d 'test@gmail.com' -d 'subject=I will always be here for PLD' -- "$1"