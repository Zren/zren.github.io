---
layout: widepage
title: KDE Repositories
permalink: /kde/repos/
redirect_from: /projects/kde/repos/
---

<style type="text/css">
#sidenav {
	display: none;
}
.page-content .wrapper {
	max-width: -webkit-calc(100vw - (30px * 2));
	max-width: calc(100vw - (30px * 2));
}
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

</style>


> **Note:** All GitHub links are source mirrors only. Do not submit issues to those repos. KDE uses <https://bugs.kde.org> for issues, and <https://phabricator.kde.org> for pull requests. The official source browser is at <https://cgit.kde.org/> but GitHub is much easier to navigate.

<style type="text/css">
#search input {
	width: 100%;
	position: relative;
	padding: .5em;
	border: 1px solid #ccc;
	border-radius: 4px;
}
.hidden {
	display: none;
}
</style>

<div id="search">
	<input type="search">
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
		{% include kdeRepoDesktop.html
			repoName='Application Launcher (Kickoff)'
			githubLink='https://github.com/KDE/plasma-desktop/blob/master/applets/kickoff'
			product='plasmashell&component=Application%20Launcher%20%28Kickoff%29'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Application Menu (Kicker)'
			githubLink='https://github.com/KDE/plasma-desktop/blob/master/applets/kicker'
			product='plasmashell&component=Application%20Menu%20%28Kicker%29'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Application Dashboard (KickerDash)'
			githubLink='https://github.com/KDE/plasma-desktop/blob/master/applets/kicker'
			product='kdeplasma-addons&component=Application%20Dashboard'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoKwin.html
			repoName='Meta Key (KWin: Input)'
			githubLink='https://github.com/KDE/kwin'
			product='kwin&component=input'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Active Window Control'
			githubLink='https://github.com/kotelnik/plasma-applet-active-window-control'
		%}
		<td><a>All Bugs</a></td>
		<td><a>New Bug</a></td>
		{% include phabLinks.html
			phabRepo='plasma-active-window-control'
			phabRepoName='Active Window Control Applet for Plasma'
			phabDiffQuery='sv1JhxTYnBq6'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Audio Volume (plasma-pa)'
			githubLink='https://github.com/KDE/plasma-pa'
			product='plasma-pa'
			phabRepo='plasma-pa'
			phabRepoName='Plasma Audio Volume Applet'
			phabDiffQuery='NlM7ES4ji2UX'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Battery and Brightness'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/applets/batterymonitor'
			product='plasmashell&component=Battery%20Monitor'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Browser Integration'
			githubLink='https://github.com/KDE/plasma-browser-integration'
			product='plasma-browser-integration'
			phabRepo='plasma-browser-integration'
			phabRepoName='Plasma Browser Integration'
			phabDiffQuery='zVTBKyUKLVBi'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Digital Clock'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/applets/digital-clock'
			product='plasmashell&component=Digital%20Clock'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoFramework.html
			repoName='MonthView'
			githubLink='https://github.com/KDE/plasma-framework/tree/master/src/declarativeimports/calendar'
			product='frameworks-kdeclarative'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Events: Holidays Plugin'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/plasmacalendarintegration'
		%}
		<td><a>All Bugs</a></td>
		<td><a>New Bug</a></td>
		{% include phabLinksWorkspace.html %}
	</tr>
	<tr class="indent2">
		{% include kdeRepo.html
			repoName='KHolidays'
			githubLink='https://github.com/KDE/kholidays/tree/master/holidays/plan2'
			product='frameworks-kholidays'
			phabRepo='kholidays'
			phabRepoName='PIM: KHolidays'
			phabDiffQuery='cy_NT_ZbMsFQ'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='[Desktop] Folder View'
			githubLink='https://github.com/KDE/plasma-desktop/tree/master/containments/desktop'
			product='plasmashell&component=Folder'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Wallpaper Plugins'
		%}
		<td><a>GitHub</a></td>
		{% include kdeBugs.html product='Plasma%20Workspace%20Wallpapers&component=general' %}
		{% include phabLinksWorkspace.html %}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Device Notifier'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/applets/devicenotifier'
			product='plasmashell&component=Device%20Notifier'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Global Menu (AppMenu)'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/applets/appmenu'
			product='plasmashell&component=Global%20Menu'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KDE Connect'
			githubLink='https://github.com/KDE/kdeconnect-kde/tree/master/plasmoid'
			product='kdeconnect'
			phabRepo='kdeconnect-kde'
			phabRepoName='KDE Connect'
			phabDiffQuery='ukrPN51zGqf8'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Android App'
			githubLink='https://github.com/KDE/kdeconnect-android'
			product='kdeconnect&component=android-application'
			phabRepo='kdeconnect-android'
			phabRepoName='KDE Connect - Android Application'
			phabDiffQuery='O5uLyNhBHBeF'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Media Player [Controller]'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/applets/mediacontroller'
			product='plasmashell&component=Media%20Player'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Minimize All'
			githubLink='https://github.com/KDE/kdeplasma-addons/tree/master/applets/minimizeall'
			product='kdeplasma-addons&component=General'
			phabRepo='kdeplasma-addons'
			phabRepoName='Plasma Addons'
			phabDiffQuery='iwcJtI0heMfD'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Network Manager'
			githubLink='https://github.com/KDE/plasma-nm'
			product='plasma-nm'
			phabRepo='plasma-nm'
			phabRepoName='Plasma Network Management Applet'
			phabDiffQuery='zTZoO20shXlW'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='Notifications'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/applets/notifications'
			product='plasmashell&component=Notifications'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Device Notifier'
			githubLink='https://github.com/KDE/plasma-desktop/blob/master/applets/pager'
			product='plasmashell&component=Pager'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Panel'
			githubLink='https://github.com/KDE/plasma-desktop/blob/master/desktoppackage'
			product='plasmashell&component=panel'
		%}
	</tr>
	<tr>
		{% include kdeRepoWorkspace.html
			repoName='System Tray'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/applets/systemtray'
			product='plasmashell&component=System%20Tray'
		%}
	</tr>
	<tr>
		{% include kdeRepoDesktop.html
			repoName='Task Manager'
			githubLink='https://github.com/KDE/plasma-desktop/blob/master/applets/taskmanager'
			product='plasmashell&component=Task%20Manager'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoDesktop.html
			repoName='Icon Tasks'
			githubLink='https://github.com/KDE/plasma-desktop/blob/master/applets/taskmanager'
			product='plasmashell&component=Icons-only%20Task%20Manager'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Timer'
			githubLink='https://github.com/KDE/kdeplasma-addons/tree/master/applets/timer'
			product='kdeplasma-addons&component=timer'
			phabRepo='kdeplasma-addons'
			phabRepoName='Plasma Addons'
			phabDiffQuery='iwcJtI0heMfD'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Vault'
			githubLink='https://github.com/KDE/plasma-vault/tree/master/plasma'
			product='Plasma%20Vault'
			phabRepo='plasma-vault'
			phabRepoName='Plasma Vault'
			phabDiffQuery='xviPAQ7cuNOx'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Weather Forecast'
			githubLink='https://github.com/KDE/kdeplasma-addons/blob/master/applets/weather'
			product='kdeplasma-addons&component=weather'
			phabRepo='kdeplasma-addons'
			phabRepoName='Plasma Addons'
			phabDiffQuery='iwcJtI0heMfD'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepoWorkspace.html
			repoName='Weather Sources'
			githubLink='https://github.com/KDE/plasma-workspace/tree/master/dataengines/weather/ions'
			product='plasmashell&component=Weather'
		%}
	</tr>
</table>


## Breeze Theme

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='Breeze Icons'
			githubLink='https://github.com/KDE/breeze-icons'
			product='Breeze&component=icons'
			phabRepo='breeze-icons'
			phabRepoName='Breeze Icons'
			phabDiffQuery='5_HzpnwoEZjH'
		%}
	</tr>
	<tr>
		{% include kdeRepoFramework.html
			repoName='Breeze DesktopTheme'
			githubLink='https://github.com/KDE/plasma-framework/blob/master/src/desktoptheme/breeze'
			product='frameworks-plasma'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Breeze Gtk'
			githubLink='https://github.com/KDE/breeze-gtk'
			product='Breeze&component=gtk%20theme'
			phabRepo='breeze-gtk'
			phabRepoName='Breeze for Gtk'
			phabDiffQuery='oZtk.c1MpUIx'
		%}
	</tr>
</table>


## KWin (The Window Manager)

<table class="repolist">
	<tr>
		{% include kdeRepoKwin.html
			repoName='KWin'
			githubLink='https://github.com/KDE/kwin'
			product='kwin'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Alt+Tab (TabBox)'
			githubLink='https://github.com/KDE/kwin/tree/master/tabbox'
			product='kwin&component=tabbox'
		%}
		{% include phabLinks.html %}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Window Decorations'
			githubLink='https://github.com/KDE/kwin/tree/master/kdecorations'
			product='kwin&component=decorations'
		%}
		{% include phabLinks.html %}
	</tr>
	<tr class="indent depth2">
		{% include kdeRepo.html
			repoName='Aurorae Decorations'
			githubLink='https://github.com/KDE/kwin/tree/master/plugins/kdecorations/aurorae'
			product='kwin&component=aurorae'
		%}
		{% include phabLinks.html %}
	</tr>
</table>


## KDE Homepage

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='www.kde.org'
		%}
		<td><a href="https://cgit.kde.org/scratch/kvermette/www-aether.git/tree/">Git Repo</a></td>
		{% include kdeBugs.html product='www.kde.org&component=general' %}
		{% include phabLinks.html
			phabRepo='websites-aether-wordpress'
			phabRepoName='Aether theme for Wordpress'
			phabDiffQuery='y_clwL62C9dN'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='docs.kde.org'
		%}
		<td><a>Git Repo</a></td>
		<td><a>All Bugs</a></td>
		<td><a>New Bug</a></td>
		{% include phabLinks.html
			phabRepo='websites-docs-kde-org'
			phabRepoName='Documentation Website (docs.kde.org)'
			phabDiffQuery='Pnz57PMZTbuM'
		%}
	</tr>
</table>


## KDE Store (store.kde.org)

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='ocs-webserver'
			githubLink='https://github.com/KDE/ocs-webserver/tree/master/application/modules/default/controllers'
		%}
		<td><a href="https://phabricator.kde.org/tag/kde_store/">All Tasks</a></td>
		<td><a href="https://phabricator.kde.org/tag/kde_store/">(▼ Create Task)</a></td>
		{% include phabLinks.html
			phabRepo='ocs-webserver'
			phabRepoName='OCS Webserver'
			phabDiffQuery='6v0DIohqTbc6'
		%}
	</tr>

	<tr class="indent">
		{% include kdeRepo.html
			repoName='Product Page'
			githubLink='https://github.com/KDE/ocs-webserver/blob/master/application/modules/default/controllers/ProductController.php'
		%}
	</tr>
	<tr class="indent">
		{% include kdeRepo.html
			repoName='Product Comments'
			githubLink='https://github.com/KDE/ocs-webserver/blob/master/application/modules/default/controllers/ProductcommentController.php'
		%}
	</tr>
</table>


## Plasma SDK

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='plasmathemeexplorer'
			githubLink='https://github.com/KDE/plasma-sdk/tree/master/themeexplorer'
			product='Plasma%20SDK&component=plasmathemeexplorer'
			phabRepo='plasma-sdk'
			phabRepoName='Plasma SDK'
			phabDiffQuery='40hfBk8vxVpb'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='plasmoidviewer'
			githubLink='https://github.com/KDE/plasma-sdk/tree/master/plasmoidviewer'
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
			repoName='Dolphin'
			githubLink='https://github.com/KDE/dolphin'
			product='dolphin'
			phabRepo='dolphin'
			phabRepoName='Dolphin'
			phabDiffQuery='Q.uZMhKXjose'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Falkon'
			githubLink='https://github.com/KDE/falkon'
			product='Falkon'
			phabRepo='falkon'
			phabRepoName='Falkon'
			phabDiffQuery='a6LykVQZeOj5'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Kdenlive'
			githubLink='https://github.com/KDE/kdenlive'
			product='kdenlive'
			phabRepo='kdenlive'
			phabRepoName='Kdenlive'
			phabDiffQuery='3i8H_hCbT9lu'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KDialog'
			githubLink='https://github.com/KDE/kdialog'
			product='kdialog'
			phabRepo='kdialog'
			phabRepoName='KDialog'
			phabDiffQuery='pJGwlCW8NtAk'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Konversation'
			githubLink='https://github.com/KDE/konversation'
			product='konversation'
			phabRepo='konversation'
			phabRepoName='Konversation'
			phabDiffQuery='MqFWDNoLKvbO'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Krita'
			githubLink='https://github.com/KDE/krita'
			product='krita'
			phabRepo='krita'
			phabRepoName='Krita'
			phabDiffQuery='Apm2jNyZrawx'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KRunner'
			githubLink='https://github.com/KDE/krunner'
			product='krunner'
			phabRepo='krunner'
			phabRepoName='KRunner'
			phabDiffQuery='bGOsxqpDNf1b'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KSysGuard'
			githubLink='https://github.com/KDE/ksysguard'
			product='ksysguard'
			phabRepo='ksysguard'
			phabRepoName='KSysguard'
			phabDiffQuery='sL4hOEh5QL6Z'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Yakuake'
			githubLink='https://github.com/KDE/yakuake'
			product='yakuake'
			phabRepo='yakuake'
			phabRepoName='Yakuake'
			phabDiffQuery='LDXG9mAnVUkh'
		%}
	</tr>
</table>



## KDE Services

<table class="repolist">
	<tr>
		{% include kdeRepo.html
			repoName='Baloo'
			githubLink='https://github.com/KDE/baloo'
			product='frameworks-baloo'
			phabRepo='baloo'
			phabRepoName='Baloo'
			phabDiffQuery='dxa5q95Y92MO'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='KScreenLocker'
			githubLink='https://github.com/KDE/kscreenlocker'
			product='kscreenlocker'
			phabRepo='kscreenlocker'
			phabRepoName='KScreenLocker'
			phabDiffQuery='54ALVMVJRT2S'
		%}
	</tr>
	<tr>
		{% include kdeRepo.html
			repoName='Powerdevil'
			githubLink='https://github.com/KDE/powerdevil'
			product='Powerdevil'
			phabRepo='powerdevil'
			phabRepoName='Powerdevil'
			phabDiffQuery='bOaiSgfPQGoI'
		%}
	</tr>
</table>



## Other

<table class="repolist">
	<tr>
		<td>Bugs</td>
		<td><a href="https://bugs.kde.org/describecomponents.cgi">By Project</a></td>
	</tr>
	<tr>
		<td>Pull Requests</td>
		<td><a href="https://phabricator.kde.org/differential/query/all/">Latest</a></td>
		<td><a href="https://phabricator.kde.org/differential/query/advanced/">Search</a></td>
	</tr>
</table>


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