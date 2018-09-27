---
layout: post
title: kdesrc-build in KDE Neon
---

I setup a [KDE Neon Git-Unstable](https://files.kde.org/neon/images/neon-devedition-gitunstable/current/) VM to try [building KDE from source](https://community.kde.org/Guidelines_and_HOWTOs/Build_from_source) so I could test C++ modifications to KDE Frameworks.

After installing all the dependencies to get `kdesrc-build plasma-workspace` to get 99% complete, I soon discovered that `networkmonitor-qt` would not build since `libnm0` (managed by ubuntu) was `v1.2` [in xenial](https://packages.ubuntu.com/xenial/libnm0).

I'd been meaning to try the [Neon update to bionic](https://community.kde.org/Neon/BionicUpgrades) so I figured why not upgrade it. `libnm0` [in bionic is](https://packages.ubuntu.com/bionic/libnm0) `v1.10` which should fix the dependency issue. (Update: Neon is now shipping bionic by default now)

## libudev.so is missing

After upgrading to bionic flawlessly, I ran `kdesrc-build` again. This time I ran into trouble with `solid` and `kwin`. Both build error logs mentioned:

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

Running `kdesrc-build plasma-workspace` will now build everything without errors, huzzah!

## plasma-desktop needs over 3Gb RAM to build

Now I tried building a few more packages with `plasma-desktop`. I first noticed it tried to rebuid everything `plama-workspace` needed as well, before finally trying to build `plasma-desktop`. After checking `kdesrc-build --help`, I realized I'd need to run the following every time I wanted to build a single package.

{% highlight bash %}
kdesrc-build plasma-desktop --resume-from=plasma-desktop
{% endhighlight %}

For now though, lets build `plasma-desktop` starting with `plasma-workspace`.

{% highlight bash %}
kdesrc-build plasma-desktop --resume-from=plasma-workspace
{% endhighlight %}

I ran into a new problem when building the `plasma-desktop` package.

{% highlight log %}
virtual memory exhausted: Cannot allocate memory
kcms/keyboard/CMakeFiles/kcm_keyboard.dir/build.make:386: recipe for target 'kcms/keyboard/CMakeFiles/kcm_keyboard.dir/preview/geometry_parser.cpp.o' failed
make[2]: *** [kcms/keyboard/CMakeFiles/kcm_keyboard.dir/preview/geometry_parser.cpp.o] Error 1
{% endhighlight %}

Turns out I was running out of RAM! This time I ran `kdesrc-build` with KSysGuard open with the RAM graph visible.

![](https://i.imgur.com/7jBMHMC.png)

Turns out building that package uses 1Gb more RAM than normal, climbing up to the max of 2Gb my VM is setup with. It also seems I forgot to properly setup the swap partition after resizing the partitions. Oops.

I first tried adding another gig of RAM to my VM, but even with 3Gb, it ran out.

![](https://i.imgur.com/rTk5fRJ.png)

So I formatted the swap and turned it on. Maybe it requires less RAM if you only build with 1 cpu core.

![](https://i.imgur.com/7DRoXDQ.png)
![](https://i.imgur.com/bI1n7vQ.png)

After setting up the swap, everything built correctly.

## Testing

The next step from building from source is appearently [setting up a runtime environment](https://community.kde.org/Guidelines_and_HOWTOs/Build_from_source#Set_up_the_runtime_environment). This involves creating a script that overrides a bunch of environment variables in the current Terminal session.

It mentions there's extra steps for Plasma, but I was interested in what would happened if I run plasmashell now? Well I tested it with the following:

{% highlight bash %}
source ~/kde/.setup-env
killall plasmashell; kstart5 plasmashell
{% endhighlight %}

Suprisingly, everything loaded okay.
