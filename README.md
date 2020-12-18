# UNICORN MAZER

### Unicorn Mazer is an Old-School Maze Game, with Cupcakes, Coffee and Evil Bulls.


## [Click Here to Download and Play!](https://gustavo-pimenta.itch.io/unicorn-mazer)

## About the Game 

Unicorn Mazer first version was made in 2019, only with Python and Pygame.
The game was a personal project, designed pixel by pixel in the hardest way.
A new (and much better) version was developed in 2020, using object-oriented programming. 

All pixel art of the game was made by myself in the pixel art tool [Pixilart](https://www.pixilart.com/)

All game musics and sound effects were free obtained from the website [Freesound](https://freesound.org/)
Music credits to [Doctor_Dreamchip](https://freesound.org/people/Doctor_Dreamchip/)


## Game Compilation

The script "setup.py" has all the configuration for the game compilation
The script sets the files to be included to install the game, using the .MSI Installer

The compiler also creates the .EXE file, to run the game with this executable you have to copy all the game images and sounds manually. The .MSI 
automatically copy all these files when install the game.

To compile the game, just set all the configuration in the setup, place all the game files togheter in the same folder and run the .BAT file.

### Tutorial video about the compilation:
How to Convert Python to Exe and Create An Installer - https://www.youtube.com/watch?v=RrpvNvklmFA

### cx_Freeze MSI shortcut bug resolution 
https://stackoverflow.com/questions/38637337/cx-freeze-shortcutdir-gives-error
The cx_Freeze lib, used to compile the game, has a bug when the MSI creates the desktop shortcut.
To fix this bug we have to enter in the "windist.py" file inside the cx_Freeze folder and make this change in the line 61:
CHANGE "None, None, None, None)])" TO "None, None, None, "TARGETDIR")])"


## Team

* Gustavo Pimenta - Computer Engineering / Game Developer / Python Coder 



