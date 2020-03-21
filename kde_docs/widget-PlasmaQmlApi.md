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

QML ships with a [Text](http://doc.qt.io/qt-5/qml-qtquick-text.html) type, but Plasma extends it with `Label.qml` which asigns a number of defaults. One thing is it sets the text color to follow the panel's color scheme. For the specifics, you can read the [`Label.qml` source code](https://github.com/KDE/plasma-framework/blob/master/src/declarativeimports/plasmacomponents/qml/Label.qml).

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
