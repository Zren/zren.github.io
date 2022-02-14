---
title: Custom Weather Widgets in Plasma 5.24
layout: post
---

For those unaware, KDE ships it's own Weather Widget. The weather service parsers are a Plasma DataEngine shipped in `plasma-workspace` while the actual visual widget is in the `kdeplasma-addons` git repo. Kubuntu breaks up that repo up into several packages however, so you'll need to install [`plasma-widgets-addons`](https://packages.ubuntu.com/focal/plasma-widgets-addons).

```bash
sudo apt install plasma-widgets-addons # Kubuntu / KDE Neon
```

* **[Weather Forecast Widget](https://zren.github.io/kde/repos/#weather-forecast):** [GitLab](https://invent.kde.org/plasma/kdeplasma-addons/-/tree/master/applets/weather) \| [All Bugs](https://bugs.kde.org/buglist.cgi?order=bug_id%20DESC&query_format=advanced&product=kdeplasma-addons&component=weather) \| [New Bug](https://bugs.kde.org/enter_bug.cgi?product=kdeplasma-addons&component=weather) \| [Merge Requests](https://invent.kde.org/plasma/kdeplasma-addons/-/merge_requests) \| [New MR](https://invent.kde.org/plasma/kdeplasma-addons/-/merge_requests/new)
* **[Weather Sources](https://zren.github.io/kde/repos/#weather-sources):** [GitLab](https://invent.kde.org/plasma/plasma-workspace/-/tree/master/dataengines/weather/ions) \| [All Bugs](https://bugs.kde.org/buglist.cgi?order=bug_id%20DESC&query_format=advanced&product=plasmashell&component=Weather) \| [New Bug](https://bugs.kde.org/enter_bug.cgi?product=plasmashell&component=Weather) \| [Merge Requests](https://invent.kde.org/plasma/plasma-workspace/-/merge_requests) \| [New MR](https://invent.kde.org/plasma/plasma-workspace/-/merge_requests/new)

In the past few versions of Plasma, there's been several changes to the official KDE weather widget shipped in the `kdeplasma-addons` repository.

* Rewritten config to use `Kirigami` + `QtQuick.Controls 2.0`.
* Updated city selector to be easier to use, searching after a key is pressed rather than requiring pressing `Enter`.

In Plasma 5.24, the city selector was changed again to drop the need to select which weather service (`noaa`, `envcan`, `wettercom`, `bbcukmet`) before searching for the city. This makes it easier to setup. It removed the private `ServiceListModel` class with an even more private `plasmoid.nativeInterface.providers` variable. `plasmoid.nativeInterface` can only be used by the official widget with the id `org.kde.plasma.weather` so forked widgets cannot use it.

https://invent.kde.org/plasma/kdeplasma-addons/-/commit/2484b96f663aa3226271a4db1f7cef0948d3b605

Alas, since I was using the private `ServiceListModel` class, I needed to update my 3 weather widgets ([Condensed Weather](https://store.kde.org/p/1353451), [Daily Forecast](https://store.kde.org/p/1287928), [Simple Weather](https://store.kde.org/p/1287571)) which fork the upstream widget.

Luckily the weather DataEngine has a `weatherDataSource.data['ions']` property which we can use instead. Install `plasma-sdk` then launch the "Plasma Engine Explorer" app to see. Select the "weather" dataengine in the dropdown, and you'll see the `ions` property.

![](/pic/2022-02-13___20-09-31.png)

It looks like there was also another weather service added in Plasma 5.24, the German Weather Service (`dwd`).

https://invent.kde.org/plasma/plasma-workspace/-/commit/bae13fa8c241f28b41cef1daeb4068c0e543801b

So to replace `ServiceListModel`, I wrote the following:

```qml
// Use weather dataengine to list weather providers instead of plasmoid.nativeInterface.providers
property alias providers: weatherDataSource.ionServiceList
readonly property bool hasProviders: providers.length > 0
property var weatherDataSource: PlasmaCore.DataSource {
	id: weatherDataSource
	engine: "weather"
	connectedSources: ['ions']

	// {"bbcukmet":"BBC Weather|bbcukmet","envcan":"Environment Canada|envcan","noaa":"NOAA's National Weather Service|noaa","wettercom":"wetter.com|wettercom"}
	readonly property var ions: data['ions']
	readonly property var ionServiceList: ions ? Object.keys(ions) : []
	// onIonsChanged: console.log('ions', JSON.stringify(ions))
	// onIonServiceListChanged: console.log('ionServiceList', JSON.stringify(ionServiceList))
}
```

The default KDE weather widget heavily uses `plasmoid.nativeInterface` for configuration as well, so I can't recommend forking it. If you want to create your own weather widget, I recommend using my `libweather` QML files, or forking one of my widgets.

* https://github.com/Zren/plasma-applet-lib/tree/master/package/contents/ui/libweather
* https://github.com/Zren/plasma-applet-simpleweather
* https://github.com/Zren/plasma-applet-dailyforecast
* https://github.com/Zren/plasma-applet-condensedweather

![](/pic/2022-02-13___19-36-15.png)
![](/pic/2022-02-13___19-34-53.png)
