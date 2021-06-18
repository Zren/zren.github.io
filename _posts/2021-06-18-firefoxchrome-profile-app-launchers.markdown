---
title: Firefox/Chrome Profile App Launchers
layout: post
---

If you share a computer and want separate bookmarks/extensions without multiple OS users, using multiple web browser profiles is the solution. In Windows, creating a new browser profile will create an app launcher for you, but in Linux you have to do it manually.

In KDE Plasma, you can use `kmenuedit` to create a new app launcher, however it cannot edit right click actions like "New Window" and "New Incognito Window".

Instead lets copy `/usr/share/applications/google-chrome.desktop` to our local directory.

```
~/.local/share/applications/google-chrome-chris.desktop
```

{% highlight ini %}
[Desktop Entry]
Actions=NewWindow;NewPrivateWindow;
Categories=Network;WebBrowser;
Comment=Access the Internet
Exec=/usr/bin/google-chrome-stable --profile-directory="Profile 1" %U
GenericName=Web Browser
Icon=google-chrome-avatar-generic-green
MimeType=text/html;image/webp;application/xml;
Name=Google Chrome (Chris)
Path=
StartupNotify=true
StartupWMClass=google_chrome_chris

[Desktop Action NewWindow]
Exec=/usr/bin/google-chrome-stable --profile-directory="Profile 1"
Name=New Window

[Desktop Action NewPrivateWindow]
Exec=/usr/bin/google-chrome-stable --profile-directory="Profile 1" --incognito
Name=New Incognito Window
{% endhighlight %}

The `--profile-directory` will either be `Default` or `Profile 1`. Visit `~/.config/google-chrome/` to check.

The `StartupWMClass` should tell the window manager (KWin) and taskbar widget (Plasma TaskManager) to not group these windows with the normal `google_chrome` windows.

You'll notice that I set the icon to an unknown icon. That's because I created a few custom icons to match chrome's builtin profile icons.

{% highlight ini %}
Icon=google-chrome-avatar-generic-green
{% endhighlight %}

Save the following SVG icons to:

```
~/.local/share/icons/google-chrome-avatar-generic-green.svg
```

<style>
.browser-icons img{
	box-shadow: none;
	display: inline-block;
}
</style>

**Chrome:** <span class="browser-icons">
	<img src="/img/browser/google-chrome-avatar-generic-aqua.svg" />
	<img src="/img/browser/google-chrome-avatar-generic-blue.svg" />
	<img src="/img/browser/google-chrome-avatar-generic-green.svg" />
	<img src="/img/browser/google-chrome-avatar-generic-orange.svg" />
	<img src="/img/browser/google-chrome-avatar-generic-purple.svg" />
	<img src="/img/browser/google-chrome-avatar-generic-red.svg" />
	<img src="/img/browser/google-chrome-avatar-generic-yellow.svg" />
</span>

Once you've finished creating the `.desktop` file, open up the Konsole terminal app and run the following command to refresh the application list.

{% highlight bash %}
kbuildsycoca5
{% endhighlight %}

Finally drag the app to your panel's task manager widget to pin it there.



## Firefox

The process for Firefox is the same as Chrome, however the `firefox-chris.desktop` file should be based on `/usr/share/applications/firefox.desktop` instead.

{% highlight ini %}
[Desktop Entry]
Actions=new-window;new-private-window;
Comment=Browse the World Wide Web
Exec=firefox --class="firefox-chris" -P chris %u
GenericName=Web Browser
Icon=mozilla-firefox-avatar-green
Keywords=Internet;WWW;Browser;Web;Explorer
MimeType=text/html;text/xml;application/xhtml+xml;application/xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;x-scheme-handler/ftp;x-scheme-handler/chrome;video/webm;application/x-xpinstall;
Name=Firefox (Chris)
NoDisplay=false
Path[$e]=
StartupNotify=true
Terminal=0
TerminalOptions=
Type=Application
Version=1.0
X-KDE-SubstituteUID=false
X-KDE-Username=
X-MultipleArgs=false
StartupWMClass=firefox-chris

[Desktop Action new-window]
Exec=firefox --class="firefox-chris" -P chris -new-window
Name=Open a New Window

[Desktop Action new-private-window]
Exec=firefox --class="firefox-chris" -P chris -private-window
Name=Open a New Private Window
{% endhighlight %}

The `-P profileId` argument can be determined by entering `about:profiles` in the Firefox addressbar. It should be either `default` or `name`.

You also need to pass the same value as `StartupWMClass` to firefox in `--class`.

Here's a couple of icons based on Chrome's profile avatars. You can easily recolor them with Inkscape.

**Firefox:** <span class="browser-icons">
	<img src="/img/browser/mozilla-firefox-avatar-green.svg" />
	<img src="/img/browser/mozilla-firefox-avatar-purple.svg" />
</span>
