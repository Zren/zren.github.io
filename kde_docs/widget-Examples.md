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



{% capture label %}...{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}
