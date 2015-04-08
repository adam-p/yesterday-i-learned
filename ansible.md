# Setup

* First run `[sudo apt-add-repository ppa:ansible/ansible](http://docs.ansible.com/intro_installation.html) && sudo apt-get update`. The version available to you will then be up to date.

# Configuration

* The [inventory file](http://docs.ansible.com/intro_getting_started.html#your-first-commands), `/etc/ansible/hosts`, list the remote servers you can SSH into.
* For remote machines that don'e support SFTP, [`scp-if-ssh`](http://docs.ansible.com/intro_configuration.html#scp-if-ssh) needs to be True.
