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
</style>

## 2016


### Plasma5 Widget - Battery Time

**Source:** <https://github.com/Zren/plasma-applets/tree/master/batterytime>

Made a simple widget which will always use the breeze battery icon and also shows the percentage and how many minutes are left.


### Plasma5 Widget - Command Output

**Source:** <https://github.com/Zren/plasma-applets/tree/master/commandoutput>

Simple widget that runs a command every second and display the output in the panel.


### Plasma5 Widget - Tiled Menu

**Link:** [Blog Post]({% post_url 2016-10-30-tiled-menu-win10-start-menu %})

**Source:** <https://github.com/Zren/plasma-applets/tree/master/tiledmenu>

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


### Atom - Open Recent
<div class="tags">Javascript NodeJS</div>

**Source:** <https://github.com/Zren/atom-open-recent>

![](https://i.imgur.com/d9y4iAi.png){:.pull-right}

Another must have feature missing from Atom was a `Open Recent` list in the menu. There existed a 3rd party plugin already to list recently opened files, and another for directories. I forked one of the projects, fixed the bugs, and streamlined both features to look like the menu in Sublime Text.


### Atom - Windows Context Menu
<div class="tags">Javascript NodeJS</div>

**Source:** <https://github.com/Zren/atom-windows-context-menu>

![](https://i.imgur.com/9v0UZKo.png){:.pull-right}

After GitHub released their new text editor, one of the key features missing was being able to open Atom from the file explorer.


### EggTimer
<div class="tags">Javascript</div>

**Source:** <https://github.com/Zren/eggtimer>

**Demo:** <http://zren.github.io/eggtimer/>

![](https://i.imgur.com/0HLSN0Z.png){:.pull-right}

A timer based on a url parameter. Based off of [e.ggtimer.com](http://e.ggtimer.com/). This version uses different parsing, focusing on short forms, and allows for clock times. Eg: `2:20` started at 1 PM will end at 2:20 PM. `1:10` started at 11 PM will end at 1:10 AM.


## 2013

### ResizeYoutubePlayerToWindowSize
<div class="tags">Javascript</div>

**Source:** <https://github.com/Zren/ResizeYoutubePlayerToWindowSize/>

![](https://i.imgur.com/ja8Kx.jpg)

After a similar userscript/extension broke, I decided to make a simplier version that would just move the video to the top of the site and scaled to the window. It got popular enough to get [Lifehackered](http://lifehacker.com/resize-youtubes-player-to-fit-your-browser-window-493160000).

![](https://i.imgur.com/RiodhIb.jpg)


### MultiView IRC UI In AngularJS
<div class="tags">Javascript AngularJS</div>

**Demo:** <http://jsfiddle.net/YwDPf/4/>

![](https://i.imgur.com/KiiKI9t.png){:.pull-right}

There was a minor discussion on #quassel on UI ideas for multi split chat. I origionally set out with the idea of adding small icons next to the selected buffers in the buffer list widget to show which buffers are selected. This idea spiralled into learning a little bit of AngularJS to make a semi-functioning UI.


### HexChat Theme Editor
<div class="tags">Javascript</div>

**Source:** <https://github.com/Zren/HexChatThemeEditor>

**Demo:** <http://zren.github.io/HexChatThemeEditor/>

![](https://i.imgur.com/t9Z5Wfq.png){:.pull-right}

Trying to edit HexChat style's was midely annoying without a live preview. So I made this.


### Hawken – Player Count Graph
<div class="tags">Python Javascript</div>

**Link:** <link>

![](https://i.imgur.com/ZIHMkgW.png){:.pull-right}

After Ashfire made his graphs private. I decided to go ahead with a project I’d been holding off because he had already made a solution. I installed MongoDB + PyMongo and wrote a script to poll the server list periodically, then store the resulting JSON in the database. Once that was done, I modified my flask web server for the server list to serve a simple graph using [HighStocks](http://www.highcharts.com/products/highstock). It uses ajax to fetch the data from the database as I did not store the derived data (the player count). Instead each request will parse X data points of server list jsons which makes it useful as a local application only.

![](https://i.imgur.com/2X7S46K.png)
![](https://i.imgur.com/IkV2oNK.png)


### Hawken – Server List
<div class="tags">Python</div>

**Link:** <https://hawken.herokuapp.com/>

![](https://i.imgur.com/E4oGvju.png){:.pull-right}

During the Beta for hawken, the developers turned off the server browser to maximize the usage of their matchmaking (in order to perfect it). This made those who wanted to setup an organized scrim very painful. I checked out how Hawken retrived the list and put together a simple interactive table using jQuery and Datatables. To actually fetch the data, I had to create a simple library in python 2.x for Hawken’s services as Javascript by itself would fail (due to some overhead required in XHRs). I then used it in combination with Flask as a proxy in order to filter and combine multiple requests together. The result would show the users on the server, the map, and the ip address + port the server is running on.


### Quassel – Web Search
<div class="tags">C++</div>

![](https://i.imgur.com/lrjlrGL.jpg){:.pull-right}

Finalized my first [pull request](https://github.com/quassel/quassel/pull/13) to a larger Open Source project. I copied Chrome’s Search for __ when right clicking selected text in chat.


## 2012

### Bukkit Plugin – PrideArena
<div class="tags">Java</div>

I took over a writing a friend’s plugin for the [Pride PvP Games](http://pridemc.com/) server. Essentially, I put into practice the game mechanics of a Deathmatch arena in the style of the Hunger Games. Actually, it’s not that much like it as there’s no cornicopia danger. You choose a kit (class) and there a grace period when there’s no PvP. My personal highlight of this project is the that I shosed the status of the arena with signs around the portal you enter. Giving a very good user feedback about the sate of the arena. While I don’t have credit for the idea, I also added a gate that closes down to prevent people from walking though the portal (as opposed to just not teleporting them).


### Quassel - Theme - Dark Monokai
<div class="tags">CSS</div>

**Link:** <https://gist.github.com/Zren/2779042>

![](https://i.imgur.com/8hJNNxG.png){:.pull-right}

Looking for an IRC client that that fully customizable skins eventually brought me to Quassel. While I love the fact everything is styleable in QSS (CSS for QT), the client itself has a few minor annoyances. Thus began my first serious foray into C++.



### Bukkit Plugin – Citizens Editor
<div class="tags">Java</div>

![](https://i.imgur.com/r5HyL8e.png){:.pull-right}

I attempted to write a GUI editor for the <http://dev.bukkit.org/bukkit-plugins/citizens/> Bukkit plugin in order to speed up NPC/Quest creation.

![](https://i.imgur.com/uhc1Lm3.png)

### Bukkit Plugin – Vault Promoter
<div class="tags">Java</div>

This project was spurred by the fact that [bPermissions](http://dev.bukkit.org/server-mods/bpermissions/)’s promotion system limitations. While it focus’s on tracks, the actual permission node for each track uses one node per group. My desired setup was that normal users could promote Guests. Giving users the `promote.User` permission node would then allow users the ability to both promote to guests to User and to demote them from it. Not ideal. While I first debated forking and submitting a patch (which I half did), I also wanted the promotion commands to be more configurable. Currently they were `/promote [trackname]`. Which would force a mod use the command more than once to go all the way from Guest => Mod.


## 2011

### jsPaint
<div class="tags">Javascript</div>

![](https://i.imgur.com/AKMhQQo.png){:.pull-right}

**Link:** <https://github.com/Zren/jsPaint>

**Demo:** <http://zren.github.io/jsPaint/>

I wanted to create my own doodle app that would upload to imgur.com. I decided to tackle javascript and its various libraries (JQuery, fabric.js). It also made me familiar with HTML’s new canvas element, and the “HTML5″ brand’s new techniques.


### MegaUpload Batch Downloader
<div class="tags">Python</div>

I started watching One Piece. Unfortunately, >400 episodes to download is fairly annoying to do manually. So I fired up python and made a script to download from megaupload in a single-threaded environment using Mechanize and BeautifulSoup.


### Bukkit Plugin – CellWar
<div class="tags">Java</div>

I started getting re-involved with Towny’s development, and got some inspiration from users about how to do warring Nations. I also took a gander at some of the mechanics of a similar plugin that did PvP stuff right, Factions. I coded up some threaded tasks that created a huge beacon in the sky overtop the area under attack. The game mechanic was to attack and hold the area. Towny’s war event is the same thing, but there’s nothing physical. So I created a focus for the defenders. Attacking would have the attacker place a flag, which the defenders would need to break / take down. I eventually merged this into the Towny plugin.


### pyTactics (PyGame)
<div class="tags">Python</div>

**Source:** <https://github.com/Zren/pyTactics>

I wanted to try making my own Tactics engine, inspired from Final Fantasy Tactics and the 40 Hour challenge, I only knew Python and Java at the time, and wanted to learn more with Python. So I took a second shot at Pygame (I’d tried to port an old Turing project before). I managed to get the isometric down right, as with the height levels, but my code re-rendered the whole map every tick which was terrible so I scrapped the project.


### Bukkit Plugin – Questioner
<div class="tags">Java</div>

**Source:** <https://github.com/Zren/Questioner>

I wanted a way to integrate accept/deny ability to Towny’s invitation’s to join towns and other user confirmations. At the time, there was no customizable API available for the task, so I made my own.


### Bukkit Plugin – Towny
<div class="tags">Java</div>

**Source:** <https://github.com/Zren/Towny>

I converted Towny to Bukkit when it became apparent hMod was dieing. The initial release didn’t include the wall generation code, however I did add iConomy support as well as a taxation system. I then coded up a (rather sloppy) implementation of having residents own plots inside towns.The rewrite had me focus on getters/setters, exception handling (as well as custom exceptions), as well as focus on the inevitable problem the hMod had. hMod didn’t plan for when Minecraft would eventually allow users to move between more than one world on a single server, but the Bukkit dev’s had foresight.

Taken over by [ElgarL](https://github.com/ElgarL). <https://github.com/ElgarL/Towny>

Then taken over by [LlmDl](https://github.com/LlmDl). <https://github.com/LlmDl/Towny>


### hMod Plugin – Arena
<div class="tags">Java</div>

A server owner was asking for a plugin to kick off his server and make it more unique. Basically a new player would be forced to tackle a waves of enemies when he first joined before being able to select his faction. This was my first tackle on a paid project, and gave me a tons of experience for what to do next time.

### Turing - Advanced Input Module
<div class="tags">Turing</div>

**Link:** <http://compsci.ca/v3/viewtopic.php?t=29263>

Turing has 2 methods of input, polling the keyboard state, and a rough key event loop. This module is to simplify if a key has just been pressed (by checking the last keyboard/mouse state).


## 2010

### hMod Plugin – Mapper
<div class="tags">Java</div>

After I first got the spark to start writing Towny, I wanted a visual representation of where the towns were. This lead me to expand on the Cartographer idea (a top down render of a minecraft world). I made it so ingame coordinates could be passed to a flatfile (type:string:x,z). I then worked on a stand alone program that would take a cartographer rendering, and draw the notes onto it. For testing, one of the types I used was all the player’s locations at the time. I like to think is the inspiration behind the current map viewers.


### hMod Plugin – ChatChannels
<div class="tags">Java</div>

A server I was on wanted specific channels for each faction on the server. I was partway into coding Towny, so this was a good relief and learning stepping stone. I took some idea’s from how IRC operated, but the code didn’t use much OOP.


### hMod Plugin – Towny
<div class="tags">Java</div>

**Source:** <https://github.com/Zren/Towny-hMod>

When hMod really started picking up heat and introduced plugins. I decided to use my Java skills I learned. I wanted a way for users to manage their own towns, and the more people in the town, the more perks. As the idea expanded, I eventually started planning that towns would be part of a hierarchy with nations at the top. I fist wrote mapper, which would show where the town was founded, but I kept getting user feedback that Towny should protect areas.

My initial code was terrible. I tried writing my own XML parser/writer for persistence.

When I finally decided on just a plain flatfile, and with the heirachy code done (but oh so buggy), I was ready to tackle integrating with another cuboid plugin for area protection. I started talking with some on IRC, and a dude was dishearted that I was just going to force players to use cuboid to select an area, and gave me the idea of having the town expand from a central point. Like a protective sphere.

I started looking into cuboid and how it did block protection. This was around the time when dev’s started talking about how checking if a block was in a list of cuboids was a terrible idea. Eventually cuboid got on the path of using K-D Tree. That threw my sphere idea out, but I started on thinking about a chunk based system.

### Animated Sprites Engine
<div class="tags">Turing</div>

**Link:** <http://compsci.ca/v3/viewtopic.php?t=25745>

A simple engine to animate a sprite character. Character can move around and jump. Uses a bit mask to perform map collision detection. Contains a background and foreground to draw above / below the character.


## 2009

### Snowfall Engine
<div class="tags">Turing</div>

**Link:** <http://compsci.ca/v3/viewtopic.php?t=22799>

![](image){:.pull-right}

A simple particle engine using trig for movement. A bit mask is used for collision detection, and the particle is drawn to the bit mask on collision (to accumulate snow).


## 2008

### Virus (Game)
<div class="tags">Turing</div>

**Link:** <http://compsci.ca/v3/viewtopic.php?t=18910>

Back when I had no clue how to do 3D, I tried zooming from the center of the screen to create the top and bottom of cubes. The game is to hit the 10 or so yellow cubes while avoiding enemy dots (anti-virus). You have safe places to avoid the enemies inside green cubes, but every time you destroy a yellow cube, more and more green havens are destroyed.
