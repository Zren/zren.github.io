---
layout: post
title: Making a DevTools Inspector for Plasma
---

2022-06-09 Update: I've published the code at <https://github.com/Zren/QmlDevTools>.

One of the the things I really miss from my few days with Gtk 3.0 in Cinnamon is that it has access to the "Chrome" DevTools inspector. It lets you easily see the Panel's DOM, and quickly test modifications. It's a must have for any web development these days too.

This isn't my first time attempting this project, so I had an some code mocked up already.

![](https://i.imgur.com/UJe3b68.png)

It's a bit rough. The right pane is a property inspector for the selected item, and the left just lists the stringified items from the target Item all the way up to the root item. We can do... much, much, beter.

So I tossed out everything to start. The right property inspector can be reused later, but lets focus on the tree view of the elements.

First we need to focus on rendering a single element. So we'll populate a ListModel with the root Item. Then for the delegate we'll use a [Flow](https://doc.qt.io/qt-5/qml-qtquick-flow.html) layout and a [Repeater](https://doc.qt.io/qt-5/qml-qtquick-repeater.html) of [Text](https://doc.qt.io/qt-5/qml-qtquick-text.html). Each Text item can be drawn in rich text, which let's us use some xml formatting `<font color="#fff">text</font>`. I used the color picker on chrome's devtools and tediously wrapped each character in it's proper color. I used a unicode triangle for the expando button (which we'll rotate later).

After things started looking good, I focused on the expando button, and dynamically populating on expansion and removing things on collapse. I was worried about populating everything at once in case doubling (at a minimum) the number of qml Items on the screen is a bad idea. I eventually did write a `expandAll()` function though.

One performance trick I did keep was to avoid expanding and binding to descendant Items of the inspector itself. It got into recursion warnings when it tried to inspect (and update) the ListView.

![](https://i.imgur.com/udPbCvY.jpg)

After getting the elements view down. I focused on readding the selected item properties pane. I fixed a few bugs from my older code, and worked on making clicking to select. Then I worked on arrow keys to select.

After it started to feel like the inspector a bit, I started filtering out the noisy properties. Things like `transition` and `anchors` which aren't raw values are fairly useless. Especially the one's inherited by every single Item. I also filtered out every property set in [Item](https://doc.qt.io/qt-5/qml-qtquick-item.html) that was still the default value. It stared took look clean.

![](https://i.imgur.com/J789NNY.jpg)

Now that it sort of worked. It was time to test it in a plasmoid with `plasmoidviewer`. Up till now I'd been using `qmlscene` to test. After a finding out the following code could cause to max out your CPU, I fixed a few other things like the background color (needed to be white).

{% highlight qml %}
Plasma.Dialog {
  mainItem: Item {
    anchors.fill: parent
  }
}
{% endhighlight %}

![](https://i.imgur.com/4JCPIJo.jpg)

I then worked on the breadcrumb navigation on the bottom. Clicking them would update the selection. I also added the hover state to the element view.

![](https://i.imgur.com/NSyai95.jpg)

Next up, I parsed the QML "Type" by stopping after the first `_` or `(` since we don't need to see the memory address. I'd already done this in the breadcrumb navigation. Around here is where I moved a lot of reused functions into a `util.js` with `.pragma library` at the top so that only one instance is loaded.

![](https://i.imgur.com/RdRBuyL.jpg)

Next up I tried testing in `plasmashell` itself. I soon found that it would be increadibly difficult to find the important things (like the plasma widgets). So I set out to implement a `Ctrl+F` search box.

A simple textbox that would do a case insensitive search on the *expanded* items "type" (the "tag"). Eg: Searching for `applet` should select the first `AppletInterface`. Since I currently had 19 widgets, I also added the ability to select the 2nd and 3rd matches too by constantly hitting `Enter`.

![](https://i.imgur.com/9F15F1K.jpg)

That's where I think I'll leave off for now. The main goal of an inspector is to easily browse the hierarchy. Next time I think I'll add another pane (and a tab bar) to quickly go to specific places (like the wallpaper, the desktop icons, the panels, the widgets, etc). Maybe I'll try my hands at a tty console. I could look into if there's a way to connect to `console.log`'s output.

Till then.
