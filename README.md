# [Grant_py](https://grantpy254.herokuapp.com/)

This project was generated with [Django](https://www.djangoproject.com) version 2.2.8 <br>

![picture](grant_py.png)

To view the site Click [Grant_py](https://grantpy254.herokuapp.com/)

## Author: 
  * [Peter Mirithu](https://github.com/petermirithu/Grant_py)

#### Authors' information
*Peter Mirithu*
    Email: pyra_m.k@yahoo.com <br>
    Address: 1394 <br>
    Software Developer.<br>
    Telephone N.O: 0790476167          
## Description
  The app goes by the name Grant_py. Its an awards app giving users a chance to post projects and their live link for them to be rated and reviewed. The winner project gets to be displayed on the home page.

## Specifications
  * Behaviours
  ```
  Displays the landing page                     ~ When the app loads on startup.

  Display sign in page                          ~ When the sign in button is clicked.

  Displays sign up page                         ~When the sign up is clicked.

  Displays profile page                         ~When one logs in automatically and when profile button is clicked.

  Displays a form to update profile             ~When one clicks the update profile button.

  Displays a form to post a new project         ~When one click the +post button.

  Displays a single project with more details   ~When one click on any landing page for a project.
   
  Displays single project with reviews          ~when one clicks the rate button on the landing page.

  Displays a user profile.                      ~when one clicks on a user profile pic or name.
  
  Displays the rate form.                       ~when one clicks the rate button on the single page with 1 project.

  Adds a user rating.                           ~when a user submits the rate form with data.

  Adds reviews to a post.                       ~when a user submits the review form with data

  Displays the search form.                     ~when one clicks the search icon.

  Display all profiles in Json Format           ~When one add this path "/api/profiles/" after the sites home page url.

  Display all projects in Json Format           ~When one add this path "/api/projects/" after the sites home page url.

  Logs out a user.                              ~when the sign out button is clicked
  ```

## Setup Requirements
  Here's a brief introduction on what a developer must do in order to start running the app locally:

  ```
  $ git clone https://github.com/petermirithu/Grant_py
  $ cd Grant_py/
  ```
  * create a virtual environment
  * Activate the virtual environment
  * create your own database
  * add configurations for the database in the project settings file
  * Update .env file with you configurations.
  
  ```
  $ pip install -r requirements.txt
  $ chmod a+x start.sh
  $ ./start.sh
  ```
  <hr>
  To run tests:

  ```
  $ python3.6 manage.py test awards
  ```
  <hr>
     
## Technologies Used
  This project was generated with:
  * [Python](https://www.python.org/) version 3.8.0. 
  * [Django](https://www.djangoproject.com/) version 2.2.8
  * Bootstrap4.  
  * CSS3
  * PSQL database.  
  * Upload Care.
  * Heroku.

 ## Support and contact details
  Incase of a problem, issue or need more clarification, feel free to send an email<br> @ pyra_m.k@yahoo.com<br>
  Contact Pyra at : 0790476167

 ## License
  This project is licensed by [MIT License](LICENSE.txt)<br>
                Copyright (c) <br>
                [Peter Mirithu](https://github.com/petermirithu/Grant_py) <br>
                  2019<br>
  
  




