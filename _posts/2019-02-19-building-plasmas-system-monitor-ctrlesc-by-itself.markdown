---
title: Building Plasma's System Monitor (Ctrl+Esc) By Itself
layout: post
---

Unlike KSysGuard, the "System Monitor" that ships with the `plasma-workspace` package is fairly useful, and defaults to a useful shortcut. I usally have System Monitor sorted by "Relative Sort Time" so that I can quickly see the newest processes and if they're the cause of what's slowing down my PC.

The System Monitor does not come bundled with the CPU/RAM/Swap usage tab, or the ability to monitor other sensors, it's just the process list.

Unfortunately, you'll need to compile the entire plasma-workspace repo just to edit it, so lets try editing the `plasma-workspace/systemmonitor/CMakeList.txt` to only build the `systemmonitor` binary.

First add the minimum cmake, qt, and KDE Frameworks version definitions, wjich I've mentioned in other "build ___ by itself" blog posts.

{% highlight cmake %}
cmake_minimum_required(VERSION 3.0)

project(plasma-workspace-systemmonitor)

set(QT_MIN_VERSION "5.5.0")
set(KF5_MIN_VERSION "5.54.0")
{% endhighlight %}

Next we're going to define a custom variable to target the minimum ksysguard version which is shipped under the "plasma" version.

{% highlight cmake %}
set(PLASMA_MIN_VERSION "5.14.5")
{% endhighlight %}

Then add some more standard stuff from previous blog posts. We populate the KF5 components using the components mentioned in the `target_link_libraries()` further down.

{% highlight cmake %}
find_package(ECM 1.8.0 REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR} ${CMAKE_MODULE_PATH})


include(KDEInstallDirs)
include(KDECMakeSettings)
include(KDECompilerSettings NO_POLICY_SCOPE)
include(ECMQtDeclareLoggingCategory)

find_package(Qt5 ${QT_MIN_VERSION} CONFIG REQUIRED COMPONENTS
    Core
    Widgets
)

find_package(KF5 ${KF5_MIN_VERSION} REQUIRED COMPONENTS
    DBusAddons
    GlobalAccel
    I18n
    WindowSystem
    XmlGui
)
{% endhighlight %}

Lastly, we import the `SysGuard` component using the `PLASMA_MIN_VERSION`.

{% highlight cmake %}
find_package(KF5 ${PLASMA_MIN_VERSION} REQUIRED COMPONENTS
    SysGuard
)
{% endhighlight %}

Finally, we need to remove a [recently added Wayland workaround](https://phabricator.kde.org/D10816) part of the code to get this folder to build.

We need to remove `PW::KWorkspace` from `target_link_libraries(systemmonitor` below. Then we need to remove the `kworkspace.h` import and function call in `main.cpp`.

{% highlight diff %}
 diff --git a/systemmonitor/CMakeLists.txt b/systemmonitor/CMakeLists.txt
index 651cc1f2..9d2c84cd 100644
--- a/systemmonitor/CMakeLists.txt
+++ b/systemmonitor/CMakeLists.txt
@@ -31,7 +31,7 @@ target_link_libraries(systemmonitor
     KF5::XmlGui
     KF5::GlobalAccel
     KF5::WindowSystem
-    PW::KWorkspace
+    # PW::KWorkspace
 )
 
 install(TARGETS systemmonitor DESTINATION ${KDE_INSTALL_BINDIR})
diff --git a/systemmonitor/main.cpp b/systemmonitor/main.cpp
index 7311580b..7397dcf6 100644
--- a/systemmonitor/main.cpp
+++ b/systemmonitor/main.cpp
@@ -21,13 +21,13 @@
 #include <QDBusConnection>
 #include <KLocalizedString>
 
-#include <kworkspace.h>
+// #include <kworkspace.h>
 
 #include "ksystemactivitydialog.h"
 
 int main(int argc, char** argv)
 {
-    KWorkSpace::detectPlatform(argc, argv);
+    // KWorkSpace::detectPlatform(argc, argv);
     QApplication app(argc, argv);
     KLocalizedString::setApplicationDomain("systemmonitor");
{% endhighlight %}



### Compiling

You might be interested in my `kmake` script [here](https://gist.github.com/Zren/3f859c267ac1148aaedcf54a9bacb00f). If not, just run the following:

{% highlight bash %}
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
cd ..
{% endhighlight %}

Test it worked with:

{% highlight bash %}
./build/systemmonitor
{% endhighlight %}
