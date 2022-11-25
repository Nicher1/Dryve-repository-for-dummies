# Create Dryve Rail

The following library is to be used for translation along the x-axis of a track controlled by the Dryve D1.
![Negative end switch (set on right side)](https://i.imgur.com/00q584T.png)
Movement of the platform along the x-axis can be done with the:
```python    
targetPosition(<point>) command.
```
The point is set in reference to the *home* position set at the negative end-switch.
As the end-switch's home position is then set to x = 0 at the designated *home* position, any input into the function is considered as relative to the universal frame set at this position. 
The *home* position will begin to be set with:
```python    
dryveInit()
```
To manually set this position for any reason, simply run:
```python
homing()
```
To set velocity profile, simply run:
```python
velocityProfile(<velocity (mm/s)>)
```
likewise, the target velocity can be set with:
```python
targetVelocity(<velocity (mm/s)>)
```
The difference between velocity profile and target velocity is that targetvelocity() simply moves a set velocity 
until a new command is set, while velocityProfile() simply modifies the velocity setting in point to point movement.

If createdryverail contributes to a project that leads to publication, please acknowledge this by citing createdryverrail.
