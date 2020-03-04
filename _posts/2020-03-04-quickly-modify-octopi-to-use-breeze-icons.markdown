---
title: Quickly Modify Octopi To Use Breeze Icons
layout: post
---

![](https://i.imgur.com/THRnpJE.png)

We'll be using inkscape to convert the SVG icons to PNG, so install it first if you haven't already.

{% highlight bash %}
sudo pacman -S inkscape
{% endhighlight %}

Next we'll create a place to put the icons on our system.

{% highlight bash %}
mkdir -p ~/.local/share/icons/octopi
{% endhighlight %}

Next we'll convert the icons to PNG. I've scaled the icons from 22x22 to 64x64 to avoid a pixelated look.

Use `export IconTheme="breeze-dark"` instead if you have a dark panel theme.

{% highlight bash %}
export IconTheme="breeze"
inkscape  --export-width=64 --export-height=64 --export-png=${HOME}/.local/share/icons/octopi/update-none.png /usr/share/icons/${IconTheme}/status/22/update-none.svg
inkscape  --export-width=64 --export-height=64 --export-png=${HOME}/.local/share/icons/octopi/update-high.png /usr/share/icons/${IconTheme}/status/22/update-high.svg
inkscape  --export-width=64 --export-height=64 --export-png=${HOME}/.local/share/icons/octopi/update-medium.png /usr/share/icons/${IconTheme}/status/22/update-medium.svg
inkscape  --export-width=64 --export-height=64 --export-png=${HOME}/.local/share/icons/octopi/view-refresh.png /usr/share/icons/${IconTheme}/actions/22/view-refresh.svg
{% endhighlight %}

Finally, we can either:

A. manually edit the icons by navigating to Octopi > Tools > Options > Icons.
B. Or run the commands below. Then right click the system tray icon and click Exit. Then search for "Octopi Notifier" in the App Menu to relaunch it.

{% highlight bash %}
sed -i 's/Use_Default_App_Icon=true/Use_Default_App_Icon=false/' ${HOME}/.config/octopi/octopi.conf
sed -i 's`Octopi_Green_Icon_Path=`Octopi_Green_Icon_Path='"${HOME}"'/.local/share/icons/octopi/update-none.png`' ${HOME}/.config/octopi/octopi.conf
sed -i 's`Octopi_Red_Icon_Path=`Octopi_Red_Icon_Path='"${HOME}"'/.local/share/icons/octopi/update-high.png`' ${HOME}/.config/octopi/octopi.conf
sed -i 's`Octopi_Yellow_Icon_Path=`Octopi_Yellow_Icon_Path='"${HOME}"'/.local/share/icons/octopi/update-medium.png`' ${HOME}/.config/octopi/octopi.conf
sed -i 's`Octopi_Busy_Icon_Path=`Octopi_Busy_Icon_Path='"${HOME}"'/.local/share/icons/octopi/view-refresh.png`' ${HOME}/.config/octopi/octopi.conf
{% endhighlight %}
