
# Objectifs de la séance
Lors de cette séance, vous implémenterez une loi de commande cinématique qui permet à l'organe terminal d'un robot d'atteindre une attitude désirée. Vous considérerez que vous disposez des modèles géométrique et cinématique du robot. Vous ferez également l'hypothèse que les boucles de contrôle locales en vitesse possèdent une bande passante très supérieure à celle de la tâche opérationnelle à accomplir.

# Environnement de travail
Le travail se fera en simulation au sein d'un environnement de développement Python et avec l'aide de la libraire Robotics Toolbox développée par Peter Corke\footnote{P.I. Corke : https://github.com/petercorke/robotics-toolbox-python/wiki}. \\

Vous vous intéresserez plus particulièrement, et sans perte de généralité, au robot UR3 à 6 degrés de liberté, et nous mettrons en \oe uvre une loi de commande basée sur la représentation axe angle de l'erreur de l'orientation. Les axes de l'UR3 sont asservis en vitesse. Au vu de l'hypothèse énoncée plus haut, vous considérerez que les entrées de commande articulaire seront directement égales aux vitesses articulaires. 
# Travail à effectuer

## # Travail préliminaire de modélisation

De façon générale, toute rotation d'un angle $\theta$ autour d'un vecteur unitaire $u = [u_x\,\,u_y\,\,u_z]^{'}$ admet une matrice de rotation de la forme suivante :

\begin{align*}
\rm{R(}\theta,u\rm{)}
& = \begin{pmatrix}
u_x^2(1-\cos(\theta) )+ \cos(\theta) & u_x u_y(1-\cos(\theta) )-u_z\sin(\theta) & u_x u_z (1-\cos(\theta))+u_y \sin(\theta) \\
u_x u_y (1-\cos(\theta) )+u_z \sin(\theta) & u_y^2(1-\cos(\theta) )+\cos(\theta) & u_y u_z (1-\cos(\theta))-u_x \sin(\theta) \\
u_x u_z (1-\cos(\theta) )-u_y \sin(\theta) & u_y u_z(1-\cos(\theta) )+u_x\sin(\theta) & u_z^2  (1-\cos(\theta)) + \cos(\theta)\\
\end{pmatrix}\\
& = \cos(\theta) \mathbb{I}_3 + \sin(\theta)\rm{AS}(u) + (1-\cos(\theta)) uu'\\
\end{align*}

Dans le cours nous avons vu que ($\theta,u$) peuvent être obtenus à partir de la matrice de rotation de la sorte :\\

\begin{equation}
\label{eq:axe_angle}
(\theta, u)=\,\left\{
    \begin{array}{lll}
                 \theta = \arccos \big(  \dfrac{r_{11}+r_{22}+r_{33}-1}{2} \big) \\
                 $ $\\
                 {\bf u} = \frac{1}{2\sin(\theta)}\begin{pmatrix}
			    r_{32} - r_{23} \\
			r_{13} - r_{31} \\
			r_{21} - r_{12}	
			    \end{pmatrix}
                \end{array}
 \right. \text{ ou encore } \theta {\bf u} = \frac{\theta}{2 \text{sin}(\theta)} \underbrace{\begin{pmatrix}
			    r_{32} - r_{23} \\
			r_{13} - r_{31} \\
			r_{21} - r_{12}	
			    \end{pmatrix}}_{l}
\end{equation}\\

Comme vous pouvez le voir, la représentation axe/angle admet des singularités pour $\theta = k \pi$

1. \item Etablissez la relation entre la trace de la matrice de rotation $\rm{R(}\theta,u\rm{)}$ et $\cos(\theta)$

2. \item Montrer que la norme de $l$ est égale à $2\sin(\theta)$

3. \item Calculez successivement la matrice de rotation $\rm{R}$  pour $\theta=0$ et $\theta=\pi$ qui correspondent à un facteur près aux angles de singularité de la représentation axe/angle

4. \item Ajouter la matrice identité à la matrice ${\rm{R}}(\theta,u)$. Constituer un vecteur à partir des éléments diagonaux et diviser le par 2. Donner le vecteur obtenu.

5. \item Proposez une méthode basée sur la matrice de rotation ${\rm{R}}(\pi,u)$ afin de trouver les signes des composants de $u$

6. \item Calculez les traces de la matrice  $\rm{R(}\theta,u\rm{)}$ et $\cos(\theta)$ pour $\theta = 0$ et $\theta=\pi$. Donnez à chaque fois le signe de la trace

7. \item  Comme $\theta=0$ et $\theta=\pi$ sont des singularités pour la représentation axe/angle. Proposez des solutions qui permettent de les contourner.

## # Etude de la stabilité numérique

Lors de l'implémentation d'une loi de commande basée sur le paramétrage axe/angle, vous commencerez par le calcul de la matrice de rotation qui correspond à l'erreur avant d'en extraire l'axe et l'angle.\\



1. Dans cette partie, vous allez procéder à l'envers :  le script « part\_1.py » vous donne la possibilité de définir un vecteur de rotation, qui sera normalisé ainsi qu'un angle de rotation. 


* Commencez par lire le code et complétez-le.
* Modifier la valeur de l'angle en gardant une rotation autour d'un angle différent de $k\pi$ et vérifier la cohérence des résultats avec la préparation
* Saisir à tour de rôle $\theta=0$ et ensuite $\theta=\pi$. Commentez.


2. Ouvrez maintenant le script "part\_2.py". Comme dans le script précédent, vous allez pouvoir définir un axe de rotation unitaire. Le code conduit ensuite une comparaison d'un angle $\theta$ qui varie dans $]-\pi,\pi[$ avec son estimation en utilisant l'arc-cosinus telle qu'exprimée dans l'équation~\eqref{eq:axe_angle} et l'arc-tangente 2. 


* Commencez par lire le code et complétez-le en fonction des résultats obtenus plus haut
* Ajouter $10^{-4}$ à la variable arg et observez les commentaires générés lors de l'interprétation du script.


3.  Vous allez maintenant distinguer le cas $\theta=0$ de celui de $\theta=k\pi$

* D'après votre préparation, quel critère permet de distinguer les 2 cas ?
* Nous allons maintenant, mettre en oeuvre le choix des signes des différents éléments de $l$. Pour cela ouvrez le script "part\_3.py" qui servira de test à la fonction "determine\_signs(R)" présente dans "commande.py" : ouvrez également ce fichier et complétez la fonction en question et procéder ensuite aux tests.

## # Commande opérationnelle
Vous allez maintenant vous attaquer à la commande opérationnelle à proprement parler. Pour cela ouvrez les scripts "tp\_main.py" et "commande.py".


1.  Commencez par lire le code de "tp\_main.py" afin d'en saisir la structure.
2.  Lisez le code contenu dans "commande.py" pour le comprendre et le compléter
3.  Dès que la loi de commande donne des résultats satisfaisants, testez les cas de singularité




