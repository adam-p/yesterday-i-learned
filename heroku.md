# Heroku cheatsheet

Action                  | Command
----------------------- | -------------
Install Heroku          | `sudo apt-get install ruby2.2 ruby2.2-dev`
                        | `wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh`
Create an app           | `cd PROJECT_ROOT && heroku create`
Deploy an app           | `git push heroku master`
View deployed app       | `heroku open`
View app logs           | `heroku logs --tail`
Scaling app up and down | `heroku ps:scale web=0`, `heroku ps:scale web=1`, ...
Files                   | `Procfile`: specifies how to start the app
                        | `Gemfile`: specifies ruby dependencies (`bundle install`)