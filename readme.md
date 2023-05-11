# Django: Contact App

I have made a simple contact app using Django and Htmx. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django.

### Pipenv
I first created a pipenv environment. 
You can skip this section if you already installed Django or virtual env in your system
```bash
pip install pipenv
```
After installing the pip env file, go to the application root directory and run
```bash
pipenv install
```
To activate your pipenv environment, simply run 
```bash
pipenv shell
```
After activating the pipenv environment now run
```bash
python3 manage.py runserver
```
### Using requirement.txt

Another way to install the dependency and run the application is to use a requirement Txt file. just go to the root of the application and run the following command

```bash
pip install -r requirements.txt
```
after installing all the dependencies run the below command to start the application

```bash
python3 manage.py runserver
```
### Port and URL

go to this link to see the running application **localhost:8000/contacts/**

## gif
![Django contact app Demo](/demo/output.png)

## License

[MIT](https://choosealicense.com/licenses/mit/)