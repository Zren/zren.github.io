---
title: Developing KRunner
layout: post
---

KRunner's source code is split amongst many repos, so I figured I'd jot down their locations here.

* [`frameworks/krunner`](https://invent.kde.org/frameworks/krunner/): declares the krunner API
* [`plasma/plasma-workspace` `/krunner`](https://invent.kde.org/plasma/plasma-workspace/-/tree/master/krunner): Logic for displaying the `Alt+Space` popup, it loads a QML view from the Plasma Global Theme (aka lookandfeel).
* [`plasma/plasma-workspace` `/lookandfeel/contents/runcommand/RunCommand.qml`](https://invent.kde.org/plasma/plasma-workspace/-/blob/master/lookandfeel/contents/runcommand/RunCommand.qml): The QML view loaded for the `Alt+Space` popup.
* `RunCommand.qml` uses [`plasma/milou`](https://invent.kde.org/plasma/milou)'s [`lib/qml` files](https://invent.kde.org/plasma/milou/-/tree/master/lib/qml).
* The `plasma/milou` repo also [contains a Plasma Widget](https://invent.kde.org/plasma/milou/-/tree/master/plasmoid). The default Application Launcher widgets also use KRunner.
* The Application Launcher widgets in `plasma-desktop` use a `Kicker.RunnerModel` which can be found in `plasma-desktop`.
  * [Application Launcher's `Kicker.RunnerModel` use](https://invent.kde.org/plasma/plasma-desktop/-/blob/master/applets/kickoff/package/contents/ui/SearchView.qml#L50)
  * [Application Menu/Dashboard's `Kicker.RunnerModel` use](https://invent.kde.org/plasma/plasma-desktop/-/blob/master/applets/kicker/package/contents/ui/main.qml#L78)
  * [`runnermodel.h`](https://invent.kde.org/plasma/plasma-workspace/-/blob/master/applets/kicker/plugin/runnermodel.h) + [`runnermodel.cpp`](https://github.com/KDE/plasma-workspace/blob/master/applets/kicker/plugin/runnermodel.cpp)
