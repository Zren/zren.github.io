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

![](/pic/2019-09-18___20-33-22.png)

* <https://store.kde.org/p/998901/>
* **Git Repo:** <https://github.com/Zren/plasma-applet-eventcalendar>
* **Submit Bugs** [here](https://github.com/Zren/plasma-applet-eventcalendar/issues)

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

## Privacy Policy

A privacy policy is required for Google to authorize access to a "[sensitive API scope](https://developers.google.com/identity/protocols/googlescopes)" like the Calendar API.

<style type="text/css">
.privacy-policy,
.privacy-policy p {
  font-family: sans-serif;
  font-size: 16px;
}
</style>

{:.privacy-policy}
> By downloading the widget from the KDE panel directly, you are downloading from the [KDE Store](https://store.kde.org) which has a privacy policty at <https://store.kde.org/privacy>. By downloading the widget from Arch Linux's AUR, you are downloading from GitHub which has their own [privacy policy](https://help.github.com/en/articles/github-privacy-statement).
>
> The widget developer has access to the number of downloads for each release of the widget. The developer does not have access to where each download originates.
>
> **Google**
>
> By default the widget will not connect to the Google Calendar API. You need to click a link in the widget's config that will open up a login form in your web browser. Once you have logged in, it will give you a "login code" to paste into the widget. The widget will then fetch your calendar, event, and task data from the Google Calendar and Google Tasks API. This data will be displayed in your KDE Plasma panel. The widget will periodically synchronize this data in order to keep it up to date. The user can also manually synchronize the data. The widget will store a cached list of your events/calendars/tasks locally on your computer so it can fallback to the cached copy when your PC is offline. The widget will also store a login/refresh token to in your widget config (`~/.config/plasma-org.kde.plasma.desktop-appletsrc`) so you do not need to login every time you restart KDE Plasma. You may wish to read Google's [privacy policy](https://policies.google.com/privacy) if you have not already.
>
> The developer has access to Google API's application metrics for this widget. This allows the developer to see the total number of correct API responses, or errors, broken down by action. Some example actions are "fetch all calendars", "fetch all events", "create event", "delete event". The totals are not broken down by user. Each action has a sum of requests by all users. This is useful for knowing how close to the Google API quota the widget is, and if there are any spikes in errors. The errors are displayed as [HTTP Error codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) and do not expose any personal data to the developer.
>
> **OpenWeatherMap**
>
> By default the widget will not connect to [OpenWeatherMap.org](https://openweathermap.org). You need to manually select your city in the widget's config. Once you have selected a city, you will then fetch the current weather forecast every hour. OpenWeatherMap will be able to know the city you requested as well as your IP address. You may wish to read OpenWeatherMap's [privacy policy](https://openweather.co.uk/privacy-policy) as well.
