1)Save soundmanage folder in the cloud(STaaS/NFS) server.
2)Mount this folder on your VM(which contains docker) on your desktop under the name "music"
3)Start docker service
4)(Just in case)Shut firewall as well as SELinux
5)Pull docker image: docker pull jakshatdesai/emofinal and rename it to emofinal:v5.