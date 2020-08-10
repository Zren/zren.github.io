---
title: Testing Wayland in a Neon LiveCD
layout: post
---

I'd like to easily test window decoration in Wayland, which requires restarting `kwin_wayland`. Unfortunately we can't do that as `kwin_wayland` is the login session.

The KDE Neon Developer/Unstable ISO currently boots into a default user by default, skipping the SDDM login screen. We can't logout, or switch user as it will automatically login to the default user again.

I figured there's probably a SDDM config file to control which Desktop Environment a user logs into, and I was right. The [Arch wiki](https://wiki.archlinux.org/index.php/SDDM#Autologin) documented the autologin configuration, though for Neon (an Ubuntu derivative), the config file was at `/etc/sddm.conf`.

Open it up with `sudoedit /etc/sddm.conf` (default editor is `nano`) to find:

{% highlight ini %}
[Users]
MinimumUid=999

[Autologin]
User=neon
Session=plasma.desktop
Relogin=true
{% endhighlight %}

`ls /usr/share/wayland-sessions` finds `plasmawayland.desktop`. So just edit `Session=plasma.desktop` to `Session=plasmawayland.desktop` and save it.

Finally logout of the user. It should automatically relog into a wayland session.

-----

Next up is figuring out if I can test wayland in a window the same way [the Neon Docker project](https://community.kde.org/Neon/Docker) does. The [`neondocker.rb`](https://invent.kde.org/packaging/docker-neon/-/raw/master/neondocker/neondocker.rb) uses `Xephyr` to create a windowed x11 server.
