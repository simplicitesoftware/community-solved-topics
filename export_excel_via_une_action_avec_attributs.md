# Export Excel via une action avec attributs

**URL:** https://community.simplicite.io/t/4672

## Question
bonjour,

je dois générer un fichier excel en intégrant des données saisies au moment de l'export.
J'ai donc créé une action de liste avec des attributs et une publication qui génère le fichier excel 
![image|690x339](upload://e4K9HUMzC3KnEc79971vOyqS381.png)

![image|690x304](upload://t3AWH0Wai9INATJ9ZepYwBQi3XG.png)

Dans le script de l'objet métier, je récupère les attributs de l'action et la méthode d’action retourne un statement de redirect : 
public String ExportLogement(Action action) {
.....
	    try{
			return this.javascript("$ui.displayPrint(null, 'foiEtabLogeXls', '" + this.getName() + "', '" + this.getRowId() + "')");
		}catch(Exception e){
			AppLog.error(getClass(),  e.getStackTrace()[0].getMethodName() , "Exception lors l'invocation de la méthode ExportLogement()", e, getGrant());
			return e.getMessage();
		}

jusque là, tout va bien.
Mon problème est que l'export ne prend pas en compte les lignes sélectionnées dans la liste.
dans le méthode exécutée lors de la publication, getSelectedIds() = null alors que j'ai sélectionné des lignes.

		/** Publication: Microsoft Excel(R) sheet Logements*/
	public Object ETABLogeExport(PrintTemplate pt) {
		try {
			// Build rows from selected IDs or from current filters
			List<String[]>rows = new ArrayList<>();
			List<String> ids = getSelectedIds();
                ...........
       }

Quand j'exécute l'export en utilisant la publication sans passer par l'action, getSelectedIds(); me ramène bien les id des lignes sélectionnées

Pour info, ce code fonctionnait très bien en V4.

![image|417x134](upload://emJ78LvUakkdeMw9PhEcqqpIW0x.png)

## Answer
1) passer l'instance de l'objet au DisplayPrint dans la méthode de l'action. Cela fonctionnera sur n'importe quelle instance. 
`return this.javascript("var o=$ui.getAjax().getBusinessObject('" + this.getName() + "', '" + this.getInstanceName()+"');$ui.displayPrint(null, 'foiEtabLogeXls', o,'"+ this.getRowId() + "')");`

2) Faire le getSelectedIds sur l'instance de son choix dans la méthode du printtemplate. Cela fonctionne sur une instance spécifique. 
`getGrant().getObject(<Nom de l'instance>,<Nom de l'objet>).getSelectedIds();`
