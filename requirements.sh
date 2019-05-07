#!/bin/BASH

clear
figlet -f big MPS-YOUTUBE | lolcat
sleep 2
echo " "
load
clear
pkg update
clear
pkg upgrade
clear
pkg install python python2 -y
clear
pip install mps-youtube
clear
pip install youtube-dl
clear
pkg install mpv
