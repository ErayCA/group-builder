# GroupBuilder API
This repository holds the code for the Python (Flask) backend for the GroupBuilder application. For more information on running this on your local machine please refer to the [Development](#Development) section.  

# Development

## Folder Structure
The python source code for this application is contained within the `/src` folder. The main entrypoint is the `/src/main.py` script. The `/src/wsgi.py` script is used as the entrypoint in the container environment. The code for each of the API routes is contained in folders within the `/src` folder. Currently, they are:
 * `affinity` - API for managing affinities
 * `auth` - API for registering users
 * `cohort` - API for managing cohorts
 * `confirmation` - API for managing confirmations 
 * `group` - API for managing groups
 * `groupmember` - API for managing groupmembers 
 * `like` - API for managing likes
 * `link` - API for managing links
 * `liveliness` - returns liveliness information about the application
 * `module` - API for managing modules
 * `modulemember` - API for managing modulemembers 
 * `project` - API for managing projects
 * `user` - API for managing users
 
All the `SQLAlchemy` models for the application database are contained within the `models` file in `/src/models`. 

## MySQL Database
Developing the application requires a `MySQL` database connection - the default development location is set to `localhost:3306` and authentication is `user:user` (username:password). A suitable `MySQL` database can be brought up by running:
```
$ docker-compose up
```
It should be noted that this would also bring up a locally built version of the application API on `localhost:8080` and an instance of `PHPMyAdmin` on `localhost:8183` - you can manage the database from `PHPMyAdmin` by logging into `mysql` using `user` as a username and `user` as a password. 

## Testing changes
When making changes to the code, you can see them take effect without having to restart the API server. To run the API server, navigate into `src/` and run: 
```
$ python main.py
```
This will start the application server, which will be available on `localhost:8000`.

# Deployment
The Docker container for this application can be built by running:
```
$ docker build .
```
This will build a Docker container with the application available on port `8080`.