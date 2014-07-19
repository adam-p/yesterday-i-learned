## Terms

* **Docker Engine**: consists of two parts: a daemon, a *server* process that manages all the *containers*, and a *client*, which acts as a remote control for the daemon.
* **Container**: Process in a box. The box contains everything the process needs to run, including the filesystem, shell, and libraries. They are not enabled by default.
* **Commit**: Save changes made to the container.

* Docker has pre-built images; run `docker search (name)` to find them, and `docker pull (user)/(name)` get them.
* To run something in a container, run `docker run (user)/(name) (command)`.
* To install something in a container, run `docker run (user)/(name) apt-get install -y ...`. The `-y` is required because docker commands cannot be interactive.
* To view a list of commands run in the container, run `docker ps -l`. It shows you IDs of states after the commands are run.
* To *commit* a container, run `docker commit (id from above) (new container name e.g. foo/bar)`. Now you can `docker run foo/bar`.
* To inspect a container, run `docker inspect (id from above)`.
* If you sign up for a Docker account, you can push your own images onto the repository using `docker push (container name e.g. foo/bar)`.