---
title: Creating a New Plasma Look and Feel
layout: post
---

A user on reddit recently asked how to modify the Breeze `Alt+Tab` theme. Unfortunately it seems to be tied to the Look and Feel as of Plasma 5.14.

## Introduction to KWin TabBox skins

The tabbox skins for the `Alt+Tab` are located at `/usr/share/kwin/tabbox/` for the preinstalled skins, and `~/.local/share/kwin/tabbox/` for the downloaded skins. However, you'll notice that the "Breeze" tabbox skin isn't there. This is because it's packaged in the Breeze "Look and Feel".

`/usr/share/plasma/look-and-feel/org.kde.breeze.desktop/contents/`

I have no idea what the "desktop" switcher is. It's not the "Desktop Switch On-Screen Display".
`desktopswitcher/DesktopSwitcher.qml`

The `Alt+Tab` skin is probably the:  
`windowswitcher/WindowSwitcher.qml`


## Creating a new Look and Feel

Here's how create your own look and feel based off Breeze.

{% highlight bash %}
mkdir -p ~/.local/share/plasma/look-and-feel/
cp -r /usr/share/plasma/look-and-feel/org.kde.breeze.desktop ~/.local/share/plasma/look-and-feel/
mv ~/.local/share/plasma/look-and-feel/org.kde.breeze.desktop ~/.local/share/plasma/look-and-feel/SystemdPlusLinux
kwriteconfig5 --file=$HOME/.local/share/plasma/look-and-feel/SystemdPlusLinux/metadata.desktop --group="Desktop Entry" --key="X-KDE-PluginInfo-Name" "SystemdPlusLinux"
kwriteconfig5 --file=$HOME/.local/share/plasma/look-and-feel/SystemdPlusLinux/metadata.desktop --group="Desktop Entry" --key="Name" "Breeze (SystemdPlusLinux)"
rm ~/.local/share/plasma/look-and-feel/SystemdPlusLinux/metadata.json
{% endhighlight %}

Note, `X-KDE-PluginInfo-Name` must be the same as the folder name.

Note, you might want to manually remove all the translated `Name[sl]=Sapica` in the `metadata.desktop` if you're not using the `en_US` locale/translations, as otherwise it'll use a translated version of "Breeze" in the System Settings instead of what we just set it as (`Breeze (SystemdPlusLinux)`).

## Editing the Look and Feel

Then play around with the `WindowSwitcher.qml` file.

To test your changes, you'll probably need to run `kwin_x11 --replace` to restart KWin. You might be able to get away with switching to another Look and Feel, then back to yours, but I believe it might cache the theme, which is why restarting kwin might be required.

You can also play around with the Volume OSD.

* <https://github.com/Zren/plasma-lookandfeel-alphablack/tree/master/contents/osd>
* <https://www.reddit.com/r/kde/comments/9j57z2/fixing_the_awful_volumebrightness_osd_size/>


## Look and Feel Explorer

There's also "Look and Feel Explorer" app in the `plasma-sdk` package, but it's probably better to learn how to edit the raw files since all that app does is "copy a look and feel", and edit it's `metadata.desktop` file.
