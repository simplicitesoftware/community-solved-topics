# Perte des path de lien dans le modeleur SVG

**URL:** https://community.simplicite.io/t/6869

## Question
### Request description

Bonjour,
Suite à [ce ticket](https://community.simplicite.io/t/probleme-de-performances-a-louverture-dun-model-svg/5674/10) j'ai utilisé la feature permettrant de ne pas synchroniser mon modèle à l'ouverture.

```
mod.get(
				    	function() {
						// instanciate in silent mode
							$ui.diagram.open(modelId, { svg:true, hidden:true, sync:false }, updateDiagram);
						}, 
						modelId, 
						{inlineDocs: true}
						);
```

Depuis nous perdons la forme des links à chaque réouverture.
 
Repositionnement + Save
![image|690x304](upload://tQIuhGEuAHv0Zv8VAYzKBzzHga2.png)

Réouverture
![image|690x251](upload://iGbIn8v4KS4T99TJ1eJD82yaM0R.png)

Avec sync = false, le modeler ne passe plus dans le ReloadNode qui dessine les links.

Est-ce un comportement attendu ? J'ai remis sync:true en attendant mais nous avons des problèmes de performances sur les gros modèles.

### Steps to reproduce



### Technical information

[details="Instance /health"]
```text
[Platform]
Status=OK
Version=5.3.12
BuiltOn=2023-08-25 09:44
Git=5.3/e2cd9f0ea850e3845169840790a1a6ef043fed16
```
[/details]

## Answer
En fait si on ouvre sans synchro, les éléments du modèle restent du pur SVG, rien est monté en mémoire.

Si on veut les manipuler en mise à jour, il faut forcement à un moment appeler le constructeur des objets Javascript qui les gèrent (Container / Node / Link...). 

Exemple pour un node :

```javascript
let n = $(".node[data-obj=...][data-id=...]"), // SVG node group
	item = {
		object: n.attr("data-obj"),
		id: n.attr("data-id"),
		template: n.attr("data-tpl"),
		keys: n.attr("data-keys")
	},
	node = new Simplicite.Diagram.Node(desktop, item, n);
// synchronize node data with DB
model.reloadNode(node, cbk);
```

Le SVG ne contient pas toutes les données (comme l'item complet du row_id).
Au moment du "save", si un élément n'a pas son objet/données associées, il sera cassé ou perdu.

On peut voir si on peut avoir des objets "minimalistes", mais on aura d'autre problèmes en cascade : les hooks peuvent par exemple accéder aux valeurs des items (issus du "get" Ajax lors de la synchro des éléments). on ne peut pas à la fois faire du "raw" et avoir des API de haut niveau (insertNode, save... qui ont besoin des données étendues / non SVG des objets).

A mon avis il faudra plutôt utiliser les API back (et ne pas mette à jour tes modèles en front qui bloque l'UX). Une première version du SVGTool en Java sera disponible en V6 en fin d'année :
**`package com.simplicite.util.diagram`**

Exemple de code back :

```java
	public static void testCreate(Grant g)
	{
		testDelete(g);
		try
		{
			ModelTool tool = new ModelBusinessObjectTool(g);
			tool.createModel("aModelSVG", "ModelBusinessObject", "Application");

			String userId = ObjectDB.getObjectId("User");
			ModelNode node1 = tool.addNode("BusinessObject", "ObjectInternal", userId, 50, 50);

			// change icon
			//node1.setIcon("bi/building");
			//node1.setIcon("fas/address-book");
			//node1.setIcon("far/address-card");
			//node1.setIcon("img/system/user");

			// Build a shape
			node1.setIcon(null);
			node1.setShape("actor");
			node1.setShapeTitlePosition("bottom");
			node1.setShadow(false);
			node1.redraw();

			// Move/Resize
			node1.position(30, 200);
			node1.size(20, 20);
			node1.redraw();

			// Add a node + link
			String respId = ObjectDB.getObjectId("Responsability");
			ModelNode node2 = tool.addNode("BusinessObject", "ObjectInternal", respId, 100, 100);
			node2.setColor("#AAFFFF");
			//node2.setRadius(10);
			node2.position(500, 100);
			node2.addClass("hide-references");  // hide referenced fields
			node2.getDimension().setSize(0, 0); // force to recalc size on redraw
			node2.redraw();

			// Change link properties
			ModelLink link1 = node2.getLinks().get(0);
			link1.setColor("#333333");
			link1.setThickness(1.5);
			link1.setCurved(true);
			link1.setBridge(false);
			link1.setDashed(false);
			link1.setLabel(true, "user link\nline 2", true);
			link1.setExtremityFrom(ModelLink.TYPE_BLANK, true);
			link1.setExtremityTo(ModelLink.TYPE_COMPOSIT, true);

			//link1.setRendering(ModelLink.RENDER_FREE, false);
			//link1.removeAllPoints();
			//link1.addPoint(400, 600);

			link1.setRendering(ModelLink.RENDER_AUTO, false);
			//link1.setRendering(ModelLink.RENDER_HORIZ_VERT, false);
			//link1.setRendering(ModelLink.RENDER_TOP_BOTTOM, false);
			link1.redraw();

			// Container
			ModelContainer cont1 = tool.addContainer("Module", "Module", ModuleDB.getModuleId("System"), 0, 0);
			cont1.position(100, 100, false, true);
			cont1.setColor("#EEEEFF");
			cont1.setRadius(5);
			cont1.setShadow(true);
			//cont1.setTitle("The system container\nline 2\nline 3");
			cont1.setTitleAnchor("middle"); // "start" "end"
			cont1.setTitleVertical(false);
			cont1.redraw();

			// move relative + auto-resize parent container
			node2.position(200, -100, true, true);

			String groupId = ObjectDB.getObjectId("Group");
			ModelNode node3 = tool.addNode("BusinessObject", "ObjectInternal", groupId, 550, 700);
			node3.setColor("#AAFFAA");
			node3.redraw();

			// Find a link
			Element e = tool.findLinksFromTo("ObjectInternal", respId, "ObjectInternal", groupId).get(0);
			ModelLink link2 = (ModelLink)e.getUserData("d");
			link2.setRendering(ModelLink.RENDER_TOP_BOTTOM, true);
			link2.setCurved(true);
			link2.redraw();

			// Add a note
			ModelNote note1 = tool.addNote(0, "This a simple note", 0, 0);
			note1.setColor(ModelNote.DEFAULT_COLOR);
			note1.position(200, 500);
			note1.setText("This a simple note\n- with new line &éç€<>\n- and a smiley 😀");
			note1.redraw();

			tool.addCaption(50,50);

			// Fit contents to visible area + save
			tool.save(true);
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
```
