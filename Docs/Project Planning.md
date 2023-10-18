
# Project Planning
## List of Features
- To set up the camera that will support the display of a real-time camera feed.
- Notification about the camera status should be displayed.
- Choosing a desired camera among the multiple cameras should be provided to the user.
- Detection of the color by the provided input (indicator on steering wheel).
- The angle of the steering wheel should be detected in real-time.
- The intensity of the movement of the steering wheel in the game can be integrated with some speed control mechanisms.
- Image enhancement to make it easier to recognize the colored paper on the steering wheel.
- Integrating gestures for performing lane change or may be a drift.
- More personalized experience can be achieved by training a machine learning model to adapt the gameplay with the help of the user's driving style.
- Creating a specific steering gesture to activate the nitro boost in the game which allows the player to use it strategically during races.
- Based on the movements recognized from the colored paper, develop a system that replicates steering input for the racing game.
- Implementing simple hand movements to open and close the game by making the user interface more interactive.
## MVP (Minimum viable product)
- Initialization of the camera and launching a graphical window in order to display the live camera feed.
- The inputs/controls of the game are ensured by color detection and tracking.
- To identify the position of the colored paper on the steering wheel.
- Reduce the visual noise and preprocess the data which enhances the image detection.
- Implement a basic car control system that can recognize steering gestures.
## User Stories
- As a user, I want the camera window to appear effectively when the program is executed.
- As a user, I don’t want to face any difficulties during the race due to the detection of color of the paper that I use on my steering wheel.

- As a user, I want to ensure that my steering inputs are recognized properly by the game when the program detects the position of the colored paper on the steering wheel.

- As a user, I expect the program to reduce the visual noise and produce a clear image in order to track the colored paper.

- As a user, I want the program to detect steering actions and use them to guide the car in the appropriate desired direction allowing me to have a smooth experience.

## Overall Structure
The goal of our project is to convert the colour representations of the steering wheel indicators into a format that can be understood by computers through the real-time input which is a simulated steering wheel. Preprocessing and refinement will be applied to optimize the visual information. The next step is to use image processing methods to identify and determine the coloured segment's outline. Subsequently, the system analyses the movements and actions of the steering wheel and extracts appropriate information. Finally, this data will be used to automate control inputs for self-contained gameplay.

To implement this, we need to break the project down into smaller segments and work on them accordingly. As described above, we have several features, including color detection, camera capturing, image processing, and recognizing steering actions. We have different files for each of these so that all team members can work efficiently.
