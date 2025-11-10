# Hello-world-2025-Gordon

## Week 1 
Assignment
    I use Phython to greet the user and display the current date.
    use the datetime module to get the current date.
    know how to use input() to get user input.
    know how to use print() to display output.
    know how to use daytime.date.today() to get the current date.

## Week 2
Assignment1 ： Pick four objects in everyday life and represent them as a data type.

lamp = {
    "color" : "Yellow"
    "isOn" : True
    "location" : "bedroom"
}

coffeeMug = {
    "color" : "blue"，
    "isFull" : True ，
    "contain" : "coffee"，
    "volume" : 500
}

myBackpack = ["laptop", "studentID", "keys", "lunchbox"]

marathon = {
    "distance": "42.6 KM",
    "isFun": False,
    "meaningful": True,
    "location": "DC"
}

Assignment 2
{
    "Name": "Gordon",
    "major": "Interaction Design",
    "time length of the program": 2,
    "fulltime": true,
    "location": "NYC"
}

Assignment 3 : please see week2_assignment3.py

## Week 3
I created a game based on the rules of rock-paper-scissors, but with some variations.
At first, it’s a single-round win; then it changes to best of three.
Later, players must win consecutively before they can proceed to a flip coin stage.

# Week 4-6
Keep rewinding 

## Week 7For this exercise, I attempted to build a simple Snake Game using pygame.
I started by installing the library, then learned how to control movements through keyboard inputs.
The main mechanic is that when the snake “eats” food, it grows longer.
Finally, I used pygame’s drawing functions to render blocks on the screen.

# Week 9 : State Machine Strucure
Below is how I deconstructed my Iris#1 interactive installation into a state machine structure.
Each state represents one stage of audience interaction and system behavior, clearly defining how the experience flows from beginning to end.

---

EXHIBIT — The system displays all previously generated Digital Iris images, forming a “digital iris wall.”
→ Transitions to CAPTURE when a new visitor approaches and the operator is ready to take a photo.

CAPTURE — The operator manually captures the visitor’s iris image.
→ Transitions to TRANSFORM after the photo is taken.

TRANSFORM — The system performs a Fourier transform and visualizes the waveform, representing the algorithmic process in motion.
→ Transitions to DISPLAY_SINGLE once the analysis is complete.

DISPLAY_SINGLE — The visitor’s Digital Iris and its unique latent code are shown together on screen.
→ Transitions to UPDATE_EXHIBIT after the display finishes.

UPDATE_EXHIBIT — The newly generated Digital Iris is added to the digital wall, expanding the collective display.
→ Loops back to EXHIBIT when the new composition is ready.

    ### Digital Iris — Interactive State Machine Prototype

This p5.js prototype acts as a lightweight **simulator** for the Digital Iris installation.  
It visualizes how the system transitions through five states — from EXHIBIT to CAPTURE, TRANSFORM, DISPLAY_SINGLE, and UPDATE_EXHIBIT — before looping back to the main wall display.

Link : https://editor.p5js.org/ccheng2/full/wsbUcogZl