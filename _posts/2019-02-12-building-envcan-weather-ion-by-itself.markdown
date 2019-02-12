---
title: Building EnvCan Weather Ion By Itself
layout: post
---

We first open up the `plasma-workspace` repo, and navigate to `dataengines/weather/ions/envcan`. This will be the folder we'll try to compile by itself.

To get started, we can take a look at the `templates/ion-dataengine` folder, which contains a template for creating a new weather ion (data source) for the weather widget. More info on the template can be found on [frinring's blog post](https://frinring.wordpress.com/2016/04/02/plasma-weather-widget-code-template-available-to-add-your-favorite-weather-data-provider/).

Open up `envcan/CmakeLists.txt` and add the following to the beginning of the file:

{% highlight cmake %}
cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)

project(plasma-ion-envcan)

set(QT_MIN_VERSION "5.5.0")
set(KF5_MIN_VERSION "5.18.0")
{% endhilight %}

Standard cmake stuff to begin with. The project name doesn't really matter.

{% highlight cmake %}
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR})
{% endhilight %}

This is almost standard. This imports the extra cmake files from `${CMAKE_CURRENT_SOURCE_DIR}/cmake`, `templates/ion-dataengine/` contains the `cmake/FindPlasmaWeatherIon.cmake` file which is used for importing the Plasma Weather Ion headers/library. So we need to copy the `cmake/` with the `cmake/FindPlasmaWeatherIon.cmake` into the `envcan/` folder.

{% highlight cmake %}
find_package(Qt5 ${QT_MIN_VERSION} CONFIG REQUIRED
    COMPONENTS
        Gui
        Network
)

find_package(KF5 ${KF5_MIN_VERSION} REQUIRED
    COMPONENTS
        Plasma
        KIO
        I18n
        UnitConversion
)
{% endhilight %}

Next up we `find_package()` for various `Qt5` and `KF5` modules. The template is missing the `KF5::KIO` and `KF5::I18n` components though.

{% highlight cmake %}
find_package(PlasmaWeatherIon REQUIRED)
set_package_properties(PlasmaWeatherIon PROPERTIES
    DESCRIPTION "Plasma Weather Ion library"
    TYPE REQUIRED
)
{% endhighlight %}

The above uses the `cmake/FindPlasmaWeatherIon.cmake` to import the `PlasmaWeatherIon` library.

{% highlight cmake %}
include(KDEInstallDirs)
include(KDECMakeSettings)
include(KDECompilerSettings NO_POLICY_SCOPE)
include(ECMQtDeclareLoggingCategory)
{% endhilight %}

More standard KDE cmake stuff, though the `ECMQtDeclareLoggingCategory` was not included in the template.

{% highlight cmake %}
add_definitions(-DTRANSLATION_DOMAIN=\"plasma_engine_weather\")
{% endhilight %}

We took this from `dataengines/weather/CMakeLists.txt` ([link](
https://github.com/KDE/plasma-workspace/blob/master/dataengines/weather/CMakeLists.txt#L1)) in order to reuse the existing KDE translations. If we we're making a new weather ion, we'd create a new translation domain like in the template.

That's all we need to add to the begining of the `envcan/CMakeLists.txt`.

We need to make 2 edits to the existing code to get this to compile.

First we need to add `KF5::KIOWidgets` and `KF5::Plasma` to 

{% highlight cmake %}
target_link_libraries (ion_envcan
    weather_ion
    KF5::KIOCore
    KF5::KIOWidgets
    KF5::Plasma
    KF5::UnitConversion
    KF5::I18n
)
{% endhilight %}

Then open up `envcan/ion_envcan.h` and remove the `#include "../ion.h"` line and add `#include <plasma/weather/ion.h>` in it's place. This imports from the `PlasmaWeatherIon` library instead of trying to import the `ion.h` 1 directory up which we're pretending doesn't exist so we can compile just this folder.

{% highlight cpp %}
// #include "../ion.h"
#include <plasma/weather/ion.h>
{% endhighlight %}

Here's the complete diff:

{% highlight diff %}
diff --git a/dataengines/weather/ions/envcan/CMakeLists.txt b/dataengines/weather/ions/envcan/CMakeLists.txt
index 51487bb0..77a71297 100644
--- a/dataengines/weather/ions/envcan/CMakeLists.txt
+++ b/dataengines/weather/ions/envcan/CMakeLists.txt
@@ -1,3 +1,43 @@
+cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)
+
+project(plasma-ion-envcan)
+
+set(QT_MIN_VERSION "5.5.0")
+set(KF5_MIN_VERSION "5.18.0")
+
+find_package(ECM 1.8.0 REQUIRED NO_MODULE)
+set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake ${ECM_MODULE_PATH} ${ECM_KDE_MODULE_DIR} ${CMAKE_MODULE_PATH})
+
+find_package(Qt5 ${QT_MIN_VERSION} CONFIG REQUIRED
+    COMPONENTS
+        Gui
+        Network
+)
+
+find_package(KF5 ${KF5_MIN_VERSION} REQUIRED
+    COMPONENTS
+        Plasma
+        KIO
+        I18n
+        UnitConversion
+)
+
+find_package(PlasmaWeatherIon REQUIRED)
+set_package_properties(PlasmaWeatherIon PROPERTIES
+    DESCRIPTION "Plasma Weather Ion library"
+    TYPE REQUIRED
+)
+
+include(KDEInstallDirs)
+include(KDECMakeSettings)
+include(KDECompilerSettings NO_POLICY_SCOPE)
+include(ECMQtDeclareLoggingCategory)
+
+
+add_definitions(-DTRANSLATION_DOMAIN=\"plasma_engine_weather\")
+
+
+
 set (ion_envcan_SRCS ion_envcan.cpp)
 ecm_qt_declare_logging_category(ion_envcan_SRCS
     HEADER ion_envcandebug.h
@@ -9,6 +49,8 @@ add_library(ion_envcan MODULE ${ion_envcan_SRCS})
 target_link_libraries (ion_envcan
     weather_ion
     KF5::KIOCore
+    KF5::KIOWidgets
+    KF5::Plasma
     KF5::UnitConversion
     KF5::I18n
 )
diff --git a/dataengines/weather/ions/envcan/cmake/FindPlasmaWeatherIon.cmake b/dataengines/weather/ions/envcan/cmake/FindPlasmaWeatherIon.cmake
new file mode 100644
index 00000000..4d8517f4
--- /dev/null
+++ b/dataengines/weather/ions/envcan/cmake/FindPlasmaWeatherIon.cmake
@@ -0,0 +1,31 @@
+# - Try to find the Plasma Weather Ion library
+# Once done this will define
+#
+#  PlasmaWeatherIon_FOUND - system has Plasma Weather Ion
+#  PlasmaWeatherIon_INCLUDE_DIR - the Plasma Weather Ion include directory
+#  PlasmaWeatherIon_LIBRARIES - Plasma Weather Ion library
+
+if (PlasmaWeatherIon_INCLUDE_DIR AND PlasmaWeatherIon_LIBRARY)
+    # Already in cache, be silent
+    set(PlasmaWeatherIon_FIND_QUIETLY TRUE)
+endif (PlasmaWeatherIon_INCLUDE_DIR AND PlasmaWeatherIon_LIBRARY)
+
+find_path(PlasmaWeatherIon_INCLUDE_DIR NAMES plasma/weather/ion.h)
+find_library(PlasmaWeatherIon_LIBRARY weather_ion)
+
+if (PlasmaWeatherIon_INCLUDE_DIR AND PlasmaWeatherIon_LIBRARY)
+    set(PlasmaWeatherIon_FOUND TRUE)
+    set(PlasmaWeatherIon_LIBRARIES ${PlasmaWeatherIon_LIBRARY})
+endif (PlasmaWeatherIon_INCLUDE_DIR AND PlasmaWeatherIon_LIBRARY)
+
+if (PlasmaWeatherIon_FOUND)
+    if (NOT PlasmaWeatherIon_FIND_QUIETLY)
+        message(STATUS "Found Plasma Weather Ion library: ${PlasmaWeatherIon_LIBRARIES}")
+    endif (NOT PlasmaWeatherIon_FIND_QUIETLY)
+else (PlasmaWeatherIon_FOUND)
+    if (PlasmaWeatherIon_FIND_REQUIRED)
+        message(FATAL_ERROR "Plasma Weather Ion library was not found")
+    endif(PlasmaWeatherIon_FIND_REQUIRED)
+endif (PlasmaWeatherIon_FOUND)
+
+mark_as_advanced(PlasmaWeatherIon_INCLUDE_DIR PlasmaWeatherIon_LIBRARY)
diff --git a/dataengines/weather/ions/envcan/ion_envcan.h b/dataengines/weather/ions/envcan/ion_envcan.h
index 9ac8a1cc..a4479ba8 100644
--- a/dataengines/weather/ions/envcan/ion_envcan.h
+++ b/dataengines/weather/ions/envcan/ion_envcan.h
@@ -22,7 +22,8 @@
 #ifndef ION_ENVCAN_H
 #define ION_ENVCAN_H
 
-#include "../ion.h"
+// #include "../ion.h"
+#include <plasma/weather/ion.h>
 
 #include <Plasma/DataEngineConsumer>
 
{% endhighlight %}


### Compiling


You might be interested in my `kmake` script [here](https://gist.github.com/Zren/3f859c267ac1148aaedcf54a9bacb00f). If not, just run the following:

{% highlight bash %}
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
sudo make install
{% endhighlight %}

Test it worked with:

{% highlight bash %}
plasmoidviewer -a org.kde.plasma.weather
{% endhighlight %}

### Patching

Now we can get started on modifying the Weather Ion code without worrying about other stuff in `kdeplasma-addons` breaking.

