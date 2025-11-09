# Tusi-s-Couple
Tusi's couple simulation program in python using pygame library

Tusi couple is a decice built by *Nasir alDin Tusi* in the 13th century. 
This is a python oriented program mimicking working of the device. Only one repository exist under the name and that
to be in javascript and uses different aproaches to animate and position sprites and
elements - [https://github.com/grahamplace/tusi.git] 

*** LIBRARIES USED ***
PYGAME - Used to animate and display the program. 
Math - Used to give calculated co-ordinates to elements at every frame.

*** FORMULAS USED ***
Relationship between central co-ordinates and co-ordinates on circumference is-:
            x = x'(central) + cos(theta)       theta gives us direction from center of x co-ordinate
            y = y'(central) + sin(theta)
Movement of dots has two factors 
    1- Motion is achieved by decreasing and increasing  radius of bigger circle
    2- Synchronization and circular motion is a result of sine function 
        r = A sin(angularSpace)         angularSpace = pi/no. of dot
        sine function ensures dot must spawn just at an accurate lag than its preceeding counterpart

*** SIGNIFICANCE ***
    Used in mechanics and robotics to achieve different kind of movements
    It also serves as an optical illusion where dot even after possessing linear movement visuals to a moving circle  
