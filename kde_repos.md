---
layout: widepage
title: KDE Repositories
permalink: /kde/repos/
---

<style type="text/css">
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
.repolist td:nth-of-type(1):after {
	content: ":";
}
.repolist td a:not([href]) {
	color: #aaa;
}
</style>


> **Note:** All GitHub links are source mirrors only. Do not submit issues to those repos. KDE uses <https://bugs.kde.org> for issues, and <https://phabricator.kde.org> for pull requests. The official source browser is at <https://cgit.kde.org/> but GitHub is much easier to navigate.

## PlasmaShell

{% assign kdeBugList = 'https://bugs.kde.org/buglist.cgi?order=bug_id%20DESC&query_format=advanced&' %}
{% assign kdeNewBug = 'https://bugs.kde.org/enter_bug.cgi?' %}
{% assign phabDiffs = 'https://phabricator.kde.org/differential/query/' %}
{% assign phabDiffsFramework = 'https://phabricator.kde.org/differential/query/7DrhVUSaAXrw/#R' %}
{% assign phabDiffsDesktop = 'https://phabricator.kde.org/differential/query/7LklMmkHDcva/#R' %}
{% assign phabDiffsWorkspace = 'https://phabricator.kde.org/differential/query/stR7aMSmxBU./#R' %}
{% assign phabDiffsAddons = 'https://phabricator.kde.org/differential/query/iwcJtI0heMfD/#R' %}
{% assign phabNewDiff = 'https://phabricator.kde.org/differential/diff/create/' %}

<table class="repolist">
	<tr>
		<td>Application Launcher (Kickoff)</td>
		<td><a href="https://github.com/KDE/plasma-desktop/blob/master/applets/kickoff/">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=Application%20Launcher%20%28Kickoff%29&list_id=1406061">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=plasmashell&component=Application%20Launcher%20%28Kickoff%29">New Bug</a></td>
		<td><a href="{{phabDiffsDesktop}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Desktop)</a></td>
	</tr>
	<tr>
		<td>Application Menu/Dashboard (Kicker)</td>
		<td><a href="https://github.com/KDE/plasma-desktop/blob/master/applets/kicker/">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=Application%20Menu%20%28Kicker%29&list_id=1406061">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=plasmashell&component=Application%20Menu%20%28Kicker%29">New Bug</a></td>
		<td><a href="{{phabDiffsDesktop}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Desktop)</a></td>
	</tr>
	<tr>
		<td>Audio Volume (plasma-pa)</td>
		<td><a href="https://github.com/KDE/plasma-pa">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasma-pa&list_id=1406062">All Bugs</a></td>
		<td><a>New Bug</a></td>
		<td><a href="{{phabDiffs}}NlM7ES4ji2UX/#R">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Audio Volume Applet)</a></td>
	</tr>
	<tr>
		<td>Battery and Brightness</td>
		<td><a href="https://github.com/KDE/plasma-workspace/tree/master/applets/batterymonitor">GitHub</a></td>
		<td><a>All Bugs</a></td>
		<td><a>New Bug</a></td>
		<td><a href="{{phabDiffsWorkspace}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Workspace)</a></td>
	</tr>
	<tr>
		<td>Digital Clock</td>
		<td><a href="https://github.com/KDE/plasma-workspace/tree/master/applets/digital-clock">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=Digital%20Clock&list_id=1406061">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=plasmashell&component=Digital%20Clock">New Bug</a></td>
		<td><a href="{{phabDiffsWorkspace}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Workspace)</a></td>
	</tr>
	<tr class="indent">
		<td>MonthView</td>
		<td><a href="https://github.com/KDE/plasma-framework/tree/master/src/declarativeimports/calendar">GitHub</a></td>
		<td><a>All Bugs</a></td>
		<td><a>New Bug</a></td>
		<td><a href="{{phabDiffsFramework}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Framework)</a></td>
	</tr>
	<tr>
		<td>[Desktop] Folder View</td>
		<td><a href="https://github.com/KDE/plasma-desktop/tree/master/containments/desktop/">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=Folder&list_id=1417574">All Bugs</a></td>
		<td><a>New Bug</a></td>
		<td><a href="{{phabDiffsDesktop}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Desktop)</a></td>
	</tr>
	<tr>
		<td>Media Player [Controller]</td>
		<td><a href="https://github.com/KDE/plasma-workspace/tree/master/applets/mediacontroller">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=Media%20Player&list_id=1428170">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=plasmashell&component=Media%20Player">New Bug</a></td>
		<td><a href="{{phabDiffsWorkspace}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Workspace)</a></td>
	</tr>
	<tr>
		<td>Minimize All</td>
		<td><a href="https://github.com/KDE/kdeplasma-addons/tree/master/applets/minimizeall">GitHub</a></td>
		<td><a>All Bugs</a></td>
		<td><a>New Bug</a></td>
		<td><a href="{{phabDiffsAddons}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Addons)</a></td>
	</tr>
	<tr>
		<td>Notifications</td>
		<td><a href="https://github.com/KDE/plasma-workspace/tree/master/applets/notifications">GitHub</a></td>
		<td><a>All Bugs</a></td>
		<td><a>New Bug</a></td>
		<td><a href="{{phabDiffsWorkspace}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Workspace)</a></td>
	</tr>
	<tr>
		<td>Pager</td>
		<td><a href="https://github.com/KDE/plasma-desktop/blob/master/applets/pager">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=Pager&list_id=1411058">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=plasmashell&component=Pager">New Bug</a></td>
		<td><a href="{{phabDiffsDesktop}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Desktop)</a></td>
	</tr>
	<tr>
		<td>System Tray</td>
		<td><a href="https://github.com/KDE/plasma-workspace/tree/master/applets/systemtray">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=System%20Tray&list_id=1408524">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=plasmashell&component=System%20Tray">New Bug</a></td>
		<td><a href="{{phabDiffsWorkspace}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Workspace)</a></td>
	</tr>
	<tr>
		<td>Task Manager</td>
		<td><a href="https://github.com/KDE/plasma-desktop/blob/master/applets/taskmanager">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=Task%20Manager&list_id=1407534">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=plasmashell&component=Task%20Manager">New Bug</a></td>
		<td><a href="{{phabDiffsDesktop}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Desktop)</a></td>
	</tr>
	<tr class="indent">
		<td>Icon Tasks</td>
		<td><a href="https://github.com/KDE/plasma-desktop/blob/master/applets/taskmanager">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=plasmashell&component=Icons-only%20Task%20Manager&list_id=1407535">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=plasmashell&component=Icons-only%20Task%20Manager">New Bug</a></td>
		<td><a href="{{phabDiffsDesktop}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma Desktop)</a></td>
	</tr>
</table>

## KDE Homepage

<table class="repolist">
	<tr>
		<td>www.kde.org</td>
		<td><a href="https://cgit.kde.org/scratch/kvermette/www-aether.git/tree/">Git Repo</a></td>
		<td><a href="{{kdeBugList}}product=www.kde.org&component=general&list_id=1430354">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=www.kde.org&component=general">New Bug</a></td>
		<td><a>Pull Requests</a></td>
		<td><a>New PR</a></td>
	</tr>
	<tr class="indent">
		<td>R848 Aether theme for Wordpress</td>
		<td><a href="R848 Aether theme for Wordpress">Phabricator</a></td>
	</tr>
	<tr>
		<td>docs.kde.org</td>
		<td><a>Git Repo</a></td>
		<td><a>All Bugs</a></td>
		<td><a>New Bug</a></td>
		<td><a>Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Documentation Website (docs.kde.org))</a></td>
		<td><a href="https://phabricator.kde.org/source/websites-docs-kde-org/">Phabricator</a></td>
	</tr>
</table>


## KDE Store (store.kde.org)

<table class="repolist">
	<tr>
		<td>ocs-webserver</td>
		<td><a href="https://github.com/KDE/ocs-webserver/tree/master/application/modules/default/controllers">GitHub</a></td>
		<td><a href="https://phabricator.kde.org/tag/kde_store/">All Tasks</a></td>
		<td><a href="https://phabricator.kde.org/tag/kde_store/">(▼ Create Task)</a></td>
		<td><a href="https://phabricator.kde.org/differential/query/6v0DIohqTbc6/#R">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: OCS Webserver)</a></td>
	</tr>

	<tr class="indent">
		<td>Product Page</td>
		<td><a href="https://github.com/KDE/ocs-webserver/blob/master/application/modules/default/controllers/ProductController.php">GitHub</a></td>
	</tr>
	<tr class="indent">
		<td>Product Comments</td>
		<td><a href="https://github.com/KDE/ocs-webserver/blob/master/application/modules/default/controllers/ProductcommentController.php">GitHub</a></td>
	</tr>
</table>


## Plasma SDK

<table class="repolist">
	<tr>
		<td>plasmoidviewer</td>
		<td><a href="https://github.com/KDE/plasma-sdk/tree/master/plasmoidviewer">GitHub</a></td>
		<td><a href="{{kdeBugList}}product=Plasma%20SDK&component=plasmoidviewer&list_id=1422702">All Bugs</a></td>
		<td><a href="{{kdeNewBug}}product=Plasma%20SDK&component=plasmoidviewer">New Bug</a></td>
		<td><a href="{{phabDiffsDesktop}}">Pull Requests</a></td>
		<td><a href="{{phabNewDiff}}">New PR (Repo: Plasma SDK)</a></td>
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
