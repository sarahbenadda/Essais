# Mario Kart — 3 circuits (version d’essai)

Cette copie est **indépendante du dépôt GitHub de groupe**. Elle réunit :
- **Jussieu** (facile) : campus, tour Zamansky, circuit extérieur.
- **Paris-Orly** (moyen) : terminal, avions, virages en S.
- **Japon** (difficile) : jardin japonais, temple, pont rouge, torii de départ.

## Sur un ordinateur avec Python et Pygame

1. Décompresser le ZIP.
2. Ouvrir un terminal dans le dossier `Mario_Kart_3_circuits_ESSAI`.
3. Installer Pygame : `python -m pip install pygame`.
4. Lancer : `python main.py`.
5. Entrée : menu de sélection ; haut/bas : choisir un circuit ; Entrée : lancer la course.
6. Pendant la course : **flèches** pour accélérer, freiner et tourner ; Échap : revenir au menu.

Cette version d'essai du code d'origine contrôle **une voiture**. La version finale du groupe devra gérer deux joueurs (ZQSD et flèches).

## Sur iPad avec clavier

Un iPad ne lance pas directement ce projet Pygame ou Godot : `main.py` requiert Python avec Pygame.

Pour découvrir les **trois décors et essayer un déplacement au clavier**, ouvrir `essai_ipad.html` dans un navigateur qui autorise les fichiers HTML locaux, ou héberger le fichier comme une page web. Cet aperçu est **autonome** : les images sont incluses dans le HTML. Si l'application Fichiers ne l'exécute qu'en prévisualisation, ouvrir la page via un hébergement web simple. Cliquer sur la scène pour donner le focus au clavier. Flèches ou ZQSD ; boutons de sélection. Le navigateur peut réserver certaines touches : essayer Safari ou un navigateur alternatif.

Cette version HTML est un **simulateur de visite très simple**, non une exécution de Pygame ni un port Godot.

## Où sont les fichiers ?

- `assets/jussieu.png`, `assets/orly.png`, `assets/tokyo.png` : décors fixes (1024 × 768).
- `model/jussieu_data.py`, `model/orly_data.py`, `model/tokyo_data.py` : grilles de route/herbe et coordonnées de départ, arrivée, checkpoints et boosts.
- `model/game_model.py` : choix du circuit, chargement des données.
- `view/game_view.py` : dessin de l’image de fond et de la voiture.
- `controller/` : lecture du clavier, menus, mise à jour.

## Limitations importantes

- **Ce n'est pas encore le jeu final**. Les données de départ/checkpoints/boosts/tours existent, mais les boosts, tours et checkpoints ne sont **pas actifs** dans Pygame.
- Le terrain hors-route ne ralentit pas encore les voitures dans cette copie du projet.
- Les grilles en cases de **64 × 64** sont approximatives et ne coïncident pas parfaitement avec les courbes décoratives des images.
- Le jeu Pygame et sa fenêtre n'ont **pas été exécutés ici** ; la syntaxe des scripts et les coordonnées des grilles ont été vérifiées. La page HTML a été vérifiée statiquement, non testée sur l'iPad.
- Ce ZIP est un **prototype**, à comparer avec les fichiers définitifs des camarades avant toute intégration.
- Cette archive ne fournit **pas** de projet Godot : Godot utilise un autre moteur et exige une conversion spécifique.
