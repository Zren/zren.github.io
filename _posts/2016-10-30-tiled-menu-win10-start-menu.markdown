---
layout: post
title: Tiled Menu (Win10 Start Menu)
---

![](https://i.imgur.com/CFBEkIh.jpg)

<https://github.com/Zren/plasma-applets/tree/master/tiledmenu>

TODO: Put on KDE Store.

The last few months I've been wanting to reskin the KDE "Start" menu. Plasma ships with 3 default menues. The Application Menu is category based with favourites along the side. You can't pin files to the favourites list, and the menu gets really tall with more than ~10 favourites. So I wanted to try cloning the Win10 menu to start, then customize it to my hearts content.

I initially mocked up the layout in QML View, and started deciphering how the [kicker](https://github.com/KDE/plasma-desktop/tree/master/applets/kicker) and [kickoff](https://github.com/KDE/plasma-desktop/tree/master/applets/kickoff) plasmoids worked. I found out apps are loaded into a nested model that also contains the recent apps and documents.

* [`RootModel`](https://github.com/KDE/plasma-desktop/blob/master/applets/kicker/plugin/rootmodel.h)
	* `Recent Applications` => `RecentUsageModel`
		* app (May contain invalid entries)
	* `Recent Documents` => `RecentUsageModel`
	* `Recent Contacts` => `RecentContactsModel`
	* Seperator (optional)
	* `All Apps` 
		* `A`
			* app
			* ...
		* `B`
		* ...
	* `Internet` (Categories begin)
		* app
		* folder
			* app
			* app
	* ...
	* `System` (Categories end)
		* app
	* `Power / Session` => `SystemModel`

You can't use each list individually very easily since recent apps/docs/contacts are optional. As is All Apps, it's only possible to use it if your categories are flat, where the folders under the categories are squished to a depth of 1 "folder". This is because "All Apps" is only used in the dashboard menu, where it's designed to have a "depth" of 1-2 folders max. The 1st depth being the sidebar category, and the 2nd depth being the sections "A"/"B"/... in the list.

Kicker's model also gives me the last 10 or so apps, when all I want to display is the last 5 or so (so that it's not using up the entire viewport when you open the menu). Normally to filter just 5 items, I'd have to use [SortFilterProxy](https://api.kde.org/frameworks/plasma-framework/html/classPlasma_1_1SortFilterModel.html). I wanted to be able to edit the models however (and add extra properties), so I decided to just parse the model into a JavaScript object, which is a bit more trouble than it's worth.

After I managed to list the apps, I started on implementing the search, and soon found that it was fairly easy to add the calculator to the menu's results, as well as all the other services.

{% include streamable.html streamableId="h9us" %}

Finally, I implemented the favourites view. I'd managed to mockup the "Large"/"Wide"/"Small" sizes with albeit a few bugs still, but realized it would be way too dificult to implement at the same time I'm trying to bind it with the [FavouritesModel](https://github.com/KDE/plasma-desktop/blob/master/applets/kicker/plugin/favoritesmodel.h), so I dropped it for a simple grid.

One thing that makes the "Start menu" is the ability to resize the menu to make more space for more favourites. Unfortunately, Plasma doesn't expose the dialog window when expanding the menu in any way, so I can't change the window flags to readd the resizeable flag. I got around this however by using the Alt+RightClick to drag "shortcut". I added a tooltip when hovering the corner and called it done.

The hardest part is probably the context menu jump lists. Right now I've parsed the models into javascript, but I need to be able to invoke functions on the old models when you click stuff. So right now it's a really complicated process that I might need to scrap, but that requires rewriting everything. I might do it someday, but not right now since my main goal was to get a favourites grid and an A-Z list of apps.

{% include streamable.html streamableId="ypps" %}
