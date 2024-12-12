Pour faire tourner ce TP, beaucoup de librairies sont indispensable, notamment la robotics-toolbox de P. Corke (P.I. Corke : https://github.com/petercorke/robotics-toolbox-python/wiki). Afin de bénéficier de tout ce qu'il faut pour travailler. 

- Installer Docker.

- Aller dans le dossier docker_install et vérifier bien la présence d'un dossier volume\_tp.

- Ecrire :

    sudo docker pull waelbachta/ubuntu_ssh_labs:latest

Cela vous permet de télécharger une image du docker prêt à l'emploi. Vous allez devoir utiliser votre mot de passe personnel.

    sudo docker build -t waelbachta/ubuntu_ssh_labs:latest .

 Cela vous permettra de créer un contenaire basé sur l'image téléchargée.


 	sudo docker run -d --rm --volume="./volume_tp:/home/" -p 220:22 waelbachta/ubuntu_ssh_labs:latest

Cela vous permet de lancer le contenaire qui établit une connexion ssh sur le port 220

- Connectez-vous avec un ssh X à votre contenaire en écrivant :
     ```
    ssh -X -p 220 root@localhost
 	```
 Vous aurez à saisir le mot de passe du contenaire qui est root123

 - Aller dans /home et vérifier qu'il correspond bien à volume\_tp.

 - Vous pouvez ainsi modifier le code sur votre ordinateur personnel et et l'interpréter sur le contenaire.