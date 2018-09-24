---
layout: post
title: KWin TabBox Keyboard Events
---

In case you didn't know, TabBox is the codename for the Alt+Tab Task Switcher. There are 2 ways to create a Task Switcher skin. A simple QML skin, or a C++ "Desktop Effect". Somehwere along the way, the QML skins were no longer able to use keyboard shortcuts.

<https://bugs.kde.org/show_bug.cgi?id=370185>

### Setting up a Dev Environemnt

To get started, let's build `kwin`. Sometimes it requires an unreleased dependency, but right now I can simply clone the repo and build the master branch in KDE Neon.

First download the code with:

{% highlight bash %}
git clone git://anongit.kde.org/kwin
cd kwin
{% endhighlight %}

Then install the build dependencies (this is the Neon/Ubuntu/Debian command).

{% highlight bash %}
sudo apt-get build-dep kwin
{% endhighlight %}

Now we can build kwin. I use [my own script](https://gist.github.com/Zren/3f859c267ac1148aaedcf54a9bacb00f) but you can use the commands below.

Note that we're not building the tests since it takes forever and adds an entire gigabyte of storage. The build directory will be 0.8 Gb without tests, and 1.8 Gb with them. Even without building the tests, the build directory will use up plenty of space (so you'll want to delete it when you're done).

{% highlight bash %}
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
cd ..
{% endhighlight %}

If things didn't compile correctly:

* If it needs a newer kde dependency:
    * (A) You could either checkout and older branch and develop on that.
    * (B) Or you could follow the `kdesrc-build` [instructions](https://community.kde.org/Guidelines_and_HOWTOs/Build_from_source) to build the entire kde stack from source.

### Testing

If everything compiled correctly, we should now test to make sure it runs correctly before we start messing with it.

Before we do, make sure to remember this command so you can restart your distro's copy of `kwin_x11` if things go bad.

{% highlight bash %}
kwin_x11 --replace &
{% endhighlight %}

Now then, lets test your recently compiled version of `kwin_x11`.

{% highlight bash %}
build/bin/kwin_x11 --replace &
{% endhighlight %}

Note that we used `&` to run `kwin_x11` in the background. This lets us restart kwin smoothly in the same Konsole terminal by hitting `Up Arrow` then `Enter`.

### Adding Simple Debug Logging

If everything went well, we can then start modifying kwin.

First open up `tabbox/tabboxhandler.cpp` and navigate to the `TabBoxHandler::eventFilter` function.

<https://github.com/KDE/kwin/blob/master/tabbox/tabboxhandler.cpp#L621>

The easiest way to debug is to log to the terminal whenever a function is called. In Qt, we usually use `qDebug()` to log to file, but as we can see elsewhere in this file, [a logging category](http://doc.qt.io/qt-5/qloggingcategory.html) for tabbox has already been set up so lets use that.

{% highlight cpp %}
bool TabBoxHandler::eventFilter(QObject *watched, QEvent *e)
{
    qCDebug(KWIN_TABBOX) << "eventFilter " << e->type();

    if (e->type() == QEvent::Wheel && watched == d->window()) {
{% endhighlight %}

After building and testing kwin, I wasn't able to see any logging though. It's possible that logging from this category is hidden by default.

If we look at `tabbox_logging.cpp` we'll find out that the exact category name is `kwin_tabbox`.

<https://github.com/KDE/kwin/blob/master/tabbox/tabbox_logging.cpp>

{% highlight cpp %}
Q_LOGGING_CATEGORY(KWIN_TABBOX, "kwin_tabbox", QtCriticalMsg)
{% endhighlight %}

So after reading the [QLoggingCategory documentation](http://doc.qt.io/qt-5/qloggingcategory.html#logging-rules), we can change our test command to:

{% highlight bash %}
QT_LOGGING_RULES="kwin_tabbox.debug=true" build/bin/kwin_x11 --replace &
{% endhighlight %}

{% include video.html youtubeId="noR582a0eBU" %}

Alright, next we'll look at where it handles the Alt+Tab, and Alt+Shift+Tab shortcuts, as it appears that code it "stealing" the keypress event. So next we'll add some debug statements in the `tabbox/tabbox.cpp` file.

{% highlight cpp %}
qCDebug(KWIN_TABBOX) << "TabBox::grabbedKeyEvent " << event->key();
qCDebug(KWIN_TABBOX) << "TabBox::keyPress " << keyQt;
{% endhighlight %}

Now pressing the left arrow key logs the following:

{% highlight log %}
# Left Arrow
kwin_tabbox: TabBox::keyPress        150994962
kwin_tabbox: TabBox::grabbedKeyEvent  16777234
{% endhighlight %}

It seems the `keyQt` in the `TabBox::keyPress` line includes the AltModifier bit flag as the number is larger. Also, it seems that it's also sent to `TabBoxHandler::grabbedKeyEvent`.

<https://github.com/KDE/kwin/blob/master/tabbox/tabboxhandler.cpp#L525>

{% highlight log %}
kwin_tabbox: TabBoxHandler::grabbedKeyEvent 16777234
kwin_tabbox:     d->m_mainItem && d->window()
kwin_tabbox:     d->window() PlasmaQuick::Dialog(0x15bcc30 exposed, visibility=QWindow::Visibility(Windowed), flags=QFlags<Qt::WindowType>(X11BypassWindowManagerHint|FramelessWindowHint), geometry=498,441 932x206)
kwin_tabbox:     d->window()->contentItem() QQuickRootItem(0x15820e0, parent=0x0, geometry=0,0 932x206)
kwin_tabbox:     d->window()->sendEvent Plasma::FrameSvgItem(0x15be890, parent=0x15820e0, geometry=0,0 932x206)
kwin_tabbox:     d->window()->sendEvent ColorScope(0x16862a0, parent=0x0, geometry=0,0 0x0)
{% endhighlight %}

Interesting. I'm testing with my [Thumbnail Grid](https://github.com/Zren/kwin-tabbox-thumbnail_grid/blob/master/package/contents/ui/main.qml) skin, and it appears it's sending the events to a `FrameSvgItem` and `ColorScope`. My theory is that it's sending the events to the children of my `PlasmaCore.Dialog`.

<https://github.com/KDE/plasma-framework/blob/master/src/plasmaquick/dialog.cpp#L757>

{% highlight cpp %}
d->frameSvgItem = new Plasma::FrameSvgItem(contentItem());
mainItem->setParentItem(contentItem());
{% endhighlight %}

So, the question is why the second `sendEvent` is sent to a `ColorScope` instance...


### QML Skins

If you're like me and was wondering which repo contains the QML tabbox skins, you can easily find out which package owns a file with `dpkg -S`.

{% highlight bash %}
$ dpkg -S /usr/share/kwin/tabbox/big_icons/
kwin-addons: /usr/share/kwin/tabbox/big_icons
{% endhighlight %}

In this case, it seems they are shipped in the [kwin-addons](https://packages.debian.org/stretch/kwin-addons) package, which grabs it's source from the [kdeplasma-addons](https://github.com/KDE/kdeplasma-addons/tree/master/windowswitchers) git repo.

