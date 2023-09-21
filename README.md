![fastfest-removebg-preview](https://github.com/mdhifta/api-services-fastapi/assets/55729354/c0b9bf56-efb1-4f78-b4bc-6e10a37534ce)
# FastFest Template API
FastFest template is a clean structur for FastAPI. I made it with a simple concept and basic structure such as schema, models, api, core and utils.

# How to Run?
* First, you have to install the package in requirements.txt
> pip install -r requirements.txt

* Second, you have to make sure you have created an .env file
> just rename the env-example file to .env

* Then just run FastFest
> python3 main.py or python main.py


# Details FastFest

_Api Folder_
- Api is used to include all the new logic and routes you want to add. for example, for example, I want to create a flow register, so just create authentication.py in the api and create the appropriate logic for the register.

_Core Folder_
- Core is used to put the core of the system requirements, I put the database configuration here which can be changed and set directly in .env

_Crud Folder_
- Crud is used to provide interactions in the database, as the name suggests it is used to create, read, update and delete.

_Models Folder_
- Models are used to set data formats according to the fields and tables in the database

_Schema Folder_
- Schema is used to provide validation of api data, whether for response or other needs.

_Utils Folder_
- Utils are used to provide simple logic that can be used to support multiple flows over and over again.

_App.py_
- All interactions and adding route URLs or Swegger can be edited in app -> app.py
