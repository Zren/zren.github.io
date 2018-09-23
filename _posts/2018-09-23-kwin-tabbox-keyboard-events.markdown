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

To get started, let's build `kwin`. Sometimes it requires an unreleased dependency, but right now I simply clone the repo and build the master branch.

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

{% highlight bash %}
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
cd ..
{% endhighlight %}

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

