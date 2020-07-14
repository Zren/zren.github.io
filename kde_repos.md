---
layout: fullwidthpage
title: KDE Repositories
permalink: /kde/repos/
redirect_from: /projects/kde/repos/
---

<style type="text/css">
/* Repo list tables */
.repolist td {
	padding: 0 0.5em;
	border-width: 0.1em 0;
	border-style: solid;
}
.repolist tr:nth-of-type(2n-1) td {
	background: #ebf2fb;
	border-color: #ebf2fb;
}
.repolist tr:nth-of-type(2n) td {
	background: #f8f8ff;
	border-color: #f8f8ff;
}
.repolist tr:nth-of-type(2n-1):hover td,
.repolist tr:nth-of-type(2n):hover td {
	border-color: #888;
}
.repolist td:nth-of-type(1) {
	font-weight: bold;
}
.repolist tr.indent td:nth-of-type(1):before {
	display: inline-block;
	content: "";
	width: 2em;
}
.repolist tr.indent.depth2 td:nth-of-type(1):before {
	width: 4em;
}
.repolist td:nth-of-type(1):after {
	content: ":";
}
.repolist td a:not([href]) {
	color: #aaa;
}
.repolist td a:not([href]):hover {
	text-decoration: none;
}

/* Anchor Link  */
.repolist {
	position: relative;
}
.repoanchorlink {
	opacity: 0;
	position: absolute;
	left: -22px;
	width: 22px;
	text-align: center;
	user-select: none;
}

.repolist tr.selected td {
	background: #ffe2a8;
}

.repolist tr.selected .repoanchorlink,
.repolist tr:hover .repoanchorlink {
	opacity: 1;
}
.repoanchorlink:hover {
	text-decoration: none;
}


/* Copy Markdown Button  */
.repolist tr:not(:hover) td.copybutton {
	visibility: hidden;
}
.repolist tr:hover td.copybutton {
	border-color: transparent;
}
.repolist tr:hover td.copybutton:hover {
	background: transparent;
}
.repolist tr:hover td.copybutton:hover a {
	background: transparent;
}
.copybutton a {
	display: block;
	margin: 0 calc(-0.5em - 2px);
	padding: 0 calc(0.5em + 2px);
	font-weight: bold;
	text-decoration: none;
	position: relative;
	white-space: nowrap;
}
.copybutton a:active:after {
	content: "Copied as Markdown";
	position: absolute;
	bottom: calc(100% + 4px);
	left: calc(50% - 50px);
	width: 100px;
	text-align: center;
	white-space: normal;
	border-radius: 4px;
	background: #ccc;
	color: #444;
}

/* Search */
#search {
	max-width: 800px;
	display: flex;
}
#search input {
	width: 100%;
	max-width: 800px;
	position: relative;
	padding: .5em;
	border: 1px solid #ccc;
	border-radius: 0 4px 4px 0;
}
.hidden {
	display: none;
}

.button-group label {
	display: flex;
	background: #eee;
	padding: 4px;
	width: 32px;
	box-sizing: border-box;
	line-height: 22px;
	font-size: 22px;
	border: 1px solid #ddd;
	box-sizing: border-box;
	border-radius: 4px 0 0 4px;
}

.button-group input {
	display: flex;
	flex:  1;
}

.icon-search {
	width: 100%;
	text-align: center;
	font-style: normal;
	font-weight: bold;
	transform: rotate(45deg);
}
.icon-search:before {
	content: "⚲";
}
</style>


> **Note:** KDE now uses GitLab (<https://invent.kde.org>). KDE still uses Bugzilla (<https://bugs.kde.org>). KDE is currently migrating off <https://phabricator.kde.org> for pull requests. There is a readonly code mirror at <https://github.com/KDE/> and <https://cgit.kde.org/>.

<div id="search" class="button-group">
	<label for="search-input">
		<i class="icon-search"></i>
	</label>
	<input type="search" id="search-input">
</div>

<script type="text/javascript">
	var searchInput = document.querySelector('#search input')
	var searchThrottleId = 0
	function updateSearch() {
		searchThrottleId = 0
		var query = searchInput.value.toLowerCase()
		var showAll = !query
		var visibleRows = []
		for (var table of document.querySelectorAll('table.repolist')) {
			var visibleCount = 0
			for (var tr of table.querySelectorAll('tr')) {
				var nameCell = tr.querySelector('td')
				var queryIndex = nameCell.textContent.toLowerCase().indexOf(query)
				if (showAll || queryIndex >= 0) {
					tr.classList.remove('hidden')
					visibleCount += 1
					visibleRows.push(tr)
				} else {
					tr.classList.add('hidden')
				}
			}
			var heading = table.previousElementSibling

			if (visibleCount > 0) {
				table.classList.remove('hidden')
				heading.classList.remove('hidden')
			} else {
				table.classList.add('hidden')
				heading.classList.add('hidden')
			}
		}
		console.log('updateSearch', query, visibleRows)
	}
	function throttledUpdateSearch() {
		if (searchThrottleId) {
			clearTimeout(searchThrottleId)
		}
		searchThrottleId = setTimeout(updateSearch, 100)
	}
	searchInput.addEventListener('input', throttledUpdateSearch)
	searchInput.focus();
</script>

## PlasmaShell

{% assign kdeBugList = 'https://bugs.kde.org/buglist.cgi?order=bug_id%20DESC&query_format=advanced&' %}
{% assign kdeNewBug = 'https://bugs.kde.org/enter_bug.cgi?' %}


<table class="repolist">
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Activity Bar'
			gitPath='applets/activitybar'
			product='plasmashell&component=Activity%20Switcher'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='[Show] Activities [Switcher]'
			gitPath='applets/showActivityManager'
			product='plasmashell&component=Activity%20Switcher'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Application Launcher (Kickoff)'
			gitPath='applets/kickoff'
			product='plasmashell&component=Application%20Launcher%20%28Kickoff%29'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Avatar/FaceIcon (KUser)'
			gitlabGroup='frameworks'
			gitRepo='kcoreaddons'
			gitPath='src/lib/util/kuser_unix.cpp#L184'
			product='frameworks-kcoreaddons'
			phabRepo='kcoreaddons'
			phabRepoName='KCoreAddons'
			phabDiffQuery='iqSqxSUsh7VC'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Application Menu (Kicker)'
			gitPath='applets/kicker'
			product='plasmashell&component=Application%20Menu%20%28Kicker%29'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Application Dashboard (KickerDash)'
			gitPath='applets/kicker'
			product='kdeplasma-addons&component=Application%20Dashboard'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Meta Key (KWin: Input)'
			product='kwin&component=input'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoWorkspace.html
			repoName='Kicker Plugin (RootModel)'
			gitPath='applets/kicker/plugin'
			product='plasmashell&component=Application%20Menu%20%28Kicker%29'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Active Window Control'
			gitlabGroup='plasma'
			gitRepo='plasma-active-window-control'
			product='Active%20Window%20Control'
			phabRepo='plasma-active-window-control'
			phabRepoName='Active Window Control Applet for Plasma'
			phabDiffQuery='sv1JhxTYnBq6'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='(Old Repo)'
			gitUrl='https://github.com/kotelnik/plasma-applet-active-window-control'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Audio Volume (plasma-pa)'
			gitlabGroup='plasma'
			gitRepo='plasma-pa'
			product='plasma-pa'
			phabRepo='plasma-pa'
			phabRepoName='Plasma Audio Volume Applet'
			phabDiffQuery='NlM7ES4ji2UX'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Battery and Brightness'
			gitPath='applets/batterymonitor'
			product='plasmashell&component=Battery%20Monitor'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Binary Clock'
			gitPath='applets/binary-clock'
			product='kdeplasma-addons&component=General'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Browser Integration'
			gitlabGroup='plasma'
			gitRepo='plasma-browser-integration'
			product='plasma-browser-integration'
			phabRepo='plasma-browser-integration'
			phabRepoName='Plasma Browser Integration'
			phabDiffQuery='zVTBKyUKLVBi'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Calculator'
			gitPath='applets/calculator'
			product='kdeplasma-addons&component=calculator'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Calendar'
			gitPath='applets/calendar'
			product='plasmashell&component=Calendar'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Clipboard (Klipper)'
			gitPath='applets/clipboard'
			product='klipper&component=plasma-widget'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Color Picker'
			gitPath='applets/colorpicker'
			product='kdeplasma-addons&component=Color%20Picker'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Comic Applet'
			gitPath='applets/comic'
			product='kdeplasma-addons&component=Comic%20Applet'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='CPU Load Monitor'
			gitPath='applets/systemmonitor'
			product='plasmashell&component=System%20Monitor'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Dictionary'
			gitPath='applets/dict'
			product='kdeplasma-addons&component=dictionary'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Digital Clock'
			gitPath='applets/digital-clock'
			product='plasmashell&component=Digital%20Clock'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoFramework.html
			repoName='MonthView'
			gitPath='src/declarativeimports/calendar'
			product='frameworks-kdeclarative'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoWorkspace.html
			repoName='Events: Holidays Plugin'
			gitPath='plasmacalendarintegration'
		%}
	</tr>
	<tr class="indent depth2">
		{% include kdeRepo.html
			repoName='KHolidays'
			gitlabGroup='frameworks'
			gitRepo='kholidays'
			gitPath='holidays/plan2'
			product='frameworks-kholidays'
			phabRepo='kholidays'
			phabRepoName='KHolidays'
			phabDiffQuery='cy_NT_ZbMsFQ'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='[Desktop] Folder View'
			gitPath='containments/desktop'
			product='plasmashell&component=Folder'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoWorkspace.html
			repoName='Wallpaper Plugins'
			gitPath='wallpapers'
			product='Plasma%20Workspace%20Wallpapers&component=general'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoWorkspace.html
			repoName='Image/Slideshow Wallpaper'
			gitPath='wallpapers/image'
			product='plasmashell&component=Image%20Wallpaper'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Device Notifier'
			gitPath='applets/devicenotifier'
			product='plasmashell&component=Device%20Notifier'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Disk Quota'
			gitPath='applets/diskquota'
			product='kdeplasma-addons&component=Disk%20Quota'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Display Configuration'
			gitlabGroup='plasma'
			gitRepo='kscreen'
			gitPath='plasmoid'
			product='KScreen&component=Plasma%20Applet'
			phabRepo='kscreen'
			phabRepoName='KScreen'
			phabDiffQuery='i2Ka89fDypU3'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Fifteen Puzzle'
			gitPath='applets/fifteenPuzzle'
			product='kdeplasma-addons&component=General'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Fuzzy Clock'
			gitPath='applets/fuzzy-clock'
			product='kdeplasma-addons&component=fuzzy-clock'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Global Menu (AppMenu)'
			gitPath='applets/appmenu'
			product='plasmashell&component=Global%20Menu'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Grouping'
			gitPath='applets/grouping'
			product='kdeplasma-addons&component=General'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Hard Disk I/O Monitor'
			gitPath='applets/systemmonitor'
			product='plasmashell&component=System%20Monitor'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Hard Disk Space Usage'
			gitPath='applets/systemmonitor'
			product='plasmashell&component=System%20Monitor'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Icon'
			gitPath='applets/icon'
			product='plasmashell&component=Icon%20Applet'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KDE Connect'
			gitlabGroup='network'
			gitRepo='kdeconnect-kde'
			gitPath='plasmoid'
			product='kdeconnect'
			phabRepo='kdeconnect-kde'
			phabRepoName='KDE Connect'
			phabDiffQuery='ukrPN51zGqf8'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Android App'
			gitlabGroup='network'
			gitRepo='kdeconnect-android'
			product='kdeconnect&component=android-application'
			phabRepo='kdeconnect-android'
			phabRepoName='KDE Connect - Android Application'
			phabDiffQuery='O5uLyNhBHBeF'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Keyboard Indicator'
			gitPath='applets/keyboardindicator'
			product='kdeplasma-addons&component=General'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Konsole Profiles'
			gitPath='applets/konsoleprofiles'
			product='kdeplasma-addons&component=konsoleprofiles'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Lock/Logout'
			gitPath='applets/lock_logout'
			product='plasmashell&component=general'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Media Frame'
			gitPath='applets/mediaframe'
			product='kdeplasma-addons&component=General'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Media Player [Controller]'
			gitPath='applets/mediacontroller'
			product='plasmashell&component=Media%20Player'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Memory Status'
			gitPath='applets/systemmonitor'
			product='plasmashell&component=System%20Monitor'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Minimize All'
			gitPath='applets/minimizeall'
			product='plasmashell&component=Show%20Desktop%2FMinimize%20All'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Network Manager'
			gitlabGroup='plasma'
			gitRepo='plasma-nm'
			product='plasma-nm'
			phabRepo='plasma-nm'
			phabRepoName='Plasma Network Management Applet'
			phabDiffQuery='zTZoO20shXlW'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Network Monitor'
			gitPath='applets/systemmonitor'
			product='plasmashell&component=System%20Monitor'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Night Color Control'
			gitPath='applets/nightcolor'
			product='kdeplasma-addons&component=Night%20Color%20Control'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Notes'
			gitPath='applets/notes'
			product='kdeplasma-addons&component=notes'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Notifications'
			gitPath='applets/notifications'
			product='plasmashell&component=Notifications'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Pager'
			gitPath='applets/pager'
			product='plasmashell&component=Pager'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Panel'
			gitPath='desktoppackage'
			product='plasmashell&component=Panel'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='[Add Panel] Layout Templates'
			gitPath='layout-templates'
			product='plasmashell&component=Panel'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Panel Spacer'
			gitPath='applets/panelspacer'
			product='plasmashell&component=Panel'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Quicklaunch'
			gitPath='applets/quicklaunch'
			product='kdeplasma-addons&component=Quicklaunch'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Quick Share'
			gitPath='applets/quickshare'
			product='kdeplasma-addons&component=QuickShare'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Search (Milou)'
			gitlabGroup='plasma'
			gitRepo='milou'
			product='plasmashell&component=Milou'
			phabRepo='milou'
			phabRepoName='Milou'
			phabDiffQuery='KeQ1uFdgDzbJ'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Show Desktop'
			gitPath='applets/showdesktop'
			product='plasmashell&component=Show%20Desktop%2FMinimize%20All'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='System Load Viewer'
			gitPath='applets/systemloadviewer'
			product='kdeplasma-addons&component=systemloadviewer'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='System Tray'
			gitPath='applets/systemtray'
			product='plasmashell&component=System%20Tray'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Task Manager'
			gitPath='applets/taskmanager'
			product='plasmashell&component=Task%20Manager'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Icon Tasks'
			gitPath='applets/taskmanager'
			product='plasmashell&component=Icons-only%20Task%20Manager'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Timer'
			gitPath='applets/timer'
			product='kdeplasma-addons&component=timer'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Trash'
			gitPath='applets/trash'
			product='plasmashell&component=general'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Updates (Discover)'
			gitlabGroup='plasma'
			gitRepo='discover'
			gitPath='notifier'
			product='Discover&component=Updater'
			phabRepo='discover'
			phabRepoName='Discover Software Store'
			phabDiffQuery='XBRvBuRvMiM5'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='User Switcher'
			gitPath='applets/userswitcher'
			product='kdeplasma-addons&component=User%20Switcher'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Vault'
			gitlabGroup='plasma'
			gitRepo='plasma-vault'
			gitPath='plasma'
			product='Plasma%20Vault'
			phabRepo='plasma-vault'
			phabRepoName='Plasma Vault'
			phabDiffQuery='xviPAQ7cuNOx'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Weather Forecast'
			gitPath='applets/weather'
			product='kdeplasma-addons&component=weather'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoWorkspace.html
			repoName='Weather Sources'
			gitPath='dataengines/weather/ions'
			product='plasmashell&component=Weather'
		%}
	</tr>
	<tr>
		{% include kdeRepoAddons.html
			repoName='Web browser'
			gitPath='applets/webbrowser'
			product='kdeplasma-addons&component=webbrowser'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Window list'
			gitPath='applets/window-list'
			product='plasmashell&component=Window%20List'
		%}
	</tr>
</table>


## Breeze Theme

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='Breeze Icons'
			gitlabGroup='frameworks'
			gitRepo='breeze-icons'
			product='Breeze&component=icons'
			phabRepo='breeze-icons'
			phabRepoName='Breeze Icons'
			phabDiffQuery='5_HzpnwoEZjH'
		%}
	</tr>
	<tr>
		{% include kdeRepoFramework.html
			repoName='Breeze DesktopTheme'
			gitPath='src/desktoptheme/breeze'
			product='frameworks-plasma'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Breeze Gtk'
			gitlabGroup='plasma'
			gitRepo='breeze-gtk'
			product='Breeze&component=gtk%20theme'
			phabRepo='breeze-gtk'
			phabRepoName='Breeze for Gtk'
			phabDiffQuery='oZtk.c1MpUIx'
		%}
	</tr>
</table>


## Breath Theme (Manjaro)

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='Breath'
			gitUrl='https://gitlab.manjaro.org/artwork/themes/breath'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Breath2'
			gitUrl='https://gitlab.manjaro.org/artwork/themes/breath2'
		%}
	</tr>
</table>


## KWin (The Window Manager)

<table class="repolist">
	<tr>
		{% include kdeRepoKwin.html
			repoName='KWin'
			product='kwin'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Alt+Tab (TabBox)'
			gitPath='tabbox'
			product='kwin&component=tabbox'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Window Decorations'
			gitPath='decorations'
			product='kwin&component=decorations'
		%}
	</tr>
	<tr class="indent depth2">
		{% include kdeRepo.html
			repoName='KDecoration2'
			gitlabGroup='plasma'
			gitRepo='kdecoration'
			product='kwin&component=decorations'
			phabRepo='kdecoration'
			phabRepoName='Window Decoration Library'
			phabDiffQuery='TX1cIo28VdCS'
		%}
	</tr>
	<tr class="indent depth2">
		{% include kdeRepo.html
			repoName='Breeze Decorations'
			gitlabGroup='plasma'
			gitRepo='breeze'
			gitPath='kdecoration'
			product='Breeze&component=window%20decoration'
			phabRepo='breeze'
			phabRepoName='Breeze'
			phabDiffQuery='5_HzpnwoEZjH'
		%}
	</tr>
	<tr class="indent depth2">
		{% include kdeRepoKwin.html
			repoName='Aurorae Decorations'
			gitPath='plugins/kdecorations/aurorae'
			product='kwin&component=aurorae'
		%}
	</tr>
	<tr class="indent depth2">
		{% include kdeRepo.html
			repoName='Emerald Decorations (Smaragd)'
			gitlabGroup='plasma'
			gitRepo='smaragd'
			product='smaragd'
			phabRepo='smaragd'
			phabRepoName='Smaragd'
			phabDiffQuery='txJJQqwJiZVM'
		%}
	</tr>
</table>


## KDE Website

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='www.kde.org'
			gitUrl='https://websvn.kde.org/trunk/www/sites/www/'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Aether Wordpress Theme'
			gitlabGroup='websites'
			gitRepo='aether-wordpress'
			phabRepo='websites-aether-wordpress'
			phabRepoName='Aether theme for Wordpress'
			phabDiffQuery='y_clwL62C9dN'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='docs.kde.org'
			gitlabGroup='websites'
			gitRepo='docs-kde-org'
			phabRepo='websites-docs-kde-org'
			phabRepoName='Documentation Website (docs.kde.org)'
			phabDiffQuery='Pnz57PMZTbuM'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='wiki.kde.org'
			gitlabGroup='websites'
			gitRepo='aether-mediawiki'
			product='KDE%20MediaWiki'
		%}
	</tr>
</table>


## KDE Store (store.kde.org)

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='ocs-webserver'
			gitlabGroup='webapps'
			gitRepo='ocs-webserver'
			gitPath='application/modules/default/controllers'
			phabWorkboard='https://phabricator.kde.org/project/board/146/'
			phabRepo='ocs-webserver'
			phabRepoName='OCS Webserver'
			phabDiffQuery='6v0DIohqTbc6'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Product Page'
			gitlabGroup='webapps'
			gitRepo='ocs-webserver'
			gitPath='application/modules/default/controllers/ProductController.php'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Product Comments'
			gitlabGroup='webapps'
			gitRepo='ocs-webserver'
			gitPath='application/modules/default/controllers/ProductcommentController.php'
		%}
	</tr>
</table>


## Plasma SDK

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='cuttlefish'
			gitlabGroup='plasma'
			gitRepo='plasma-sdk'
			gitPath='cuttlefish'
			product='Plasma%20SDK&component=cuttlefish'
			phabRepo='plasma-sdk'
			phabRepoName='Plasma SDK'
			phabDiffQuery='40hfBk8vxVpb'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='plasmathemeexplorer'
			gitlabGroup='plasma'
			gitRepo='plasma-sdk'
			gitPath='themeexplorer'
			product='Plasma%20SDK&component=plasmathemeexplorer'
			phabRepo='plasma-sdk'
			phabRepoName='Plasma SDK'
			phabDiffQuery='40hfBk8vxVpb'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='plasmoidviewer'
			gitlabGroup='plasma'
			gitRepo='plasma-sdk'
			gitPath='plasmoidviewer'
			product='Plasma%20SDK&component=plasmoidviewer'
			phabRepo='plasma-sdk'
			phabRepoName='Plasma SDK'
			phabDiffQuery='40hfBk8vxVpb'
		%}
	</tr>
</table>


## KDE Apps

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='Discover'
			gitlabGroup='plasma'
			gitRepo='discover'
			product='Discover'
			phabRepo='discover'
			phabRepoName='Discover Software Store'
			phabDiffQuery='XBRvBuRvMiM5'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Dolphin'
			gitlabGroup='system'
			gitRepo='dolphin'
			product='dolphin'
			phabRepo='dolphin'
			phabRepoName='Dolphin'
			phabDiffQuery='Q.uZMhKXjose'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='dolphin-plugins'
			gitlabGroup='sdk'
			gitRepo='dolphin-plugins'
			product='dolphin&component=plugins%3A bazaar&component=plugins%3A dropbox&component=plugins%3A git&component=plugins%3A mercurial&component=plugins%3A svn'
			phabRepo='dolphin-plugins'
			phabRepoName='Plugins for Dolphin'
			phabDiffQuery='Va5Sq8plksJF'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='KIO'
			gitlabGroup='frameworks'
			gitRepo='kio'
			product='kio'
			phabRepo='kio'
			phabRepoName='KIO'
			phabDiffQuery='38lmUxypxGRG'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='KIO Extras'
			gitlabGroup='network'
			gitRepo='kio-extras'
			product='kio-extras'
			phabRepo='kio-extras'
			phabRepoName='KIO Extras'
			phabDiffQuery='U_e72SrCJaT1'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Emoji Picker'
			gitPath='applets/kimpanel/backend/ibus/emojier'
			product='plasmashell&component=general'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Falkon'
			gitlabGroup='network'
			gitRepo='falkon'
			product='Falkon'
			phabRepo='falkon'
			phabRepoName='Falkon'
			phabDiffQuery='a6LykVQZeOj5'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Gwenview'
			gitlabGroup='graphics'
			gitRepo='gwenview'
			product='gwenview'
			phabRepo='gwenview'
			phabRepoName='Gwenview'
			phabDiffQuery='hRSwCAgRbJhD'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Kdenlive'
			gitlabGroup='multimedia'
			gitRepo='kdenlive'
			product='kdenlive'
			phabRepo='kdenlive'
			phabRepoName='Kdenlive'
			phabDiffQuery='3i8H_hCbT9lu'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KDialog'
			gitlabGroup='utilities'
			gitRepo='kdialog'
			product='kdialog'
			phabRepo='kdialog'
			phabRepoName='KDialog'
			phabDiffQuery='pJGwlCW8NtAk'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Konsole'
			gitlabGroup='utilities'
			gitRepo='konsole'
			product='konsole'
			phabRepo='konsole'
			phabRepoName='Konsole'
			phabDiffQuery='K5WA0r5foHBY'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Konversation'
			gitlabGroup='network'
			gitRepo='konversation'
			product='konversation'
			phabRepo='konversation'
			phabRepoName='Konversation'
			phabDiffQuery='MqFWDNoLKvbO'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Krita'
			gitlabGroup='graphics'
			gitRepo='krita'
			product='krita'
			phabRepo='krita'
			phabRepoName='Krita'
			phabDiffQuery='Apm2jNyZrawx'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KRunner'
			gitlabGroup='frameworks'
			gitRepo='krunner'
			product='krunner'
			phabRepo='krunner'
			phabRepoName='KRunner'
			phabDiffQuery='bGOsxqpDNf1b'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KSysGuard'
			gitlabGroup='plasma'
			gitRepo='ksysguard'
			product='ksysguard'
			phabRepo='ksysguard'
			phabRepoName='KSysguard'
			phabDiffQuery='sL4hOEh5QL6Z'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Spectacle [Screenshots]'
			gitlabGroup='graphics'
			gitRepo='spectacle'
			product='spectacle'
			phabRepo='spectacle'
			phabRepoName='Spectacle'
			phabDiffQuery='d0ahfxoZg5xe'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Yakuake'
			gitlabGroup='utilities'
			gitRepo='yakuake'
			product='yakuake'
			phabRepo='yakuake'
			phabRepoName='Yakuake'
			phabDiffQuery='LDXG9mAnVUkh'
		%}
	</tr>
</table>


## System Settings

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='System Settings'
			gitlabGroup='plasma'
			gitRepo='systemsettings'
			product='systemsettings'
			phabRepo='systemsettings'
			phabRepoName='System Settings'
			phabDiffQuery='PlE.UXMKpvQe'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Accessibility'
			gitPath='kcms/access'
			product='systemsettings&component=kcm_accessibility'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Activities'
			gitPath='kcms/activities'
			product='kwin&component=activities'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='[Qt] Application Style'
			gitPath='kcms/style'
			product='systemsettings&component=kcm_style'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Autostart'
			gitPath='kcms/autostart'
			product='systemsettings&component=kcm_autostart'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Background Services'
			gitPath='kcms/kded'
			product='systemsettings&component=kcm_kded'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Colors'
			gitPath='kcms/colors'
			product='systemsettings&component=kcm_colors'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Compositor'
			gitPath='kcmkwin/kwincompositing'
			product='systemsettings&component=compositing'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Cursors'
			gitPath='kcms/cursortheme'
			product='systemsettings&component=kcm_cursortheme'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Date & Time'
			gitPath='kcms/dateandtime'
			product='systemsettings&component=kcm_clock'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Default Applications'
			gitPath='kcms/componentchooser'
			product='systemsettings&component=kcm_componentchooser'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Desktop Effects'
			gitPath='kcmkwin/kwineffects'
			product='systemsettings&component=kcm_kwin_effects'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Desktop Session'
			gitPath='kcms/ksmserver'
			product='systemsettings&component=kcm_ksmserver'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Device Actions'
			gitPath='kcms/solid_actions'
			product='systemsettings&component=kcm_solid-actions'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='[Kubuntu] Driver Manager'
			gitlabGroup='system'
			gitRepo='kubuntu-driver-kcm'
			product='KDE%20Config%20Driver%20Manager'
			phabRepo='kubuntu-driver-kcm'
			phabRepoName='Kubuntu Proprietary Driver Manager'
			phabDiffQuery='8WNeIi9_K_p3'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Emoticons'
			gitPath='kcms/emoticons'
			product='systemsettings&component=kcm_emoticons'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='File Search'
			gitPath='kcms/baloo'
			product='systemsettings&component=kcm_baloo'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Fonts'
			gitPath='kcms/fonts'
			product='systemsettings&component=kcm_fonts'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Font Management'
			gitPath='kcms/kfontinst/kcmfontinst'
			product='systemsettings&component=kcm_fontinst'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Formats'
			gitPath='kcms/formats'
			product='systemsettings&component=kcm_formats'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Game Controller'
			gitPath='kcms/hardware/joystick'
			product='systemsettings&component=kcm_joystick'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='General Behavior'
			gitPath='kcms/workspaceoptions'
			product='systemsettings&component=general'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='GNOME/GTK Application Style'
			gitlabGroup='plasma'
			gitRepo='kde-gtk-config'
			product='kde-gtk-config'
			phabRepo='kde-gtk-config'
			phabRepoName='KDE Gtk Configuration Tool'
			phabDiffQuery='j8derDIaiCMm'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Global Shortcuts'
			gitPath='kcms/keys'
			product='systemsettings&component=kcm_keys'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Global Theme'
			gitPath='kcms/lookandfeel'
			product='systemsettings&component=kcm_lookandfeel'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Icons'
			gitPath='kcms/icons'
			product='systemsettings&component=kcm_icons'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Keyboard'
			gitPath='kcms/keyboard'
			product='systemsettings&component=kcm_keyboard'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='KRunner'
			gitPath='kcms/runners'
			product='krunner'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='KWin Scripts'
			gitPath='kcmkwin/kwinscripts'
			product='kwin&component=scripting'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Launch Feedback'
			gitPath='kcms/launch'
			product='systemsettings&component=kcm_launch'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Locations'
			gitPath='kcms/desktoppaths'
			product='systemsettings&component=kcm_desktoppath'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Mouse'
			gitPath='kcms/mouse'
			product='systemsettings&component=kcm_mouse'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Night Color'
			gitPath='kcms/nightcolor'
			product='systemsettings&component=kcm_nightcolor'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Notifications'
			gitPath='kcms/notifications'
			product='systemsettings&component=kcm_notify'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Plasma Style'
			gitPath='kcms/desktoptheme'
			product='systemsettings&component=kcm_desktoptheme'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Screen Edges'
			gitPath='kcmkwin/kwinscreenedges'
			product='systemsettings&component=kcm_kwinscreenedges'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Splash Screen'
			gitPath='kcms/ksplash'
			product='systemsettings&component=kcm_splashscreen'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Spell Check'
			gitPath='kcms/spellchecking'
			product='systemsettings&component=kcm_language'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Standard Shortcuts'
			gitPath='kcms/standard_actions'
			product='systemsettings&component=kcm_standard_actions'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Task Switcher'
			gitPath='kcmkwin/kwintabbox'
			product='kwin&component=tabbox'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Touchpad'
			gitPath='kcms/touchpad/src/kcm'
			product='Touchpad-KCM'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Touch Screen'
			gitPath='kcmkwin/kwinscreenedges'
			product='systemsettings&component=kcm_kwintouchscreen'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Virtual Desktops'
			gitPath='kcmkwin/kwindesktop'
			product='systemsettings&component=kcm_kwin_virtualdesktops'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Window Behavior'
			gitPath='kcmkwin/kwinoptions'
			product='kwin&component=general'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Window Rules'
			gitPath='kcmkwin/kwinrules'
			product='kwin&component=rules'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Window Decorations'
			gitPath='kcmkwin/kwindecoration'
			product='systemsettings&component=kcm_kwindecoration'
		%}
	</tr>
</table>


## KDE Services

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='Baloo [File Indexer]'
			gitlabGroup='frameworks'
			gitRepo='baloo'
			product='frameworks-baloo'
			phabRepo='baloo'
			phabRepoName='Baloo'
			phabDiffQuery='dxa5q95Y92MO'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KGlobalAccel (Global Shortcuts)'
			gitlabGroup='frameworks'
			gitRepo='kglobalaccel'
			product='frameworks-kglobalaccel'
			phabRepo='kglobalaccel'
			phabRepoName='KGlobalAccel'
			phabDiffQuery='YtlirHsPPMpy'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='KSMServer (Session Manager)'
			gitPath='ksmserver'
			product='ksmserver'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoWorkspace.html
			repoName='Logout Theme'
			gitPath='lookandfeel/contents/logout'
			product='ksmserver&component=ui'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KScreenLocker'
			gitlabGroup='plasma'
			gitRepo='kscreenlocker'
			product='kscreenlocker'
			phabRepo='kscreenlocker'
			phabRepoName='KScreenLocker'
			phabDiffQuery='54ALVMVJRT2S'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='polkit-kde-agent-1 (Password Prompt)'
			gitlabGroup='plasma'
			gitRepo='polkit-kde-agent-1'
			product='policykit-kde-agent-1'
			phabRepo='polkit-kde-agent-1'
			phabRepoName='Policykit (Polkit) KDE Agent'
			phabDiffQuery='hRFIy.6nV9HA'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Powerdevil'
			gitlabGroup='plasma'
			gitRepo='powerdevil'
			product='Powerdevil'
			phabRepo='powerdevil'
			phabRepoName='Powerdevil'
			phabDiffQuery='bOaiSgfPQGoI'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='xdg-desktop-portal-kde'
			gitlabGroup='plasma'
			gitRepo='xdg-desktop-portal-kde'
			product='xdg-desktop-portal-kde'
			phabRepo='xdg-desktop-portal-kde'
			phabRepoName='Flatpak Support: KDE Portal for XDG Desktop'
			phabDiffQuery='gNr_6_SymR34'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='xdg-desktop-portal'
			gitUrl='https://github.com/flatpak/xdg-desktop-portal'
		%}
	</tr>
</table>


## KDE Frameworks

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='KPackage'
			gitlabGroup='frameworks'
			gitRepo='kpackage'
			product='frameworks-kpackage'
			phabRepo='kpackage'
			phabRepoName='KPackage'
			phabDiffQuery='pW.6iUCaNzoP'
		%}
	</tr>
</table>



## Other

* **Bugs:**
	* [Listed By Project](https://bugs.kde.org/describecomponents.cgi) - Including projects not listed here
* **GitLab:**
	* [Projects](https://invent.kde.org/explore/projects)
	* [Recent Activity](https://invent.kde.org/dashboard/activity) - Must be logged in
* **Phabricator Pull Requests:**
	* [Latest](https://phabricator.kde.org/differential/query/all/)
	* [Search](https://phabricator.kde.org/differential/query/advanced/)


<script type="text/javascript">
	function updateSelectedRow() {
		var selectedRow = document.querySelector('.repolist tr.selected')
		if (selectedRow) {
			selectedRow.classList.remove('selected')
		}
		if (window.location.hash) {
			var selectedAnchor = document.querySelector('.repoanchorlink[href="' + window.location.hash + '"]')
			if (selectedAnchor) {
				var tr = selectedAnchor.parentNode.parentNode // $.parent('tr')
				tr.classList.add('selected')
			}
		}
	}
	window.addEventListener('hashchange', updateSelectedRow)
	updateSelectedRow()
</script>


<script type="text/javascript">
	// https://stackoverflow.com/questions/26336138/how-can-i-copy-to-clipboard-in-html5-without-using-flash
	// https://stackoverflow.com/a/36610696/947742
	function copyText(text){
		function selectElementText(element) {
			if (document.selection) {
				var range = document.body.createTextRange()
				range.moveToElementText(element)
				range.select()
			} else if (window.getSelection) {
				var range = document.createRange()
				range.selectNode(element)
				window.getSelection().removeAllRanges()
				window.getSelection().addRange(range)
			}
		}
		var element = document.createElement('div')
		element.textContent = text
		document.body.appendChild(element)
		selectElementText(element)
		document.execCommand('copy')
		element.remove()
	}

	function copyRowAsMarkdown(el) {
		// console.log('copyRowAsMarkdown', el)
		var tr = el.parentNode.parentNode

		var str = ''

		for (var i = 0; i < tr.childElementCount; i++) {
			var td = tr.children[i]
			if (i == 0) {
				var a = td.querySelector('a')
				var linkifyName = a.classList.contains('repoanchorlink')

				var name = td.textContent
				if (name[0] == "¶") {
					name = name.substr(1)
				}

				str += '**'
				if (linkifyName) {
					var link = a.href

					str += '['
					str += name
					str += ']('
					str += link
					str += ')'
				} else {
					str += name
				}
				str += ':**'
			} else if (!td.classList.contains('copybutton')) {
				if (i == 1) {
					// str += ' [ '
					str += ' '
				} else {
					str += ' | '
				}
				var a = td.querySelector('a')
				str += '['
				str += a.textContent
				str += ']('
				str += a.href
				str += ')'
			}
		}
		// str += ' ]'
		console.log(str)

		copyText(str)
	}
	function genCopyButtons() {
		for (var tr of document.querySelectorAll('.repolist tr')) {
			var td = document.createElement('td')
			td.classList.add('copybutton')
			var a = document.createElement('a')
			a.setAttribute('href', 'javascript:void(0)')
			a.setAttribute('onclick', 'copyRowAsMarkdown(this)')
			a.textContent = 'md'
			td.appendChild(a)
			tr.appendChild(td)
		}
	}
	genCopyButtons()
</script>


<script type="text/javascript" src="/js/livereload.js"></script>




