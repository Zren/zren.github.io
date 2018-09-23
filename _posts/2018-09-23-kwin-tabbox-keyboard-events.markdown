---
layout: post
title: KWin TabBox Keyboard Events
---

In case you didn't know, TabBox is the codename for the Alt+Tab Task Switcher. There are 2 ways to create a Task Switcher skin. A simple QML skin, or a C++ "Desktop Effect". Somehwere along the way, the QML skins were no longer able to use keyboard shortcuts.

<https://bugs.kde.org/show_bug.cgi?id=370185>

If your like me and was wondering which repo contains the QML tabbox skins, you can easily find out which package owns a file with `dpkg -S`.

{% highlight bash %}
$ dpkg -S /usr/share/kwin/tabbox/big_icons/
kwin-addons: /usr/share/kwin/tabbox/big_icons
{% endhighlight %}

In this case, it seems they are shipped in [kwin-addons](https://packages.debian.org/stretch/kwin-addons) package, but grabs it's source from the [kdeplasma-addons](https://github.com/KDE/kdeplasma-addons/tree/master/windowswitchers] git repo.

To get started, let's build `kwin`. Sometimes it requires an unreleased dependency, but right now I simply clone the repo and build the master branch in KDE Neon.

First download the code with:

{% highlight bash %}
git clone git://anongit.kde.org/kwin
cd kwin
{% endhighlight %}

Then install the build dependencies (this is the Neon/Ubuntu/Debian command).

{% highlight bash %}
sudo apt-get build-dep kwin
{% endhighlight %}

Now we can build kwin. I use [my own script](https://gist.github.com/Zren/3f859c267ac1148aaedcf54a9bacb00f) which does the same thing.

Note that we're not building the tests since it takes forever and requires over several gigabytes of storage. Even without building the tests, the build directory will use up 1.7 Gb of space (so you'll want to delete it when you're done).

{% highlight bash %}
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
cd ..
{% endhighlight %}

If things didn't compile correctly:

* If it needs a newer kde dependency
    a) you could either checkout and older branch and develop on that
    b) or you could follow the `kdesrc-build` [instructions](https://community.kde.org/Guidelines_and_HOWTOs/Build_from_source) to build everything.

If everything compiled correctly, we can now test to make sure it runs correctly before we start messing with it.

Before we do, rememeber this command so you can restart your distros copy of `kwin_x11`.

{% highlight bash %}
kwin_x11 --replace &
{% endhighlight %}

Now then, lets test your recently compiled version of `kwin_x11`.

{% highlight bash %}
build/bin/kwin_x11 --replace &
{% endhighlight %}

Note that we used `&` to run `kwin_x11` in the background. This lets us restart kwin smoothly in the same Konsole terminal by hitting `Up Arrow` then `Enter`.

If everything went well, we can then start modifying kwin.

First open up `tabbox/tabboxhandler.cpp` and navigate to the `TabBoxHandler::eventFilter` function.

https://github.com/KDE/kwin/blob/master/tabbox/tabboxhandler.cpp#L621

The easiest way to debug is to make it log to the terminal whenever a function is called. In Qt, we usually use `qDebug()` to log to file, but as we can see elsewhere in this file, [a logging category](http://doc.qt.io/qt-5/qloggingcategory.html) for tabbox has already been set up so lets use that.

{% highlight cpp %}
bool TabBoxHandler::eventFilter(QObject *watched, QEvent *e)
{
    qCDebug(KWIN_TABBOX) << "eventFilter " << e->type();

    if (e->type() == QEvent::Wheel && watched == d->window()) {
{% endhighlight %}

After building and testing kwin, I wasn't able to see any logging though. It's possible that logging from this category is hidden by default.

If we look at `tabbox_logging.cpp` we'll find out that the exact category name is `kwin_tabbox`.

https://github.com/KDE/kwin/blob/master/tabbox/tabbox_logging.cpp

{% highlight cpp %}
Q_LOGGING_CATEGORY(KWIN_TABBOX, "kwin_tabbox", QtCriticalMsg)
{% endhighlight %}

So after reading the [QLoggingCategory documentation](http://doc.qt.io/qt-5/qloggingcategory.html#logging-rules), we can change our test command to:

{% highlight bash %}
QT_LOGGING_RULES="kwin_tabbox.debug=true" build/bin/kwin_x11 --replace &
{% endhighlight %}

{% include video.html youtubeId="noR582a0eBU" %}
