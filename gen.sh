#!/bin/bash
python3 gen.py $1 > $1.html
python3 gog.py $2 $3 > $1.json
