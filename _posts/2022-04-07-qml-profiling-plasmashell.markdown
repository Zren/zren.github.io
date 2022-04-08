---
title: QML Profiling Plasmashell
layout: post
---

Since [my last article]({% post_url 2021-03-18-qml-profiling-plasmashell %}) on the subject, I've found out that `plasmashell` has an environment variable that enables QML Profiling which makes debugging Plasma far simpler.


Open up the Konsole app (`Meta+T`), then paste the following (`Ctrl+Shift+V`) to restart plasmashell in debug mode:

```bash
PLASMA_ENABLE_QML_DEBUG=1 plasmashell --replace -qmljsdebugger=port:5555,5565,services:CanvasFrameRate,EngineControl,DebugMessages,DebugTranslation
```

You should see the following in the logs.

```
QML debugging is enabled. Only use this in a safe environment.
QML Debugger: Waiting for connection on port 5555...
```

`PLASMA_ENABLE_QML_DEBUG=1` [tells plasmashell](https://invent.kde.org/plasma/plasma-workspace/-/blame/master/shell/main.cpp#L58-62) to create a `QQmlDebuggingEnabler` which tells it not to ignore the `-qmljsdebugger` argument.

* `-qmljsdebugger=` configures what data to expose and how to connect to it.
* `port:5555,5565` will select an open port between `5555` .. `5565`
* Without `,block,` `plasmashell` continues loading and display the panels + wallpapers.
* If we add `,block,` `plasmashell` will pause from loading until `qmlprofiler` (explained below) connects to it. This allows you to profile the startup of `plasmashell`.
* `services:CanvasFrameRate,EngineControl,DebugMessages,DebugTranslation` enables the same services that Qt Creator does. `CanvasFrameRate` is the important service as it is [the code name for the "QML Profiler"](https://github.com/qt/qtdeclarative/blob/784c62441333de8d13d31c719ac01e6096247c01/src/qml/debugger/qqmldebugserviceinterfaces.cpp#L47).

To read more about the `-qmljsdebugger` read the Qt documentation:  
<https://doc.qt.io/qt-5/qtquick-debugging.html#starting-applications>

### qmlprofiler

`qmlprofiler` (`qmlprofiler-qt5` in OpenSUSE) is a terminal command we run in a separate Konsole window/tab (`Meta+T`).

```bash
qmlprofiler --interactive --record off --attach localhost --port 5555 --output ~/Desktop/plasmashell$(date +%s).qtd
```

Breaking this command down:

* `--interactive` allows us to enter type commands to start recording, or save recordings to file.
* `--record off` tells it to not record when we connect to `plasmashell`
* `--attach localhost` switches to connecting to an already running program
* `--port 5555` which port to connect to
* `--output ~/Desktop/plasmashell$(date +%s).qtd` Make sure you save as a `.qtd` filetype or you won't be able to open it in Qt Creator.

For more help, type `qmlprofiler --help`.

After running the command you should see:

```
Connected to localhost:5555. Wait for profile data or type a command (type 'help' to show list of commands).
Recording Status: off
> 
```

Type `help` then hit `Enter`.

```
> help
The following commands are available:
'r', 'record'
    Switch recording on or off.
'o [file]', 'output [file]'
    Output profiling data to <file>. If no <file>
    parameter is given, output to whatever was given
    with --output, or standard output.
'c', 'clear'
    Clear profiling data recorded so far from memory.
'f [file]', 'flush [file]'
    Stop recording if it is running, then output the
    data, and finally clear it from memory.
'q', 'quit'
    Terminate the target process if started from
    qmlprofiler, and qmlprofiler itself.
```

Since `plasmashell` creates huge amounts of profiling data, we'll only start recording after plasma is loaded to make it easier to track down the issues occurring after it's fully loaded.

```
> record
Recording started
```

When you've finished triggering the memory leak. Type `flush` to save to the output file we specified when `qmlprofiler` was run.

```
> flush
Data written to /home/chris/Desktop/plasmashell1649368701.qtd.
```

Please note that the longer the command runs, the more data the output file uses. A simple 10 second test can create a file 2 Mb. If you do lots of interactions over 60 seconds, it can be 20 Mb. The larger the file, the longer it'll take to load in Qt Creator, and the more RAM is needed to preview it. At launch, Qt Creator uses 60-120Mb of RAM. After loading a 2Mb `.qtd` file, it uses 300Mb of RAM. After loading the 20Mb `.qtd` file, it used 600Mb of RAM and took 10 seconds to load in Qt Creator.

### Compress/Share

If you're a user, at this point you'll need to compress the file before uploading it.

Right click the file > Compress > Here (as TAR.GZ)

### Profiling Plasmashell startup

Previously, we skipped recording when plasma started up to minimize the file size. However a KDE dev might want you to profile the startup, so use these commands instead.

```bash
PLASMA_ENABLE_QML_DEBUG=1 plasmashell --replace -qmljsdebugger=port:5555,5565,block,services:CanvasFrameRate,EngineControl,DebugMessages,DebugTranslation
```

```bash
qmlprofiler --interactive --attach localhost --port 5555 --output ~/Desktop/plasmashell$(date +%s).qtd
```

If you're a developer, you can even turn this into a one liner with:

```bash
PLASMA_ENABLE_QML_DEBUG=1 qmlprofiler --interactive --output ~/Desktop/plasmashell$(date +%s).qtd plasmashell --replace
```

All you need to do is type `f` then `Enter` (ignore the plasma logs) and it'll save to file.

### Loading Trace Files In Qt Creator

If you haven't yet installed Qt Creator:

{% include installPackage.html
	ubuntu='qtcreator'
	arch='qtcreator'
	opensuse='qt5-creator'
%}

Open Qt Creator.

Click the triangle on the Debug tab, a context menu should appear. Select QML Profiler.

![](/pic/2022-04-07___19-28-40.png)

Right click the empty timeline area > Load Trace File

Select your `.qtd` file. It takes a few seconds to load small trace files. Larger files take a minute.

You'll notice a number of sections in the timeline. "Pixmap Cache", "Scene Graph", "Memory Usage", "Debug Messages", "Animations", "Compiling", "Creating", "Binding", "Handling Signal", and "JavaScript".

<video src="/vid/screen-2021-03-18_20.46.41.mp4" width="100%" autoplay loop muted controls></video>

The timeline can be scrolled, and clicked to view the details. Use `Ctrl+MouseWheel` to zoom if something is hard to click. As you can see in the video, it seems it took a while to load my wallpaper and the tile images in my [Tiled Menu](https://store.kde.org/p/1160672/) app launcher. This "Pixmap Cache" is likely asynchronous however since it's IO.

<video src="/vid/screen-2021-03-18_20.41.38.mp4" width="100%" autoplay loop muted controls></video>

There's an interesting Memory Usage section which should be useful.

![](/pic/2021-03-18___20-56-29.png)

There's also a "Flame Graph" and "Statistics" tab which tell me that my [Event Calendar widget](https://store.kde.org/p/998901/) code could be better. Functions are starting, then ending much later.

![](/pic/2021-03-18___20-42-22.png)

![](/pic/2021-03-18___20-43-13.png)
