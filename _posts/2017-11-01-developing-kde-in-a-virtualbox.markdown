---
layout: post
title: Developing KDE in a VirtualBox
---

First download the [git-unstable KDE Neon iso](https://files.kde.org/neon/images/neon-devedition-gitunstable/current/neon-devedition-gitunstable-current.iso) while we setup the rest.

We'll need to install virtualbox if you haven't already.

{% highlight bash %}
sudo apt install virtualbox-qt
{% endhighlight %}

Then create a new virtual machine.

* Type: `Linux`
* Version `Ubuntu (64-bit)`

Allocate `1536` Mb (1.5Gb) of RAM.

Create a new virtual hard disk.

* (VDI / Virtualbox Disk Image)
* Dynamically Allocated
* 40Gb in size

> Note: While you don't need a full 40Gb, since the vdi automatically grows, you should still expect the `NeonDev.vdi` to be around 10Gb after at the end of the install.

After finishing creating the virtualbox, right click on it and open it's Settings.

* System Tab > Processor Tab > Give it 2-3 CPUs. Leave at least 1 CPU for your Host OS.
* Display Tab > Acceleration > Check enabled 3D Acceleration if you can.
* Storage Tab
    1. Click the "DVD disk icon" / Add Optical Drive
    2. Choose the neon iso.
* Network Tab
    1. Click Advanced
    2. Click Port Forwarding
    3. Click the Add New Port Forwarding icon.
        * Name: `SSH`
        * Protocol: `TCP`
        * Host Port: `2222`
        * Guest Port: `22`

Click Okay and close the settings, then start the virtual machine.

Install KDE Neon

* Create a new user called `neondev`. Use the password `neondev` so you don't forget it.
* When it asks you to remove the disk before restarting:
    * Devices > Optical Drives > Remove disk from virtual drive.

If after restarting you notice it's a bit sluggish, try disabling a few Desktop Effects. Open System Settings:

* Desktop Behavior > Desktop Effects
    * Disable "Sliding Popups"
    * Enable "Resize" (unless you want to test wayland resizing)

Now to link your host OS to your virtual machine so that you can develop in with your current IDE and tools while being able to test in an environment you're okay with breaking.

Inside the virtual machine, open the terminal and install openssh-server.

{% highlight bash %}
sudo apt install openssh-server
{% endhighlight %}

We previously port forwarded the virtual machines port 22 (SSH) to port 2222 on the host OS.

Open up your terminal in your Host OS. You can now connect to it's terminal with:

{% highlight bash %}
ssh -p 2222 neondev@localhost
{% endhighlight %}

It will prompt you for your password (`neondev`). If you want to skip the password step, you can copy your ssh key if you have one already setup with:

{% highlight bash %}
ssh-copy-id -p 2222 neondev@localhost
{% endhighlight %}


Now open dolphin (in the Host OS) and browse to:

{% highlight bash %}
fish://neondev@localhost:2222/home/neondev/
{% endhighlight %}

Congrats, now you can develop with your current tools and test with a fresh environment without affecting your day to day OS.
