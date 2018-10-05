<img src="https://raw.githubusercontent.com/dkwok94/AdventureUs_v1/master/app/static/icons/logo2.png" height="105" width="95">

# AdventureUs 

## Application
The goal of AdventureUs is to provide users with a solution to easily finding groups of people to travel with. It is a social network of sorts for travelers who are looking to make new friends.

## Installation
1. Clone the repository from GitHub
2. Run the `setup` script to install the environment.
3. The setup script will install Python virtual environment and install all modules and libraries on this virtual library so they can be easily removed.
4. After the setup script completes, run `sudo python3 -m app.adventureus` and it will be running on `0.0.0.0:5000` per Flask

## Technologies Used
* Ubuntu 14.04
* Python 3.4.3
* Flask 1.0.2
* Bootstrap 3.3.7
* MongoDB 4.0.2
* JQuery 3.3.1
* HTML
* CSS
* Javascript

### Tech Stack
<img src="https://raw.githubusercontent.com/dkwok94/AdventureUs_v1/master/tech_stack.PNG">

### MVP Flowchart
<img src="https://raw.githubusercontent.com/dkwok94/AdventureUs_v1/master/mvp_flowchart.PNG">

## Features
* User can login and logout of an account
* User can view their personal profile and see their hosted and other active trips
* User can host their own trip and select a city, country, date range, and description
* Other users can view the active trips and join them, which will send a request to the host
* User can view notifications that they have sent and received
* User can approve or reject other users' trip requests
* Hosts can delete any trip they have created
* All trips and notifications load dynamically in modals - trip modals contain all trip information and profile pictures of all users that are currently approved to go on that trip.

## Author
Derek Kwok [@dlangshk](https://twitter.com/dlangshk)
