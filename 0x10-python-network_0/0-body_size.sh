#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -sLI -- "$1" | grep -i 'content-length' | tr -s '\t ' ' ' | cut -d ' ' -f 2