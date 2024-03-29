# hemontika-web

## Goals of the project
This is the Web Application for hemontika. Hemontika is a website where author can write their own poems, stories, novels, plays, share paintings, recitations (and many more) in multiple languages. We are working to make the UI of this application similar to the printed books. So that readers while reading can feel as if they are reading on a printed book.

# Run in a local machine
To install in a local machine, you have to first fork it. After that, clone it to your local machine using git.
```bash
git clone https://github.com/<your-username>/hemontika.git
```

Now there are two options to run the application on your local machine - with docker and without docker

## With docker
It is the easiest and the recommended method to run the application. 

### Pre-Requistics - 
1. you need to have docker and docker-compose installed(installing docker desktop will install both tools)

### Procedure - 
Open your terminal and type `sudo docker-compose up`. That's it! You will see that the server has started running after some time. Now open your browser and go to `127.0.0.1:8000/` . You will see the backend server is running. The front end part can be seen at `127.0.0.1:3000`.

## Without docker - 
This procedure is little bit complex compared to the previous one and can produce `Works on my computer` type errors. So be ready to solve those.
As this is a django + React app, you have to install python dependencies as well as npm dependencies. So let's start - 
### creating a virtual enviornment
You have to create a virtual enviornment for your project so that the python dependencies do not create conflicts due to different versions of same package. To create a virtual enviornment run the following commands - 
```bash
cd backend_server/
python -m venv venv
```
**Note: The above command is for windows. In linux you have to write `python3` instead of python**
This will create a virtual enviornment named `venv`. While creating virtual enviornment, make sure you named it as `venv`. Git will automatically ignore it.
### activate the virtual environment
Before running any other command, first activate the virtual environment. The command for activaing the `venv` is different across different OS. For windows, run `venv/Scripts/activate` on the terminal, `source venv/bin/activate` for the rest of others. 
### install python dependencies 
Run the following command to install all python package requirements - 
```bash
pip install -r requirements.txt
```
### install npm dependencies 
Now if everything is fine, change your current directory from `backend_server` to `frontend` - `cd ../frontend`. Now run `yarn`. It will install all the npm dependencies for the application.
### Run the front end
Run the `yarn start` command on the terminal and you will be able to see the front end part at `127.0.0.1:3000`.
### Run the server
Now if all are great, change your current working directory to `backend_server/src`. Run `python manage.py runserver` and wait till the server starts. Now go to `127.0.0.1:8000/`. You will see the application running locally!

# Contribution
Contributions are welcome. Feel free to create issues as well as PRs to make this application better! Please maintain the template for issues and PRs while creating them. To know more, see our Code_of_Conduct.md. 

# Tests
We mainly prefer test driven development. So before adding any new code, try to write tests first. Then do changes until the tests pass. This makes our code less buggy.
Before commiting any changes make sure it passes all the tests.
### Running python tests
Go to `backend_server/src` on your terminal and run the command -
```bash
pytest .
```
If all tests are passing, then check if the written code is following our style convention or not. Run `cd ..` and use `python -m flake8 .` and `black --check .` to do this. If any warning or error occur then please solve those. `black .` will help you to automatically resolve some of these errors.
### Running Js tests
Go to `frontend` on your terminal and run `yarn test` or `npm test` to run the javaScript tests.
**Note: Passing flake8 and black checks are necessary to pass the circleci python tests. So make sure all the above tests are passing before opening any PR**
