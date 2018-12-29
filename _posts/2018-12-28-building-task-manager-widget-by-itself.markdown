---
title: Building Task Manager Widget By Itself
layout: post
---

I recently was debugging KDE [Bug #401579](https://bugs.kde.org/show_bug.cgi?id=401579) and wanted to build just the Task Manager QML widget and C++ plugin by itself.

Normally you would need to compile the entire plasma-desktop project, which isn't a huge hurdle once you've gotten the development packages installed. The much more annoying problem is testing. Installing plasma-desktop without rebuilding and installing all the dependencies like plasma-workspace and plasma-frameworks could break your Plasma installation. To properly build it, you'd use the kdesrc-build scripts, but we want to avoid that.

To build it by itself, we just need to edit the `applets/taskmanager/CMakeLists.txt` so it thinks it's the "root" `CMakeList.txt` so we can avoid compiling everything else.

First lets download the plasma-desktop repo.

{% highlight bash %}
git clone git://anongit.kde.org/plasma-desktop
cd plasma-desktop
{% endhighlight %}

Then we'll open up `applets/taskmanager/CMakeLists.txt` and some of the stuff from the missing info which is mostly taken from the `CMakeLists.txt` in plasma-desktop's root directory.

{% highlight cmake %}
cmake_minimum_required(VERSION 3.0)

project(plasma-desktop)

set(PROJECT_VERSION "5.14.80")
set(PROJECT_VERSION_MAJOR 5)

set(QT_MIN_VERSION "5.11.0")
set(KF5_MIN_VERSION "5.50.0")

find_package(ECM ${ECM_MIN_VERSION} REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR} ${CMAKE_MODULE_PATH})

include(KDEInstallDirs)
include(KDECMakeSettings)
include(KDECompilerSettings NO_POLICY_SCOPE)

find_package(Qt5 ${QT_MIN_VERSION} REQUIRED COMPONENTS
    Core
    Gui
    DBus
    Widgets
    Quick
)
find_package(KF5 REQUIRED COMPONENTS
    CoreAddons
    Declarative
    DocTools
    GlobalAccel
    I18n
    Plasma
    KIO
    Activities
    ActivitiesStats
)
{% endhighlight %}

Next we can try compiling just the `applets/taskmanager` folder. We create a new "build" directory and enter it. Then we run cmake using the source code from the parent directory (`applets/taskmanager`) using `..`. `cmake` will check if all the dependencies mentioned in `CMakeLists.txt` are installed.

Then we run `make` which actually compiles your code. If you missed mentioning a dependency using `find_package()` in the `CMakeLists.txt`, `make` might throw an error. Further down in `CMakeLists.txt` will be a `target_link_libraries()` function you can use as a reference for populating `find_package()`.

{% highlight bash %}
cd applets/taskmanager
mkdir -p build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
{% endhighlight %}

If everything compiled correctly, we can install it to test it.

{% highlight bash %}
sudo make install
{% endhighlight %}

Then in another terminal, run the following to restart `plasmashell`.

{% highlight bash %}
killall plasmashell; kstart5 plasmashell
{% endhighlight %}

Now that you've setup a test environment, you can start poking around the Task Manager C++ plugin.
