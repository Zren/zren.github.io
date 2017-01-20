---
layout: docpage
title: Plasma (Unofficial) API Docs
permalink: /kde/docs/
---

<style>
/* Assume all ul in the right side are file trees */
section .right ul {
    border-left: 2px solid #bfcdd8;
    margin-left: 16px;
}
section .right li {
    position: relative;
    list-style-type: none;
    padding-left: 8px;
}
section .right li:before {
    position: absolute;
    left: -8px;
    content: "├";
    margin-right: 0;
}
section .right li:last-child:before {
    content: "└";
}
</style>

<!-- ------- -->
{% include docHeader.html label="Setup" %}

{% capture label %}Folder Structure{% endcapture %}
{% capture sectionLeft %}

First create a folder for your new widget. Inside it create another folder called `package`. Everything inside the `package` folder will be what we eventually zip and share online, so we can keep text editor project files in the `helloworld` folder.

Inside the package folder will be `metadata.desktop` file which is basically an Linux INI file. This file will describe the name of the widget, the category it's in, and various other plasma specific keys like the main qml file.

Inside `contents` we will create `ui` and `config`. `ui` is the folder which should contain your layout files like the `main.qml` and the `configGeneral.qml`. The latter is the layout for the widget's configuration window.

Inside `config` we have the `main.xml` which contains the schema of all our serialized configuration keys+values. The `config.qml` is used to define the tabs in the configuration window, and which QML layout file in the tab will open (like `ui/configGeneral.qml`).

Note that you don't *need* the 3 config files. You can get away with just the `main.qml` and `metadata.desktop` for a barebones widget.

{% endcapture %}{% capture sectionRight %}

* `helloworld/`
    * `package/`
        * `contents/`
            * `config/`
                * `config.qml`
                * `main.xml`
            * `ui/`
                * `configGeneral.qml`
                * `main.qml`
        * `metadata.desktop`

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}metadata.desktop{% endcapture %}
{% capture sectionLeft %}

Inside the `metadata.desktop` file we need to set the `Name` of the widget. The `Type` should be `Service` since the `.desktop` file is not an app launcher and we don't want this to appear in the app menu.

`Icon` is the icon name associated with the widget. You can search for icon names in the `/usr/share/icon` folder. You can also look for an icon name by right clicking your app launcher and editing the icon, which will bring up a searchable interface. Plasma also has Cuttlefish ([screenshot](https://www.kde.org/images/screenshots/cuttlefish.png)) which you can install with `sudo apt install plasma-sdk`.

`X-KDE-PluginInfo-Name` is the folder your package will be installed to, so to make sure it's unique. You could use `com.github.zren.helloworld` if you're on github, or use `org.kde.plasma.helloworld` if you're planning on contributing the widget to kde.

Widget's installed by the user (without root) like when you "Install New Widgets" will be installed to `~/.local/share/plasma/plasmoids/` (which may not yet exist). The default widgets are installed to `/usr/share/plasma/plasmoids/`.

`X-KDE-PluginInfo-Category` is the category the widget can be filtered into in the widget list. A list of category names can be found [here](https://techbase.kde.org/Projects/Plasma/PIG).

`X-KDE-ServiceTypes`, `X-Plasma-API`, and `X-Plasma-MainScript` are also needed to just define that this package is a plasma widget, and where it's entry point is.

For more, read the [Getting Started](https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#The_.desktop_file) tutorial on the KDE wiki.


{% endcapture %}{% capture sectionRight %}

{% highlight ini %}
[Desktop Entry]
Name=Hello World
Comment=A widget to take over the world!

Type=Service
Icon=battery
X-KDE-ServiceTypes=Plasma/Applet

X-Plasma-API=declarativeappletscript
X-Plasma-MainScript=ui/main.qml

X-KDE-PluginInfo-Author=My Name
X-KDE-PluginInfo-Email=myemail@gmail.com
X-KDE-PluginInfo-Name=com.github.zren.helloworld
X-KDE-PluginInfo-Version=1
X-KDE-PluginInfo-Website=https://github.com/Zren/plasma5-applet-helloworld
X-KDE-PluginInfo-Category=System Information
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}contents/ui/main.qml{% endcapture %}
{% capture sectionLeft %}

This is the entry point. Various properties are available to set. You should know that widgets have severeal ways of being represented. You can have a widget in the panel which is just an icon, those shows a popup. You could have it on the desktop as a desktop widget which can be resized by the user. As a desktop widget it can switch between the "icon" which opens a popup and directly showing the popup on the desktop when there's enough room. The widget can also be run like an application in it's own window. You can also have the widget inside another widget (a containment) like the system tray or the panel itself.

`plasmoid.location` and `plasmoid.formFactor` can tell you how the widget is placed. `plasmoid` is a global variable which is defined when you `import org.kde.plasma.plasmoid 2.0`. Read more below.

`Plasmoid.compactRepresentation` (with a capital) and `Plasmoid.fullRepresentation` are used to define layout of the small "icon" view and the full "popup" view. These are both properties of the main Item. If neither are set, by default the main item is the full representation.

`Layout.preferredWidth` can be used to define the default width of a desktop widget, the size of the popup window (unless in the system tray). The system tray has a fixed hardcoded size for it's popups. It can also define the width of the compact "icon" view in the horizontal panel. Note that the preferredWidth/preferredHeight of the compactRepresentation will automatically scale to the thickness of the panel depending on if it's a vertical or horizontal panel.

`Layout.minimumWidth` can be used to define the minimum size for a desktop widget / popup.

You can set the tooltip contents and various other things in the `main.qml`.

#### Examples

* Various examples in the [Getting Started](https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#main.qml) tutorial on the KDE wiki.
* [colorpicker/package/contents/ui/main.qml](https://github.com/KDE/kdeplasma-addons/blob/master/applets/colorpicker/package/contents/ui/main.qml)
* [fifteenPuzzle/package/contents/ui/main.qml](https://github.com/KDE/kdeplasma-addons/blob/master/applets/fifteenPuzzle/package/contents/ui/main.qml)
{% endcapture %}{% capture sectionRight %}

{% highlight qml %}
import QtQuick 2.0
import org.kde.plasma.components 2.0 as PlasmaComponents

PlasmaComponents.Label {
    text: "Hello World!"
}
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


<!-- ------- -->
{% include docHeader.html label="Testing" %}


{% capture label %}plasmoidviewer{% endcapture %}
{% capture sectionLeft %}
We now have enough to test our widget. If you haven't yet, install the `plasma-sdk` with `sudo apt install plasma-sdk`.
{% endcapture %}{% capture sectionRight %}

{% highlight bash %}
plasmoidviewer --help
{% endhighlight %}
{% highlight log %}
QML debugging is enabled. Only use this in a safe environment.
Usage: plasmoidviewer [options]
Run Plasma widgets in their own window

Options:
  -v, --version                    Displays version information.
  -c, --containment <containment>  The name of the containment plugin
  -a, --applet <applet>            The name of the applet plugin
  -f, --formfactor <formfactor>    The formfactor to use (horizontal, vertical,
                                   mediacenter, planar or application)
  -l, --location <location>        The location constraint to start the
                                   Containment with (floating, desktop,
                                   fullscreen, topedge, bottomedge, leftedge,
                                   rightedge)
  -x, --xPosition <xPosition>      Set the x position of the plasmoidviewer on
                                   the plasma desktop
  -y, --yPosition <yPosition>      Set the y position of the plasmoidviewer on
                                   the plasma desktop
  -s, --size <widthXheight>        Set the window size of the plasmoidview
  -p, --pixmapcache <size>         The size in kB to set the pixmap cache to
  -t, --theme <themeName>          The name of the theme which the shell will
                                   use
  -h, --help                       Displays this help.
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Test as Desktop Widget{% endcapture %}
{% capture sectionLeft %}
Note that `--location=desktop` is used for the desktop wallpaper, not desktop widgets. Desktop widgets use `--location=floating`.
{% endcapture %}{% capture sectionRight %}

{% highlight bash %}
plasmoidviewer -a package --location=floating
plasmoidviewer -a package -l=floating
plasmoidviewer -a package # floating is the default.
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Test as Horizontal Panel Widget{% endcapture %}
{% capture sectionLeft %}
plasmoidviewer isn't really a good testing setup for panel widgets, but you assign `plasmoid.formFactor` and `plasmoid.location` while still having size of a desktop widget.
{% endcapture %}{% capture sectionRight %}

{% highlight bash %}
plasmoidviewer -a package -l bottomedge -f horizontal
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Testing High DPI{% endcapture %}
{% capture sectionLeft %}
By setting the `QT_DEVICE_PIXEL_RATIO=2` we can set the DPI to 192 just for the plasmoidviewer window. This is great for testing if your code will support a HiDPI monitor. You can also use `QT_DEVICE_PIXEL_RATIO=1.5` for 144 DPI.

If you're testing a much higher DPI, you'll probably find the default plasmoidviewer window is too small to show the widget, so we'll set the size and position of the window. Note that the window will go maximized if you set a size larger than you desktop has available.
{% endcapture %}{% capture sectionRight %}

{% highlight bash %}
QT_DEVICE_PIXEL_RATIO=2 plasmoidviewer -a package
QT_DEVICE_PIXEL_RATIO=2 plasmoidviewer -a package -l floating -f horizontal -x 0 -y 0 -s 1920x1080
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


<!-- ------- -->
{% include docHeader.html label="Qml" %}


{% capture label %}Rectangle{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}RowLayout{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}PlasmaCore.Label{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


<!-- ------- -->
{% include docHeader.html label="Configuration" %}


{% capture label %}contents/config/mail.xml{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}contents/config/config.qml{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

{% capture label %}contents/ui/configGeneral.qml{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}
