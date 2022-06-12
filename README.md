# machine_learning_project
My first Machine Learning Project


Creating conda environment
```
conda create -p venv python==3.7 -y
```

Activating venv
```
conda activate venv/
```

To add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
```commandline
To check all version maintained by git: git log
```

To create version/commit all changes by git
```commandline
git commit -m message
```

To send version/changes to github
```commandline
git push origin main
```

To check remote url
```commandline
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = mobosomto@gmail.com
2. HEROKU_API_KEY = 471dc9f0-5cd3-4ba0-81f9-73c0c66790cf
3. HEROKU_APP_NAME = ml-reg-project

BUILD DOCKER IMAGE
```commandline
docker biuid -t <image_name>:<tagname> .
```

> Note: Image name for docker must be lowercase

To list docker image
```commandline
docker images
```

To run docker image
```commandline
docker run -p 5000:5000 -e PORT=5000
```

To check running container in docker
```commandline
docker ps
```

To stop docker container
```commandline
docker stop <container_id>
```