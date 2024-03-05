---
layout: post
title: OpenSUSE Krypton Plasma 6 Setup
---

The last time I tried installing Plasma 6 in a VM with [OpenSUSE Krypton](https://en.opensuse.org/SDB:Argon_and_Krypton#Krypton), I failed to actually install Plasma 6 to develop with.

## Install via LiveCD

> Download OpenSUSE Krypton at:
> <https://download.opensuse.org/repositories/KDE:/Medias/images/iso/?P=*Krypton.*.iso>
{:.alert.alert-info}

Even though the LiveCD runs Plasma 6, if you run the installation with the default setup it will install **Plasma 5**.

![](/pic/2024-03-04___20-07-40.png)

On the [Plasma 6 wiki entry on community.kde.org](https://community.kde.org/Plasma/Plasma_6), it mentions you need to change the installed Desktop Environment.

> At the last step (installation summary), **select "Software"** and **tick "Plasma 6 Desktop Base"**.

![](/pic/2024-03-04___20-08-42.png)
![](/pic/2024-03-04___20-09-17.png)
![](/pic/2024-03-04___20-09-47.png)


## First Login

Another issue I found is that by default, the user will login to the "IceWM" Desktop Environment instead of "Plasma (Wayland)".

![](/pic/2024-03-04___21-34-01.png)

So click the App Launcher button in the bottom-left of the IceWM panel, then click Logout.

![](/pic/2024-03-04___21-34-42.png)

At the bottom-left of the SDDM Login Screen is a selector drop down to select the desktop environment you login to.

![](/pic/2024-03-04___21-35-23.png)
![](/pic/2024-03-04___21-36-36.png)


However if you have AutoLogin enabled then you will need to open up KDE's System Settings.

Search for "Login Screen (SDDM)" under "Colors & Themes".

![](/pic/2024-03-04___21-42-59.png)

Click on the "Behavior" button.

![](/pic/2024-03-04___21-43-53.png)

Then change from "(System Default)" to "Plasma (Wayland)"

![](/pic/2024-03-04___21-44-28.png)

> If you know how to change the system default [please let me know](https://github.com/Zren/zren.github.io/issues).
{:.alert.alert-warning}


## Improving the VM Experience

### Remove grub timeout

By default OpenSUSE will wait 8 seconds for you to select which boot drive you want.

* Search for "YaST" in the App Launcher
* Click "Boot Loader"
* Click the "Bootloader Options" tab
* Change "Timeout in Seconds" from `8` to `0`

![](/pic/2024-03-04___22-03-42.png)


### Disable the lock screen

First open up KDE's "System Settings".

Under "Screen Locking" change "Lock screen automatically" from `5 minutes` to `Never`.

![](/pic/2024-03-04___22-26-10.png)

Also, under "Power Management" uncheck "Turn off screen".

![](/pic/2024-03-04___22-25-18.png)


