---
layout: post
title: kdesrc-build in KDE Neon
---

I setup a [KDE Neon Git-Unstable](https://files.kde.org/neon/images/neon-devedition-gitunstable/current/) VM to try [building KDE from source](https://community.kde.org/Guidelines_and_HOWTOs/Build_from_source) so I could test C++ modifications to KDE Frameworks.

After installing all the dependencies to get `kdesrc-build plasma-workspace` to get 99% complete, I soon discovered that `networkmonitor-qt` would not build since `libnm0` (managed by ubuntu) was `v1.2` [in xenial](https://packages.ubuntu.com/xenial/libnm0).

I'd been meaning to try the [Neon update to bionic](https://community.kde.org/Neon/BionicUpgrades) so I figured why not upgrade it. `libnm0` [in bionic is](https://packages.ubuntu.com/bionic/libnm0) `v1.10` which should fix the dependency issue.

After upgrading to bionic flawlessly, I ran `kdesrc-build` again. This time I ran into trouble with `solid` and `kwin`. Both complained build error logs mentioned:

{% highlight log %}
make[2]: *** No rule to make target '/usr/lib/x86_64-linux-gnu/libudev.so', needed by 'bin/libKF5Solid.so.5.51.0'. Stop.
{% endhighlight %}

{% highlight log %}
make[2]: *** No rule to make target '/usr/lib/x86_64-linux-gnu/libudev.so', needed by 'bin/libinputtest'. Stop.
{% endhighlight %}

`apt search libudev` shows that `libudev1` and `libudev-dev` are installed, so it's not that. `apt show libudev1` showed that it's part of systemd btw. `locate libudev.so` had interesting output though.

{% highlight log %}
/lib/x86_64-linux-gnu/libudev.so
/lib/x86_64-linux-gnu/libudev.so.1
/lib/x86_64-linux-gnu/libudev.so.1.6.9
/snap/core/5328/lib/x86_64-linux-gnu/libudev.so.1
/snap/core/5328/lib/x86_64-linux-gnu/libudev.so.1.6.4
{% endhighlight %}

It seems that it can't find `libudev.so` in `/usr/lib/`, but it did exist in `/lib`. Well solid was compiling before the bionic upgrade, lets check my host OS KDE Neon User which is still on xenial.

{% highlight log %}
/home/chris/.local/share/lutris/...
/home/chris/.steam/...
/lib/i386-linux-gnu/libudev.so.1
/lib/i386-linux-gnu/libudev.so.1.6.4
/lib/x86_64-linux-gnu/libudev.so.1
/lib/x86_64-linux-gnu/libudev.so.1.6.4
/snap/core/*/...
/usr/lib/x86_64-linux-gnu/libudev.so
/var/tmp/mkinitramfs_*/...
{% endhighlight %}

So it looks like it's got `/usr/lib/x86_64-linux-gnu/libudev.so`, lets see which package owns it with `dpkg -S /usr/lib/x86_64-linux-gnu/libudev.so`.

{% highlight log %}
libudev-dev:amd64: /usr/lib/x86_64-linux-gnu/libudev.so
{% endhighlight %}

Welp. A glance at the file list on <https://packages.ubuntu.com> for xenial and bionic shows the removal of the `/usr/lib` `libudev.so` file.

* <https://packages.ubuntu.com/xenial/amd64/libudev-dev/filelist>
* <https://packages.ubuntu.com/bionic/amd64/libudev-dev/filelist>

For now, I'll try symlinking the file to the one in `/lib`.

{% highlight bash %}
cd /usr/lib/x86_64-linux-gnu
sudo ln -s /lib/i386-linux-gnu/libudev.so.1 libudev.so
{% endhighlight %}


