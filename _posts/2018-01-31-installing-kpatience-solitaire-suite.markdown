---
layout: post
title: Installing KPatience Solitaire Suite
---

I was recently asked "where's solitaire"? Since they were using KDE Neon, I skimmed to Ubuntu LTS apps. There's the `aisleriot` solitaire that uses Gtk, but there's also [KPatience](https://www.kde.org/applications/games/kpatience/) (`kpat`) in the KDE Apps. After installing, I noticed it only created 1 launcher called KPatience, which isn't friendly to a branch new linux user. So I made a few `.desktop` launchers for the 3 more popular games: Solitaire (aka Klondike), Spider Solitaire, and FreeCell.

The icons are from various Android games found by [googling](https://www.google.com/search?q=solitaire+icon+type:png&tbm=isch) `solitaire icon type:png` image search.

## KPatience

First install the app with:

{% highlight bash %}
sudo apt install kpat
{% endhighlight %}

## Solitaire

Save the following image as `~/.local/share/icons/solitaire.png`

![](https://i.imgur.com/k4R2ntA.png)

And create the launcher at `~/.local/share/applications/solitaire.destkop`

{% highlight ini %}
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Solitaire
GenericName=Solitaire Card Game
Comment=Solitaire Card Game
Icon=solitaire
Type=Application
Exec=kpat --gametype=klondike
Categories=Qt;KDE;Game;CardGame;
X-DBUS-ServiceName=org.kde.kpat
X-DBUS-StartupType=Multi
X-DocPath=kpat/index.html
{% endhighlight %}


## Spider Solitaire

Save the following image as `~/.local/share/icons/spidersolitaire.png`

![](https://i.imgur.com/xFwr2V7.png)

And create the launcher at `~/.local/share/applications/spidersolitaire.destkop`

{% highlight ini %}
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=Spider Solitaire
GenericName=Spider Solitaire Card Game
Comment=Spider Solitaire Card Game
Icon=spidersolitaire
Type=Application
Exec=kpat --gametype=spider
Categories=Qt;KDE;Game;CardGame;
X-DBUS-ServiceName=org.kde.kpat
X-DBUS-StartupType=Multi
X-DocPath=kpat/index.html
{% endhighlight %}

## FreeCell

Save the following image as `~/.local/share/icons/freecell.png`

![](https://i.imgur.com/2HS68mk.png)

And create the launcher at `~/.local/share/applications/freecell.destkop`

{% highlight ini %}
#!/usr/bin/env xdg-open
[Desktop Entry]
Name=FreeCell
GenericName=FreeCell Card Game
Comment=FreeCell Card Game
Icon=freecell
Type=Application
Exec=kpat --gametype=freecell
Categories=Qt;KDE;Game;CardGame;
X-DBUS-ServiceName=org.kde.kpat
X-DBUS-StartupType=Multi
X-DocPath=kpat/index.html
{% endhighlight %}


## Apply Changes

Finally, we need to run `kbuildsycoca5` to update the list of apps in the panel launcher and KRunner.
