Award
#### Author: [Rubyroy12](https://github.com/Rubyroy12) : 
## Description

As a user of the web application you will be able to:
1. user authentication user registration and login.
2. User can create and posta  blog
3. Ability to comment to the created Blogs
4. writers can delete and update blogs


## Setup and installations
* Clone Projec to your machine
* Create a virtual environment uising `python3 -m venv venv`
* Activate a virtual environment on terminal: `source venv/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3 manage.py runserver`
* Access the live site using the local host provided
  
## Specifications
1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

### Prerequisites
* python3
* virtual environment
* pip
#### Clone the Repo and rename it to suit your needs.
bash
git clone https://github.com/Rubyroy12/instacom.git


#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
#### Make and run migrations
bash
- python3 manage.py check
- python3 manage.py makemigrations instagram 
- python3 manage.py migrate

#### Run the app
bash
python3 manage.py runserver

Open [localhost:5000](http://127.0.0.1:5000)
## Testing the Application
`python3.9 manager.py test`
## Built With
* [Python3.9](https://docs.python.org/3/)
* Django
* Boostrap
* HTML
* CSS
* git

### Licence
This project is under the  [MIT](LICENSE.md) licence