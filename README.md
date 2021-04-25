# The Swamp

A browser-based text adventure created as a final project for East Carolina University's Web Applications class. Powered by flask and a healthy dose of javascript. Developed by [Cason White](https://github.com/whitecas18), [Malik Brantley](https://github.com/brantleym13), and [Robert Saul](https://github.com/rowaul)

[Live site](http://theswamp.life/)

## About the game

![swamp logo](/static/assets/swamplogo.png)

Travel through East Carolina University, now warped into an unforgiving swamp land by a mysterious curse. The other students may be gone, but the presence of the Old Ones still remains, and they are the key to undoing the curse. Overcoming the trials of the Old Ones will grant you Crystals of their great knowledge, and collecting all 6 will give you the best chance at survival. Armed with only your wisdom and courage, traverse the land and free the campus or become another soul lost to The Swamp.

## Directory Structure

```
  .                                                        ...
    ├── data                  # Database for saves  |       └── static
    │   ├── data.sqlite                             |           ├── assets                # Images
    ├── static                # css/js/binaries     |           │   └── ...
    |   └── ...                                     |           ├── audio                 # Sound and music
    ├── templates             # HTML files          |           │   └── ...
    │   ├── about.html                              |           ├── scripts               # Javascript
    │   ├── index.html                              |           │   └── game.js
    │   └── game.html                               |           ├── Bleeding Pixels.ttf
    ├── __init__.py                                 |           ├── about.css
    ├── location.py                                 |           ├── index.css
    ├── maze.py                                     |           └── swamp.css
    ├── util.py                                     |
    ├── world.py                                    |
    ├── requirements.txt                            |
    └── README.md                                   |

```

## Local Test Setup

First, we need to install a Python 3 virtual environment with:

```
sudo apt-get install python3-venv
```

Create a virtual environment:

```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:

```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:

```
pip3 install -r requirements.txt
```

Then you can start the server with:

```
python3 __init__.py
```
