# Open-Mouse
This is a Virtual Mouse software with codebase in **python**. It uses packages **autopy**, **openCV** and **MediaPipe**.
## Hand Tracking Module
https://user-images.githubusercontent.com/63851624/149654504-e144f9fb-8313-4e3b-aece-d362f27fe1fc.mp4

## Open Mouse Module
https://user-images.githubusercontent.com/63851624/149654511-d888187e-56f3-4a1f-a8f9-353265c200ed.mp4

It tracks down the hand movement and if these movements are within the given rectangle, them it will change cursor's position based on these hand movements.
If Index finger is up then it it considered to be in Hovering Mode
If a scissor chop is done using Index and Middle Finger then it will be considered as a Right-Click.
If both Index and Middle Fingers are kept closed to each other then it will be considered as No Operation Mode.
An FPS Counter is also provided in top left corner for the user to know the FPS.
## Scope for Extended Uses:
A Hand Tracking Module is also provided which can detect number of hands(provided by user).
Project's implementation can further be opitimized for increased benefits like draw-on-image or virtual keyboard.
