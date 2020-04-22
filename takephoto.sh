#!/bin/bash
DATE=$(date +"%s")
raspistill -o /home/pi/stills/photos/$DATE.jpg
