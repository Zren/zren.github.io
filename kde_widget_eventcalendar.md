---
layout: page
title: Widget - Event Calendar
permalink: /kde/widget/eventcalendar/
---

An extended calendar with daily weather forecasts and events from Google Calendar. Also includes a timer and 24 hour forecast graph.

Based on the [Event Flow Calendar](https://play.google.com/store/apps/details?id=com.syncedsynapse.eventflowwidget) for android. Combines code from [weather-widget](https://store.kde.org/p/998917/), volume control from the [Media Controller Compact](https://store.kde.org/p/998887/) widget, and the default calendar + timer widgets.

* <https://store.kde.org/p/998901/>
* Git Repo: <https://github.com/Zren/plasma-applet-eventcalendar>
* Submit Bugs [here](https://github.com/Zren/plasma-applet-eventcalendar/issues>)


### Install (All KDE Distros)

1. Right click your panel > Panel Options > Add Widgets
2. Get New Widgets > Download New Plasma Widgets
3. Search for "Event Calendar" > Install
4. Right click the clock in your panel > Show Alternatives
5. Select "Event Calendar"

### Install (Arch Linux)

{% highlight bash %}
pacman -S plasma5-applets-eventcalendar
{% endhighlight %}

### Features

<style type="text/css">
.card-grid {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
.card {
  position: relative;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0,0,0,.125);
  border-radius: .25rem;
}
.card-img-top {
  width: 100%;
  border-top-left-radius: calc(.25rem - 1px);
  border-top-right-radius: calc(.25rem - 1px);
}
.card-body {
  -webkit-box-flex: 1;
  -ms-flex: 1 1 auto;
  flex: 1 1 auto;
  padding: 1.25rem;
}
h5.card-title {
  font-family: sans-serif;
  font-size: 18px;
  margin-bottom: 10px;
}
p.card-text {
  font-family: sans-serif;
  font-size: 14px;
}

.feature-grid > .feature  {
  width: 30%;
  margin-bottom: 20px;
}
</style>

<div class="card-grid feature-grid">
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/2019-09-17___19-56-43.png">
      <div class="card-body">
        <h5 class="card-title">Weather</h5>
        <p class="card-text">Daily forecast in the agenda, and hourly forecast in the meteogram.</p>
      </div>
    </div>
  </div>
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/2019-09-17___19-18-11.png">
      <div class="card-body">
        <h5 class="card-title">Agenda</h5>
        <p class="card-text">View a quick list of upcoming events from your Google Calendar or your regional Holidays.</p>
      </div>
    </div>
  </div>
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/2019-09-17___19-59-36.png">
      <div class="card-body">
        <h5 class="card-title">Timer</h5>
        <p class="card-text">A quick to access timer.</p>
      </div>
    </div>
  </div>
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/.png">
      <div class="card-body">
        <h5 class="card-title">Google Calendar Integration</h5>
        <p class="card-text">Double click an event in the Calendar to create a new event in the web browser.</p>
      </div>
    </div>
  </div>
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/2019-09-17___20-08-18.png">
      <div class="card-body">
        <h5 class="card-title">Google Calendar Integration</h5>
        <p class="card-text">Clicking a day in the agenda opens a quick form for creating an event.</p>
      </div>
    </div>
  </div>
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/.png">
      <div class="card-body">
        <h5 class="card-title">Google Calendar Integration</h5>
        <p class="card-text">Clicking an event in the agenda opens the event in the browser.</p>
      </div>
    </div>
  </div>
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/.png">
      <div class="card-body">
        <h5 class="card-title">Mouse Wheel Volume Control</h5>
        <p class="card-text">Scrolling over the clock controls the volume.</p>
      </div>
    </div>
  </div>
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/2019-09-17___20-00-43.png">
      <div class="card-body">
        <h5 class="card-title">Hide Meteogram/Timer</h5>
        <p class="card-text">You can turn off various features.</p>
      </div>
    </div>
  </div>
  <div class="feature">
    <div class="card">
      <img class="card-img-top" src="/pic/.png">
      <div class="card-body">
        <h5 class="card-title">Single Column Layout</h5>
        <p class="card-text"></p>
      </div>
    </div>
  </div>
</div>




