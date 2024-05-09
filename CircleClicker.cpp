/*____ _          _         ____                     _                __  __            _     _
 / ___(_)_ __ ___| | ___   |  _ \ _ __ __ ___      _(_)_ __   __ _   |  \/  | __ _  ___| |__ (_)_ __   ___
| |   | | '__/ __| |/ _ \  | | | | '__/ _` \ \ /\ / / | '_ \ / _` |  | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
| |___| | | | (__| |  __/  | |_| | | | (_| |\ V  V /| | | | | (_| |  | |  | | (_| | (__| | | | | | | |  __/
 \____|_|_|  \___|_|\___|  |____/|_|  \__,_| \_/\_/ |_|_| |_|\__, |  |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                             |___/
By Sam Rohrbach (github.com/TesseractPi)
Built for Neal.fun's perfect circle test at https://neal.fun/perfect-circle/
This should be on my website (https://samrohrbach.space)
In its default state, this is built for a 1920x1200 screen in fullscreen. Change the values accordingly.
*/

#include <iostream> // so we can talk to it
#include <cmath> // include some mathy stuff
#include <math.h> // oooh more math
#include <time.h> // just casually including ALL OF TIME
#include <windows.h> // do some windows integration magic (i'll implement linux later)

double center_x = 683.5;
double center_y = 364.5;
double radius = 256;

double angle_increment = 1;
double angle_repeat = ((360 / angle_increment) + 1);
double angle = 0;

int getX(int XTheta) {
    long double x = ((radius * sin(M_PI * 2 * angle / 360)) + center_x);
    return(x);
}

int getY(int YTheta) {
    long double y = ((radius * cos(M_PI * 2 * angle / 360)) + center_y);
    return(y);
}

int main(void) {
    std::cout << "Press A to draw a circle or Q to quit" << std::endl;
    while(true) {
        if (GetKeyState('Q') & 0x8000) { // when Q key pressed
            std::cout << "Goodbye!" << std::endl;
            return 69;
            break; // end
        }

        if (GetKeyState('A') & 0x8000) { // when A key pressed
            SetCursorPos(center_x, (center_y + radius)); // move mouse
            Sleep(250); // wait 0.25 seconds
            mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0); // start holding mouse
            std::cout << "Circle started..." << std::endl;
            for(int c = 1; c <= angle_repeat; c++) {
                SetCursorPos(getX(angle), getY(angle)); // move mouse
                std::cout << "Point drawn at (" << getX(angle) << ", " << getY(angle) << ")" << std::endl; // log point
                angle = angle + angle_increment;
                Sleep(1); // change to go slower
            }
            mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
            std::cout << "Circle complete!" << std::endl;
        }
    }
}







//this line is here to be 69 lines long and the last char here is 69