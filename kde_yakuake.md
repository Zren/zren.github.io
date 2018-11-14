---
layout: page
title: Yakuake
permalink: /kde/yakuake/
redirect_from: /projects/kde/yakuake/
---

The Yakuake terminal is installed by default on some ditros. It's basically a fancy dropdown terminal with a global shortcut that will hide when it loses focus.

There are a few mods I apply to it to make it and Konsole look better.

![](https://i.imgur.com/baM5xrA.png)

## 1. Use a skin with a thin/hidden titlebar.

I personally use [a skin I made](https://store.kde.org/p/1165686/) based on Sublime Text 3 called Soda Dark.

## 2. DarkSolarized color scheme.
* Save [this DarkSolarized.colorscheme](https://gist.githubusercontent.com/Zren/ac21428f75e4d121026df0fe1264ad86/raw/DarkSolarized.colorscheme) to `~/.local/share/konsole/DarkSolarized.colorscheme`
* Right click Yakuake > Edit Current Profile > Appearance and select DarkSolarized.

## 3. Apply color scheme to the scrollbar

This also colors the scrollbar + tabs in Konsole.

* [Paste this](https://gist.githubusercontent.com/Zren/b77d43816125676e9db55e69837c8e5d/raw/konsolerc) into `~/.config/konsolerc` and `~/.config/yakuakerc`
* Restart yakuake `killall yakuake; kstart5 yakuake`


## 4. Change the `$PS1`

I prefer having the current directory on a different line than the command input.

![](https://i.imgur.com/dgFucbV.png)

So add this to your `~/.bashrc`.

{% highlight bash %}
### http://stackoverflow.com/questions/4133904/ps1-line-with-git-current-branch-and-colors

# \e     an ASCII escape character (033)
# \]     end a sequence of non-printing characters
# \s     the  name  of  the shell, the basename of $0
#        (the portion following the final slash)
# \a     an ASCII bell character (07)
# \n     newline
# \[     begin a sequence of non-printing characters,
#        which could be used to embed a terminal
#        con­trol sequence into the prompt
# \w     the current working directory
### https://wiki.archlinux.org/index.php/Bash/Prompt_customization#Colors
# \e[1      bold
# \e[4Xm    set background color X (0-7)
# \e[3Xm    set text color X (0-7)
# \e[m      reset text attributes
function __git_stuff {
  if [ -n "$(git rev-parse --git-dir 2>/dev/null)" ]; then
    local __a=`git name-rev --name-only @`
    echo "($__a) "
  fi
}
PS1_a='\e];\s\a\n'                # Cleanup?
PS1_b='\e[1m\e[36m$(__git_stuff)' # Git
PS1_c='\e[31m\w'                  # Working Dir
PS1_d='\e[m\n$ '                  # Prompt (on new line)
PS1="$PS1_a$PS1_b$PS1_c$PS1_d"
{% endhighlight %}

## 5. Popup from the bottom.

* Disable animations (duration = 0ms).
* Width: 100%
* Height: 70%
* Use a KWin Rule to position at the bottom.
    * Position: `Force` `0,315`  
      1080 pixel height screen - 30px bottom panel = 1050px  
      100% - 70% screen height = 30%
      1050px * 0.3 = 315px

## 6. Add "Open Yakuake Here" right click action to Dolphin (the file manager).

> Note: This was based off the [KDE3 Service menu on the KDE Store](https://store.kde.org/p/998412/).

Create the `/usr/local/bin/yakuakehere` command.

{% highlight bash %}
sudo touch /usr/local/bin/yakuakehere
sudo chmod +x /usr/local/bin/yakuakehere
SUDO_EDITOR=kate sudoedit /usr/local/bin/yakuakehere
{% endhighlight %}

with the contents:

{% highlight bash %}
#!/bin/bash

if [ "$1" != "" ]; then
    command="cd ""'"$1"'"
else
    PWD=`pwd`
    command="cd ""'"$PWD"'"
fi

qdbus org.kde.yakuake /yakuake/sessions addSession
qdbus org.kde.yakuake /yakuake/sessions runCommand "$command"
qdbus org.kde.yakuake /yakuake/sessions runCommand "clear"
qdbus org.kde.yakuake /yakuake/window toggleWindowState
{% endhighlight %}

then create: `~/.local/share/kservices5/ServiceMenus/YakuakeHere.desktop`

{% highlight bash %}
mkdir -p ~/.local/share/kservices5/ServiceMenus/
touch ~/.local/share/kservices5/ServiceMenus/YakuakeHere.desktop
{% endhighlight %}

with the contents:

{% highlight bash %}
[Desktop Entry]
Type=Service
X-KDE-ServiceTypes=KonqPopupMenu/Plugin
MimeType=inode/directory
Actions=OpenYakuake
X-KDE-AuthorizeAction=shell_access
X-KDE-Priority=TopLevel

[Desktop Action OpenYakuake]
Icon=yakuake
Exec=yakuakehere %f
Name=Open Yakuake Here
Comment=Opens a new tab in Yakuake at the current folder
{% endhighlight %}

then finally run `kbuildsycoca5` to apply the changes.

## 7. Make shortcuts similiar to the web browser

* Close Session: `Ctrl+W`
* New Session: `Ctrl+T`
* Next Session: `Ctrl+Tab`
* Previous Session: `Ctrl+Shift+Tab`

I also set the global shortcut to toggle Yakuake to be <code>Meta+`</code> (the backtick underneath `~`).
