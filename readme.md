# Template for Django (dev and production)

###
## Source tutorial:
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

## How to use (reminder to myself):
1. Clone this repository to my PC
2. Spin the dev containers 
    ```
    docker-compose up -d --build
    ```
3. Develop stuff (hard part). Comment out flushing and migration in .sh file as needed
4. Take the dev containers down
    ```
    docker-compose down -v
    ```
5. Spin the production containers
    ```
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
    ```

6. If it works, clone the finished repo to remote server
7. Copy the production env file 
8. Bring production containers back to life again

## Goal for a future Django Project:<br>
Elonjet Twitter account (not Elon Musk, but a much more evil person)