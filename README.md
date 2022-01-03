# Tadarida-D - For Raspberry Pi

Tadarida is a software toolbox that can be used for automatic identification of species that produces sound, in this case ultrasonic sound. Tadarida is based on an AI technique for supervised learning that is called random forest. The Tadarida software is divided into three software modules, Tadarida-D (detecting), Tadarida-L (labelling) and Tadarida-C (classifier). Tadarida-L is used for work with the reference sound library and Tadarida-C takes care of the random forest parts, both when building the classifiers and when running the automatic classification of recorded sound. The source code for all Tadarida modules can be found here: https://github.com/YvesBas

The module we use here is the Tadarida-D module. It will locate the sound events in the recorded sound files, and then extract a huge number of features from each sound event that will be stored in a tabular text file. There will be one text file for each sound file and they will have the same name as the corresponding sound file, but with the extension ".ta". Those text files can then be used when running Tadarida-C for automatic identification to species level.

There are two main reasons for why it can be useful to implement Tadarida-D in a detector.

1. The size of the tabular text files containing extracted features are small compared to the recorded sound files. Therefore it can be more effective to use this compact file format when the recorded data is shared with someone who want to run the Tadarida classification on their machines. Running the entire classification locally is not possible because the reference sound library and reference sound database are not publicly available.

2. The features extracted by Tadarida-D can be used for other purposes, for example visualisation or running other AI systems for classification. This can be used, for example, to build classifiers based on other reference sound libraries from other parts of the world, that maybe also are based on other AI techniques. Tadarida-D is released under the LGPL-3.0 license and can therefore be modified when needed. The extracted features are described in this document: Manual_Tadarida-D.odt

## Installation

    # Always start with an update/upgrade.
    sudo apt update
    sudo apt upgrade

    # Install QT and the two libraries used.
    sudo apt install qt5-default
    sudo apt install libfftw3-3
    sudo apt install libsndfile-dev

    # Check out this fork of Tadatida-D code from GitHub.
    git clone https://github.com/cloudedbats/Tadarida-D.git

## Run Tadarida-D

Example where you have a directory called "StationA_2021-10-01" where the sound files are located.

    cd /home/pi/Tadarida-D/install_rpi
    ./TadaridaD /home/pi/wurb_recordings/StationA_2021-10-01/

## Python script to run Tadarida-D

TODO...

## Compile and build Tadarida-D

There are pre build versions of Tadarida-D for Windows and Linux from the original GitHub repository, but the Linux version does not work directly on Raspberry Pi. Therefore a rebuild was needed to match the 32 bits OS running on an ARM processor.
This is already done in this GitHub fork of Tadarida-D, but the process for the rebuild is described below if it must be done again in the future.

    # Always start with an update/upgrade.
    sudo apt update
    sudo apt upgrade

    # Install QT and the two libraries used. 
    # sudo apt install qt5-default # Not available in Bullseye.
    sudo apt install qttools5-dev-tools # Use this in Bullseye.
    sudo apt install qt5-qmake
    sudo apt install libfftw3-3
    sudo apt install libsndfile-dev

    # Check out this fork of Tadatida-D code from GitHub.
    git clone https://github.com/cloudedbats/Tadarida-D.git

    # Go to the source directory.
    cd Tadarida-D/sources/

    # Locate the installed modules and move them to the source directory. 
    sudo find / -name libsndfile*
    sudo find / -name libfftw3f*
    # Remove the old versions of the two used libs and copy the new versions.
    rm Libs/libfftw3f.so 
    rm Libs/libsndfile.so
    # Note: These paths may be different depending on the results from the "find" commands above.
    cp /usr/lib/arm-linux-gnueabihf/libfftw3f.so.3 Libs/libfftw3f.so
    cp /usr/lib/arm-linux-gnueabihf/libsndfile.so.1 Libs/libsndfile.so

    # Build Tadarida-D. 
    qmake
    make

    # Create a new directory and copy files.
    mkdir /home/pi/Tadarida-D/install_rpi
    cp TadaridaD /home/pi/Tadarida-D/install_rpi
    cp Libs/libfftw3f.so /home/pi/Tadarida-D/install_rpi
    cp Libs/libsndfile.so /home/pi/Tadarida-D/install_rpi
    
    # And finally commit and push to GitHub.
    
