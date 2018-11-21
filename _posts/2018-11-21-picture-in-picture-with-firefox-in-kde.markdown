---
title: Picture In Picture With Firefox in KDE
layout: post
---

I used to be able to get Picture In Picture with Chrome by maximizing the video, `Alt+F3+M+F` to exit fullscreen but stay in Chrome's "fullscreen mode" with the addressbar and window frame hidden. I would then hit `Alt+F3+M+A` to make the window stay on top. Finally I would use `Alt+RightClick` to resize the window to be smaller, and `Alt+LeftClick` to move the window into the bottom right of the screen. This worked for the most part, but was cumbersome to setup.

Unfortunately, I cannot do the same procedure for Firefox, as when we use `Alt+F3+M+F` to exit fullscreen, Firefox does not say in the "fullscreen mode" and the addressbar reappears.

After [playing around with Firefox's `userChrome.css`](/kde/#firefox), when exploring [Firefox's browser toolbox](https://developer.mozilla.org/en-US/docs/Tools/Browser_Toolbox) I noticed you can easily `display: none;` to hide the CSD titlebar + addressbar.

If you haven't already made a `userChrome.css` file, then navigate to `~/.mozilla/firefox/abcde124.default/` or whatever your profile's folder name is. Then create the `.../abcde124.default/chrome/userChrome.css` directory and file. Open up `userChrome.css` then add the following:

{% highlight css %}
/* Picture in Picture */
#main-window[sizemode="normal"][width="565"][height="318"] #titlebar,
#main-window[sizemode="normal"][width="565"][height="318"] #navigator-toolbox {
	display: none;
}
{% endhighlight %}

**Restart firefox.**

Next up lets create a KWin Script that will resize the firefox window to `565 x 318` when snapped to the bottom right corner of the screen.

Navigate to `~/.local/share/` then create any missing folders in the path `~/.local/share/kwin/scripts/FirefoxPictureInPicture/contents/code/`. Then make 2 new files `FirefoxPictureInPicture/metadata.desktop` and `FirefoxPictureInPicture/contents/code/main.js`.

{% highlight bash %}
mkdir -p ~/.local/share/kwin/scripts/FirefoxPictureInPicture/contents/code/
touch ~/.local/share/kwin/scripts/FirefoxPictureInPicture/metadata.desktop
touch ~/.local/share/kwin/scripts/FirefoxPictureInPicture/contents/code/main.js
{% endhighlight %}

In `metadata.desktop` put the following:

{% highlight ini %}
[Desktop Entry]
Name=Firefox Picture in Picture
Comment=
Icon=preferences-system-windows-script-test

Type=Service

X-Plasma-API=javascript
X-Plasma-MainScript=code/main.js
X-KDE-PluginInfo-Author=
X-KDE-PluginInfo-Email=
X-KDE-PluginInfo-Name=FirefoxPictureInPicture
X-KDE-PluginInfo-Version=1

X-KDE-PluginInfo-Depends=
X-KDE-PluginInfo-License=GPL
X-KDE-ServiceTypes=KWin/Script
{% endhighlight %}

Next in `contents/code/main.js` put:

{% highlight js %}
// Breeze Gtk3 [Kubuntu/KDE Neon] has windowBorderWidth=0
// Breath Gtk3 [Manjaro] has windowBorderWidth=1
var windowBorderWidth = 0
var popupWidth = windowBorderWidth + 565 + windowBorderWidth
var popupHeight = windowBorderWidth + 318 + windowBorderWidth
var scrollbarAreaWidth = 20

function isFirefox(client) {
	return client.resourceClass == "firefox"
}

function withinThreshold(x, targetX, threshold) {
	return targetX - threshold <= x && x <= targetX + threshold
}

var applyCheck = function(client) {
	var rect = client.geometry

	var area = workspace.clientArea(KWin.WorkArea, workspace.activeScreen, workspace.currentDesktop)
	var halfX = area.width / 2
	var halfY = area.height / 2

	var screenX = rect.x - area.x
	var screenY = rect.y - area.y

	var isPosCenter = withinThreshold(screenX, halfX, 10) && withinThreshold(screenY, halfY, 10)
	var isHalfSize = withinThreshold(rect.width, halfX, 10) && withinThreshold(rect.height, halfY, 10)
	var isLargerSize = rect.width > halfX || rect.height > halfY

	if (!client.keepAbove && isPosCenter && isHalfSize) {
		rect.x = area.x + area.width - popupWidth - scrollbarAreaWidth
		rect.y = area.y + area.height - popupHeight
		rect.width = popupWidth
		rect.height = popupHeight
		client.geometry = rect
		client.keepAbove = true
		client.onAllDesktops = true
		client.skipTaskbar = true
		client.skipPager = true
	} else if (client.keepAbove && isLargerSize) {
		client.keepAbove = false
		client.onAllDesktops = false
		client.skipTaskbar = false
		client.skipPager = false
	}

}

function onClientFinishUserMovedResized(client) {
	applyCheck(client)
}

function onClientAdded(client) {
	if (isFirefox(client)) {
		client.clientFinishUserMovedResized.connect(onClientFinishUserMovedResized)
	}
}

workspace.clientAdded.connect(onClientAdded)

var clients = workspace.clientList()
for (var i = 0; i < clients.length; i++) {
	var client = clients[i]
	onClientAdded(client)
}
{% endhighlight %}

Open System Settings > Window Management > KWin Scripts.

To reload the script, uncheck to disable our new script, click Apply, then enable our script, and click Apply.

Lets focus on the variables at the top.

{% highlight js %}
// Breeze Gtk3 [Kubuntu/KDE Neon] has windowBorderWidth=0
// Breath Gtk3 [Manjaro] has windowBorderWidth=1
var windowBorderWidth = 0
var popupWidth = windowBorderWidth + 565 + windowBorderWidth
var popupHeight = windowBorderWidth + 318 + windowBorderWidth
var scrollbarAreaWidth = 20
{% endhighlight %}

In Kubuntu, which uses the Breeze Gtk3 theme, you'll notice that the windows don't have any border/outline around the windows. So leaving it at 0 should be fine. The window will resize to `565 x 318`.

However, in Manjaro, the Gtk3 theme in **Breath** and has a 1px border around the window. This border means we need to resize the window to `567 x 320`. So we need to set `windowBorderWidth=1`.

The `scrollbarAreaWidth=20` adjusts how far away from the right side of the screen you wish the popup to appear. If you wish the popup to appear further from the bottom, it should be rather simple to modify the script to do so by using this variable as an example.

{% include video.html youtubeId="7q2Lh-uGvQ4" %}
