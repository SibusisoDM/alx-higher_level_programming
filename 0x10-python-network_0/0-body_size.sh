#!/bin/bash
# send a request to an URL with curl, and displays the size of the body of the response
body_size=$(curl -s "$1" | wc -c)
