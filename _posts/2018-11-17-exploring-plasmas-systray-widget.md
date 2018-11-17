---
title: Exploring Plasma's System Tray Widget
layout: post
---

A [user on reddit recently asked](https://www.reddit.com/r/kde/comments/9xcin7/configure_default_plasmoid_size/) how to resize a few widgets. With the "Notes" widget, it is pretty straight forward by changing the `Layout.preferredWidth` / `Layout.preferredHeight` as outlined in [KDE's Getting Started with Plasma Widgets](https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted) article on the KDE wiki. However the user wanted to resize the System Tray and had no idea how to do so.

I personally wouldn't recommend a new user modify the system tray, as it uses some fairly complicated code in order to embed other widgets inside itself (like the panel). However, this offers a learning opportunity for the reader on how a Plasma Widget is written, so lets jump down the rabbit hole.

## Compact / Full Representations

First a refresher on how Plasma widget's are structured.

A widget has 2 different "views". The compact area that's shown when there's not much space, like when it's in the panel, and the full view when there is enough room, which is shown in a popup.

{% highlight qml %}
Item {
	id: main

	Plasmoid.compactRepresentation: {
		id: panelView
	}

	Plasmoid.fullRepresentation: {
		id: popupView
	}
}
{% endhighlight %}

When we do not define the full view, the main Item is treated as the full representation.

{% highlight qml %}
Item {
	id: main // also the popupView

	Plasmoid.compactRepresentation: {
		id: panelView
	}
}
{% endhighlight %}

When we do not define the compact view, Plasma uses a "default" compact representation that displays the icon defined in the `metadata.desktop` or the icon defined with `Plasmoid.icon`.

{% highlight qml %}
Item {
	id: main

	Plasmoid.icon: 'audio-headphones'
}
{% endhighlight %}

We can also ignore the "compact" representation, and show the full representation in the panel. With this, the widget will not have a popup.

{% highlight qml %}
Item {
	id: main // also the full representation which will be shown

	Plasmoid.preferredRepresentation: Plasmoid.fullRepresentation
}
{% endhighlight %}

## The System Tray Widget

The System Tray widget is a specical beast. In order for it to work, it needs to embed other widgets inside itself (like the panel). It embeds the Volume widget, the Network widget, the Notification widget, etc. Normal widget's (aka applets) cannot do this. It needs to be a special [ContainmentInterface](https://github.com/KDE/plasma-framework/blob/master/src/scriptengines/qml/plasmoid/containmentinterface.h#L51) instead of the standard [AppletInterface](https://github.com/KDE/plasma-framework/blob/master/src/scriptengines/qml/plasmoid/appletinterface.h) that a widget uses.

To get around this, the System Tray widget has a public "container" widget under the namespace `org.kde.plasma.systray`, which has some C++ magic to load a single private widget `org.kde.plasma.private.sytray`.

<https://github.com/KDE/plasma-workspace/blob/master/applets/systemtray/container/package/contents/ui/main.qml#L32>

Notice how the "public" widget sets `preferredRepresentation` so that we only have a "full representation" as the default view with no "compact view". It doesn't set the `Plasmoid.fullRepresentation` so this means the main Item is the full representation. And when the "private" `internalSystray` widget is loaded, it sets adds it as a child of the main Item (called `id: root` in this case).

{% highlight qml %}
onInternalSystrayChanged: {
    root.internalSystray = plasmoid.nativeInterface.internalSystray;
    root.internalSystray.parent = root;
    root.internalSystray.anchors.fill = root;
}
{% endhighlight %}

So, in order for the user to edit the system tray's popup size, we don't want to modify the "public" container widget's code. Instead **we want to edit the private code under** `org.kde.plasma.private.sytray`.

## SysTray's Private Widget

Navigate to the systray's private widget `/usr/share/plasma/plasmoids/org.kde.plasma.private.systemtray/`, then open up it's `contents/ui/main.qml`.

I'm not quite sure where it defines full/compact representations. However this private widget is definitely different as it defines it's own Dialog popup. I think that since it's loaded as a ContainmentInterface, it needs to define those itself.

> Note: The dialog for a normal widget is defined in `plasma-desktop` repo under [desktoppackage/contents/applet](https://github.com/KDE/plasma-desktop/tree/master/desktoppackage/contents/applet) if you're interested in comparing them.

Back to the system tray widget. Now with the [PlasmaCore.Dialog](https://github.com/KDE/plasma-framework/blob/master/src/plasmaquick/dialog.h), the size of the dialog is the same size as the `Dialog.mainItem`, so if [we look at it](https://github.com/KDE/plasma-workspace/blob/master/applets/systemtray/package/contents/ui/main.qml#L375) we see that the `mainItem` is passed a `ExpandedRepresentation {}`. If we look in the `contents/ui/` folder, we see that there is a `ExpandedRepresentation.qml` file. So lets open that up as there does not seem to be any width/height definitions in the `main.qml` file for the dialog.

And there we go. `Layout.minimumWidth`/`Layout.minimumHeight` is what is controlling the size of the system tray width/height.

<https://github.com/KDE/plasma-workspace/blob/master/applets/systemtray/package/contents/ui/ExpandedRepresentation.qml>

## Changing the SysTray Popup Height

Again, I do not recommend changing the system tray widget. It's actively being updated and bugfixed. However we can modify for learning puposes.

If we add `import QtQuick.Window 2.2` to the top of the `ExpandedRepresentation.qml` file, we can then use QML's [Screen](http://doc.qt.io/qt-5/qml-qtquick-window-screen.html) variables like `Screen.desktopAvailableHeight`. Normally we should probably using `plasmoid.screenGeography.height` however it appears that variable isn't "defined" in this widget as it's set to be a 0x0 rectangle.

If we set height to `Screen.desktopAvailableHeight`, the system tray popup should be the same height as our screen!

{% highlight qml %}
import QtQuick.Window 2.2

Item {
    id: expandedRepresentation

    height: Layout.minimumHeight
    Layout.minimumHeight: Screen.desktopAvailableHeight
{% endhighlight %}

We can test with the following. Note that we do *not* use the private namespace.

{% highlight bash %}
plasmawindowed org.kde.plasma.systemtray
{% endhighlight %}

![](https://i.imgur.com/tU90hd9.png)

Cool. Now lets try to get the popup to slide in from the right!

If we go back to the private system tray's `main.qml` and look at the `PlasmaCore.Dialog` once more, we can see that the dialog specifies which location/edge/direction the dialog should appear from.

{% highlight qml %}
PlasmaCore.Dialog {
    location: plasmoid.location
{% endhighlight %}

If we look at the [API docs for the PlasmaCore.Dialog](https://api.kde.org/frameworks/plasma-framework/html/classPlasmaQuick_1_1Dialog.html), we'll [see that the property](https://api.kde.org/frameworks/plasma-framework/html/classPlasmaQuick_1_1Dialog.html#a8c2acce4b34db6a325d8da57bca55bc3) is a [Plasma::Types::Location](https://api.kde.org/frameworks/plasma-framework/html/classPlasma_1_1Types.html#aeb81fc9475c441643b6226dfb16a6c0f) enum value. So we should be able to change `plasmoid.location` to a hardcoded value of `PlasmaCore.Types.RightEdge` to make it slide in from the right.

{% highlight qml %}
PlasmaCore.Dialog {
    location: PlasmaCore.Types.RightEdge
{% endhighlight %}

<video src="https://i.imgur.com/FUqR5aD.mp4" width="100%" autoplay loop muted></video>

As you can see, while it does animate the slide in from the right, it's no longer positioned above the system tray. Next, lets try to position it to the right of the screen. The reason why it's on the left side of the screen is because it's trying to position itself to the "left" of my bottom panel, just like we saw with the `plasmawindowed` window up above.

![](https://i.imgur.com/tU90hd9.png)

This is because the [Dialog.visualParent](https://api.kde.org/frameworks/plasma-framework/html/classPlasmaQuick_1_1Dialog.html#a6db1282a406b6503c701d5167e5f43e6) is set. If we remove the `visualParent: root` line of code, the popup will now appear at the default location of `(0,0)`, or the top left of the screen.

![](https://i.imgur.com/ZRdC5zC.png)

Now lets move the popup to the right side of the screen. We'll set the dialogs x-coordinate to be the "width of the screen" minus "width of the dialog". Don't forget to add the import to the top of the file!

{% highlight qml %}
import QtQuick.Window 2.2

MouseArea {
    id: root

    //Main popup
    PlasmaCore.Dialog {
        id: dialog
        x: Screen.desktopAvailableWidth - dialog.width
        location: PlasmaCore.Types.RightEdge
{% endhighlight %}

<video src="https://i.imgur.com/UyextCM.mp4" width="100%" autoplay loop muted></video>

## This is just for fun!

Reminder that editing files in `/usr/share/plasma/plasmoids` not recommended. Whenever your system updates Plasma, the files will be overwritten with an updated version with bugfixes + new features, or just revert it back to the original file.

While we could copy the system tray's code to the home directory, I would not recommend it for the system tray, as it has a lot of C++ code that works with the QML view code, and using and older version of QML code you modified with new C++ code after a Plasma update could possibly cause PlasmaShell to crash. So while a system tray that open from the right side of the screen is neat, a kde plasma tweaker should probably keep it as is.
