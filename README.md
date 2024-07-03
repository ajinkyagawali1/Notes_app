
## Notes App

It's a web-based platform for students and teachers alike to create a repository of academic material for different Engineering streams.


## Installation

1. Clone the repository in your local machine

```cmd
  git clone https://github.com/ajinkyagawali1/Notes_app.git
 ```
2. Go to the Notes_app folder
    
```cmd
  cd Notes_app
 ```
3. Install all the required Python packages with

 ```cmd
    pip install -r requirements.txt
 ```
4. Edit the ".env" file to include your Email, Password and Secret Key.

5. Set the environment variable for FLASK_APP

 Linux 

 ```cmd
    export FLASK_APP=run.py
 ``` 

 Windows

  ```cmd
    set FLASK_APP=run.py
 ```
6. To run the app 

 ```cmd
    flask run
 ```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MAIL_USERNAME`

`MAIL_PASSWORD`

`SECRET_KEY`     

