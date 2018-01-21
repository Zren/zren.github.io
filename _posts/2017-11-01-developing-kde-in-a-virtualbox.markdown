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

## Installing VirtualBox Additions

Next we need to link our "Code" folder in the host OS to the client OS so that if the client OS breaks, we still have access to the code.

... TODO

Now that's we've installed the VBox Additions, we can now create shared folders.

Go to the NeonDev's Settings and visit the Shared Folders section.

Create a new shared folder with the name `Code` that auto-mounts, and is permanent. Do not make it read only.

After restarting the VM, you should now be able to visit your host OS's folder at `/media/sf_Code`.

I've aliased the following in my Host OS's `~/.bashrc` so all I need is to type `neondev` to start in my Code directory.

{% highlight bash %}
alias neondev='ssh -t -p 2222 neondev@localhost "cd /media/sf_Code ; bash -l"'
{% endhighlight %}

Congrats, you've now linked the virtual machine enough to develop with your current dev tools (at full speed), with the ability to build and test with a secluded environment that won't break your day to day OS.


## Building a KDE Package

I want to modify `frameworksintegration`. A mirror of the source code [can be found on GitHub](https://github.com/KDE/frameworkintegration).

First we download the source with:

{% highlight bash %}
git clone git@github.com:KDE/frameworkintegration.git
cd frameworkintegration
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

Next we test building the project.

{% highlight bash %}
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=ON -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
sudo make install
{% endhighlight %}

I've personally made a `/usr/local/bin/kmake` script to simplify the above.

<https://gist.github.com/Zren/55ef7c10088ee69480ae73a594e00456>

{% highlight bash %}
SUDO_EDITOR=kwrite sudoedit /usr/local/bin/kmake
sudo chmod +x /usr/local/bin/kmake
{% endhighlight %}

If all went well, we can move onto trying to modify the code.



