<!-- ------- -->
{% include docHeader.html
    label="Examples"
    editUrl="https://github.com/Zren/zren.github.io/blob/master/kde_docs/widget-Examples.md"
%}

{% capture label %}Configurable panel widget width/height{% endcapture %}
{% capture sectionLeft %}
While the user can resize the popup window temporarily with `Alt+RightClick+Drag`, it will reset on when the user relogs. To allow the user to permanently configure the popup size in a panel widget, or the size of the compact view in the panel, we'll need a store the width/height in the config.

So we change to our hardcoded sizes:

{% highlight qml %}
// ui/main.qml
Item {
    id: widget
    Plasmoid.fullRepresentation: Item {
        Layout.preferredWidth: 640 * units.devicePixelRatio
        Layout.preferredHeight: 480 * units.devicePixelRatio
    }
}
{% endhighlight %}

into this:

{% highlight qml %}
// ui/main.qml
Item {
    id: widget
    Plasmoid.fullRepresentation: Item {
        Layout.preferredWidth: plasmoid.configuration.width * units.devicePixelRatio
        Layout.preferredHeight: plasmoid.configuration.height * units.devicePixelRatio
    }
}
{% endhighlight %}

Make sure you still multiply the stored width/height by `units.devicePixelRatio`, otherwise your popup will look smaller by default on HiDPI/4k monitors.

To simplify testing, I added `Plasmoid.hideOnWindowDeactivate: false` to prevent the popup from closing when you focus the config window.

Next we register the config keys and their default values in the `config/main.xml`.

Then create a configuration form in `ui/configGeneral.qml`. We use [`SpinBox`](https://doc.qt.io/qt-5/qml-qtquick-controls2-spinbox.html) and set the max value to [the maximum signed integer value in QML](https://stackoverflow.com/questions/41378583/qml-highest-number-float-integer-possible).

Lastly we register the General config tab in `config/config.qml`.

{% endcapture %}{% capture sectionRight %}

{% highlight qml %}
// ui/main.qml
Item {
    id: widget
    Plasmoid.fullRepresentation: Item {
        id: popupView
        Layout.preferredWidth: plasmoid.configuration.width * units.devicePixelRatio
        Layout.preferredHeight: plasmoid.configuration.height * units.devicePixelRatio
        Plasmoid.hideOnWindowDeactivate: false
        ColumnLayout {
            id: layout
            anchors.fill: parent
            PlasmaComponents.Label {
                text: i18n("Size: %1 x %2", popupView.width, popupView.height)
            }
        }
    }
}
{% endhighlight %}

-----

{% highlight xml %}
<!-- config/main.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<kcfg xmlns="http://www.kde.org/standards/kcfg/1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.kde.org/standards/kcfg/1.0 http://www.kde.org/standards/kcfg/1.0/kcfg.xsd">
    <kcfgfile name=""/>

    <group name="General">
        <entry name="width" type="int">
            <default>640</default>
        </entry>
        <entry name="height" type="int">
            <default>480</default>
        </entry>
    </group>
</kcfg>
{% endhighlight %}

-----

{% highlight qml %}
// ui/configGeneral.qml
import QtQuick 2.0
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.12
import org.kde.kirigami 2.4 as Kirigami

Item {
    id: page
    width: childrenRect.width
    height: childrenRect.height

    property alias cfg_width: widthSpinBox.value
    property alias cfg_height: heightSpinBox.value

    Kirigami.FormLayout {
        anchors.left: parent.left
        anchors.right: parent.right

        RowLayout {
            Kirigami.FormData.label: i18n("Size:")
            SpinBox {
                id: widthSpinBox
                from: 0
                to: 2147483647 // 2^31-1
            }
            Label {
                text: " x "
            }
            SpinBox {
                id: heightSpinBox
                from: 0
                to: 2147483647 // 2^31-1
            }
        }
    }
}
{% endhighlight %}

-----

{% highlight qml %}
// config/config.qml
import QtQuick 2.0
import org.kde.plasma.configuration 2.0

ConfigModel {
    ConfigCategory {
        name: i18n("General")
        icon: "configure"
        source: "configGeneral.qml"
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


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


{% capture label %}Avoid widget resize on text change{% endcapture %}
{% capture sectionLeft %}
We use [`TextMetrics`](https://doc.qt.io/qt-5/qml-qtquick-textmetrics.html) to calculate the size of the [Text](https://doc.qt.io/qt-5/qml-qtquick-text.html) label when it is the widest/maximum value of `100%`.
{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
import QtQuick 2.4
import QtQuick.Layouts 1.0
import org.kde.plasma.components 2.0 as PlasmaComponents
import org.kde.plasma.plasmoid 2.0

Item {
    id: widget
    property int value: 0
    property int maxValue: 100
    function formatText(n) {
        return "" + n + "%"
    }

    Plasmoid.preferredRepresentation: Plasmoid.compactRepresentation

    Plasmoid.compactRepresentation: PlasmaComponents.Label {
        id: label
        Layout.minimumWidth: textMetrics.width
        Layout.minimumHeight: textMetrics.height

        text: widget.formatText(value)

        font.pointSize: 40
        horizontalAlignment: Text.AlignHCenter

        TextMetrics {
            id: textMetrics
            font.family: label.font.family
            font.pointSize: label.font.pointSize
            text: widget.formatText(100)
        }

        // Since we overrode the default compactRepresentation,
        // we need to setup the click to toggle the popup.
        MouseArea {
            anchors.fill: parent
            onClicked: plasmoid.expanded = !plasmoid.expanded
        }
    }

    Plasmoid.fullRepresentation: Item {
        Layout.preferredWidth: 640 * units.devicePixelRatio
        Layout.preferredHeight: 480 * units.devicePixelRatio

        Rectangle {
            id: popup
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            width: parent.width * (widget.value / 100)
            color: theme.highlightColor
        }
    }

    Timer {
        interval: 100
        running: true
        repeat: true
        onTriggered: widget.value = (widget.value + 1) % (widget.maxValue+1)
    }
}
{% endhighlight %}
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

{% capture label %}Bundle icon/svg with widget{% endcapture %}
{% capture sectionLeft %}
If we're packaging a QML only widget to be put on the [KDE Store](https://store.kde.org), we won't be able to install an icon to `/usr/share/icons/`. Instead we'll package the icon in the widget directory. For this example, we will place our icon in `contents/icons/customicon.svg`. Copy `/usr/share/icons/breeze/apps/22/kde.svg` as a placeholder if you don't have an icon drawn up yet.

The [`DefaultCompactRepresentation.qml`](https://github.com/KDE/plasma-desktop/blob/master/desktoppackage/contents/applet/DefaultCompactRepresentation.qml) uses `PlasmaCore.IconItem`, which supports a `source: "iconname"` only if the icon is installed to `/usr/share/icons/`. Instead we'll need to use the full path to the svg.

Eg: `source: "/path/.../contents/icon/customicon.svg"`

Use `plasmoid.file('', 'icons/customicon.svg')` to get the absolute path to that file. Note that [`plasmoid.file()`](https://github.com/KDE/plasma-framework/blob/master/src/scriptengines/qml/plasmoid/appletinterface.h#L303-L310) calls [`KPackage::filePath()`](https://github.com/KDE/kpackage/blob/master/src/kpackage/package.h#L139-L151) which will return an empty string if the file does not exist.

{% highlight qml %}
PlasmaCore.IconItem {
    source: plasmoid.file('', 'icons/customicon.svg')
}
{% endhighlight %}

Unfortunately, the `PlasmaCore.IconItem` image loading logic will not apply the Color Scheme colors if you use an absolute filepath. It only applies the Color Scheme colors if you use `source: "iconname"`. To workaround this, we'll use a [`PlasmaCore.SvgItem`]() + [`PlasmaCore.Svg`]().

{% highlight qml %}
Item {
    id: appletIcon
    readonly property int minSize: Math.min(width, height)
    PlasmaCore.SvgItem {
        id: svgItem
        anchors.centerIn: parent
        readonly property real minSize: Math.min(naturalSize.width, naturalSize.height)
        readonly property real widthRatio: naturalSize.width / svgItem.minSize
        readonly property real heightRatio: naturalSize.height / svgItem.minSize
        width: appletIcon.minSize * widthRatio
        height: appletIcon.minSize * heightRatio
        smooth: true
        svg: PlasmaCore.Svg {
            id: svg
            imagePath: plasmoid.file('', 'icons/customicon.svg')
        }
    }
}
{% endhighlight %}

I've written [`AppletIcon.qml`](https://github.com/Zren/plasma-applet-lib/blob/master/package/contents/ui/lib/AppletIcon.qml) which allows you to easily use `AppletIcon { source: "customicon" }` to draw the icon with `PlasmaCore.SvgItem`. It also supports `AppletIcon { source: "kde" }` which first checks to see if `icons/kde.svg` exists, then falls back to the `kde` icon from the icon theme. This way you can easily support a configrable icon in your widget.

Now that we've drawn the icon, we need to fixup `customicon.svg` to support the color scheme. I will summarize the Plasma Style (aka desktoptheme) [documentation on system colors](https://techbase.kde.org/Development/Tutorials/Plasma5/ThemeDetails#Using_system_colors) here.

Open up [`kde.svg`](https://github.com/KDE/breeze-icons/blob/master/icons/apps/22/kde.svg?short_path=87978f1) up in a text editor, you'll see:

{% highlight xml %}
<style type="text/css" id="current-color-scheme">
    .ColorScheme-Text { color:#232629; }
</style>
<path class="ColorScheme-Text" style="fill:currentColor" ... />
{% endhighlight %}

The contents of the `<style id="current-color-scheme" />` stylesheet is replaced with [generated CSS](https://github.com/KDE/kiconthemes/blob/master/src/kiconloader.cpp#L64) with the current Color Scheme colors when the icon is loaded. The normal `<path style="fill:#111111">` has also been edited to use `fill:currentColor` which uses the `class="ColorScheme-Text"` color.

Finally, if you edit `customicon.svg`, you may need to delete the svg cache to see changes. I usually run it before `plasmoidviewer` when testing a widget with a bundled SVG.

{% highlight bash %}
rm ~/.cache/plasma-svgelements-*
{% endhighlight %}

{% endcapture %}{% capture sectionRight %}
{% highlight qml %}
// contents/ui/AppletIcon.qml
import QtQuick 2.0
import org.kde.plasma.core 2.0 as PlasmaCore

Item {
    id: appletIcon
    property string source: ''
    property bool active: false
    readonly property bool usingPackageSvg: filename // plasmoid.file() returns "" if file doesn't exist.
    readonly property string filename: source ? plasmoid.file('', 'icons/' + source + ".svg") : ''
    readonly property int minSize: Math.min(width, height)
    property bool smooth: true

    PlasmaCore.IconItem {
        anchors.fill: parent
        visible: !appletIcon.usingPackageSvg
        source: appletIcon.usingPackageSvg ? '' : appletIcon.source
        active: appletIcon.active
        smooth: appletIcon.smooth
    }

    PlasmaCore.SvgItem {
        id: svgItem
        anchors.centerIn: parent
        readonly property real minSize: Math.min(naturalSize.width, naturalSize.height)
        readonly property real widthRatio: naturalSize.width / svgItem.minSize
        readonly property real heightRatio: naturalSize.height / svgItem.minSize
        width: appletIcon.minSize * widthRatio
        height: appletIcon.minSize * heightRatio

        smooth: appletIcon.smooth

        visible: appletIcon.usingPackageSvg
        svg: PlasmaCore.Svg {
            id: svg
            imagePath: appletIcon.filename
        }
    }
}
{% endhighlight %}
-----
{% highlight qml %}
// contents/ui/main.qml
import QtQuick 2.0
import QtQuick.Layouts 1.1
import org.kde.plasma.plasmoid 2.0
import org.kde.plasma.core 2.0 as PlasmaCore

Item {
    id: widget

    Plasmoid.compactRepresentation: Item {
        id: panelItem

        readonly property bool inPanel: (plasmoid.location == PlasmaCore.Types.TopEdge
            || plasmoid.location == PlasmaCore.Types.RightEdge
            || plasmoid.location == PlasmaCore.Types.BottomEdge
            || plasmoid.location == PlasmaCore.Types.LeftEdge)

        Layout.minimumWidth: {
            switch (plasmoid.formFactor) {
            case PlasmaCore.Types.Vertical:
                return 0;
            case PlasmaCore.Types.Horizontal:
                return height;
            default:
                return units.gridUnit * 3;
            }
        }

        Layout.minimumHeight: {
            switch (plasmoid.formFactor) {
            case PlasmaCore.Types.Vertical:
                return width;
            case PlasmaCore.Types.Horizontal:
                return 0;
            default:
                return units.gridUnit * 3;
            }
        }

        Layout.maximumWidth: inPanel ? units.iconSizeHints.panel : -1
        Layout.maximumHeight: inPanel ? units.iconSizeHints.panel : -1

        AppletIcon {
            id: icon
            anchors.fill: parent
            source: 'customicon'
            active: mouseArea.containsMouse
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent
            hoverEnabled: true
            property bool wasExpanded: false
            onPressed: wasExpanded = plasmoid.expanded
            onClicked: plasmoid.expanded = !wasExpanded
        }
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
