---
layout: page
title: KDE Plasma5 Fixes
permalink: /kde/
---


This page aims to setup a nice KDE Plasma5 desktop for someone who's coming from Windows.

## KDE Neon: Missing Software / Fixes

There are a few things missing from User Edition of KDE Neon for regular usage.

{% highlight bash %}
sudo apt install -y kdeplasma-addons # "Big Icons" Alt+Tab
sudo apt install -y libnotify-bin
    # notify-send (Dota 2 Notifications)
sudo apt install -y p7zip-full p7zip-rar # (.7z)
sudo apt install -y qapt-deb-installer # (.deb) GUI Installer
sudo apt install -y software-properties-common
    # add-apt-repository
sudo apt install -y unrar # (.rar)
{% endhighlight %}

## Useful Software

{% highlight bash %}
sudo apt install -y clementine # Music Player (.mp3 SoundCloud)
sudo apt install -y comix # Image Viewer (.cbr .zip .rar)
sudo apt install -y gimp # Image Editor (.jpg .png)
sudo apt install -y htop # Command Line Task Manager
sudo apt install -y inkscape # Vector Image Editor (.svg)
sudo apt install -y scrot # Command Line Screen Capture
sudo apt install -y xbindkey # Remap Mouse Buttons / Keys
sudo apt install -y xdotool # Command Line Trigger Mouse/Keys
sudo apt install -y vlc # Video Player (.mp4 .mkv)

## Chrome
cd ~/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
# Set Chrome as the default browser for hexchat (TODO: xdg-mime)
gvfs-mime --set x-scheme-handler/http google-chrome.desktop
gvfs-mime --set x-scheme-handler/https google-chrome.desktop

## Calibre
# https://calibre-ebook.com/download_linux (Isolated install)
# Installs to ~/calibre-bin/
wget -nv -O- https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py | python -c "import sys; main=lambda x,y:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main('~/calibre-bin', True)"

## Redshift (Redden the Screen / f.lux Alternative)
sudo apt install -y redshift
# Unlock Widgets > Right Click ☰ > Add Widgets
# Get New Widgets > Download New Widgets > Redshift Control
# System Tray Settings > General Tab > Enable Redshift
{% endhighlight %}


### Windows Software Emulation

{% highlight bash %}
sudo apt install -y virtualbox-qt # Virtual Machine
{% endhighlight %}

### Developer Software

{% highlight bash %}
sudo apt install -y cmake
sudo apt install -y curl
sudo apt install -y pgadmin3 # DB Editor (PostgreSQL)
sudo apt install -y postgresql postgresql-contrib
sudo apt install -y python-pip python3-pip
sudo apt install -y sqliteman # DB Editor (.sqlite)

## Android Studio
# Via ubuntu-make: http://askubuntu.com/a/677805/513249
# "umake android" is broken in 16.04
sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
sudo apt update
sudo apt install ubuntu-make
umake android # Prompts InstallDirectory + License
sudo apt install openjdk-8-jre
# Run with:
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/ /home/chris/.local/share/umake/android/android-studio/bin/studio.sh

## Git
sudo apt install -y git
git config --global push.default matching

## Heroku
# https://toolbelt.heroku.com/debian
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku login # Prompts for Credentials

## NodeJS
# https://nodejs.org/en/download/package-manager/
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
sudo apt install -y nodejs
sudo apt install -y build-essential

## Sublime Text
# http://askubuntu.com/questions/172698/how-do-i-install-sublime-text-2-3
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt update
sudo apt install -y sublime-text-installer
# To install Package Control: https://packagecontrol.io/installation
{% endhighlight %}

### Gaming Software

{% highlight bash %}
sudo apt install -y steam # Prompts with License Agreement
sudo apt install -y playonlinux
{% endhighlight %}



## Configuration

{% assign i = 0 %}

<style>
li:first-line,
li > p:first-line {
  font-weight: bold;
}
</style>


### Desktop

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Show the (`~/Desktop`) files/links on the desktop.
  Right Click the desktop wallpaper > Desktop Settings
  Wallpaper Tab > Layout: Folder View
  Icon Tab > Arrange In: Columns
  Icon Tab > Sorting: Unsorted
  Icon Tab > Size: 4 (out of 6)

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Hide the ☰ button in the top corner
  Right Click the desktop wallpaper > Desktop/Folder View Settings
  Tweaks Tab > Uncheck: Show the desktop toolbox

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Hide the ☰ button in the panel on the bottom right
  Right Click the ☰ button > Lock Widgets.

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Always Hide System Tray Notification Icons
  Right Click the “Expand System Tray Triangle” > System Tray Settings.
  Entries Tab > Networks > Visibility: Hidden

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Disable SysTray Icon
  Right Click the “Expand System Tray Triangle” > System Tray Settings.
  General Tab > Extra Items > Uncheck: Clipboard, Battery

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Classic “Start” Menu
  While the widgets are unlocked
  Right Click the “Start” menu > Alternatives > Application Menu

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Don’t sort windows in Taskbar
  Right Click a Task > Task Manager Settings
  General Tab > Sorting: Manual

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Hide windows from other Desktops in Taskbar
  Right Click a Task > Task Manager Settings
  General Tab > Filters > Check: Current Desktop

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Pin to Apps to Taskbar
  Launch App
  Right Click app in Taskbar > Check: Show Launcher When Not Running

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Disable Top Left “Hot Corner”
  System Settings > Desktop Behaviour
  Screen Edges Tab > Top Left: No Action

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Bind Ctrl+Alt+Left/Right to Switch Desktop
  System Settings > Desktop Behaviour
  Virtual Desktops Tab > Switching > Shortcuts
  Switch One Desktop Left: Ctrl+Alt+Left
  Switch One Desktop Right: Ctrl+Alt+Right
  Switch To Desktop 1, 2, …: None

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Disable Switch Desktop when scrolling over desktop wallpaper
  Right Click the desktop wallpaper > Desktop/Folder View Settings
  Mouse Actions Tab > Remove: Vertical Scroll => Switch Desktop

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Disable focus stealing prevention
  System Settings > Window Management
  Window Behaviour Tab > Focus Stealing Prevention: None

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} “Normal” Alt+Tab popup
  System Settings > Window Management
  Task Switcher Tab > Click the "star icon"
  Install "Thumbnail Grid", then close the installer window.
  Select "Thumbnail Grid" in the dropdown.

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Disable Lock Screen
  System Settings > Desktop Behaviour > Screen Locking Tab
  Uncheck: Lock screen automatically after __ min
  Uncheck: Lock screen on resume

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Disable Logout/Shutdown Confirmation
  System Settings > Startup and Shutdown
  Desktop Session Tab > Uncheck: Confirm Logout

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Windows Keybindings for moving windows
  System Settings > Shortcuts > Global Keyboard Shortcuts Tab
  KWin > Show Desktop: Win+M
  KWin > Maximize Window: Win+Up
  KWin > Minimize Window: Win+Down
  KWin > Quick Tile Window to the Left: Win+Left
  KWin > Quick Tile Window to the Right: Win+Right
  To open the “Start Menu” with the Windows key see the next item.

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Present all windows with Win+Tab
  System Settings > Desktop Behavior
  Desktop Effects Tab > Check Present Windows
  Click the Gear Icon > Change the Ctrl+F10 shortcut to Meta+Tab

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Open “Start Menu” with Windows/Meta key
  * KDE 5.8.2
    Feature has been added by default.
  * <= KDE 5.7
    `sudo apt install ksuperkey`
  * <= KDE 5.7 (Or just use Win+Space)
    Right Click the KDE Icon > Application Menu Settings
    Keyboard Shortcuts Tab > Shortcut: Meta+Space


### Dolphin (File Manager)

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Double Click to open files
  System Settings > Input Devices
  Mouse Tab > Icons: Double Click to open files and folders

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Always Show Hidden Files
  ☰ Control > Adjust View Properties
  Check: Show hidden files
  Apply view properties to: All Folders
  Check: Use these view properties as default

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Browse (.zip / .tar.gz / .rar) with Dolphin
  ☰ Control > Configure Dolphin
  Navigation Tab > Check: Open archives as folder

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Clean up Context Menu (Right Click Menu)
  ☰ Control > Configure Dolphin
  Services Tab > Uncheck: “Copy To”, “Delete”, “File to activity”, “Send as Email”, “Send to IM”, “Send via Bluetooth”, “Send via KDE Connect”

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Show Terminal Panel
  ☰ Control > Panels > Terminal (F4)

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Paste into Terminal Panel
  ☰ Control > Configure Shortcuts
  Paste > Set Alternative (Defaulted to Shift+Insert) as “None”


# Chrome

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Overlay tabs on top of the title bar
  ⋮Button > Settings
  Appearance > Uncheck: Use system title bar and borders

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Match Titlebar with Desktop Theme
  Breeze
  Breeze Dark: [Chrome Theme](https://chrome.google.com/webstore/detail/breeze-dark/nkhdomjgcjkhipblklfchdkojecapgmc)


# Steam

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Launching Steam Fixes
  Right Click the “Start” menu > Edit Applications
  Games > Steam
  Change the command to `STEAM_FRAME_FORCE_CLOSE=1 LD_PRELOAD='/usr/$LIB/libstdc++.so.6' DISPLAY=:0 /usr/games/steam %U`
  Broken down, we just fixed:
  * Close Steam to the System Tray
    Launch with `STEAM_FRAME_FORCE_CLOSE=1 steam`
  * AMD GPU Open Source Driver Fix
    <http://askubuntu.com/questions/641700/steam-not-working-with-open-source-drivers>
    Launch with `LD_PRELOAD='/usr/$LIB/libstdc++.so.6' DISPLAY=:0 steam`

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} PixelVision2 Skin
  `cd ~/.steam/skins `
  `git clone https://github.com/somini/Pixelvision2.git`
  Steam > Settings
  Interface Tab > Select Skin: default skin => PixelVision2

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Hide “Big Picture”, etc in the System Tray Context Menu
  Steam > Settings > Interface Tab
  Set Taskbar Preferences > Only Check: Library, Exit Steam

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Hide “Friend is playing ___” Notifications
  Steam > Settings > Friends Tab
  Uncheck: When friend joins a game: display a notification

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Never Show Advertisements Popup
  Steam > Settings > Interface Tab
  Uncheck: Notify me about additions to my games and other releases


# Clementine

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Clean up UI
  Tools > Preferences
  Playback Tab > Uncheck: Show a glowing animation on the current track
  Search Tab > Uncheck: DigitallyImported, DropBox, Google Drive, Jazz
  Last.fm Tab > Uncheck: Show the “love” amd “ban” buttons
  Last.fm Tab > Uncheck: Show the scrobble button

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Don’t fade between songs
  Playback Tab > Uncheck: Fade out when stopping a track
  Playback Tab > Uncheck: Cross-fade when changing tracks manually

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} Double Click song should play song now
  Behaviour > Using the menu to add a song will: Always start playing
  Behaviour > Double clicking a song will: Replace the playlist + Always start playing

-----

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} 

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} 

{% assign i = i | plus: 1 %}
* {:#cfg-{{ i }}} 



<script>
function el(html) {
  var e = document.createElement('div');
  e.innerHTML = html;
  return e.removeChild(e.firstChild);
}

var headings = document.querySelector('.post-content').querySelectorAll('h1,h2,h3,h4,h5,h6,li[id]');
for (var e of headings) {
  var id = e.getAttribute('id');
  var a = el('<a class="header-link">¶</a>');
  a.setAttribute('href', '#' + id);
  e.insertBefore(a, e.firstChild);
  console.log(id, e, a)
}
</script>

