# Nasa-Background
This program will automatically get the latest image from [NASA's Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html) and set it to your desktop background. It runs in the background and checks for a new image at 4 AM every day. The images from the website aren't necessarily meant to be used as backgrounds, but most of them are high resolution and should look okay. Sometimes the website features videos, so this program will look at previous days until an image is found instead. 

## Getting Started
To run this program, first download the project. You then have the option of running the python script directly if you have python installed

```
python nasaBackground.py
```

or you can run the executable version, which is located in the dist folder.

### Installing
If you want the program to run automatically every time you start your computer, you can use the installer to set it up. 
You can run the installation script directly if you have python installed. It will look for 'NASA Background.exe', so you will have to make sure that you copy that from the dist folder.

```
python nasaBackgroundInstaller.py
```

or you can run the executable version of the installer, which is located in the dist folder. The installer gives you an option of installing or uninstalling the program from your system. 

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Pyinstaller](https://www.pyinstaller.org/) - Used to convert python script to executable program

## Authors

* **[Wesley Paglia](https://github.com/wrp1002)** - *Initial work*

## Acknowledgments
* The icon that is used can be found [here](https://icon-icons.com/icon/satelite-space/86323)

