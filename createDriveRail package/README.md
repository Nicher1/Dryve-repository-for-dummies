# Dryve D1 Script

The following library is to be used for translation along the x-axis of a track controlled by the Dryve D1.
![Negative end switch (set on right side)](https://i.imgur.com/00q584T.png)
Movement of the platform along the x-axis can be done with the:
    targetPosition(<point>)
The point is set in reference to the *home* position set at the negative end-switch.
As the end-switch's home position is then set to x = 0 at the designated *home* position, any input into the function is considered relatively to the universal frame set at this position. 
At each consecutive execution of the function above, this *home* position is set. To manually set this position for any reason, simply run:
    homing()

If Matplotlib contributes to a project that leads to publication, please acknowledge this by citing DryveD1.
