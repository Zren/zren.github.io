---
layout: post
title: Unity Ambiance Integration for the Present Windows Button
---

* United (Look and Feel): <https://store.kde.org/p/1167950/>
* Unity Ambiance (Desktop Theme): <https://store.kde.org/p/998797/>
* Present Windows Button Widget): <https://store.kde.org/p/1181039/>

{% include video.html youtubeId="C0W5Uf_cryA" %}

The main piece of code I added was:

* <https://github.com/Zren/plasma-applet-presentwindows/blob/master/package/contents/ui/Unity7Workspaces.qml>

Basically all I did was:

1. Grab the ["tasks.svg" from the taskmanger](https://github.com/KDE/plasma-desktop/blob/master/applets/taskmanager/package/contents/ui/Task.qml#L307-L319).
2. Copy the ["grid" from the default pager](https://github.com/KDE/plasma-desktop/blob/master/applets/pager/package/contents/ui/main.qml#L223). I removed the part where it the rectangles use the same aspect ratio as your screen, and removed the "pager.svg" it drew.
3. Make sure the grid [fit inside the "tasks.svg" padding](https://github.com/KDE/plasma-desktop/blob/master/applets/taskmanager/package/contents/ui/Task.qml#L400-L405).
4. Drew seperators on the right and bottom of a grid cell, unless it's the last cell in a row/column.
5. Converted Unity 7's "selected desktop" icon into a svg: 

![](https://i.imgur.com/UR3sEl6.png)

The more annoying part was to make it only use this "skin" on the Unity Ambiance theme.

1. We can easily detect the current Desktop Theme with `theme.themeName`, so it's trivial to [hide the current icon if we detect it](https://github.com/Zren/plasma-applet-presentwindows/blob/master/package/contents/ui/Main.qml#L54).
2. Users might want to disable this skin if they put the button in the top panel since there isn't much room (22px). So we need to provide a toggle button in the config. That's easy to do. Just add a boolean config item to `contents/config/main.xml`, and add a CheckBox to the `contents/config/ConfigGeneral.qml` tab. An example of this can be found in [this widget](https://github.com/Zren/plasma-applet-commandoutput/tree/master/package/contents). It's not that easy in this case, since we want it to default to "true" with the Breeze Ambiance theme, but also default to false for every other desktop theme. This is where a "3 state checkbox" should be used. QML calls these [CheckBoxes "partially checked"](http://doc.qt.io/qt-5/qml-qtquick-controls-checkbox.html#partiallyCheckedEnabled-prop). Luckily, we have Digital Clock's 24 hour checkbox to use as an example.
	* I [define the config key](https://github.com/Zren/plasma-applet-presentwindows/blob/master/package/contents/config/main.xml#L15). `CheckBox.checkedState` is weird, as `0` is true, `1` is "partially checked", and `2` is false.
	* I parse the desktop theme and config value [here](https://github.com/Zren/plasma-applet-presentwindows/blob/master/package/contents/ui/UnityThemeDetector.qml).
	* The actual config button is drawn [here](https://github.com/Zren/plasma-applet-presentwindows/blob/master/package/contents/ui/config/ConfigGeneral.qml#L78). Note that I'm using my own CheckBox file instead of the default one. It's source can be seen [here](https://github.com/Zren/plasma-applet-presentwindows/blob/master/package/contents/ui/lib/ConfigTriStateCheckBox.qml).

This was a fairly easy change, but took a bit so that things we're very polished, which is what ex-Unity users are expecting.
