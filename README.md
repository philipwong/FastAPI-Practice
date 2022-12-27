# FastAPI-Practice

It was inspired by a youtube - JVP Design

https://www.youtube.com/playlist?list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p

I strongly encourage you take a look on this tutorial, share it out. It is really good practice and learning material for FastAPI.

--------

## FastAPI related
![image](https://user-images.githubusercontent.com/9277122/209690901-9aa1dc44-6925-4178-b506-e749e9986205.png)
	1. Setup the virtual environment
		a. python3 -m venv .env	Install the virtual environment
		. .env/bin/activate	Activate the virtual environment
	2. Setup requirements.txt
		a. Create	Create file for python package installation
		
		Requirements.txt
		Insert	Insert the necessary package in it. Possibly include the version number in the package to avoid potential version issue.
		
		fastapi
		uvicorn
		Run	Install the necessary packages for the project
		
		pip install -r requirements.txt
    
	3. Setup git ignore file
		a. Create file ".gitignore"	Create the git ignore file
		Insert:	It is important to setup the git ignore file so that it can prevent uploaded sensitive and excessive files to git
		
		config.ini
		.env/
		First commit:	Setup the first init into the git repository
		Run
		
		git init
	4. Init the FastAPI route
		a. Init the FastAPI function call	This is the hello world program
			
			Reminder: the return use { }
		from fastapi import FastAPI
		
		app = FastAPI()
		
		@app.get("/")
		async def root():
		    return{"Hello World"}
		
		To run the FastAPI	Start the FastAPI / Uvicorn web server
			
		Run	The parameter --reload will able to auto detect each change of the main route, and it will auto refresh the uvicorn instead of kill it and restart it every time. It is good for development environment.
			
		uvicorn main:app --reload --no-server-header	the

