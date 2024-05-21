#!/bin/bash
#   ____ _          _         ____                     _                __  __            _     _
#  / ___(_)_ __ ___| | ___   |  _ \ _ __ __ ___      _(_)_ __   __ _   |  \/  | __ _  ___| |__ (_)_ __   ___
# | |   | | '__/ __| |/ _ \  | | | | '__/ _` \ \ /\ / / | '_ \ / _` |  | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
# | |___| | | | (__| |  __/  | |_| | | | (_| |\ V  V /| | | | | (_| |  | |  | | (_| | (__| | | | | | | |  __/
#  \____|_|_|  \___|_|\___|  |____/|_|  \__,_| \_/\_/ |_|_| |_|\__, |  |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
#                                                              |___/ 
# By Sam Rohrbach (github.com/TesseractPi)
# Built for Neal.fun's perfect circle test at https://neal.fun/perfect-circle/
# This should be on my website (https://samrohrbach.space)
# In its default state, this is built for a 1366x768 screen in fullscreen. Change the values accordingly.

pi=$(seq -f '4/%g' 1 2 99999 | paste -sd-+ | bc -l) # because there's no built-in pi

center_x=683.5 # center x of circle
center_y=364.5 # center y of circle
radius=256 # radius of circle
new_center_y=$(( $center_y + $radius ))

angle_increment=6 # must be divisible by 360 AND be less than 180, ***CHANGE THIS VARIABLE!***
angle_repeat=$(( ( 360 / $angle_increment ) + 1 ))
angle=0 # starting angle, DO NOT CHANGE

function getXY ()
{
	x=$(( ( $radius * sin($pi * 2 * $angle / 360) ) + $center_x ))
	y=$(( ( $radius * sin($pi * 2 * $angle / 360) ) + $center_y ))
	echo "($x, $y)"
}

clear
echo "Press A to draw a circle or press Q to quit"

while true
do
	read -rsn1 isPressed_A
	read -rsn1 isPressed_Q

	if [ $isPressed_Q = "q" ]
	then
		echo "Goodbye!"
		break
	fi

	if [ $isPressed_A = "a" ] 
	then
		xdotool mousemove $center_x $new_center_y
fi
done
