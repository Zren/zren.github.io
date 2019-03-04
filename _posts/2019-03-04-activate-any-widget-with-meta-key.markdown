---
title: Activate any widget with Meta key
layout: post
---

[A user on reddit recently asked](https://www.reddit.com/r/kde/comments/awja8m/windows_key_not_opening_dashboard_in_latte_dock/ehrz8dt/?context=3) how to trigger any widget using the Meta key.

The Meta key "shortcut" works by KWin detecting the keypress and sending a DBus signal to another process (`plasmashell` or `latte-dock`). I believe this is necessary since the [Qt keyboard shortcut "Actions"](https://doc.qt.io/qt-5/qaction.html) do not support modifier only shortcuts, and the only way to add support for it would be to patch Qt upstream or fork Qt and rewrite every KDE app using that fork of Qt (like KDE4 did?).

Technically, we can have it trigger a widget using a `qdbus org.kde.kglobalaccel ...` command.

{% highlight bash %}
qdbus
qdbus org.kde.kglobalaccel
qdbus org.kde.kglobalaccel /component/plasmashell
qdbus org.kde.kglobalaccel /component/plasmashell shortcutNames | sort
qdbus org.kde.kglobalaccel /component/plasmashell invokeShortcut "activate widget 56"
{% endhighlight %}

In order to determine which widget id (`56`) you need, check `~/.config/plasma-org.kde.plasma.desktop-appletsrc`.

{% highlight bash %}
grep windowlist -B5 ~/.config/plasma-org.kde.plasma.desktop-appletsrc
{% endhighlight %}

Eg:
{% highlight txt %}
$ grep sysmonitordash -B5 ~/.config/plasma-org.kde.plasma.desktop-appletsrc
deviceId=aaaaaaaaaaaaaaaa
deviceName=Motorola Moto G

[Containments][1][Applets][56]
immutability=1
plugin=com.github.zren.sysmonitordash
{% endhighlight %}

In order to assign the `[ModifierOnlyShortcut]` in `kwinrc`, you need to turn the command into a StringList. Replace the spaces between arguments with a comma `,`. We also need the `invokeShortcut` method's namespace, which we normally can normally leave it out when running `qdbus` from the terminal since there usually isn't a name conflict. First run the following command:

{% highlight bash %}
qdbus org.kde.kglobalaccel /component/plasmashell
{% endhighlight %}

to find all the functions and their namespaces for the `/component/plasmashell` path.

{% highlight txt %}
property read QString org.kde.kglobalaccel.Component.friendlyName
property read QString org.kde.kglobalaccel.Component.uniqueName
...
method void org.kde.kglobalaccel.Component.invokeShortcut(QString shortcutName)
...
{% endhighlight %}

So `invokeShortcut`'s namespace is `org.kde.kglobalaccel.Component`

{% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/plasmashell,org.kde.kglobalaccel.Component,invokeShortcut,activate widget 56"
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}

Since the `,` is the separator, we didn't need to wrap `activate widget 56` in quotes as spaces ` ` are no longer the separator.

