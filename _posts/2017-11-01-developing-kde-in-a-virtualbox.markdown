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


## Installing KDE Neon

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

We previously port forwarded the virtual machines port 22 (SSH) to port 2222 on the host OS when configuring the VM. So we can now connect to it.

Open up your terminal in your Host OS. You can now connect to it's terminal with:

{% highlight bash %}
ssh -p 2222 neondev@localhost
{% endhighlight %}

It will prompt you for your password (`neondev`). If you want to skip the password step, you can copy your ssh key if you have one already setup with:

{% highlight bash %}
ssh-copy-id -p 2222 neondev@localhost
{% endhighlight %}

I've aliased the following in my `~/.bashrc` so all I need to type is `neondev` to start in my Code directory.

{% highlight bash %}
alias neondev='ssh -t -p 2222 neondev@localhost "cd ~/Code ; bash -l"'
{% endhighlight %}

Now open the Dolphin file browser (in the Host OS) and browse to:

{% highlight bash %}
fish://neondev@localhost:2222/home/neondev/
{% endhighlight %}

Save it as a favourite so you can easily navigate to it later.

Congrats, you've now linked the virtual machine enough to develop with your current dev tools (at full speed), with the ability to build and test with a secluded environment that won't break your day to day OS.


## Building a KDE Package

I want to modify `frameworksintegration`. A mirror of the source code [can be found on GitHub](https://github.com/KDE/frameworkintegration).

First we download the source with:

{% highlight bash %}
git clone git@github.com:KDE/frameworkintegration.git
{% endhighlight %}

Since KDE Neon already packages the code we want to build, we can find it with `apt search frameworkintegration`.


{% highlight bash %}
$ apt search frameworkintegration
Sorting... Done
Full Text Search... Done
frameworkintegration/xenial,now 5.39.0-0neon+16.04+xenial+build42 amd64 [installed]
  KF5 cross-framework integration plugins

frameworkintegration-dbg/xenial 5.18.0-0ubuntu1 amd64
  KF5 cross-framework integration plugins - debug files

frameworkintegration-dbgsym/xenial 5.39.0-0neon+16.04+xenial+build42 amd64
  Debug symbols for frameworkintegration
{% endhighlight %}

Looks like neon packages it under the name `frameworkintegration`. We can now install the dependencies with:

{% highlight bash %}
sudo apt-get build-dep frameworkintegration
{% endhighlight %}



