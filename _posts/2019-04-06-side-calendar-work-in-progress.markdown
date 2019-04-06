---
title: Side Calendar Work In Progress
layout: post
---

While skimming around the net for inspiration for my [Event Calendar widget](https://store.kde.org/p/998901/), I discovered a [Gnome Calendar mockup](https://feaneron.com/2016/09/28/the-future-of-gnome-calendar/) from 2016.

![](https://i.imgur.com/Yws3lZY.png)


I currently have a "single column" option in event calendar, but while it's functional, it has a few papercuts.

* On a bottom panel, it slides up instead of from the side of the screen.
* The calendar is below the agenda. Dynamically reordering a [GridLayout](https://doc.qt.io/qt-5/qml-qtquick-layouts-gridlayout.html) is just too complicated while leaving the default "two column" view.
* It doesn't support checkable tasks.
* The calendar is huge. We can't easily limit the height without turning the calendar cells into rectangles when it should be squares. We should add whitespace to the left/right of the calendar.

I first mocked up the view in QML without actually implementing it. This let me focus on the design without worrying about the underlying features.

![](https://i.imgur.com/9Z4Hvbh.png)

Getting it to slide in from the side was fairly easy, as I'd done it before for the system tray.

I needed to rewrite the rendering of the MonthView significantly, but it turned out rather pretty. I still need to implement the coloured dot "event badges".

I'm also rewriting a large chunk of the calendar plugins in a python3 library. I now have a google calendar implementation (read only so far). I'm still not sure if I'll merge that into EventCalendar, but it's sort of necessary to solve several things:

* Moving the google acess/refresh token + cached calendarList data out of the plasma config.
* Move the HTTP stuff out of the QML JavaScript as I can't use the HTTP PATCH method due to a Qt bug. This means I need to keep a reference to the raw calendar event object, and use HTTP PUT instead when I want to modify an event.
* I need to somehow cache events so we can see them when offline. QML does have a SQLite LocalStorage feature which I used for my GitHub Issues widget, but I want to experiment with a python3 solution and see which is best.
* This is less of a worry after Plasma 5.13, but I figured parsing the events in a seperate process would keep memory down in the `plasmashell` process. This has yet to be proven though, and it could actually use up more memory.

Even if I end up throwing out this mockup or the backend python library, the "edit event" dialog code should be reuseable in the current Event Calendar widget.
