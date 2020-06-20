---
title: QML Connections "onFoo warnings" will get logging category in Qt 5.15.1
layout: post
---

After updating Manjaro recently, I noticed Qt 5.15 has a new deprecation warning:

> `file:///.../ToolButtonStyle.qml:209:13`:
> QML Connections:
> Implicitly defined `onFoo` properties in `Connections` are deprecated.
> Use this syntax instead: `function onFoo(<arguments>) { ... }`

This warning shows up 20-50 times when testing a widget. It's rather annoying, as it drowns out the useful warnings.

According to [the commit that added the warning](https://github.com/qt/qtdeclarative/commit/efe0bec9468d75b768d1e26d2a8b440ade5ba632), the syntax change is to remove some "magic" that figured out which variables are the signal parameters. It is being done for the ability to compile this type of QML code into C++, which is a good reason despite the headache.

So why can't we just implement the new `function onFoo() {}` format in `Connections`? Well it [is not supported in Qt 5.12](https://github.com/qt/qtdeclarative/commit/a2eef6b511988b2435c4e39b6b5551e857ce7775).

Distros using Qt 5.12 are:

* <https://repology.org/project/qt/versions>
* Ubuntu 20.04
* openSUSE Leap 15.2
* Debian Unstable + Testing
* Debian Stable (Qt 5.11)

I can't drop support for most LTS distros. Hell, Kubuntu 20.04 is only a few months old.

The only way I've found to hide these warnings, is to use the logging rule `QT_LOGGING_RULES="*.warning=false"`. That hides **all** warnings however, including the useful ones.

Fortunately David Edmundson [sent a patch](https://codereview.qt-project.org/c/qt/qtdeclarative/+/293011) to add a new logging category. The category will be `qt.qml.connections`. So I imagine I'll need to use `QT_LOGGING_RULES="qt.qml.connections.warning=false"` to hide those warnings.

Unfortunately, I'll be stuck living with these spam-like warnings until Qt 5.15.1, which is [scheduled to be released](https://wiki.qt.io/Qt_5.15_Release) in August 2020.

More discussion can be found [on StackOverflow](https://stackoverflow.com/questions/62297192/qml-connections-implicitly-defined-onfoo-properties-in-connections-are-deprecat).

----

After a night's sleep, I though about trying to build qtdeclarative from source, then ~~installing it to `/usr/local/...`~~ use `LD_PRELOAD=... plasmoidviewer`.

First things first is to download the `qtdeclarative` project. It's pretty large, so just do a shallow copy of the 5.15 branch.

```
mkdir -p ~/Code/qt
cd ~/Code/qt
git clone https://github.com/qt/qtdeclarative.git --branch 5.15 --depth 1
cd qtdeclarative
```

Looks like there's a `qtdeclarative.pro`, so that means `qmake` to generate the Makefiles. Then run `make` to compile the code.

```
qmake
make
```

`make` only uses 1 CPU core. We can use `make -j4` to use 4 cores. Don't use `make -j`. It spins up far too many threads... as I found out the hard way. It wasn't the CPU that slowed things down though. After 5 mins of slowly switching to tty2 (`Ctrl+Alt+F2`) and running `htop`, it seemed my 8Gb RAM + 10Gb Swap was full.

Anyways, as `make -j4` chugged along, I ran into a `vulkan.h` not found error. So I installed those headers by searching for and installing the package.

```
pacman -Ss vulkan
pacman -S vulkan-headers
```

The build finally completed. Now it's time to figure out which `.so` file the `qqmlconnections.cpp` code belongs to.

* No build files in `src/qml/types/`
* [`src/qml/CMakeLists.txt`](https://github.com/qt/qtdeclarative/blob/dev/src/qml/CMakeLists.txt)
* [`src/qml/qml.pro`](https://github.com/qt/qtdeclarative/blob/dev/src/qml/qml.pro)

Looks like the `.so` generated will be similar to `Qml.so`, so searching for that finds:

```
lib/libQt5Qml.so
lib/libQt5Qml.so.5
lib/libQt5Qml.so.5.15
lib/libQt5Qml.so.5.15.0
```

Awesome! Lets ~~copy those to `/usr/local/lib`~~. On second thought, installing `libQt5Qml.so.5.15.0` to `/usr/local/lib` might break all Qt Apps, including KDE Plasma. Instead lets try to localize the usage of our `libQt5Qml.so` by using a tool I just remembered, the `LD_PRELOAD=.../libQt5Qml.so` environment variable. `LD_PRELOAD` is used by tools like [MangoHUD](https://github.com/flightlessmango/MangoHud) to overload a library.

Lets try it!

```
LD_PRELOAD=~/Code/qt/qtdeclarative/lib/libQt5Qml.so.5.15.0 \
    QT_LOGGING_RULES="qt.qml.connections.warning=false=false" \
    QML_DISABLE_DISK_CACHE=false \
    plasmoidviewer -a org.kde.plasma.digitalclock
```

Unfortunately we get an error.

```
plasmoidviewer: symbol lookup error: /usr/lib/libQt5Quick.so.5: undefined symbol: _ZN12QQmlMetaType13propertyCacheEPK11QMetaObjecti, version Qt_5_PRIVATE_API
```

It looks like it's trying to access a function in `libQt5Quick.so`, but since `/usr/lib/` has an older version it does not work. Luckily, `libQt5Quick.so` is part of `qtdeclarative` too. We just need to also preload the other `lib/*.so` files.

A quick google finds [a StackOverflow solution](https://stackoverflow.com/questions/13820171/ld-library-path-not-working-while-ld-preload-works-fine) on preloading an entire folder of `.so` files. We just need to use the `LD_LIBRARY_PATH` environment variable instead!

```
LD_LIBRARY_PATH=~/Code/qt/qtdeclarative/lib/ \
    QT_LOGGING_RULES="qt.qml.connections.warning=false" \
    QML_DISABLE_DISK_CACHE=false \
    plasmoidviewer -a org.kde.plasma.digitalclock
```

It runs! And there's no more "onFoo" warnings!

As a final note, I should point out that the `qdeclarative` folder is over 1.3 Gb after building, while the `lib` folder is just 20 Mb. I recommend copying the `lib` folder and renaming it `~/Code/qt/qdeclarative-build-lib`. Then delete the 1.3 Gb `qdeclarative` folder.

This was a rather fun dive into Qt. The temporary (2 month) solution was much more difficult accomplish than I first thought, but it's satisfying to know a solution exists.

Yes... I know I could have used [`qt5-declarative-git` from the AUR](https://aur.archlinux.org/packages/qt5-declarative-git/).
