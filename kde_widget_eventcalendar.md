---
layout: page
title: Widget - Event Calendar
permalink: /kde/widget/eventcalendar/

features:
  - title: Weather
    text: Daily forecast in the agenda, and hourly forecast in the meteogram.
    img: /pic/2019-09-17___19-56-43.png
  - title: Agenda
    text: View a quick list of upcoming events from your Google Calendar or your regional Holidays.
    img: /pic/2019-09-17___19-18-11.png
  - title: Timer
    text: A quick to access timer.
    img: /pic/2019-09-17___19-59-36.png
  - title: Google Calendar Integration
    text: Double click a day in the Calendar to create a new event in the web browser.
    img: /pic/2019-09-18___20-21-01.png
  - title: Google Calendar Integration
    text: Clicking a day in the agenda opens a quick form for creating an event.
    img: /pic/2019-09-17___20-08-18.png
  - title: Google Calendar Integration
    text: Clicking an event in the agenda opens the event in the browser.
    img: /pic/2019-09-18___20-16-58.png
  - title: Mouse Wheel Volume Control
    text: Scrolling over the clock controls the volume.
    img: /pic/2019-09-18___20-27-03.png
  - title: Hide Meteogram/Timer
    text: You can turn off various features.
    img: /pic/2019-09-17___20-00-43.png
  - title: Single Column Layout
    text: Configure the agenda to appear above the calendar.
    img: /pic/2019-09-18___20-24-04.png
---

An extended calendar with daily weather forecasts and events from Google Calendar. Also includes a timer and 24 hour forecast graph.

* <https://store.kde.org/p/998901/>
* **Git Repo:** <https://github.com/Zren/plasma-applet-eventcalendar>
* **Submit Bugs** [here](https://github.com/Zren/plasma-applet-eventcalendar/issues>)

Based on the [Event Flow Calendar](https://play.google.com/store/apps/details?id=com.syncedsynapse.eventflowwidget) for android. Combines code from [weather-widget](https://store.kde.org/p/998917/), volume control from the [Media Controller Compact](https://store.kde.org/p/998887/) widget, and the default calendar + timer widgets.


## Install (All KDE Distros)

1. Right click your panel > Panel Options > Add Widgets
2. Get New Widgets > Download New Plasma Widgets
3. Search for "Event Calendar" > Install
4. Right click the clock in your panel > Show Alternatives
5. Select "Event Calendar"

## Install (Arch Linux)

{% highlight bash %}
pacman -S plasma5-applets-eventcalendar
{% endhighlight %}

## Features

{% include featureList.html features=page.features %}




