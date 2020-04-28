---
title: How To Change Plasma Icon Theme in the Terminal
layout: post
---

![](https://i.imgur.com/dkIEQeY.png)

/u/Da_Viper on Reddit [recently asked](https://www.reddit.com/r/kde/comments/g986ql/reload_icons_and_themes_without_restarting_kde/) how to change the plasma icon theme from bash. He'd figured out that `[Icons] Theme=breeze` in `~/.config/kdeglobals` changes when you select an icon theme. However modifying that file doesn't update running applications until you restart.

If we dive into [the code for the System Settings KCM](https://github.com/KDE/plasma-desktop/tree/master/kcms/icons) on the GitHub mirror, we can see that a new file, `changeicons.cpp`, was recently [added 6 months ago](https://github.com/KDE/plasma-desktop/commit/38ba450787ae39f2e50ff0410da2296bb0b2ddd7). Looking at the `CMakeLists.txt`, that file is used for a new command line called `plasma-changeicons`. It's not in `$PATH` however, so we'll need to call the full filepath.

Run `locate plasma-changeicons` to find the filepath. For me in Manjaro with Plasma 5.18, it's `/usr/lib/plasma-changeicons`.

Now that we know the filepath, we can use the folder names found at `/usr/share/icons/` and `~/.local/share/icons/` as arguments for the command.

{% highlight bash %}
/usr/lib/plasma-changeicons breeze 
/usr/lib/plasma-changeicons breeze-dark
/usr/lib/plasma-changeicons breath # Manjaro
{% endhighlight %}

-----

Breaking down the code, `CMakeLists.txt` compiles `changeicons.cpp`, which in turn will call a function in `iconssettings.cpp`.

* <https://github.com/KDE/plasma-desktop/blob/master/kcms/icons/CMakeLists.txt#L27>
* <https://github.com/KDE/plasma-desktop/blob/master/kcms/icons/changeicons.cpp>
* <https://github.com/KDE/plasma-desktop/blob/master/kcms/icons/iconssettings.cpp#L45>
* <https://github.com/KDE/kiconthemes/blob/master/src/kiconloader.cpp#L427>

It seems `iconssettings.cpp` will:

1. Delete `~/.cache/icon-cache.kcache`
2. Notify the change to all KIconLoaders using DBus.
3. Run `kbuildsycoca5`

----

* **System Settings > [Icons](https://zren.github.io/kde/repos/#icons):** [GitHub](https://github.com/KDE/plasma-desktop/tree/master/kcms/icons) | [All Bugs](https://bugs.kde.org/buglist.cgi?order=bug_id%20DESC&query_format=advanced&product=systemsettings&component=kcm_icons) | [New Bug](https://bugs.kde.org/enter_bug.cgi?product=systemsettings&component=kcm_icons) | [Phabricator](https://phabricator.kde.org/source/plasma-desktop/) | [Pull Requests](https://phabricator.kde.org/differential/query/7LklMmkHDcva/#R) | [New PR (Repo: Plasma Desktop)](https://phabricator.kde.org/differential/diff/create/)
