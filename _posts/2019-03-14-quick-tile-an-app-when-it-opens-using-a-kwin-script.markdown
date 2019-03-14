---
title: Quick Tile An App When It Opens Using A KWin Script
layout: post
---

[A user on reddit recently asked](https://www.reddit.com/r/kde/comments/b0dhk6/force_quick_tile_to_right_as_a_window_rule/) how to quick tile a window when it opens in a multi monitor setup. While they could easily position the app using a KWin Rule, that solution would only work for a single monitor. As if you launched the app on the 2nd monitor, the app would always show up on the 1st monitor.

When KWin Rules fails, you can write a KWin Script!

<https://techbase.kde.org/Development/Tutorials/KWin/Scripting/API_4.9>

{% highlight bash %}
mkdir -p ~/.local/share/kwin/scripts/QuickTileAppOnStart/contents/code
kate ~/.local/share/kwin/scripts/QuickTileAppOnStart/metadata.desktop
{% endhighlight %}

Then paste this in the `metadata.desktop` file:

{% highlight ini %}
[Desktop Entry]
Name=Quick Tile App On Start
Comment=
Icon=preferences-system-windows-script-test

Type=Service

X-Plasma-API=javascript
X-Plasma-MainScript=code/main.js
X-KDE-ServiceTypes=KWin/Script

X-KDE-PluginInfo-Author=Zren
X-KDE-PluginInfo-Email=zren@goobers.mail
X-KDE-PluginInfo-Name=QuickTileAppOnStart
X-KDE-PluginInfo-License=GPL
X-KDE-PluginInfo-Version=1
{% endhighlight %}

That'll define the name/icon of script that shows up in System Settings. Make sure `X-KDE-PluginInfo-Name=QuickTileAppOnStart` uses the same name as the folder you place it under. Next up is the actual script.

{% highlight bash %}
kate ~/.local/share/kwin/scripts/QuickTileAppOnStart/contents/code/main.js
{% endhighlight %}

Then in the `main.js` paste:

{% highlight js %}
function onClientAdded(client) {
    if (client.resourceName == "navigator" && client.resourceClass == "firefox") {
        client.activeChanged.connect(function quickTileClientOnFocus(){
            workspace.slotWindowQuickTileRight()
            client.activeChanged.disconnect(quickTileClientOnFocus)
        })
    }
}

workspace.clientAdded.connect(onClientAdded)
{% endhighlight %}


Change `navigator` and  `firefox` to whatever "window class" you'd use in a KWin Rule to limit this quick tile effect to a single application. Otherwise remove the if statement.

Finally, open up KWin Scripts in System Settings, enable the script and hit apply. If it doesn't work and you edited the `main.js`, to "reload" the script, disable the script, hit apply, then re-enable the script and hit apply.
