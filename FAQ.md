# FAQ (questions récurrentes)

Cette FAQ synthétise les questions qui reviennent le plus souvent dans les fichiers de `topics/` (extraits de sujets résolus de la communauté Simplicité).

## Sommaire

- [UI / listes / formulaires](#ui--listes--formulaires)
- [Actions / contraintes / hooks](#actions--contraintes--hooks)
- [Documents / email](#documents--email)
- [SSO / OpenID Connect / Azure AD](#sso--openid-connect--azure-ad)
- [Git / DevOps](#git--devops)
- [Cache / performance / migration](#cache--performance--migration)
- [Logs](#logs)

## UI / listes / formulaires

### Comment différencier le contexte **liste** vs **formulaire** (et éviter du code “trop exécuté”) ?

Beaucoup de comportements “bizarres” viennent du fait qu’un même objet est instancié dans plusieurs contextes (liste principale, panel/liste fille, formulaire, treeview…). Évitez de mettre de la logique lourde dans des endroits trop génériques, et conditionnez vos réglages à l’instance/contexte (ex. `initList` vs `initForm`, instance principale vs panel vs treeview). L’objectif est de ne pas payer le coût (requêtes, calculs) là où ce n’est pas nécessaire.

- **Voir aussi**:
  - `topics/comment_identifier_différencier_les_instances_formulaire_et_liste_d_un_objet.md`
  - `topics/edition_en_liste_contexte_treeview_.md`
  - `topics/masquer_le_bouton_de_création_en_liste_dynamiquement.md`

### Comment masquer le bouton **Créer** en liste (souvent en **liste fille**) sans casser d’autres boutons/actions ?

Si vous “coupez” la création via une règle globale, vous pouvez impacter des comportements UI attendus (navigation standard, actions “Associer…”, etc.). Préférez une approche ciblée par instance (ex. liste principale OK, liste fille non), plutôt qu’une désactivation générale.

- **Voir aussi**:
  - `topics/masquer_le_bouton_de_création_en_liste_dynamiquement.md`
  - `topics/la_création_d_un_objet_ne_doit_être_possible_que_depuis_le_parent.md`
  - `topics/configurer_une_child_list_with_creation_.md`

### Comment publier un **TreeView** dans le menu principal ?

Un treeview peut exister et fonctionner sans être exposé comme entrée “menu principal”. Assurez-vous que la configuration du nœud racine / de la vue est bien publiée dans le menu, et pas uniquement dockée dans un panneau de navigation.

- **Voir aussi**:
  - `topics/comment_insérer_un_treeview_dans_le_menu_principal_de_l_utilisateur_.md`
  - `topics/vue_en_arbre_générale.md`

### Pourquoi “Éditer en liste” n’apparaît pas dans une liste ouverte depuis un **TreeView** ?

Selon le contexte d’ouverture (treeview vs instance “main”), l’UI peut ne pas exposer les mêmes capacités (dont l’édition en liste) même si l’objet, lui, sait “éditer en liste”. Si vous avez besoin des mêmes comportements qu’une liste ouverte depuis le menu, il faut aligner l’instance/contexte d’ouverture.

- **Voir aussi**:
  - `topics/edition_en_liste_contexte_treeview_.md`
  - `topics/items_de_list_non_initialisés_sur_displaylist_en_mode_edit.md`
  - `topics/enum_multiple_avec_contrainte_en_edit_cell.md`

### Comment filtrer/masquer dynamiquement des valeurs d’une **liste de valeurs (LOV)** / d’un **enum** ?

Le pattern le plus simple consiste souvent à **basculer** la LOV (changer la liste utilisée) en fonction d’une condition (ex. via une contrainte “avec impact”), plutôt que de tenter de masquer des codes un par un. Pour des cas très fins (masquer quelques codes), il faut parfois structurer différemment les listes ou passer par du code.

- **Voir aussi**:
  - `topics/masquer_dynamiquement_des_codes_de_liste_sans_code.md`
  - `topics/contrainte_sur_une_liste_en_fonction_d_un_attribut_énuméré_simple.md`
  - `topics/liste_vide_si_aucun_code_de_liste_lié_sélectionnée.md`

## Actions / contraintes / hooks

### Comment afficher une **action** seulement pour un groupe, ou pour le “responsable” courant (ou les deux) ?

Séparez bien:
- la **sécurité** (qui peut exécuter) via les habilitations,
- et le **confort UI** (afficher/activer) via une contrainte de visibilité/activation.

Combinez ensuite les conditions (souvent un OR entre “user courant = responsable” et “user a telle responsabilité/groupe”) pour répondre au besoin.

- **Voir aussi**:
  - `topics/contrainte_sur_la_visibilité_d_une_action.md`
  - `topics/ajouter_une_contrainte_de_visibilité_sur_un_attribut_d_action.md`
  - `topics/actions_visibles_même_lorsque_les_états_ne_correspondent_pas.md`

### Pourquoi certains hooks `initXXX` ne se déclenchent pas via API REST (RESTMappedObject) ?

Selon le point d’entrée (UI vs REST, REST “mappée”, etc.), la plateforme ne suit pas forcément exactement les mêmes chemins d’exécution. Évitez de mettre des règles métier essentielles uniquement dans des hooks très “UI-contextuels” (type `initCreate`, `initUpdate`), et préférez les hooks/points d’extension adaptés à la validation/sauvegarde, ou des méthodes partagées appelées depuis plusieurs canaux.

- **Voir aussi**:
  - `topics/les_appels_post_sur_les_api_mappées_restmappedobject_n_exécutent_pas_le_hook_initcreate.md`
  - `topics/les_données_fournies_en_body_des_calls_api_put_sont_prises_en_compte_dès_les_hooks_isxxxenabled.md`
  - `topics/création_d_api_rest.md`

## Documents / email

### Pourquoi `setDocument(...)` fonctionne en action synchrone mais pas en hook / asynchrone ?

En asynchrone, rien ne garantit que les données issues de l’UI (dont un upload) soient encore disponibles au moment où le job s’exécute. Pour les actions avec upload, le fichier est stocké temporairement côté serveur: il faut récupérer le fichier temporaire (ex. via `doc.getUploadFile()`), puis traiter en asynchrone à partir de ce fichier/stream. Évitez de compter sur `getBytes()` si le fichier n’est pas garanti en mémoire.

- **Voir aussi**:
  - `topics/utilisation_de_setdocument_dans_différents_contexte_action_hook_.md`
  - `topics/copier_des_champs_documents_en_code.md`
  - `topics/renommer_un_document_après_upload_dans_un_hook.md`

### Pourquoi une pièce jointe “Document” n’est pas envoyée par email ?

Souvent, le record porteur du document n’est pas correctement **sélectionné/chargé** au moment où l’API mail tente de lire le champ document, ou le grant n’a pas les droits de lecture. Vérifiez le `select(rowId)` (ou l’équivalent dans votre flux) avant d’attacher le document, et les droits.

- **Voir aussi**:
  - `topics/impossible_de_joindre_un_document_à_un_mail.md`
  - `topics/envoi_de_pièce-jointe_mail_et_alertes_.md`
  - `topics/erreur_d_envoi_dans_les_logs_apres_parametrage_du_smtp.md`

### Erreur 404 au téléchargement d’un document (doc présent mais inaccessible)

Un 404 peut être dû non pas au fichier, mais à la vérification d’accès au **record métier** support (droits, filtres, search-spec…). Si l’utilisateur ne peut pas “voir” le record porteur, le service de document peut refuser de servir le fichier.

- **Voir aussi**:
  - `topics/erreur_404_pour_télécharger_un_document_déposé.md`
  - `topics/télécharger_un_document_blob_dans_un_objet_externe.md`

## SSO / OpenID Connect / Azure AD

### OpenID Connect: quelles URIs pour **redirect** et **logout** ?

- **Redirect URI** (côté application): typiquement `<base URL>/oauth2callback` (cf doc).
- **Logout**: il y a deux URL à considérer selon le flux choisi:
  - l’URL de logout à configurer côté Simplicité est l’URL de logout de votre IdP,
  - l’URL de logout à configurer côté IdP pour revenir à l’application est typiquement `<base URL>/logout`.

- **Voir aussi**:
  - `topics/uri_pour_configuration_openid.md`
  - `topics/oidc_logout.md`
  - `topics/implémentation_du_parseauth.md`

### Azure AD / OIDC: pourquoi ça “boucle” entre création et update d’un user au login ?

Quand la session et les droits se (re)chargent, un paramétrage de scope/home non cohérent (ou un mapping login/UPN/email inconsistent) peut déclencher des rechargements et donner l’impression de boucles create/update. Vérifiez la cohérence du login “technique” choisi, ainsi que les attributs de profil/scope (ex. home) affectés au user et leur compatibilité avec ses responsabilités.

- **Voir aussi**:
  - `topics/problème_azure_ad_comportement_étrange_entre_création_et_update_d_un_user.md`
  - `topics/groupes_de_responsabilité_paramètres_utilisateurs_visibilité_du_menu_lors_de_la_connexion.md`
  - `topics/implémentation_du_parseauth.md`

## Git / DevOps

### Un push Git depuis Simplicité est “succès” mais rien n’arrive sur le remote: comment diagnostiquer ?

Le push plateforme correspond à un `git push` standard exécuté dans le repo Git du module côté serveur. Si votre remote impose des mécanismes non standards (ex. création automatique de MR/PR, règles serveur, protections), Simplicité peut considérer l’opération “OK” sans refléter le résultat attendu côté remote. Le diagnostic le plus fiable est de cloner localement le repo Git du module (côté instance), récupérer les commits, puis pousser vers le remote depuis un environnement où vous voyez précisément les retours du serveur Git.

- **Voir aussi**:
  - `topics/debug_du_push_git.md`
  - `topics/repo_git_simplicité.md`
  - `topics/git_push_depuis_simplicité_ne_pousse_que_vers_master.md`

## Cache / performance / migration

### Faut-il automatiser un “clear cache” quotidien ? (et que faire en cluster)

En général, non: un clear cache “planifié” n’a pas de raison d’être hors déploiements, sauf à contourner un problème sous-jacent (mémoire, contexte, etc.). En cluster, la tâche interne `CheckClearCache` sert surtout à propager l’invalidation si un nœud n’a pas reçu la notification. Si vous devez déclencher un reset via du code, une action dédiée peut appeler `SystemTool.resetCache(...)` (grant admin) en assumant l’impact (sessions, indisponibilité temporaire, etc.).

- **Voir aussi**:
  - `topics/automatisation_du_clear_cache_.md`
  - `topics/clear_cache_sur_instances_multiples.md`
  - `topics/instance_bcsi_renault_simplicite_io_en_carafe_pendant_plusieurs_minutes_lors_des_clear_cache.md`

### Performance: pourquoi l’export PDF “en masse” peut saturer CPU/heap, et quels garde-fous appliquer ?

L’export PDF est souvent plus coûteux que d’autres formats (génération, buffers mémoire, librairies). Évitez de lancer des exports “toute la base” depuis l’UI; préférez des exports batch/offline, des limites (nombre de lignes), des confirmations, et/ou des restrictions par droits. Si vous devez supporter de gros volumes, privilégiez des approches streaming/batch et des garde-fous fonctionnels.

- **Voir aussi**:
  - `topics/l_export_pdf_en_masse_peut_saturer_les_ressources_du_serveur_applicatif.md`
  - `topics/exporter_un_formulaire_en_pdf.md`
  - `topics/impression_document_pdf.md`

### Migration/upgrade (ex. v5 → v6): quels “breaking changes” typiques bloquent une migration ?

Les blocages viennent souvent de changements de dépendances/API (ex. bibliothèques PDF), ou de hooks/points d’extension modifiés/supprimés entre versions. La méthode la plus robuste est de compiler/valider les modules sur la chaîne cible (BOM/dépendances), corriger les erreurs de compilation, puis seulement importer/valider sur l’instance migrée.

- **Voir aussi**:
  - `topics/migration_de_5_3_76_vers_6_2_15.md`
  - `topics/migration_v5_vers_v6_bloquée_à_cause_de_script_rhino_encore_présent.md`
  - `topics/migration_4_0_-_5_0.md`

## Logs

### Peut-on changer la rétention/rotation des logs (Tomcat / Log4J) sans risque ?

Oui, mais vérifiez l’impact sur les outils/écrans qui lisent des fichiers précis (ex. lecture de `simplicite.log`). Ajuster la rotation/rétention est généralement OK (surtout si vous externalisez vers une solution d’observabilité), mais gardez en tête les usages “legacy” basés sur des fichiers locaux.

- **Voir aussi**:
  - `topics/roulement_des_logs_catalina.md`
  - `topics/gestion_des_niveaux_de_logs.md`
  - `topics/ecriture_des_logs.md`
  - `topics/customisation_des_business_logs.md`

