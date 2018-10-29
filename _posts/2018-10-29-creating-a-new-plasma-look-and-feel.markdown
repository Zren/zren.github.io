---
title: Creating a New Plasma Look and Feel
layout: post
---

A user on reddit (/u/systemd-plus-Linux) recently asked how to modify the Activity Switcher theme. Unfortunately it seems to be tied to the Look and Feel as of Plasma 5.14.

<https://www.reddit.com/r/kde/comments/9sa51b/any_way_to_move_the_activity_manager_to_the_right/>

## Introduction to KWin TabBox skins

The tabbox skins for the `Alt+Tab` and the activity switcher are similar. The `Alt+Tab` skins are located at `/usr/share/kwin/tabbox/` for the preinstalled skins, and `~/.local/share/kwin/tabbox/` for the downloaded skins. However, you'll notice that the "Breeze" tabbox skin isn't there. This is because it's packaged in the Breeze "Look and Feel".

`/usr/share/plasma/look-and-feel/org.kde.breeze.desktop/contents/`

I **think** the "activity" switcher is the:  
`desktopswitcher/DesktopSwitcher.qml`

The `Alt+Tab` skin is probably the:  
`windowswitcher/WindowSwitcher.qml`

In any case, I don't think you can change the activity switcher skin without making a new look and feel, as while I see a "Task Switcher" in the System Settings for `Alt+Tab`, I don't see anything for the activity switcher.


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

Then play around with the `DesktopSwitcher.qml` file. When you wish to test, switch from your Look and Feel to Breeze, then back to your Look and Feel, then task the Activity Switcher.


## Look and Feel Explorer

There's also "Look and Feel Explorer" app in the `plasma-sdk` package, but it's probably better to learn how to edit the raw files since all that app does is "copy a look and feel", and edit it's `metadata.desktop` file.
