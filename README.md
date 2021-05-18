# hemontika-web

## Goals of the project
This is the Web Application for hemontika. Hemontika is a website where author can write their own poems, stories, novels, plays, paintings, recitation (and many more) in multiple languages. We are working to make the UI of this application like the printed books. So that readers while reading can feel as if they are reading on a printed book.

# Run in a local machine
To install in a local machine, you have to first fork it. After that, clone it to your local machine using git.
<pre>
git clone https://github.com/{your-username}/hemontika-web.git
</pre>

Now there are two options to run the application on your local machine - with docker and without docker

## With docker
It is the easiest and the recommended method to run the application. 

### Pre-Requistics - 
1. you have installed docker and docker-compose (installing docker desktop will install both tools)
2. For windows, you have your wsl enabled.

### Procedure - 
Open your terminal and type <code> sudo docker-compose up </code>. That's it! You will see that thr server is started running after a few time. Now open your browser and go to 127.0.0.1:8000/ . The application is now running on your local machine!

## Without docker - 
This procedure is little bit complex compare to the previous one and can produce "works on my computer" type errors. So be ready to solve those.
As this is a django + React app, you have to install python dependencies as well as npm dependencies. So let's start - 
### creating a virtual enviornment
You have to create a virtual enviornment for your project so that the python dependencies do not create conflicts due to different versions of same package. To create a virtual enviornment run the following commands - 
cd backend_server/
python -c venv venv
This will create a virtual enviornment named "venv". While creating virtual enviornment, make sure you named it as "venv". It will automatically be added to .gitignore file.
### activate the virtual environment
Before running any other command, first activate the virtual environment. The command for activaing the venv is different across different OS. For windows, run "venv/Scripts/activate" on the terminal, "source venv/bin/activate" for the rest of others. 
### install python dependencies 
Run the following command to install all python package requirements - python install -r requirements.txt .
### install npm dependencies 
Now if everything look fine, change your current directory from backend_server to frontend - cd ../frontend. Now run npm install. It will install all the npm dependencies for the application. 
### Run the server
Now if all look great, change your current working directory to backend_server/src. Run python manage.py runserver and wait till the server starts. Now go to 127.0.0.1:8000/. You will see the application running locally!

# Contribution
Contributions are welcome. Feel free to create issues as well as PRs to make this application better! Please maintain the template for issues and PRs while creating them. To know more, see our Code_of_Conduct.md. 

# Tests
You mainly prefer test driven development. So before adding any new code, try to write tests first. Then do changes until the tests pass. This makes our project less buggy.
Before commiting any changes make sure it passes all the tests. Go to backend_server/src on your terminal and run the command - pytest
If all tests are passing, then you are good to go! 