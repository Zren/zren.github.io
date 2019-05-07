---
layout: docpage
title: Plasma Widget Tutorial
permalink: /kde/docs/widget/
---

The KDE wiki has a [Getting Started](https://techbase.kde.org/Development/Tutorials/Plasma5) tutorial which you can read as well.

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
/* Bootstrap Alerts */
.alert {
    position: relative;
    padding: .75rem 1.25rem;
    margin-bottom: 1rem;
    border: 1px solid transparent;
    border-radius: .25rem;
}
.alert-primary {
    color: #004085;
    background-color: #cce5ff;
    border-color: #b8daff;
}
.alert-secondary {
    color: #383d41;
    background-color: #e2e3e5;
    border-color: #d6d8db;
}
</style>

<!-- ------- -->
{% include docHeader.html label="Setup" %}

{% capture label %}Folder Structure{% endcapture %}
{% capture sectionLeft %}

First create a folder for your new widget. Inside it create another folder called `package`. Everything inside the `package` folder will be what we eventually zip and share online, so we can keep text editor project files in the `helloworld` folder.

Inside the package folder will be `metadata.desktop` file which is basically an Linux `.ini` file. This file will describe the name of the widget, the category it's in, and various other plasma specific keys like the main QML file.

Inside `contents`, we will create the `ui` and `config` folders. `ui` is the folder which should contain your layout files like the `main.qml` and the `configGeneral.qml`. The latter is the layout for the widget's configuration window.

Inside the `config` folder we have the `main.xml` which contains the schema of all our serialized configuration keys+values. The `config.qml` is used to define the tabs in the configuration window, and which QML layout file in the tab will open (like `ui/configGeneral.qml`).

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

`Icon` is the icon name associated with the widget. You can search for icon names in the `/usr/share/icon` folder. You can also look for an icon name by right clicking your app launcher widget then editing the icon in it's settings. It uses a searchable interface and lists them by category. Plasma's SDK also has the Cuttlefish app ([screenshot](https://www.kde.org/images/screenshots/cuttlefish.png)) which you can install with `sudo apt install plasma-sdk`.

`X-KDE-PluginInfo-Name` needs to be a unique name, since it's used for the folder name it's installed into. You could use `com.github.zren.helloworld` if you're on github, or use `org.kde.plasma.helloworld` if you're planning on contributing the widget to KDE.  

Widget's installed by the user (without root) like when you "Install New Widgets" will be installed to `~/.local/share/plasma/plasmoids/` (which may not yet exist). The default widgets shipped with KDE are installed to `/usr/share/plasma/plasmoids/`.

`X-KDE-PluginInfo-Category` is the category the widget can be filtered with in the widget list. A list of category names can be found [here](https://techbase.kde.org/Projects/Plasma/PIG).

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
X-KDE-PluginInfo-Website=https://github.com/Zren/plasma-applet-helloworld
X-KDE-PluginInfo-Category=System Information
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}contents/ui/main.qml{% endcapture %}
{% capture sectionLeft %}

This is the entry point. Various properties are available to be set. You should know that widgets have several ways of being represented. 

* You can have a widget in the panel, which is just an icon that will show a popup window when clicked.
* You can also have it on the desktop as a desktop widget which can be resized by the user. As a desktop widget it can switch between the "icon view", which opens a popup, and directly showing the popup on the desktop when there's enough room.
* You can also have the widget inside another widget (a containment) like the system tray or the panel itself.
* The widget can also be run like an application in it's own window.

`plasmoid.location` and `plasmoid.formFactor` can tell you how the widget is placed. `plasmoid` is a global variable which is defined when you `import org.kde.plasma.plasmoid 2.0`. Read more below.

`Plasmoid.compactRepresentation` (with a capital) and `Plasmoid.fullRepresentation` are used to define the layout of the small "icon" view and the full "popup" view. These are both properties of the main `Item`. If neither are set, by default the main `Item` is the full representation.

`Layout.preferredWidth` can be used to define the default width of a desktop/panel widget, or the size of the popup window (unless it is in the system tray). The system tray has a fixed hardcoded size for it's popups. It can also define the width of the compact "icon" view in the horizontal panel. Note that the `Layout.preferredWidth`/`Layout.preferredHeight` of the `Plasmoid.compactRepresentation` will automatically scale to the thickness of the panel depending on if it's a vertical or horizontal panel.

`Layout.minimumWidth` can be used to define the minimum size for a desktop widget / popup.

You can set the tooltip contents and various other things in the `main.qml`.

#### Examples of `main.qml`

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
We now have enough to test our widget. If you haven't yet, install the `plasma-sdk` package with `sudo apt install plasma-sdk`.
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
If we set `plasmoidviewer`'s `plasmoid.formFactor` to be `horizontal` and `plasmoid.location` to the `topedge` or `bottomedge`, we can test a widget focusing in the panel.
{% endcapture %}{% capture sectionRight %}

{% highlight bash %}
plasmoidviewer -a package -l topedge -f horizontal
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Testing DPI Scaling{% endcapture %}
{% capture sectionLeft %}
By setting the `QT_SCALE_FACTOR=2` we can double the DPI value to `192` just for the `plasmoidviewer` window. This is great for testing if your code will support a HiDPI screen.

If you're testing a very high DPI, you'll probably find the default `plasmoidviewer` window is too small to show the widget, so we'll set the size and position of the window. Note that the window will go maximized if you set a size larger than you screen has available.
{% endcapture %}{% capture sectionRight %}

{% highlight bash %}
QT_SCALE_FACTOR=2 plasmoidviewer -a package
QT_SCALE_FACTOR=2 plasmoidviewer -a package -l topedge -f horizontal -x 0 -y 0 -s 1920x1080
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Enable logging{% endcapture %}
{% capture sectionLeft %}
By default in Qt 5.9, `console.log()`, which used to write a string to stdout (the Terminal output), is hidden by default. In order to reenable it, we need to run `kwriteconfig5 --file ~/.config/QtProject/qtlogging.ini --group "Rules" --key "qml.debug" "true"` to configure it to do so.
{% endcapture %}{% capture sectionRight %}

{% highlight qml %}
Item {
    Component.onCompleted: {
        console.log("Hello World")
    }
}
{% endhighlight %}
{% highlight bash %}
kwriteconfig5 --file ~/.config/QtProject/qtlogging.ini --group "Rules" --key "qml.debug" "true"
{% endhighlight %}
{% highlight ini %}
[Rules]
qml.debug=true
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


<!-- ------- -->
{% include docHeader.html label="Qml" %}


{% capture label %}Quick Intro{% endcapture %}
{% capture sectionLeft %}

This is a quick intro to QML. If you're comfortable with it, skip to the next section.

The official QML tutorial can be found in the [QML Documentation](http://doc.qt.io/qt-5/qtqml-syntax-basics.html).

{% endcapture %}{% capture sectionRight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

{% capture label %}Item{% endcapture %}
{% capture sectionLeft %}

An [Item](http://doc.qt.io/qt-5/qml-qtquick-item.html) is a simple object. It can have children as well. Item's have a default width and height of 0px, and will not grow to fit their contents. So unlike the HTML box model, you'll need to use layouts mentioned below.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0

Item {
    id: widget

    Item {
        id: childItemA
    }

    Item {
        id: childItemB
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Rectangle{% endcapture %}
{% capture sectionLeft %}

If we want to draw a colored rectangle, we can easily do so with. For other properties of the [Rectangle](http://doc.qt.io/qt-5/qml-qtquick-rectangle.html), like border color and width, read it's [page in the QML Documentation](http://doc.qt.io/qt-5/qml-qtquick-rectangle.html).

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0

Rectangle {
    color: "#0ff" // Teal
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Items are 0px wide by default{% endcapture %}
{% capture sectionLeft %}

By default, an [Item](http://doc.qt.io/qt-5/qml-qtquick-item.html) will not expand to fit it's contents. Nor will it expand to fit the width of it's parent (like a `<div>` in HTML). So we need to scale.

In the this example, only the Teal Rectangle will be visible, since the Green Rectangle has the default width of 0px and height of 0px.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0

Rectangle { // Unlike everything else, the widget's main item will have a default size.
    color: "#0ff" // Teal
    
    Rectangle { // For everything else, we need to set the size.
        color: "#00f" // Green
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}anchors.fit{% endcapture %}
{% capture sectionLeft %}

In this second example, we make the Green Rectangle resize to the parent item, the Teal Rectangle. This will completely cover the Teal Rectangle so only the Green Rectangle will be visible.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0

Rectangle { // Unlike everything else, the widget's main item will have a default size.
    color: "#0ff" // Teal
    
    Rectangle { // For everything else, we need to set the size.
        color: "#00f" // Green
        anchors.fit: parent // Make sure we're the same size as the parent.
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}anchors.bottom{% endcapture %}
{% capture sectionLeft %}

In this third example, we anchor the Green Rectangle to the bottom right, and make it half the width & height of the Teal rectangle. So we end up with a rectangle which is 3/4 teal and 1/4 green.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0

Rectangle {
    color: "#0ff" // Teal
    
    Rectangle {
        color: "#00f" // Green
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        width: parent.width / 2
        height: parent.height / 2
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}ColumnLayout{% endcapture %}
{% capture sectionLeft %}

If you want to stack a number of items on top of each other, you should use a [ColumnLayout](http://doc.qt.io/qt-5/qml-qtquick-layouts-columnlayout.html).

Labels (which are just fancy Text items which follow Plasma's colors) have a default font size, which means they have their own default height. So they will be stacked on top of each other.

Note that if the ColumnLayout is taller than it's contents, the children will have padding between them.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0
import org.kde.plasma.components 2.0 as PlasmaComponents

ColumnLayout {
    PlasmaComponents.Label {
        text: "Item 1"
    }
    PlasmaComponents.Label {
        text: "Item 2"
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Layout.fitWidth: true{% endcapture %}
{% capture sectionLeft %}

If you want an item to scale to the parent's width, you have the option of setting it to be the same width as the parent (which doesn't work in a Layout). You can also try anchoring to the left and right (which does work).

Within a [Layout](http://doc.qt.io/qt-5/qml-qtquick-layouts-layout.html) however, the proper way to do so is to use the special property attached to the contents of a Layout, `Layout.fillWidth`. Setting it to `true` will make the item scale to fill up the empty space.

![](https://i.imgur.com/s2QXkON.png)

The other Layout related properties can be [read here](http://doc.qt.io/qt-5/qml-qtquick-layouts-layout.html).

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0

ColumnLayout {
    Rectangle {
        color: "#f00" // Red
        height: 40
        Layout.fillWidth: true
    }
    Rectangle {
        color: "#0f0" // Green
        height: 40
        width: parent.width // Does not work
    }
    Rectangle {
        color: "#00f" // Blue
        height: 40
        width: 40 // Does not fill parent
    }
    Rectangle {
        color: "#ff0" // Yellow
        height: 40
        anchors.left: parent.left
        anchors.right: parent.right
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Layout.fillHeight: true{% endcapture %}
{% capture sectionLeft %}

If you want one item (or several) in a Layout to expand to take up the unused space, you can use `Layout.fitHeight : true`.

![](https://i.imgur.com/xo0LyfQ.png)

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0

ColumnLayout {
    Rectangle {
        color: "#f00" // Red
        height: 40
        Layout.fillWidth: true
    }
    Rectangle {
        color: "#0f0" // Green
        Layout.fillHeight: true
        Layout.fillWidth: true
    }
    Rectangle {
        color: "#00f" // Blue
        Layout.fillHeight: true
        Layout.fillWidth: true
    }
    Rectangle {
        color: "#ff0" // Yellow
        height: 40
        Layout.fillWidth: true
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Spacing between items in a Layout{% endcapture %}
{% capture sectionLeft %}

In the last screenshot you might have noticed how there is still spacing between the items. That's because the default [ColumnLayout.spacing](http://doc.qt.io/qt-5/qml-qtquick-layouts-columnlayout.html#spacing-prop) property is set to `5`. Assigning it to `0` will remove the extra whitespace.

![](https://i.imgur.com/LuScHdK.png)

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0

ColumnLayout {
    spacing: 0

    Rectangle {
        color: "#f00" // Red
        height: 40
        Layout.fillWidth: true
    }
    Rectangle {
        color: "#0f0" // Green
        Layout.fillHeight: true
        Layout.fillWidth: true
    }
    Rectangle {
        color: "#00f" // Blue
        Layout.fillHeight: true
        Layout.fillWidth: true
    }
    Rectangle {
        color: "#ff0" // Yellow
        height: 40
        Layout.fillWidth: true
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

{% capture label %}Other Layouts{% endcapture %}
{% capture sectionLeft %}

There's also [RowLayout](http://doc.qt.io/qt-5/qml-qtquick-layouts-rowlayout.html) and [GridLayout](http://doc.qt.io/qt-5/qml-qtquick-layouts-gridlayout.html). Lastly there's [Flow](http://doc.qt.io/qt-5/qml-qtquick-flow.html) which will treat it's contents as if they all had the CSS `display: inline-block`.

![](https://i.imgur.com/qrDdw8L.png)

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0
import org.kde.plasma.components 2.0 as PlasmaComponents

RowLayout {
    PlasmaComponents.Label {
        text: "Item 1"
    }
    PlasmaComponents.Label {
        text: "Item 2"
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}



<!-- ------- -->
{% include docHeader.html label="Plasma's QML API" %}


{% capture label %}Intro{% endcapture %}
{% capture sectionLeft %}
KDE Frameworks ships with a number of useful extensions to Qt's QML. The [API documentation](https://api.kde.org/frameworks/plasma-framework/html/index.html) is a good start if you need to know what a specific property does. If you want to browse any of the sources easier, it's also [mirrored on GitHub](https://github.com/KDE/plasma-framework/tree/master/src/declarativeimports/).


{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}PlasmaComponents.Label{% endcapture %}
{% capture sectionLeft %}

QML ships with a [Text](http://doc.qt.io/qt-5/qml-qtquick-text.html) type, but Plasma extends with a `Label.qml` which asigns a number of defaults. One thing that is defaulted is it uses the color scheme's text color. For the specifics, you can read the [`Label.qml` source code](https://github.com/KDE/plasma-framework/blob/master/src/declarativeimports/plasmacomponents/qml/Label.qml).

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
import QtQuick 2.0
import org.kde.plasma.components 2.0 as PlasmaComponents

PlasmaComponents.Label {
    text: "Hello World"
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


<!-- ------- -->
{% include docHeader.html label="Configuration" %}


{% capture label %}Configuration Intro{% endcapture %}
{% capture sectionLeft %}

Every widget by default has a configure action when you right click the widget called `MyWidget Settings...`. By default it will contain a form to set a global shortcut to activate your widget.

![](https://i.imgur.com/gle3dAy.png)

{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}contents/config/main.xml{% endcapture %}
{% capture sectionLeft %}
`main.xml` is where you define the properties that will be serialized into `~/.config/plasma-org.kde.plasma.desktop-appletsrc`. All properties will be accesible with `plasmoid.configuration.variableName` reguardless of was group it's in.
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}contents/config/config.qml{% endcapture %}
{% capture sectionLeft %}
`config.qml` is where we define the tabs in the configuration window.
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

{% capture label %}contents/ui/configGeneral.qml{% endcapture %}
{% capture sectionLeft %}
`configGeneral.qml` is where we can place all the checkboxes and textboxes.

By default, all values are copied to cfg_variableName. This is so the user can hit discard or apply at leisure.


{% endcapture %}{% capture sectionRight %}
import QtQuick.Controls 1.4
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}configPage.cfg_variableName{% endcapture %}
{% capture sectionLeft %}

By default, all values are copied to the top level Item of the file prefixed with `cfg_` like `cfg_variableName`. This is so the user can hit discard or apply the changes. You will need to define each `cfg_` so you can assign to it with a QML control.

Note that you can use a property [alias](http://doc.qt.io/qt-5/qtqml-syntax-objectattributes.html#property-aliases) to a control's property like `checkBox.checked` or `textField.text`.

> TODO: Confirm if configuration keys from other groups are copied to the current page's `cfg_` variables.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// configGeneral.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4

Item {
    id: page
    property alias cfg_variableName: variableName.checked

    CheckBox {
        id: variableName
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}CheckBox{% endcapture %}
{% capture sectionLeft %}

[CheckBox](http://doc.qt.io/qt-5/qml-qtquick-controls-checkbox.html)es are usually used for boolean on/off types. See the [Visual Design Group's tips](https://community.kde.org/KDE_Visual_Design_Group/HIG/CheckBox) on usuing CheckBoxes.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// configGeneral.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4

Item {
    id: page
    property alias cfg_variableName: variableName.checked

    CheckBox {
        id: variableName
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Assigning to plasmoid.configuration.variableName{% endcapture %}
{% capture sectionLeft %}

You can also assign directly to `plasmoid.configuration.variableName` if necessary in the configruation window or anywhere else in your widget. If you do this in the configuration page, you will skip the "apply" process and the property will be applied right away. I leave this up to the reader wither this is a pro or con.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// configGeneral.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4

Item {
    id: page

    CheckBox {
        id: variableName
        checked: plasmoid.configuration.variableName
        onCheckedChanged: plasmoid.configuration.variableName = checked
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}No-Apply Control Library{% endcapture %}
{% capture sectionLeft %}

I have written a few files that apply the above pattern of skipping "Apply" and updating right after you change the value.

{% endcapture %}{% capture sectionRight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}ConfigCheckBox{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// ConfigCheckBox.qml
import QtQuick 2.0
import QtQuick.Controls 1.0
import QtQuick.Layouts 1.0

CheckBox {
    id: configCheckBox

    property string configKey: ''
    checked: plasmoid.configuration[configKey]
    onClicked: plasmoid.configuration[configKey] = !plasmoid.configuration[configKey]
}
{% endhighlight %}

{% highlight qml %}
// configGeneral.qml
import QtQuick 2.0
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.4

Item {
    id: page

    ConfigCheckBox {
        id: variableName
        configKey: 'variableName'
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


<!-- ------- -->
{% include docHeader.html label="Translations/i18n" %}


{% capture label %}ki18n{% endcapture %}
{% capture sectionLeft %}
[Ki18n](https://api.kde.org/frameworks/ki18n/html/index.html) (<b>K</b>DE <b>i</b>nternationalizatio<b>n</b>) is the translation library for KDE. It has a [programmer's guide](https://api.kde.org/frameworks/ki18n/html/prg_guide.html) which you can read, but we'll cover the basics here.
{% endcapture %}{% capture sectionRight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}i18n(){% endcapture %}
{% capture sectionLeft %}
Translated strings need to be wrapped in the `i18n(...)` function. Note that single quotes `i18n('Test')` will be ignored by the tool that parses your code for all the translation strings. Always use double quotes `i18n("Test")`.
{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// configGeneral.qml
CheckBox {
    id: showThing
    label: i18n("Show notification")
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Variables in i18n(){% endcapture %}
{% capture sectionLeft %}
The `i18n(...)` is an overloaded function which allows you to pass values into the translation `i18n(format, variable1, variable2)`. Just place `%1` where you want the first variable to be substitued, and `%2` where the second should go.
{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
Item {
    id: showThing
    property int unreadEmailCount: 3
    Plasmoid.toolTipSubText: i18n("%1 unread emails", unreadEmailCount)
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

{% capture label %}Plural in i18n(){% endcapture %}
{% capture sectionLeft %}
In English, a translated sentence will is different when there's just 1 item and when there is 2 or more items. `i18np(...)` can be used in such a situation.

An example from the [Ki18n docs](https://api.kde.org/frameworks/ki18n/html/prg_guide.html#write_i18n) is:

{% highlight qml %}
i18np("One image in album %2", "%1 images in album %2", numImages, albumName)
{% endhighlight %}

{% highlight qml %}
i18np("One image in album %2", "More images in album %2", numImages, albumName)
{% endhighlight %}

Using `i18np(...)` can improve our previous example. When `unreadEmailCount` was `1`, the tooltip would have read `"1 unread emails"`.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// main.qml
Item {
    id: showThing
    property int unreadEmailCount: 3
    Plasmoid.toolTipSubText: i18np("%1 unread email", "%1 unread emails", unreadEmailCount)
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

{% capture label %}Translation Folder Structure{% endcapture %}
{% capture sectionLeft %}
After we've wrapped all the messages in our code with `i18n(...)` calls, we then need to extract all the messages for our translators into a `template.pot` file which they can then create a `fr.po` for their French translations.

We'll place the `template.pot` file under a `translate` folder inside the bundled package so that our users can easily translate our widget when they go poking into our code.

We'll also create a `merge.sh` script which will extract the messages from our code into a `template.pot`, then update the translated `fr.po` file with any changes.

Lastly, we'll make a `build.sh` script to convert the `fr.po` text files into the binary `.mo` files which are needed for KDE to recognize the translations.

The latest copy of my `merge.sh` and `build.sh` can be found in any of my widgets:

* [`translate/merge.sh`](https://github.com/Zren/plasma-applet-tiledmenu/blob/master/package/translate/merge)
* [`translate/build.sh`](https://github.com/Zren/plasma-applet-tiledmenu/blob/master/package/translate/build)
{% endcapture %}{% capture sectionRight %}

* `helloworld/`
    * `package/`
        * `contents/`
            * `...`
        * `translate/`
            * `template.pot`
            * `build.sh`
            * `merge.sh`
        * `metadata.desktop`

After running `build.sh` we should end up with:

* `helloworld/`
    * `package/`
        * `contents/`
            * `locale/`
                * `fr/`
                    * `LC_MESSAGES/`
                        * `plasma_applet_com.github.zren.helloworld.mo`
        * `...`

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Install GetText{% endcapture %}
{% capture sectionLeft %}
After we've wrapped all the messages in our code with `i18n(...)` calls, we then need to extract all the messages for our translators into a `template.pot` file.

To do this, we need to install the `gettext` package.
{% endcapture %}{% capture sectionRight %}
{% highlight bash %}
sudo apt install gettext
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Generating template.pot{% endcapture %}
{% capture sectionLeft %}
First thing we need to do in our `merge.sh` script, is list all files we wish to get translated in our widgets code.

> The latest copy of my complete `merge.sh` script [can be found here](https://github.com/Zren/plasma-applet-tiledmenu/blob/master/package/translate/merge).
{:.alert.alert-secondary}

`DIR` is the directory (absolute path to `package/translate/`) since we may run the merge script from another directory.

We use `kreadconfig5` to grab the widget's namespace (`com.github.zren.helloworld`) and store it in `plasmoidName`. We then remove the beginning of the namespace so we are left with `helloworld` and store that in `widgetName`. We also grab the website which a link to the GitHub repo for use as the `bugAddress`.

After validating that `plasmoidName` is not an empty string with bash's `[ -z "$plasmoidName" ]` operator, we then list all `.qml` and `.js` files using `find` and store the results of the command in a temporary `infiles.list` file.

Then we generate a `template.pot.new` using the `xgettext` command. After generating it, we use `sed` to replace a few placeholder strings.

{% endcapture %}{% capture sectionRight %}
`translate/merge.sh`
{% highlight bash %}
#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" # Script's directory
plasmoidName=`kreadconfig5 --file="$DIR/../metadata.desktop" --group="Desktop Entry" --key="X-KDE-PluginInfo-Name"`
widgetName="${plasmoidName##*.}" # Strip namespace
website=`kreadconfig5 --file="$DIR/../metadata.desktop" --group="Desktop Entry" --key="X-KDE-PluginInfo-Website"`
bugAddress="$website"
packageRoot=".." # Root of translatable sources
projectName="plasma_applet_${plasmoidName}" # project name

#---
if [ -z "$plasmoidName" ]; then
    echo "[merge] Error: Couldn't read plasmoidName."
    exit
fi

#---
echo "[merge] Extracting messages"
find "${packageRoot}" -name '*.cpp' -o -name '*.h' -o -name '*.c' -o -name '*.qml' -o -name '*.js' | sort > "${DIR}/infiles.list"

xgettext --from-code=UTF-8 -C -kde -ci18n -ki18n:1 -ki18nc:1c,2 -ki18np:1,2 -ki18ncp:1c,2,3 \
    -ktr2i18n:1 -kI18N_NOOP:1 -kI18N_NOOP2:1c,2  -kN_:1 -kaliasLocale -kki18n:1 -kki18nc:1c,2 \
    -kki18np:1,2 -kki18ncp:1c,2,3 --msgid-bugs-address="${bugAddress}" --files-from=infiles.list \
    --width=200 --package-name="${widgetName}" --package-version="" \
    -D "${packageRoot}" -D "${DIR}" -o "template.pot.new" || \
    { echo "[merge] error while calling xgettext. aborting."; exit 1; }

sed -i 's/# SOME DESCRIPTIVE TITLE./'"# Translation of ${widgetName} in LANGUAGE"'/' "template.pot.new"
sed -i 's/# Copyright (C) YEAR THE PACKAGE'"'"'S COPYRIGHT HOLDER/'"# Copyright (C) $(date +%Y)"'/' "template.pot.new"
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Updating template.pot{% endcapture %}
{% capture sectionLeft %}
Continuing our `merge.sh` script, we then check to see if an older `template.pot` file exists.

If it does, we'll replace the `POT-Creation-Date` in the new file with the older creation date, then run the `diff` command to detect if there's been any changes. If there has been changes, we fix the `POT-Creation-Date` and overwrite the old `template.pot` file. To make the changes more noticeable, we also list the added/removed translation messages.

If there hasn't been any changes, we simply delete the `template.pot.new` file.

Lastly, we delete the `infiles.list` to clean things up.
{% endcapture %}{% capture sectionRight %}
{% highlight bash %}
if [ -f "template.pot" ]; then
    newPotDate=`grep "POT-Creation-Date:" template.pot.new | sed 's/.\{3\}$//'`
    oldPotDate=`grep "POT-Creation-Date:" template.pot | sed 's/.\{3\}$//'`
    sed -i 's/'"${newPotDate}"'/'"${oldPotDate}"'/' "template.pot.new"
    changes=`diff "template.pot" "template.pot.new"`
    if [ ! -z "$changes" ]; then
        # There's been changes
        sed -i 's/'"${oldPotDate}"'/'"${newPotDate}"'/' "template.pot.new"
        mv "template.pot.new" "template.pot"

        addedKeys=`echo "$changes" | grep "> msgid" | cut -c 9- | sort`
        removedKeys=`echo "$changes" | grep "< msgid" | cut -c 9- | sort`
        echo ""
        echo "Added Keys:"
        echo "$addedKeys"
        echo ""
        echo "Removed Keys:"
        echo "$removedKeys"
        echo ""

    else
        # No changes
        rm "template.pot.new"
    fi
else
    # template.pot didn't already exist
    mv "template.pot.new" "template.pot"
fi

rm "${DIR}/infiles.list"
echo "[merge] Done extracting messages"
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Examining template.pot{% endcapture %}
{% capture sectionLeft %}
Now that we've got a `template.pot`, let's take a look at it.

The messages we want to translate appear as `msgid "Show Thing"`, with the file it came from appearing in a comment in the line above. Underneath is an empty `msgstr ""` which is where the translator will place the translated messages.
{% endcapture %}{% capture sectionRight %}
{% highlight po %}
# Translation of helloworld in LANGUAGE
# Copyright (C) 2018
# This file is distributed under the same license as the helloworld package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: helloworld \n"
"Report-Msgid-Bugs-To: https://github.com/Zren/plasma-applet-helloworld\n"
"POT-Creation-Date: 2018-12-03 18:47-0500\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"Language: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=CHARSET\n"
"Content-Transfer-Encoding: 8bit\n"

#: ../contents/configGeneral.qml:10
msgid "Show notification"
msgstr ""

#: ../contents/ui/configGeneral.qml:20
msgid "%1 unread emails"
msgstr ""

#: ../contents/ui/configGeneral.qml:30
msgid "%1 unread email"
msgid_plural "%1 unread emails"
msgstr[0] ""
msgstr[1] ""
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}fr.po{% endcapture %}
{% capture sectionLeft %}
Now that we've got a `template.pot`, our translators can copy it and rename it to `fr.po`.

We use `fr` since it is the locale code for French, which we'll be using later.

A full list of locale codes [can be found on StackOverflow](https://stackoverflow.com/questions/3191664/list-of-all-locales-and-their-short-codes#answer-28357857). Make sure you use underscores (`fr_CA`) instead of dashes (`fr-CA`) if the language you are translating is not reusable for the generic `fr` language.

Translators can then start filling out the empty `msgstr ""` with translations.
{% endcapture %}{% capture sectionRight %}
{% highlight po %}
#: ../contents/configGeneral.qml:10
msgid "Show notification"
msgstr "Montrer les notifications"
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Merging updates into fr.po{% endcapture %}
{% capture sectionLeft %}
Our `merge.sh` currently only extracts messages into `template.pot`. We should next merge the any new messages for translation into our `fr.po` file.

We'll first filter the translate directory for `.po` files.

Then for each `.po` file, we'll extract the locale code (`fr`) from the filename using the `basename` command then striping out the file extension.

We then use another GetText command `msgmerge` to generate a new `fr.po.new` file based on the old `fr.po` and the current `template.pot`.

Afterwards, we use `sed` to replace the `LANGUAGE` placeholder with our current locale code in case our translator left them as is.

When we're done, we overwrite the old `fr.po` with `fr.po.new`.

{% endcapture %}{% capture sectionRight %}
`translate/merge.sh`
{% highlight bash %}
#---
echo "[merge] Merging messages"
catalogs=`find . -name '*.po' | sort`
for cat in $catalogs; do
    echo "[merge] $cat"
    catLocale=`basename ${cat%.*}`
    msgmerge \
        --width=400 \
        --no-fuzzy-matching \
        -o "$cat.new" "$cat" "${DIR}/template.pot"
    sed -i 's/# SOME DESCRIPTIVE TITLE./'"# Translation of ${widgetName} in ${catLocale}"'/' "$cat.new"
    sed -i 's/# Translation of '"${widgetName}"' in LANGUAGE/'"# Translation of ${widgetName} in ${catLocale}"'/' "$cat.new"
    sed -i 's/# Copyright (C) YEAR THE PACKAGE'"'"'S COPYRIGHT HOLDER/'"# Copyright (C) $(date +%Y)"'/' "$cat.new"

    mv "$cat.new" "$cat"
done

echo "[merge] Done merging messages"
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Building .mo{% endcapture %}
{% capture sectionLeft %}
Once our `fr.po` has been filled out, we can then convert it to a binary `.mo` file. So lets get started on our `build.sh` script.

> The latest copy of my complete `build.sh` script [can be found here](https://github.com/Zren/plasma-applet-tiledmenu/blob/master/package/translate/build).
{:.alert.alert-secondary}

We start with the same code that we used in our `merge.sh` script to parse our `metadata.desktop` file and get the widget's namespace. We also reuse the same code to iterate the `.po` files.

Then we use another GetText command `msgfmt` to convert the `fr.po` file into a `fr.mo` file.

We then make sure a `contents/locale/fr/LC_MESSAGES/` folder exists, creating it if it does not.

Then we copy the `fr.mo` to the `LC_MESSAGES` folder, renaming it to `plasma_applet_com.github.zren.helloworld.mo`. Notice that we put `plasma_applet_` in front of the widget's namespace.
{% endcapture %}{% capture sectionRight %}
{% highlight bash %}
#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" # Script's directory
plasmoidName=`kreadconfig5 --file="$DIR/../metadata.desktop" --group="Desktop Entry" --key="X-KDE-PluginInfo-Name"`
website=`kreadconfig5 --file="$DIR/../metadata.desktop" --group="Desktop Entry" --key="X-KDE-PluginInfo-Website"`
bugAddress="$website"
packageRoot=".." # Root of translatable sources
projectName="plasma_applet_${plasmoidName}" # project name

#---
if [ -z "$plasmoidName" ]; then
    echo "[build] Error: Couldn't read plasmoidName."
    exit
fi

#---
echo "[build] Compiling messages"

catalogs=`find . -name '*.po' | sort`
for cat in $catalogs; do
    echo "$cat"
    catLocale=`basename ${cat%.*}`
    msgfmt -o "${catLocale}.mo" "$cat"

    installPath="$DIR/../contents/locale/${catLocale}/LC_MESSAGES/${projectName}.mo"

    echo "[build] Install to ${installPath}"
    mkdir -p "$(dirname "$installPath")"
    mv "${catLocale}.mo" "${installPath}"
done

echo "[build] Done building messages"
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Testing our translations{% endcapture %}
{% capture sectionLeft %}
First make sure you run our `build.sh` translation script.

Then we need to override the locale environment variables just for our `plasmoidviewer` instance. If you run the `locale` command, it should list all the environment variables available to override.

In practice, we only need to override `LANG="fr_CA.UTF-8"` and another variable it didn't list `LANGUAGE="fr_CA:fr"`. If your widget is a clock, then you might also need to override `LC_TIME="fr_FR.UTF-8"`.
{% endcapture %}{% capture sectionRight %}
{% highlight bash %}
sh package/translate/build.sh
LANGUAGE="fr_CA:fr" LANG="fr_CA.UTF-8" plasmoidviewer -a package
{% endhighlight %}

{% highlight bash %}
$ locale
LANG=en_CA.UTF-8
LC_CTYPE="en_CA.UTF-8"
LC_NUMERIC=en_CA.UTF-8
LC_TIME=en_US.UTF-8
LC_COLLATE="en_CA.UTF-8"
LC_MONETARY=en_CA.UTF-8
LC_MESSAGES="en_CA.UTF-8"
LC_PAPER=en_CA.UTF-8
LC_NAME=en_CA.UTF-8
LC_ADDRESS=en_CA.UTF-8
LC_TELEPHONE=en_CA.UTF-8
LC_MEASUREMENT=en_CA.UTF-8
LC_IDENTIFICATION=en_CA.UTF-8
LC_ALL=
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}Reusing other translations{% endcapture %}
{% capture sectionLeft %}
While it's bad practice to link to private code, if you know another widget a translated string, you can use `i18nd(domain, string, ...)` to use translations from that domain. Note that a widget's domain starts with `plasma_applet_`, and ends with the widget's `X-KDE-PluginInfo-Name`.

Eg: `plasma_applet_com.github.zren.helloworld`

An example can be found in `org.kde.image`'s [main.qml](https://github.com/KDE/plasma-workspace/blob/master/wallpapers/image/imagepackage/contents/ui/main.qml) which reuses the same code for the `org.kde.slideshow`.

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
Item {
    Button {
        text: i18nd("plasma_applet_org.kde.image", "Open Wallpaper Image")
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

<!-- ------- -->
{% include docHeader.html label="Examples" %}


{% capture label %}Time DataSource{% endcapture %}
{% capture sectionLeft %}
An extremely simple example of this can be found in the "fuzzy clock" widget in the `kdeplasma-addons` repo ([link](https://github.com/KDE/kdeplasma-addons/blob/master/applets/fuzzy-clock/package/contents/ui/main.qml)).

The `new Date()` should be familiar if you come from a javascript background. We could use a Timer with the Date type, but we want to precisely sync all clock widgets so they all show the same time on all screens. This is where Plasma's DataEngines come in. They are used to share data between widgets. There are [various dataengines](https://github.com/KDE/plasma-workspace/tree/master/dataengines) for notifications, plugged in usb drives (hotplug), and event the weather data so it only has to fetch the data once to show it in all widgets on each screen.

To use the "time" data engine, we use [`PlasmaCore.DataSource`](https://github.com/KDE/plasma-framework/blob/master/src/declarativeimports/core/datasource.h) to connect to it. The "time" needs us to connect to our "Local" timezone. Once connected, it gives us a DateTime object we can access using `dataSource.data.Local.DateTime`. This property will update every 60000 milliseconds, or every 1 minute.

We also tell the data engine to align these updates to the next minute. If we want to modify this to update every second, we'd change the interval to `interval: 1000` (1 second), then remove the `intervalAlignment` assignment since there isn't an "AlignToSecond", just a [`PlasmaCore.Types.NoAlignment`](https://api.kde.org/frameworks/plasma-framework/html/classPlasma_1_1Types.html#ab7f729a56f6c44a067c79ca5354b8d64).

A clock can then use Qt's `Qt.formatTime(currentDateTime)` to display the time in a human readable format. You can read more about that function on the Qt documentation for [`Qt.formatDateTime(...)`](http://doc.qt.io/qt-5/qml-qtqml-qt.html#formatDateTime-method).

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
import QtQuick 2.0
import QtQuick.Layouts 1.1

import org.kde.plasma.plasmoid 2.0
import org.kde.plasma.core 2.0 as PlasmaCore
import org.kde.plasma.components 2.0 as PlasmaComponents
import org.kde.plasma.extras 2.0 as PlasmaExtras
import org.kde.plasma.calendar 2.0 as PlasmaCalendar

Item {
    id: root

    readonly property date currentDateTime: dataSource.data.Local ? dataSource.data.Local.DateTime : new Date()

    width: units.gridUnit * 10
    height: units.gridUnit * 4

    Plasmoid.preferredRepresentation: Plasmoid.compactRepresentation

    Plasmoid.toolTipMainText: Qt.formatTime(currentDateTime)
    Plasmoid.toolTipSubText: Qt.formatDate(currentDateTime, Qt.locale().dateFormat(Locale.LongFormat))

    PlasmaCore.DataSource {
        id: dataSource
        engine: "time"
        connectedSources: ["Local"]
        interval: 60000
        intervalAlignment: PlasmaCore.Types.AlignToMinute
    }

    Plasmoid.compactRepresentation: FuzzyClock { }

    Plasmoid.fullRepresentation: PlasmaCalendar.MonthView {
        Layout.minimumWidth: units.gridUnit * 20
        Layout.minimumHeight: units.gridUnit * 20

        today: currentDateTime
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}...{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

<script type="text/javascript" src="/js/livereload.js"></script>
