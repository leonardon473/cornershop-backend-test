## cornershop-backend-test

### Running the development environment

* `make up`
* `dev up`

##### Rebuilding the base Docker image

* `make rebuild`

##### Resetting the local database

* `make reset`

### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000


### About building local environment with Linux systems

If you bring up the local environment in a linux system, maybe you can get some problems about users permissions when working with Docker.
So we give you a little procedure to avoid problems with users permissions structure in Linux.:

1- Delete containers

```
# or docker rm -f $(docker ps -aq) if you don't use docker beyond the test
make down
```

2- Give permissions to your system users to use Docker

```
## Where ${USER} is your current user
sudo usermod -aG docker ${USER}
```

3- Confirm current user is in docker group

```
## If you don't see docker in the list, then you possibly need to log off and log in again in your computer.
id -nG
```


4-  Get the current user id

```
## Commonly your user id number is near to 1000
id -u
```

5- Replace user id in Dockerfiles by your current user id

Edit `.docker/Dockerfile_base` and replace 1337 by your user id.

6- Rebuild the local environment

```
make rebuild
make up
```

## .env
When set the variable BACKEND_HOST start the host with http:// o https://
to see correctly the menu link in slack.

## Concerts
- The time zone used in this project is Chile/Continental that is equal to
  UTC-4 but in summer UTC-3 is in use.

## Possible improvements
- The id field in the model MenuOfTheDay can be changed by date field
  as PK if you believe it is better.
- Pagination can be added in the future for menus of the day list.
- Improve the display of error messages in the menus admin.
- Disable menu selection changes can be implemented.
- Pytest fixtures aren't used to have type hint in the tests.
- The admin use is_staff User field to allow menus changes, this can be
  changed to use django table "auth_group_permissions".
- The function to get slack can be improved by use pagination.
- Composed keys can be used to improve DB design.
- Limit time to order a food dish should be edited from the db.
- Error management in send_menu_of_the_day_to_employees can be improved.
- A flag of sent can be added to EmployeeMenuSelection.
- Celery beat database should be changed to Django db instead of the file db.
