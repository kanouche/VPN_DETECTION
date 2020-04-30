# VPN DETECTION PROJECT USING DEEP LEARNING

## Introduction

VPN DETECTION is a project with the purpose to implement a deep learning model and analyze multiple classification models in order to detect VPN usage on a computer network. The project started with a literature review on the subject to gather as much information on the subject to help with the next phases, refer to [wiki-literature review](
https://github.com/kanouche/VPN_DETECTION/wiki/Literature-Review). 
At the start of this project, proper data mining techniques will be utilized to collect the appropriate data. For this project, we used the VPN-nonVPN dataset from the University of New Brunswick, [VPN-nonVPN dataset](https://www.unb.ca/cic/datasets/vpn.html). Then, the collected data was prepared, preprocessed, and discretized for ease of classification. Finally, using keras libraries, we generate different classification models and results will be analyzed. This project has an aim to deliver a trained machine learning program with a minimum of 95% certainty of vpn detection in a network. 


## Tools and Librairies

Python 3.6

Librairies:
   - pandas  
   - keras 
   - sklearn 
   - tensorflow

Technologies:
   - [Netflowmeter](https://netflowmeter.ca)
   - [IPinfo](https://ipinfo.io/)

## Data preprocessing & Exploration

for our clean data set, we added removed unwanted columns and added new ones for ports type, latitude and longitude. For port type, please refer to [Data preprocessing](https://github.com/kanouche/VPN_DETECTION/wiki/Planning). Latitude and longitude were generated using IPinfo, code is at **location.py** file, and ports were processed in the file **ports.py**.

## Feature Engineerring
For this project, we agreed on developing the two main following features:

     - Connection-based features : The window here is X number of connections preceding the current netflow.
           
     - Time-based features : The window here is X minutes (or seconds) preceding the current netflow timestamp. 
     
     Refer to Sprint 7 in [Sprints and Planning](https://github.com/kanouche/VPN_DETECTION/wiki/Sprints-and-Planning)
            
