# EmoShuffle
EmoShuffle is an application which plays songs as per the user's emotions detected from his/her voice. Songs are stored on a cloud server from where user devices can access the interface of vlc playing inside a personalized docker container( Each user has a separate docker container. Hence every user can play a different song on their own docker on the same server.). The project uses Docker, Ansible, Python, NFS, SSH, Vokaturi, etc.
In the current version of the app, the application is run on windows while the server is on RHEL7.
