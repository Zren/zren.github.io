<!-- ------- -->
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
