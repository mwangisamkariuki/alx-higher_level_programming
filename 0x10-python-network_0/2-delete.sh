#!/bin/bash
# DELETE request to the URL passed as the first argument
curl -sL -X DELETE -- "$1"
