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
li a {
    display: inline-block;
}
li:nth-of-type(2n) {
    background: #ebf2fb;
}
</style>

> **Note:** All GitHub links are source mirrors only. Do not submit issues to those repos.

## PlasmaShell

{% assign kdeBugList = 'https://bugs.kde.org/buglist.cgi?order=bug_id%20DESC&query_format=advanced&' %}
{% assign kdeNewBug = 'https://bugs.kde.org/enter_bug.cgi?' %}
{% assign phabDiffs = 'https://phabricator.kde.org/differential/query/' %}
{% assign phabDiffsDesktop = 'https://phabricator.kde.org/differential/query/7LklMmkHDcva/#R' %}
{% assign phabDiffsWorkspace = 'https://phabricator.kde.org/differential/query/stR7aMSmxBU./#R' %}
{% assign phabNewDiff = 'https://phabricator.kde.org/differential/diff/create/' %}


* **Application Launcher (Kickoff):** [GitHub](https://github.com/KDE/plasma-desktop/blob/master/applets/kickoff/) / [All Bugs]({{kdeBugList}}product=plasmashell&component=Application%20Launcher%20%28Kickoff%29&list_id=1406061) / [New Bug]({{kdeNewBug}}product=plasmashell&component=Application%20Launcher%20%28Kickoff%29) / [Pull Requests]({{phabDiffsDesktop}}) / [New PR (Repo: Plasma Desktop)]({{phabNewDiff}})
* **Application Menu/Dashboard (Kicker):** [GitHub](https://github.com/KDE/plasma-desktop/blob/master/applets/kicker/) / [All Bugs]({{kdeBugList}}product=plasmashell&component=Application%20Menu%20%28Kicker%29&list_id=1406061) / [New Bug]({{kdeNewBug}}product=plasmashell&component=Application%20Menu%20%28Kicker%29) / [Pull Requests]({{phabDiffsDesktop}}) / [New PR (Repo: Plasma Desktop)]({{phabNewDiff}})
    * **Application Dashboard:**
* **Audio Volume (plasma-pa):** [GitHub](https://github.com/KDE/plasma-pa) / [All Bugs]({{kdeBugList}}product=plasma-pa&list_id=1406062) / New Bug / [Pull Requests]({{phabDiffs}}NlM7ES4ji2UX/#R) / [New PR (Repo: Plasma Audio Volume Applet)]({{phabNewDiff}})
* **Battery and Brightness:** [GitHub](https://github.com/KDE/plasma-workspace/tree/master/applets/batterymonitor) / All Bugs / New Bug / Pull Requests / [New PR (Repo: Plasma Workspace)]({{phabNewDiff}})
* **Digital Clock:** [GitHub](https://github.com/KDE/plasma-desktop/blob/master/applets/kicker/) / [All Bugs]({{kdeBugList}}product=plasmashell&component=Digital%20Clock&list_id=1406061) / [New Bug]({{kdeNewBug}}product=plasmashell&component=Digital%20Clock) / [Pull Requests]({{phabDiffsWorkspace}}) / [New PR (Repo: Plasma Desktop)]({{phabNewDiff}})
    * **MonthView:** <https://github.com/KDE/plasma-framework/tree/master/src/declarativeimports/calendar>
* **Media Player [Controller]:** [GitHub](https://github.com/KDE/plasma-workspace/tree/master/applets/mediacontroller) / All Bugs / New Bug / Pull Requests / [New PR (Repo: Plasma Workspace)]({{phabNewDiff}})
* **Notifications:** [GitHub](https://github.com/KDE/plasma-workspace/tree/master/applets/notifications) / All Bugs / New Bug / Pull Requests / [New PR (Repo: Plasma Workspace)]({{phabNewDiff}})
* **Pager:** [GitHub](https://github.com/KDE/plasma-desktop/blob/master/applets/pager/) / [All Bugs]({{kdeBugList}}product=plasmashell&component=Pager&list_id=1411058) / [New Bug]({{kdeNewBug}}product=plasmashell&component=Pager) / [Pull Requests]({{phabDiffsDesktop}}) / [New PR (Repo: Plasma Desktop)]({{phabNewDiff}})
* **System Tray:** [GitHub](https://github.com/KDE/plasma-workspace/tree/master/applets/systemtray/) / [All Bugs]({{kdeBugList}}product=plasmashell&component=System%20Tray&list_id=1408524) / [New Bug]({{kdeNewBug}}product=plasmashell&component=System%20Tray) / [Pull Requests]({{phabDiffsWorkspace}}) / [New PR (Repo: Plasma Workspace)]({{phabNewDiff}})
* **Task Manager:** [GitHub](https://github.com/KDE/plasma-desktop/blob/master/applets/taskmanager/) / [All Bugs]({{kdeBugList}}product=plasmashell&component=Task%20Manager&list_id=1407534) / [New Bug]({{kdeNewBug}}product=plasmashell&component=Task%20Manager) / [Pull Requests]({{phabDiffsDesktop}}) / [New PR (Repo: Plasma Desktop)]({{phabNewDiff}})
    * **Icon Tasks:** [All Bugs]({{kdeBugList}}product=plasmashell&component=Icons-only%20Task%20Manager&list_id=1407535) / [New Bug]({{kdeNewBug}}product=plasmashell&component=Icons-only%20Task%20Manager) / Pull Requests / [New PR (Repo: Plasma Desktop)]({{phabNewDiff}})
