1 - Fibo -
En parallélisant, gain d'environ 5,5

2 - Schedule -

-En parallelisant : Resultat inchangé 
-Pour répartir sur 50 pixels, on rajouter schedule(static, 50)
-Pour obtenir les bandes horizontales, on parcours sequentiellement la largeur en parallélisant la hauteur.

3 - Random -
-En parallelisant : Resultat inchangé, gain de seulement 2 (gain acceptable à 4 + 30%). 
-Pourquoi ? Dans la deuxième parallélisation, on utilise toujours la même machine (accès concurrent) et donc certains threads sont bloqués.
-En rendant les variables privées on obtient un gain de 5. Dans la troisième parallélisation, on utilise une machine privée pour chaque thread, ils ne sont pas bloqués mais le résultat n'est pas celui attendu car nous utilisons la même graine.
-Dans la 4ieme parallélisation, la méthode est la même, donc aucune diffèrence au niveau du temps. Resultat OK car diffèrenciation de la graine.

4 - Filter -
-En parallelisant : Resultat inchangé, speed-up de 3.6 (gain acceptable à 4 + 30%).