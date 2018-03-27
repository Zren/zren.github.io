---
layout: widepage
title: KDE Bugs (plasmashell)
permalink: /kde/bugs/
---

<style type="text/css">
#sidenav {
	display: none;
}
.page-content .wrapper {
	max-width: -webkit-calc(100vw - (30px * 2));
	max-width: calc(100vw - (30px * 2));
}
</style>

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
		var visibleBugs = []
		for (var table of document.querySelectorAll('.buglist')) {
			var visibleCount = 0
			for (var bugItem of table.querySelectorAll('.bug-item')) {
				var bugSummary = bugItem.getAttribute('data-summary') || ''
				var queryIndex = bugSummary.toLowerCase().indexOf(query)
				if (showAll || queryIndex >= 0) {
					bugItem.classList.remove('hidden')
					visibleCount += 1
					visibleBugs.push(bugItem)
				} else {
					bugItem.classList.add('hidden')
				}
				
				var bugSummaryEl = bugItem.querySelector('.bug-summary')
				if (queryIndex >= 0) {
					var queryRegex = new RegExp(query, 'ig')
					bugSummaryEl.innerHTML = bugSummary.replace(queryRegex, '<span class="search-highlight">$&</span>')
				} else {
					bugSummaryEl.textContent = bugSummary
				}
			}
		}
		console.log('updateSearch', query, visibleBugs)
	}

	function bindThrottledSearch(el, callback, interval) {
		var timerId = 0
		function onTimeout() {
			timerId = 0
			callback()
		}
		function onInput() {
			if (timerId) {
				clearTimeout(timerId)
			}
			timerId = setTimeout(onTimeout, 100)
		}
		el.addEventListener('input', onInput)
	}


	function fetchQueriedBugs() {
		fetchProductBugs(window.product, searchInput.value)
	}


	bindThrottledSearch(searchInput, updateSearch, 100)
	bindThrottledSearch(searchInput, fetchQueriedBugs, 1000)
</script>

<style type="text/css">
/* GitHub theme */
.buglist {
	width: 100%;
	border: 1px solid #e1e4e8;
	border-top: none;
}
.bug-item {
	border-top: 1px solid #e1e4e8;
}
.bug-item:hover {
	background-color: #ebf2fb;
}
.bug-row {
	display: flex;
	flex-direction: row;
}
.bug-row > * {
	display: table-cell;
}
.bug-status {
	padding-top: 8px;
	padding-left: 16px;
	padding-right: 8px;
	font-size: 24px;
	line-height: 24px;
	width: 24px;
	vertical-align: middle;
}
.bug-status .octicon {
	display: inline-block;
	vertical-align: text-top;
	fill: currentColor;
}
.octicon-issue-opened {
	color: #28a745;
}
.bug-contents {
	padding: 8px;
	flex: 1; /* fill width */
}
.bug-rightside {
	padding: 8px;
}
.bug-id {
	font-size: 16px;
	vertical-align: middle;
}
.bug-summary {
	font-size: 16px;
	font-weight: 600;
	vertical-align: middle;
}
.bug-summary,
.bug-summary:visited {
	color: #24292e;
}
.bug-item.bug-critical .bug-summary {
	color: #f00;
}
.bug-item.bug-resolved .bug-summary {
	color: #92969D;
}
.bug-summary:hover {
	color: #0366d6;
	text-decoration: none;
}
.search-highlight {
	display: inline-block;
	background-color: yellow;
}
.bug-labels {
	line-height: 1.5;
}
a.bug-label {
	display: inline-block;
	vertical-align: text-top;
	height: 20px;
	padding: 0.15em 4px;
	font-size: 12px;
	font-weight: 600;
	line-height: 20px;
	border-radius: 2px;
	margin-top: -2px;
	box-shadow: inset 0 -1px 0 rgba(27,31,35,0.12);
}
a.bug-label,
a.bug-label:visited {
	background-color: #bfdadc;
	color: #244042;
}
a.bug-label:hover {
	text-decoration: none;
}
a.bug-label.bug-component {
	font-size: 14px;
}
a.bug-label.bug-resolution-UNMAINTAINED {
	background-color: #92969D;
	color: #FFFFFF;
}
a.bug-label.bug-resolution-FIXED {
	background-color: #bfe5bf;
	color: #000000;
}
a.bug-label.bug-resolution-DUPLICATE,
a.bug-label.bug-resolution-INVALID {
	background-color: #e5e5e5;
	color: #666;
}
.bug-critical a.bug-label.bug-severity {
	background-color: #a90f0f;
	color: #fde8e8;
	text-transform: uppercase;
}

</style>
<div class="buglist" name="buglist">
</div>
<div id="bug-template" class="buglist" style="display: none">
	<div class="bug-item">
		<div class="bug-row">
			<div class="bug-status"></div>
			<div class="bug-contents">
				<div>
					<span class="bug-labels">
						<a class="bug-label bug-component">general</a>
					</span>
					<a class="bug-summary" href="https://bugs.kde.org/show_bug.cgi?id=54973">program launch doesn't show error message on linker error</a>
					<span class="bug-id">#54973</span>
				</div>
			</div>
			<div class="bug-rightside">
				<span class="bug-labels">
					<a class="bug-label bug-severity">normal</a>
					<a class="bug-label bug-resolution">fixed</a>
				</span>	
			</div>
		</div>
	</div>
</div>


<script type="text/javascript">

function el(html) {
	var e = document.createElement('div')
	e.innerHTML = html.trim()
	console.log(e)
	console.log(e.firstChild)
	return e.removeChild(e.firstChild)
}
var octiconIssueOpened = '<svg class="octicon octicon-issue-opened open" viewBox="0 0 14 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>'
var octiconIssueClosed = '<svg class="octicon octicon-issue-closed closed" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M7 10h2v2H7v-2zm2-6H7v5h2V4zm1.5 1.5l-1 1L12 9l4-4.5-1-1L12 7l-1.5-1.5zM8 13.7A5.71 5.71 0 0 1 2.3 8c0-3.14 2.56-5.7 5.7-5.7 1.83 0 3.45.88 4.5 2.2l.92-.92A6.947 6.947 0 0 0 8 1C4.14 1 1 4.14 1 8s3.14 7 7 7 7-3.14 7-7l-1.52 1.52c-.66 2.41-2.86 4.19-5.48 4.19v-.01z"></path></svg>'
function renderBug(bug) {
	var bugTemplate = document.querySelector('#bug-template')
	console.log('bugTemplate', bugTemplate)
	console.log('bugTemplate.innerHTML', bugTemplate.innerHTML)
	var bugEl = el(bugTemplate.innerHTML)
	console.log('bugEl', bugEl)
	var bugStatus = bugEl.querySelector('.bug-status')
	if (bug.status == "RESOLVED") {
		bugStatus.innerHTML = octiconIssueClosed
		bugEl.classList.add('bug-resolved')
	} else {
		bugStatus.innerHTML = octiconIssueOpened
		bugEl.classList.add('bug-open')
	}

	var bugComponent = bugEl.querySelector('.bug-component')
	bugComponent.textContent = bug.component

	var bugId = bugEl.querySelector('.bug-id')
	bugId.textContent = '#' + bug.id

	var bugSummary = bugEl.querySelector('.bug-summary')
	bugEl.setAttribute('data-summary', bug.summary)
	bugSummary.textContent = bug.summary
	bugSummary.href = 'https://bugs.kde.org/show_bug.cgi?id=' + bug.id

	var bugResolution = bugEl.querySelector('.bug-resolution')
	if (bug.resolution) {
		bugResolution.textContent = bug.resolution
		bugResolution.classList.add('bug-resolution-' + bug.resolution)
	} else {
		bugResolution.remove()
	}

	var bugSeverity = bugEl.querySelector('.bug-severity')
	if (bug.severity) {
		bugSeverity.textContent = bug.severity
		bugSeverity.classList.add('bug-severity-' + bug.resolution)
		if (bug.severity == 'critical' || bug.severity == 'grave' || bug.severity == 'major' || bug.severity == 'crash') {
			bugEl.classList.add('bug-critical')
		} else { // We don't care about normal/minor/wishlist/task
			bugSeverity.remove()
		}
	}
	
	return bugEl
}
function renderBugList(bugListData) {
	var bugList = document.querySelector('.buglist[name="buglist"]')

	// Clear existing list
	while (bugList.firstChild) {
		bugList.removeChild(bugList.firstChild)
	}

	for (var bug of bugListData.bugs) {
		var bugEl = renderBug(bug)
		bugList.appendChild(bugEl)
	}

	updateSearch()
}

window.product = 'plasmashell'
window.bugLimit = 25
function fetchProductBugs(product, query) {
	var url = 'https://bugs.kde.org/rest/bug'
	url += '?product=' + encodeURIComponent(product)
	url += '&limit=' + window.bugLimit
	url += '&order=bug_id%20DESC'
	if (query) {
		url += '&short_desc_type=allwordssubstr'
		url += '&short_desc=' + encodeURIComponent(query)
	}

	fetch(url).then(function(response){
		return response.json()
	}).then(function(data){
		console.log(data)
		renderBugList(data)
	}).catch(function(error){
		console.log(error)
	})
}

fetchProductBugs(window.product)

</script>
<script type="text/javascript">
function fetchDebugBugs() {
	var url = '/js/plasmashell-bugs.json'
	fetch(url).then(function(response){
		return response.json()
	}).then(function(data){
		console.log(data)
		renderBugList(data)
	}).catch(function(error){
		console.log(error)
	})
}

// fetchDebugBugs()

</script>