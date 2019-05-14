---
layout: widepage
title: KDE Plasma5 Fixes
permalink: /kde/
redirect_from: /projects/kde/
---

This page aims to setup a nice KDE Plasma5 desktop for someone who's coming from Windows.

## KDE Neon: Missing Software / Fixes

There are a few things missing from User Edition of KDE Neon for regular usage.

{% highlight bash %}
sudo apt install -y kubuntu-driver-manager # Proprietary/Nvidia Driver Installer
sudo apt install -y kdeplasma-addons # "Big Icons" Alt+Tab
sudo apt install -y libnotify-bin # notify-send (Dota 2 Notifications)
sudo apt install -y p7zip-full p7zip-rar # (.7z)
sudo apt install -y qapt-deb-installer # (.deb) GUI Installer
sudo apt install -y software-properties-common # add-apt-repository
sudo apt install -y unrar # (.rar)
sudo apt install -y kcron # Task Scheduler in System Settings
{% endhighlight %}

## Useful Software

{% highlight bash %}
sudo apt install -y clementine # Music Player (.mp3 SoundCloud)
sudo apt install -y mcomix # Image Viewer (.cbr .zip .rar)
sudo apt install -y gimp # Image Editor (.jpg .png)
sudo apt install -y htop # Command Line Task Manager
sudo apt install -y inkscape # Vector Image Editor (.svg)
sudo apt install -y krita # Digital Painting (.jpg .png)
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
# JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/ ~/.local/share/umake/android/android-studio/bin/studio.sh

## Git
sudo apt install -y git
git config --global push.default matching

## Heroku
# https://toolbelt.heroku.com/debian
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku login # Prompts for Credentials

## NodeJS
# https://nodejs.org/en/download/package-manager/
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt install -y nodejs
sudo apt install -y build-essential

## Sublime Text
# https://www.sublimetext.com/docs/3/linux_repositories.html
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
# To install Package Control: https://packagecontrol.io/installation
{% endhighlight %}

### Gaming Software

{% highlight bash %}
sudo apt install -y steam # Prompts with License Agreement
sudo apt install -y playonlinux
{% endhighlight %}


### LibreOffice (Microsoft Office/Word Substitute)

(Optional) If you want a more up to date version of libreoffice (v6.0) vs the LTS version (v5.1), use the following ppa.

{% highlight bash %}
sudo add-apt-repository ppa:libreoffice/ppa
sudo apt update
{% endhighlight %}

Otherwise, install the gtk3 version (since it's designed for it) and the breeze style. We need the Calibri and Cambria replacement fonts otherwise Microsoft Office files will look weird. Lastly we should clean the icon cache just in case.

{% highlight bash %}
sudo apt install -y libreoffice libreoffice-gtk3 libreoffice-style-*
sudo apt install -y fonts-crosextra-carlito fonts-crosextra-caladea
rm ~/.cache/icon-cache.kcache
{% endhighlight %}


## Configuration

{% assign i = 0 %}

<style>
.tip-section > a,
.post-content li.tip > a {
  color: #606c71;
}
.post-content li.tip > a,
.post-content li.tip li:first-line {
  font-weight: bold;
}
.tip-section > a:hover,
.post-content li.tip > a:hover {
  text-decoration: none;
  color: #727E83;
}
.tip-section > a:active,
.post-content li.tip > a:active {
  color: #828E93;
}


.tip-section > a::before,
.tip > a::before {
  content: "¶";
  font-family: monospace;
  position: absolute;
  margin-left: -1em;
  min-width: 1em;
  font-weight: bold;
  opacity: 0;
  user-select: none;
}
.tip > a::before,
.tip > a:hover::before,
.tip > a:visited::before {
  color: #888;
  text-decoration: none;
}
.tip-section > a::before {
  margin-top: -0.1em;
}
.tip > a::before {
  margin-left: -2em;
  min-width: 2em;
}
.tip-section > a:hover::before,
.tip > a:hover::before {
  opacity: 1;
}
</style>


{% include_relative kde_tips/tips.md %}


-----

# Known Bugs

<ul>
{% capture label %}Open Bugs in Plasma (the taskbar/panel){% endcapture %}{% capture contents %}
  [bugs.kde.org search](https://bugs.kde.org/buglist.cgi?list_id=1536784&order=bug_id%20DESC&product=plasmashell&product=kdeplasma-addons&product=plasma-nm&product=plasma-pa&product=Plasma%20Vault&product=frameworks-plasma&product=plasma-browser-integration&product=plasma-integration&query_format=advanced)
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}File a New Bug{% endcapture %}{% capture contents %}
  <https://bugs.kde.org/>
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>


<script>
function el(html) {
  var e = document.createElement('div');
  e.innerHTML = html;
  return e.removeChild(e.firstChild);
}

var headings = document.querySelector('.post-content').querySelectorAll('h1,h2,h3,h4,h5,h6')
for (var e of headings) {
  e.classList.add('tip-section')
  var id = e.getAttribute('id')
  var a = el('<a />')
  a.setAttribute('href', '#' + id)
  a.innerHTML = e.innerHTML
  e.innerHTML = ''
  e.insertBefore(a, e.firstChild)
  console.log(id, e, a)
}
</script>

