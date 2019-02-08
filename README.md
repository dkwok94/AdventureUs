<img src="https://raw.githubusercontent.com/dkwok94/AdventureUs_v1/master/app/static/icons/logo2.png" height="105" width="95">

# AdventureUs 
Application can be accessed here: https://adventureusapp-v1.herokuapp.com/

Login with any of the following users while registration functionality is being implemented:

```
username: derekkwok
password: password

username: spiderman
password: newyork
```

## Application
The goal of this iteration of the application was to show a proof of concept (MVP) and design a mechanism by which multiple users could join groups together. The goal of AdventureUs as a whole is to provide users with a solution to easily find groups of people to travel with. It is a social network of sorts for travelers who are looking to make new friends. This is an MVP written in about 2 weeks as a personal project for learning that implements the trip creation, group joining, and notification sending/approval functionalities. Thus, it is far from finished and I plan to add more functionality to it in the future. The application will be updated at a later time, as well as more functionality like registration, friends, chat messaging, booking tickets, etc!

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

### Application Overview
For those that do not have time to explore the Heroku app, here is a brief overview of a typical user story that involves creating a trip and having another user join that trip.
  
The user is first greeted with a login screen where they can type their username and password into the box.
  
<img src="https://drive.google.com/uc?id=1gAciU2wYddq2TvcDaUKeu_fM2YrjXDoM"/>
  
The user profile is displayed on login. It contains a description, a list of destinations that the user wants to travel to, and the languages that the user knows. Additionally, there are two panels on the side: one for trips that the user is hosting, and one for the trips that user has joined. The top navbar consists of profile, notifications, and a global view of all hosted trips on the site.
  
<img src="https://drive.google.com/uc?id=1RNEN6pWDoXPTonSQ96GdLFRomNhAcBKZ"/>
  
If the user clicks the "Host Trip" button on the top right corner, a modal pops up where the user can input information about the trip they wish to host. I want to go to Paris, France between 2/8/19 - 2/22/19. After the trip is created, it shows up in the global list of trips and is now visible in the "Hosted Trips" panel on the user's profile.
  
<img src="https://drive.google.com/uc?id=1fQEyet8DUdz8qmjNXqYpuN2BNHAgsVpw"/>
<img src="https://drive.google.com/uc?id=1-33hk7LOFTm_La5MZCZMZAH1MdVxT1sx"/>
<img src="https://drive.google.com/uc?id=1hEB_6ZnM8qDwI7euh0zLYK_Nw7SrJjH1"/>
  
If the user clicks on the trip, the trip information is displayed in a modal with only that user as the current attendant of the trip.
  
<img src="https://drive.google.com/uc?id=1tYumls5HbwcXIUIgIvfA8rDxLBngrPfN"/>
  
If another user logs into their account, they will be greeted with their respective profile screen as shown below.
  
<img src="https://drive.google.com/uc?id=1PEUOXBDSihKdwSwobnN4Gnn_EZXY49Us"/>
  
Going to the global trips tab in the navigation bar, they will see the trip that I originally posted. They can send a request to join the trip. If they look in their notifications tab, they will see that notification they just sent under "Sent Requests".
  
<img src="https://drive.google.com/uc?id=1nU2ySmf46VyX8K1xxlN34K4Sikl6L_mV"/>
<img src="https://drive.google.com/uc?id=1lqz3LXHLdppSTooowoUPnKhSwO__71LV"/>
  
When I log back into my account and go to my notifications tab, I will see the request in "Received Requests". When I open it, I can choose to either accept or reject the request.
  
<img src="https://drive.google.com/uc?id=1C3nZElqh6tmmbornlUqo4HNqIZinlyk1"/>
<img src="https://drive.google.com/uc?id=1QNhDSjUYIYgs2PCKVNHfIj5AnqQt11sH"/>
  
Assuming I accept the request, the user is added to my trip. In the trip information, his/her picture will be added to the group roster. Additionally, the trip will appear on his/her profile in "Other Adventures". The request is deleted from the database.
  
<img src="https://drive.google.com/uc?id=1ThVTBf4j3FEM8uHDIUnJl79bjQGYZjgZ"/>
<img src="https://drive.google.com/uc?id=1190Wf7a19JYruy84_qFH8iXA5KgXeCpS"/>
  
If I instead rejected the request, the user's request is deleted from the database and they are not added to the trip roster.

## Features
* User can login and logout of an account
* User can view their personal profile and see their hosted and other active trips
* User can host their own trip and select a city, country, date range, and description
* Other users can view the active trips and join them, which will send a request to the host
* User can view notifications that they have sent and received
* User can approve or reject other users' trip requests
* Hosts can delete any trip they have created
* All trips and notifications load dynamically in modals - trip modals contain all trip information and profile pictures of all users that are currently approved to go on that trip.

## Future Improvements
* I have not added registration functionality to the application. That is first on my list of things to add.
* I plan to implement a user dashboard so that users can see friend updates, view pictures of trip experiences, post statuses and discussions, etc.
* I plan to add a multi-person messaging system, the ability to book tickets from the app, and a friends system as well.
* Modals are probably not the best way to display trip information. I should treat this like a typical social network and just open a new page when loading trip information. There is only so much you can fit on a modal anyways, and given the nature of this product, good communication about trip logistics requires way more space.
* The user inputs are not restricted. The users can enter anything they want. If I wanted each trip posting to be more standardized, I would put several fields to add more specificity to the information they can enter and how each posting will look.
* The countries menu is not organized by alphabetical order.
* Opening user profiles results in a new tab being opened on the browser. This is not very efficient as a user can easily end up with 10 tabs open just for viewing 10 different users. I would make it so that the user profiles are opened up on the current page and the user just has to press "back" if they want to go back to the trip information. This is also another reason why the trip information should be displayed in its own page so that the modal does not have to keep being opened just to see information.
* The organization of the "Hosted Trips" and "Other Trips" panels in the user profile can clutter the profile page, especially if the user travels a lot and has several trips on the panel. The app might benefit from a separate "My Trips" tab in the navigation bar so that only the user has access to the trips they are going on, and other users cannot see this information.
* I have not implemented an "Edit Profile" or "Add Friend" feature to the app yet. 

### Tech Stack
<img src="https://raw.githubusercontent.com/dkwok94/AdventureUs_v1/master/tech_stack.PNG">

### MVP Flowchart
<img src="https://raw.githubusercontent.com/dkwok94/AdventureUs_v1/master/mvp_flowchart.PNG">

## Installation
If you want to interact with the code, here are the steps to get the app installed on your system:
  
1. Clone the repository from GitHub
2. `cd` into `AdventureUs_v1` directory. Run the `setup` script to install the environment. In Linux, you can do this with `./setup`
3. The setup script will install Python virtual environment and install all modules and libraries on this virtual library so they can be easily removed.
4. After the setup script completes, type `source env/bin/activate` to boot into the virual environment.
5. Run `pip3 install -r requirements.txt` to install all packages into the virtual environment.
6. Run `python3 -m app.adventureus` and it will be running on `0.0.0.0:5000` per Flask.
7. You can log into any of the users listed in the `example_users` file.

## Author
Derek Kwok [@dlangshk](https://twitter.com/dlangshk)
