---
layout: page
title: AMD Gaming with KDE Neon
permalink: /amdgaming/
---

<style type="text/css">
.post-content h2 {
    border-bottom: 1px solid;
    font-weight: bold;
    line-height: 1;
    margin-top: 1.5em;
}
</style>



## Dead Island

**Updated:** June 16, 2018

I previously tried running this game around the release of Ubuntu 16.04.0, and it could not get past the "New Game" menu. It would crash when trying to load the actual game.

Note, I only own the original version, not the [Dead Island Definitive Edition](https://store.steampowered.com/app/383150/Dead_Island_Definitive_Edition/).

24 months later, I hoped the AMD drivers had gotten good enough to play this game. Unfortunately, it was worse. I couldn't even get pass the "title screen" after the intro movie. It crashes while loading after the "Press any key to continue" screen when trying to load the Main Menu.

* KDE Neon / Ubuntu 16.04.4
* [XFX - Radeon R7 370 2GB](https://ca.pcpartpicker.com/product/9jyxFT/xfx-video-card-r7370p2255)
* Linux Kernel: `v4.13.0-45-generic`
* `glxinfo | grep OpenGL`
    * OpenGL renderer string: AMD PITCAIRN (DRM 2.50.0 / 4.13.0-45-generic, LLVM 5.0.0)
    * OpenGL core profile version string: 4.5 (Core Profile) Mesa 17.2.8

### Crashes

* Game crashes when trying to load the main menu after the title screen.




## Shadow Warrior

**Updated:** June 14, 2018

I tried out Shadow Warrior today. Experience a few freezes, so I think I'll wait for the next Mesa update before trying again.

* KDE Neon / Ubuntu 16.04.4
* [XFX - Radeon R7 370 2GB](https://ca.pcpartpicker.com/product/9jyxFT/xfx-video-card-r7370p2255)
* Linux Kernel: `v4.13.0-45-generic`
* `glxinfo | grep OpenGL`
    * OpenGL renderer string: AMD PITCAIRN (DRM 2.50.0 / 4.13.0-45-generic, LLVM 5.0.0)
    * OpenGL core profile version string: 4.5 (Core Profile) Mesa 17.2.8

### Crashes

* During the Chapter 1 intro cutscene, after the sword was placed on the ground. The screen froze, as if the it dropped to 0 FPS, while the audio continued to play. Eventually the audio stopped (audio buffer was used up), and the screen turned off (lost video output). `Ctrl+Alt+F1` to change to TTY1 didn't work. After restarting the PC, I could not reproduce the second time through the cutscene.
* Same crash happened later on in the chapter when you first encounter human enemies.




## Mad Max

**Updated:** June 13, 2018

I played through Mad Max without any crashes. I had to open up my case and point a desk fan to keep the GPU temps down (70°C => 60°C). This is more of an issue with my Desktop PC having bad airflow than a problem with the game.

* KDE Neon / Ubuntu 16.04.4
* [XFX - Radeon R7 370 2GB](https://ca.pcpartpicker.com/product/9jyxFT/xfx-video-card-r7370p2255)
* Linux Kernel: `v4.13.0-45-generic`
* `glxinfo | grep OpenGL`
    * OpenGL renderer string: AMD PITCAIRN (DRM 2.50.0 / 4.13.0-45-generic, LLVM 5.0.0)
    * OpenGL core profile version string: 4.5 (Core Profile) Mesa 17.2.8

