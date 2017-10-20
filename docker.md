## Terms

* **Docker Engine**: consists of two parts: a daemon, a *server* process that manages all the *containers*, and a *client*, which acts as a remote control for the daemon.
* **Container**: Process in a box. The box contains everything the process needs to run, including the filesystem, shell, and libraries. They are not enabled by default.
* **Commit**: Save changes made to the container.

## Get started

* Docker has pre-built images; run `docker search (name)` to find them, and `docker pull (user)/(name)` get them.
* To run something in a container, run `docker run (user)/(name) (command)`.
* Run ubuntu with `sudo docker run -it ubuntu bash`. See that it is running using `sudo docker ps`. But once you exit from the shell, the container dies; every time you run `sudo docker run -it ubuntu bash`, you get a brand new user in a brand new shell. It would appear that `-i` is interactive, and `-t` is terminal.
* To install something in a container, run `docker run (user)/(name) apt-get install -y ...`. The `-y` is required because docker commands cannot be interactive.
* To view a list of commands run in the container, run `docker ps -l`. It shows you IDs of states after the commands are run.
* To *commit* a container, run `docker commit (id from above) (new container name e.g. foo/bar)`. Now you can `docker run foo/bar`.
* To inspect a container, run `docker inspect (id from above)`.
* If you sign up for a Docker account, you can push your own images onto the repository using `docker push (container name e.g. foo/bar)`.
* The advantage Vagrant has over Docker is: [full isolation](https://www.upguard.com/articles/docker-vs-vagrant). Docker cannot guarantee the virtual hardware that the environment gets.

## [`Dockerfile`](https://docs.docker.com/get-started/part2/#define-a-container-with-a-dockerfile)

`Dockerfile`s are essentially scripts that define what you will install, what the container will run, and what ports the container will expose. Read the damn guide. There is also that [example file](book-summaries/Dockerfile) you can look at. It does not include required files to run the example Flask app.

* In the same directory with `Dockerfile`, running `sudo docker build -t (your container name in all lowercase) .` will build a new container. Check if you actually built one with `docker images`. Note that `python:2.7-slim` is a base container that does not imply ubuntu... in fact [they](https://hub.docker.com/_/python/) are mostly Debian and Windows ones.
* Run `sudo docker run -p 4000:80 (your container name)` to run it. You access the container's port 80 from your own port 4000.
* Alternatively, with `-d`, `sudo docker run -p 4000:80 (your container name)` runs the container in detached mode.
* [There is no difference between `docker ps` and `docker container ls`.](https://stackoverflow.com/a/45254760/1558430) Both list your containers.
