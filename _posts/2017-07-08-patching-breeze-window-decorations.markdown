---
layout: post
title: Patching Breeze Window Decorations
---

KDE ships with the Breeze window decorations. Which are drawn via a C++ KDecoration2 "plugin". You can also download other decorations from the KDE Store (via Get Hot New Stuff) that are SVG based themes for the Aurorae KDecoration2 "plugin" (which is also preinstalled in KDE).

Editing the other SVG based themes is pretty easy, however to edit the Breeze theme, you'll need to recompile some C++, which isn't as newbie friendly.

First off, lets download the source. The window decorations are a [subfolder](https://github.com/Zren/breeze/tree/zdev/kdecoration) of the [breeze repo](https://github.com/KDE/breeze), which means we have to download the breeze cursors and the wallpapers too. Luckily the icons are in [another repo](https://github.com/KDE/breeze-icons), but the repo is still several megabytes in size since each wallpaper updates every version and is in 10 different sizes including 4K.

So lets just clone the last commit.

{% highlight bash %}
git clone git@github.com:KDE/breeze.git --depth=1
cd breeze/kdecoration
{% endhighlight %}

When you try to build, you'll probably be missing dependencies, 

{% highlight bash %}
sudo apt install libkf5config-dev libkdecorations2-dev libqt5x11extras5-dev qtdeclarative5-dev
{% endhighlight %}

If you're missing something else, it'll tell you the name, and it's probably [in this list of packages](https://askubuntu.com/a/577334/513249) you can install.

Now lets attempt to build it. Note that we'll get an error, just keep reading.

{% highlight bash %}
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DKDE_INSTALL_LIBDIR=lib -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
{% endhighlight %}

Now, we tried to compile the `kdecoration` folder by itself, rather than compiling the `breeze` project as a whole. Lets edit the `kdecoration/CMakeList.txt` so that it doesn't need the `CMakeList.txt` in the parent directory.

Lets look at everything before it imports the `kdecoration` folder and calls it's `CMakeLists.txt`.

{% highlight cmake %}
project(breeze)
set(PROJECT_VERSION "5.10.90")
set(PROJECT_VERSION_MAJOR 5)

cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)

option(USE_KDE4 "Build a widget style for KDE4 (and nothing else)")

include(WriteBasicConfigVersionFile)
include(FeatureSummary)

if(USE_KDE4)
  add_subdirectory(kstyle)
else()
  find_package(ECM 0.0.9 REQUIRED NO_MODULE)
  set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR} ${CMAKE_SOURCE_DIR}/cmake)

  include(ECMInstallIcons)
  include(KDEInstallDirs)
  include(KDECMakeSettings)
  include(KDECompilerSettings NO_POLICY_SCOPE)
  include(GenerateExportHeader)
  include(GtkUpdateIconCache)

  option(WITH_DECORATIONS "Build Breeze window decorations for KWin" ON)
  if(WITH_DECORATIONS)
    find_package(KDecoration2 REQUIRED)
    add_subdirectory(kdecoration)
  endif()
{% endhighlight %}

We can ignore the `USE_KDE4` and `WITH_DECORATIONS` conditionals since they are always going to be `false` and `true` in our case. We can also ignore the `GtkUpdateIconCache` include.

{% highlight diff %}
diff --git a/kdecoration/CMakeLists.txt b/kdecoration/CMakeLists.txt
index 5f8a873..eaba25f 100644
--- a/kdecoration/CMakeLists.txt
+++ b/kdecoration/CMakeLists.txt
@@ -1,3 +1,25 @@
+project(breeze)
+set(PROJECT_VERSION "5.10.90")
+set(PROJECT_VERSION_MAJOR 5)
+
+cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)
+
+include(WriteBasicConfigVersionFile)
+include(FeatureSummary)
+
+find_package(ECM 0.0.9 REQUIRED NO_MODULE)
+set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR} ${CMAKE_SOURCE_DIR}/cmake)
+
+include(ECMInstallIcons)
+include(KDEInstallDirs)
+include(KDECMakeSettings)
+include(KDECompilerSettings NO_POLICY_SCOPE)
+include(GenerateExportHeader)
+# include(GtkUpdateIconCache)
+
+find_package(KDecoration2 REQUIRED)
+
+
 add_definitions(-DTRANSLATION_DOMAIN="breeze_kwin_deco")
 
 find_package(KF5 REQUIRED COMPONENTS CoreAddons GuiAddons ConfigWidgets WindowSystem I18n)
{% endhighlight %}

After editing the `kdecoration/CMakeList.txt`, you'll need to clean the build directory (just delete the folder `rm -r build`). Then you can try building again.

If everything compiled 100%, we can focus on patching Breeze with new features. There are 3 things I ended up doing myself.

1. Remove the blue (highlight color) line under the titlebar when a window is focused.
2. Remove the triangle in the bottom right when set to No Borders.
3. Attempt to draw the shadows as if the light source is coming from the top/north instead of the top-left.

Here's the diffs for each.

## 1. Remove the blue (highlight color) line under the titlebar when a window is focused.

For this, we just need to comment out where it draws the line. This line is always drawn if the window's titlebar color and the window's background is different which you can [see here](https://github.com/KDE/breeze/blob/2cc0f8ba2da50ca3efa500ebdcc3655c8d0e47f8/kdecoration/breezedecoration.cpp#L154).

![](https://i.imgur.com/kP0XG9Y.png)

{% highlight diff %}
diff --git a/kdecoration/breezedecoration.cpp b/kdecoration/breezedecoration.cpp
index b186798..53d53ee 100644
--- a/kdecoration/breezedecoration.cpp
+++ b/kdecoration/breezedecoration.cpp
@@ -523,15 +523,15 @@ namespace Breeze
 
         }
 
-        const QColor outlineColor( this->outlineColor() );
-        if( !c->isShaded() && outlineColor.isValid() )
-        {
-            // outline
-            painter->setRenderHint( QPainter::Antialiasing, false );
-            painter->setBrush( Qt::NoBrush );
-            painter->setPen( outlineColor );
-            painter->drawLine( titleRect.bottomLeft(), titleRect.bottomRight() );
-        }
+        // const QColor outlineColor( this->outlineColor() );
+        // if( !c->isShaded() && outlineColor.isValid() )
+        // {
+        //     // outline
+        //     painter->setRenderHint( QPainter::Antialiasing, false );
+        //     painter->setBrush( Qt::NoBrush );
+        //     painter->setPen( outlineColor );
+        //     painter->drawLine( titleRect.bottomLeft(), titleRect.bottomRight() );
+        // }
 
         painter->restore();

{% endhighlight %}

### Testing the changes

Then build.

If everything went without a hitch, we can now install it into your system.

{% highlight bash %}
sudo make install
{% endhighlight %}

Then we can restart KWin to test our changes.

{% highlight bash %}
kwin_x11 --replace & disown
{% endhighlight %}


## 2. Remove the triangle in the bottom right when set to No Borders.

For some reason, when you chose "no borders" it adds this stupid little triangle, which is drawn *on top* of the window. For now I've been using "No side borders" which draws a bottom border but I'd like to fix that.

![](https://i.imgur.com/c8getbo.png)

It's also straightforward to remove by commenting out some code.

{% highlight diff %}
diff --git a/kdecoration/breezedecoration.cpp b/kdecoration/breezedecoration.cpp
index 53d53ee..43698c1 100644
--- a/kdecoration/breezedecoration.cpp
+++ b/kdecoration/breezedecoration.cpp
@@ -303,8 +303,8 @@ namespace Breeze
         createShadow();
 
         // size grip
-        if( hasNoBorders() && m_internalSettings->drawSizeGrip() ) createSizeGrip();
-        else deleteSizeGrip();
+        // if( hasNoBorders() && m_internalSettings->drawSizeGrip() ) createSizeGrip();
+        // else deleteSizeGrip();
 
     }
 
{% endhighlight %}


## 3. Attempt to draw the shadows as if the light source is coming from the top/north instead of the top-left.

This was a request from someone in IRC one time since it's how OS X does shadows. So I'd already spotted where things we handled. Unfortunately, it was a bit more complicated than I thought, resulting in a bit of trial and error. I'm still not 100% sure I did it correctly, but it works.

![](https://i.imgur.com/6JBaYqr.png)

{% highlight diff %}
diff --git a/kdecoration/breezedecoration.cpp b/kdecoration/breezedecoration.cpp
index 43698c1..b6f67a7 100644
--- a/kdecoration/breezedecoration.cpp
+++ b/kdecoration/breezedecoration.cpp
@@ -670,8 +670,8 @@ namespace Breeze
 
             // contrast pixel
             QRectF innerRect = QRectF(
-                g_shadowSize - shadowOffset - Metrics::Shadow_Overlap, g_shadowSize - shadowOffset - Metrics::Shadow_Overlap,
-                shadowOffset + 2*Metrics::Shadow_Overlap, shadowOffset + 2*Metrics::Shadow_Overlap );
+                g_shadowSize - Metrics::Shadow_Overlap, g_shadowSize - shadowOffset - Metrics::Shadow_Overlap,
+                2*Metrics::Shadow_Overlap, shadowOffset + 2*Metrics::Shadow_Overlap );
 
             painter.setPen( gradientStopColor( g_shadowColor, g_shadowStrength*0.5 ) );
             painter.setBrush( Qt::NoBrush );
@@ -687,7 +687,7 @@ namespace Breeze
 
             g_sShadow = QSharedPointer<KDecoration2::DecorationShadow>::create();
             g_sShadow->setPadding( QMargins(
-                g_shadowSize - shadowOffset - Metrics::Shadow_Overlap,
+                g_shadowSize - Metrics::Shadow_Overlap,
                 g_shadowSize - shadowOffset - Metrics::Shadow_Overlap,
                 g_shadowSize - Metrics::Shadow_Overlap,
                 g_shadowSize - Metrics::Shadow_Overlap ) );
diff --git a/kstyle/breezeshadowhelper.cpp b/kstyle/breezeshadowhelper.cpp
index 80fcf73..e26b0e1 100644
--- a/kstyle/breezeshadowhelper.cpp
+++ b/kstyle/breezeshadowhelper.cpp
@@ -517,7 +517,7 @@ namespace Breeze
         int size( shadowSize - Metrics::Shadow_Overlap );
         int topSize = ( size - shadowOffset ) * devicePixelRatio;
         int bottomSize = size * devicePixelRatio;
-        const int leftSize( (size - shadowOffset) * devicePixelRatio );
+        const int leftSize( size * devicePixelRatio );
         const int rightSize( size * devicePixelRatio );
 
         if( widget->inherits( "QBalloonTip" ) )
{% endhighlight %}
