---
layout: post
title: XBox One Controller in KDE Neon
---

As of Dec 9th 2016, KDE Neon (which is based on Ubuntu 16.04 LTS) is only using the Linux 4.4.0-53 kernel. Which means the XBox One controller isn't fully supported without some running some commands manually.

There are at least 3 revisions of the XBox One controller.

* Origional Launch Model
* Model with Headphone Jack
* Model S

I owned the second model with the headphone jack. When plugged in on Dec 9th, it produced a small rumble, but the xbox led did not light up. After opening System Settings > Input Devices > Joystick, pressing the buttons produced no visible response.

After a bit of googling, I discovered the updated version of the xpad driver is suppose to be in Linux 4.5, Unfortunately the Ubuntu 16.04 LTS will not recived the newer kernel until January (so anyone reading this will probably discover their controller works).

It does come with instrutions on how to update the kernel module.

{% highlight bash %}
sudo git clone https://github.com/paroj/xpad.git /usr/src/xpad-0.4
sudo dkms install -m xpad -v 0.4
{% endhighlight %}

Then restart your computer. There's probably a way to unload the old version and load the new version but I didn't bother looking around.

Now when you plug the controller in, the xbox logo should light up, and going to System Settings should show visible feedback when moving the joystick.
