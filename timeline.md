---
layout: page
title: Timeline / Projects
permalink: /timeline/
---

<style type="text/css">
.page-content .wrapper {
    border-left: 4px solid #333;
}

.post-content h3:before {
    content: "";
    display: block;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    position: absolute;
    margin-left: -42px;
    margin-top: .5em;
    border: 4px solid #333;
    background: #888;
    box-sizing: border-box;
    transition: 400ms;
}
.post-content h3:hover:before {
    width: 30px;
    height: 30px;
    margin-left: -47px;
    margin-top: calc(.5em - 5px);
}

.post-content h2 {
    background: #333;
    color: #fff;
    margin-left: -30px;
    padding-left: 30px;
    clear: both;
}

.post-content h3 {
    border-bottom: 1px solid;
    clear: both;
}

.tags {
    font-size: 0.9em;
    word-spacing: 1em;
    color: #999;
}
h3 + .tags {
    margin-top: -15px;
    margin-bottom: 15px;
}

@media screen and (min-width: 64em) {
    .post-content img.pull-right,
    .post-content img.pull-left {
        max-width: calc(50vw - 1em);
        border: 2px solid #eee;
        max-height: 60vh;

    }
    .post-content img.pull-left {
        margin: 0 1em 1em calc(-50vw + 50%);
        float: left;
    }
    .post-content img.pull-right {
        margin: 0 calc(-50vw + 50%) 1em 1em;
        float: right;
    }
}
</style>

## 2016


### Plasma5 Widget - Tiled Menu

**Link:** [Blog Post]({% post_url 2016-10-30-tiled-menu-win10-start-menu %})

I reskinned the app menu based on the Win10 Start Menu. I mainly did this because I wanted an A-Z menu without the dashboard (and a grid of favourites).


### Plasma5 Widget - KDE Connect Phone Charge

Later on, I realized that I rarely look at the desktop, so I redesigned the widget to focus primarily out of the system tray or on the panel. This time I focused on one widget per device.

I redrew the breeze battery icon using rectangles so it looks good (and is functional) on all themes. I also experimented with a battery charge over time graph.


### Plasma5 Widget - KDE Connect Desktop

After KDE Connect was released, I was very interested in learning it's API. So I made a simple list of the connected devices with their battery icon on the desktop.


### Plasma5 TabBox - Thumbnail Grid

Plasma ships with an odd Alt Tab skin (a scrollable list on the left side). There were a few skins similar to Window's thumbnail skin but to my amazement, it didn't expand to a second row, but instead scrolled in a single row. It didn't really bother me till someone pointed it out. It's a bit sad that this is the only downloadable skin that works. To be fair though, all the many many working skins are in KDE repos.


### Plasma5 Widget - Todo List

The Note widget is a little ugly (all that look like a sticky note do) so I reskinned to to be a list of items with checkboxes. I also parse http links and render them as clickable links.


### Plasma5 Widget - Win7 Volume Mixer

I loved the look of the volume mixer in Win7. I was dissapointed that most volume applets in linux are horizontal (as is Win10's) so I reskinned the applet to have vertical sliders. I also presented the streams similar to Win7 expanded view. 2 after writing this applet, I learned about KMix (which also had vertical sliders). Luckily it was being deprecated so my work didn't go to waste. It's now got a few features more than the default widget.


### Plasma5 Widget - Event Calendar

The default clock didn't have the ability to sync with Google Calendar at the time, so I figured out how to obtain a Google API session without the browser. I added a timer and weather forecast similar to what my Android phone layout has. I also changed the scrolling over the clock to change the volume instead of time zones.


### Plasma5 Widget - Win7 Show Desktop

I liked the slim little button in Windows so I modified the default widget to be visually similar. I also added the ability to control volume when scrolling over it, so that it's easy to blindly control the volume by flicking to the bottom right corner.

### NixShot

After moving to linux, I needed a new screenshot tool that would easily capture a region of the screen and upload it to imgur (authed to an account). While I found a few that did *some* of that, none of them did everything, or opened a window on completion.

In the process, I found out that KDE Global Shortcuts don't fire immediately, causing expanded plasma widgets to start closing before the screenshot is taken. I was forced to base nixshot around xbindkeys and scrot to get an immediate capture. Unfortunately, scrot doesn't capture the mouse cursor.


### Plasma5 Theme - Breeze AlphaBlack

I needed a light theme with a black panel, and I wanted to make a few adjustments to the default theme.


## 2015

### HawkenAPI - Periodic Diff Check Emails
<div class="tags">Python SMTP</div>

![](https://i.imgur.com/g2Gp6r1.jpg){:.pull-right}

After the responses for certain endpoints in the Hawken API started going haywire (due to Reloaded taking over), I wrote a script to check if it had changed and, if it had, send an email. I learned a little about GMail, and styling emails.


### Hawken - Distribution Charts
<div class="tags">Python Flask SQLAlchemy PostgreSQL</div>

**Link:** <http://home.xshade.ca/users/recent/7-days/pilotlevel-distribution/>

![](https://i.imgur.com/tX1pRGc.jpg){:.pull-right}

After noticing the existing MMR distribution charts were wildly inaccurate because they included users who hadn't played in months, I made a chart fetching data from the leaderboards which filtered out older users.


### Hawken - Leaderboards
<div class="tags">Python Flask SQLAlchemy PostgreSQL</div>

**Link:** <http://home.xshade.ca/users/leaderboard/>

![](https://i.imgur.com/0pQcZhZ.jpg){:.pull-right}

After data mining a list of users by name in order to add a user search function to the server list app, I decided to start mining some other data as well. I ended up making a simple leaderboard based on MMR (MatchMaking Ranking) which the community had been using for a while.

## 2014

### QuasselPy
<div class="tags">Python Flask jQuery.DataTables</div>

**Source:** <https://github.com/Zren/QuasselPy>

![](https://i.imgur.com/ay00toq.png){:.pull-right}

After being dissatisfied with quasselsuche, I decided to reinplement the feature using DataTables to have dynamic filtering.


### quassel-pushbullet
<div class="tags">Javascript NodeJS</div>

**Source:** <https://github.com/Zren/quassel-pushbullet>

![](https://i.imgur.com/V3oQJ5vl.png){:.pull-right}

After toying around with quassel-webserver, I tried pulling it apart to make an always connected client that would speedup the load time. I eventually ended up creating a new "client" and hooking the new message event to send a pushbullet notification to my phone when I get highlighted. Unfortunately I have more or less abandoned this project due to libquassel's meomory consumption.


### quassel-webserver (Contributor)
<div class="tags">Javascript NodeJS Angular</div>

**Source:** <https://github.com/magne4000/quassel-webserver>

![](https://i.imgur.com/yDOGT1H.png){:.pull-right}

magne4000 released a quasselclient implementation using NodeJS and socket.io. I made a number of pull requests to make the UI more similar to the desktop application. I was hoping to replace QuasselDroid with this in order to lower battery consumption on my phone.


### OpenUserJS.org
<div class="tags">Javascript NodeJS MongoDB Mongoose Bootstrap</div>

![](https://i.imgur.com/SkGA17P.png){:.pull-right}

After userscript.org went down due to neglect. A few replacements appeared. The mojority with a UI made by programmers. I decided to help redisign on of them. My decision to help OUJS is mainly due it being the first I was able to setup a dev environment for. I'd worked with NodeJS before, and the developer had a default remote MongoDB database which made it very easy to setup.

I ended up reskinning theming Bootstrap for them, and refactoring all the views ([old frontpage](https://i.imgur.com/laIdySZ.png)). I implemented saner pagination, along with a pagination widget.


### name
<div class="tags">tags</div>

**Link:** <>

![](image){:.pull-right}

description


### name
<div class="tags">tags</div>

**Link:** <>

![](image){:.pull-right}

description


### name
<div class="tags">tags</div>

**Link:** <>

![](image){:.pull-right}

description


### name
<div class="tags">tags</div>

**Link:** <>

![](image){:.pull-right}

description


