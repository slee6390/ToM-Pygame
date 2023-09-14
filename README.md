# ToM-Pygame
## Description

### Overview:
This project is an attempt to digitize experiments designed to test a psychological theory called Theory of Mind, a crucial aspect of human cognition. It refers to the human ability to ascribe mental states to those other than ourselves and how we use such ability to understand others. This project includes two interactive activities that serve as different experiments to assess this important skill and have been implemented using the Pygame framework. While relatively simple, they provide an engaging and interactive way to explore and understand the concept of Theory of Mind.

### Built With:
Pygame in Python.

### Getting Started: 
#### Prerequisites (work in progress)
how to install and run software locally (npm)
#### Installation (work in progress)

### Usage: (work in progress)
how to use the project

### Roadmap:
- [x] Finish Activity 1
- [x] Finish Activity 2
- [x] Add a Main Menu screen
- [ ] Add a feature that reads the instructions
- [ ] Make the instructions simpler by improving the interactivity aspect of the project
- [ ] Simplify the code substituting some activity 1 or activity 2 modules with the Display class (continue buttons, sprites, etc.)

### Project Structure:
#### main.py
Includes the basic framework of the project and serves as the initial screen to the users. It displays a main menu with three options: Activity 1, Activity 2, and Quit. 

#### display.py
Contains the Display class which is used in all other python files to set up any text or buttons.

#### activity1_screen.py
Contains the activity1_screen function called in main.py, which is what is displayed when the user clicks on 'Activity 1' from the Main Menu. It sets up the variables, static text, and background used in activity 1. By calling the modules from activity1_modules.py, it runs through the entirety of Activity 1. The code is mainly set up into four separate sections, in which each section codes for each "slide" within the activity.

#### activity1_modules.py
Contains the classes used in activity1_screen to run Activity 1. The classes included are Apple_box, Grape_box, Continue_button, and Child, and each class contain the needed functions for each sprite to fulfill its role in Activity 1.

#### activity2_screen.py
Similar to activity1_screen.py, this file sets up the activity2_screen function that is called in main.py and runs the entirety of Activity 2 by calling in classes from activity2_modules.py. It sets up the necessary variables and other configurations needed to successfully run Activity 2.

#### activity2_modules.py
Includes the classes used in activity2_screen.py. These are comprised of Girl, Chest, Box, Ball, Okay_buttion, and Continue_button. These classes have their separate functions that are used to carry out Activity 2.
