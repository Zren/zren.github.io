---
title: Unity7 Styled Icon For The Plasma App Launcher
layout: post
---

Under the `unity` project on Launchpad, there a [resources folder](https://git.launchpad.net/unity/tree/resources) which contains the `launcher_bfb.png` ([download](https://git.launchpad.net/unity/plain/resources/launcher_bfb.png)). This image contains the Unity 7 swirl.

I personally downloaded the master branch with:

{% highlight bash %}
git clone https://git.launchpad.net/unity --depth=1
{% endhighlight %}

While I could try to fuss with a rasterized image in Gimp, I'd rather open it up in Inscape so I can easily replace the ubuntu icon with the KDE icon, which is a svg. It'll also be a lot easier to do the drop shadow underneath the masked icon.

After making a 128x128 image in Inscape, we'll embed the `laucher_bfb.png`. I recommend setting the Background Color to be `5e0a2300` which is the "Unity purple" color but a 0% opacity. The background will be coloured while we modify the image, but the background color won't show up in the final rendering.

First we'll mask out the Ubuntu icon in the circle. Create a rectangle 128x128 at (0,0) and a circle 72x72 at (28, 28).

![](https://i.imgur.com/n3bBwRv.png)

Then run Path > Exclusion to create a circular hole in the square.

![](https://i.imgur.com/npq2yMo.png)

Now comes the tricky part. First make sure the square is filled a pure white. Then click the square, hold down `Shift` and click the ubuntu logo below to select the embedded png. Then right click it and click "Set Mask".

{% include video.html streamableId="ayz9x" %}

Now to make the circle masked with our kde icon. Make another circle 72x72 at (28, 28).

Then open up `/usr/share/icons/breeze/apps/22/kde.svg` to copy the KDE icon into our document. Scale the kde icon object to be 48x48. Then since `(128-48)/2 = 40`, position it at `(40, 40)`.

![](https://i.imgur.com/oHv1IQe.png)

Now select the KDE icon and the circle and apply Path > Exclusion. This should have cut out the kde icon from the circle.

![](https://i.imgur.com/Va6zvca.png)

Don't forget to make the cutout circle white. Lastly, we'll add the dropshadow.

Go to Filters > Shadows and Glows > Drop Shadow. Use the defaults to give it a black shadow. While you'll see a nice drop shadow inside the icon, we'll also get some unwanted shadow in the bottom right.

So we'll make another circle 72x72 at (28, 28). Make sure the circle is pure white. Next select both the circle we made and the cutout circle with the dropshadow. Right click the white circle we just made and click "Set Mask". This should have clipped the unwanted shadows.

{% include video.html streamableId="bb8qe" %}

If you export our current image as a 128x128 pixel png it should look like below. Do not load the `.svgz` as Plasma ignores the masking and drop shadows it contains.

![](https://i.imgur.com/7H5wN8s.png)


It doesn't look that great yet. We'll need to do an outline, and add a background fill.

If you've already downloaded the [Unity Ambiance desktop theme](https://store.kde.org/p/998797/) then navigate to `~/.local/share/plasma/desktoptheme/UnityAmbiance/`, then open up `widgets/tasks.svgz`.

Copy one of the buttons to a new layer in our image. Scale it to 128x128. Delete the green "margin" squares.

![](https://i.imgur.com/gPtSGgI.png)

Unfortunately, it doesn't look perfect. Even if we use the blue or orange it looks pretty meh.

![](https://i.imgur.com/Pr6I3hx.png)

Looking at the screenshots, it seems that the icon is only 48x48 in size on a 64px wide panel.

Hmmm. If we look at a screenshot of Unity7, we'll get the following dimensions.

* `64px` wide panel
* `1px` wide shadow / outline
* `52px` wide icon boxes.
* `(64 - 52) / 2 = 6px` panel padding
* `46px` wide icons
* `(52 - 46) / 2 = 3px` icon padding
