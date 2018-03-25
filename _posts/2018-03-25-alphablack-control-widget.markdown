---
layout: post
title: AlphaBlack Control Widget
---

For a long while now, I've had a widget that simplifies changing the accent color of my [Breeze AlphaBlack](https://store.kde.org/p/1084931/) desktop theme. It had a few major usuability flaws so I never got around to cleaning it up for general release.

This weekend I got around to cleaning fixing the more pressing issue that the color picker would reset to black after relogging. The titlebars would still be using the accent color you chose, but the color picker wouldn't display it.

Rather than trying to read the rendered `background.svg` file for the color, a simpler fix was to just serialize the color we used into an `config.ini` file.

{% include streamable.html streamableId="jxe60" %}

As you can see in the video. We can currently do 3 things:

1. Change the accent color. This will change the panel color, the panel popups, and the titlebar (window decorations) color if using the Breeze window decorations.
2. The panel opacity. We can change the transparency of the panel fairly easily. I wouldn't recommend making it fully transparent, as there's still a blur Desktop effect and it looks weird. If you have a white window nearby, the blur will also cause the white to bleed into the panel area.
3. The "task" style to switch between the Breeze default and the Windows 10 style where it's an underline on the edge of the screen.

## How stuff works

A long time ago, I learned that in order to justreload a desktop theme, you needed to switch to another theme first (I use `breeze-dark`) then back again a second later. The `~/.config/plasmarc` file is watched by Plasma, so we can easily write to it with `kwriteconfig5` to switch themes.

There doesn't seem to be a way to tell Plasma to just "reload" the color scheme since it's saved as a "stylesheet" when we load the svgs. The stylesheet isn't updated when the color scheme is changed in the system settings either.

Plasma uses the Desktop Theme's `colors` to set the color scheme for the theme's svg files. In order for a Desktop Theme svg file to follow the color scheme, it first needs to have a `<style id="current-color-scheme">` element. When the svg is loaded by Plasma, the contents of this `<style>` tag are replaced by a generated stylesheet based on the color scheme.

* https://github.com/KDE/plasma-framework/blob/master/src/plasma/svg.cpp#L583
* https://github.com/KDE/plasma-framework/blob/master/src/plasma/svg.cpp#L88

After you've defined the `<style>` tag, you'll then need to edit the svg in a text editor, and replace all `<rect style="fill:#000000;" />` with:

{% highlight xml %}
<rect class="ColorScheme-Background" style="fill:currentColor;" />
{% endhighlight %}

Note that you should probably use `.svg` in desktop themes instead of the gzipped `svgz`. You can open an `svgz` with Ark to extract the `svg` if necessary.

Also, be careful of editing with Inkscape, as when you save using Inkscape, all your `style="fill:currentColor;"` will turn back to `style="fill:#000000;"`.
