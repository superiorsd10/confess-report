# Confess Report
> "It generates a profanity score for the sent text."


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [App Demonstration](#app-demonstration)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Confess Report is a Flask app that calculates a profanity score for the reported confession. 
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)


## Features
- When a user reports a confession, the request is sent to the _Confess Report Flask app_. It generates a _profanity score_ for the reported confession, and return it as a JSON response. 
- This app uses [alt-profanity-check](https://pypi.org/project/alt-profanity-check/) to calculate the profanity score for the reported confession. 


## App Demonstration
https://confess-report.onrender.com

> To see the profanity score for a text, add /api?query={your_text} to the base url. 


<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
```
$ Clone the project.
$ Open it in Visual Studio Code or any of your favorite IDE. 
$ Open a terminal and type:- flask run or python app.py
```


## Usage
- Add /api?query={your_text} to the base url, and click enter. 


## Project Status
Project is: _completed_.



## Contact
Created by [@superiorsd10](https://github.com/superiorsd10)   
Email:- [Sachin Dapkara](mailto:sachindapkara6@gmail.com) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
