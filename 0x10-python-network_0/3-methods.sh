#!/bin/bash
# Display all HTTP methods that a server of a URL will accept
curl -sLI -- "$1" | grep -i 'allow' | tr -s '\t ' ' ' | cut -d ' ' -f 2-
