---
layout: page
title: Yakuake
permalink: /kde/yakuake/
---

The Yakuake terminal is installed by default on some ditros. It's basically a fancy dropdown terminal with a global shortcut that will hide when it loses focus.

There are a few mods I apply to it to make it

1. I first use a skin with a thin/hidden titlebar. I personally use a skin I made ased on Sublime Text 3 called Soda Dark.
2. Popup from the bottom.
    * Disable animations (duration = 0ms).
    * Width: 100%
    * Height: 70%
    * Use a KWin Rule to position at the bottom.
        * Position: `Force` `0,315`  
          1080 pixel height screen - 30px bottom panel = 1050px  
          100% - 70% screen height = 30%
          1050px * 0.3 = 315px
3. Add "Open Yakuake Here" right click action to Dolphin (the file manager).
    * Note: This was based off the [KDE3 Service menu on the KDE Store](https://store.kde.org/p/998412/).

Create `~/bin/yakuakehere`

{% highlight bash %}
mkdir -p ~/bin
touch ~/bin/yakuakehere
chmod +x ~/bin/yakuakehere
{% endhighlight %}

with the contents:

{% highlight bash %}
#!/bin/bash

if [ "$1" != "" ]; then
    command="cd ""'"$1"'"
else
    PWD=`pwd`
    command="cd ""'"$PWD"'"
fi

qdbus org.kde.yakuake /yakuake/sessions addSession
qdbus org.kde.yakuake /yakuake/sessions runCommand "$command"
qdbus org.kde.yakuake /yakuake/sessions runCommand "clear"
qdbus org.kde.yakuake /yakuake/window toggleWindowState
{% endhighlight %}

then create: `~/.local/share/kservices5/ServiceMenus/YakuakeHere.desktop`

{% highlight bash %}
mkdir -p ~/.local/share/kservices5/ServiceMenus/
touch ~/.local/share/kservices5/ServiceMenus/YakuakeHere.desktop
{% endhighlight %}

with the contents:

{% highlight bash %}
[Desktop Entry]
Type=Service
X-KDE-ServiceTypes=KonqPopupMenu/Plugin
MimeType=inode/directory
Actions=OpenYakuake
X-KDE-AuthorizeAction=shell_access
X-KDE-Priority=TopLevel

[Desktop Action OpenYakuake]
Icon=yakuake
Exec=yakuakehere %f
Name=Open Yakuake Here
Comment=Opens a new tab in Yakuake at the current folder
{% endhighlight %}

then finally run `kbuildsycoca5` to apply the changes.
