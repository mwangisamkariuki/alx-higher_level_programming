#!/bin/bash
# Send GET request to a URL and display the body of the response
curl -sL -H 'X-School-User-Id: 98' -- "$1"
