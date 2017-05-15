#!/bin/bash

cat godeep.txt | xxd -r -p | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | xxd -r -p | base64 -d | base64 -d | xxd -r -p | base64 -d | base64 -d | 
base64 -d | xxd -r -p | base64 -d | base64 -d | base64 -d | base64 -d | xxd -r -p | base64 -d | xxd -r -p | base64 -d | xxd -r -p | xxd -r -p
