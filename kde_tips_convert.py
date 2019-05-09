#!/bin/python3

# This file will convert the kde_tips.md file into mediawiki syntax
# for the KDE Userbase Wiki page
# https://userbase.kde.org/Plasma/Tips
# 
# Paste the contents of kde_tips.mediawiki into:
# https://userbase.kde.org/index.php?title=Plasma/Tips&action=edit

import re

ignoringLines = False
insideCodeTag = False
formattedText = ""
i = 0
lastLineWasEmpty = True

def formatCodeTags(line):
	oldLine = line
	startCodeTag = True
	while True:
		if startCodeTag:
			line = line.replace('`', '<code>', 1)
		else:
			line = line.replace('`', '</code>', 1)

		startCodeTag = not startCodeTag

		if oldLine == line:
			break
		else:
			oldLine = line
			continue
	return line

def formatShortcutCodeTags(line):
	line = re.sub(r'(<code>)(((Ctrl|Alt|Shift|Meta|Win) ?\+ ?)*([A-Z9-9]|F\d+|Left|Right|Up|Down))(</code>)', r'<keycap>\2</keycap>', line)
	return line

def formatPathCodeTags(line):
	def pathrepl(match):
		text = match.group(2)
		if text == '/r/': # Firefox bookmark search engine
			return match.group(0)
		elif '%U' in text: # Steam launch commnad
			return match.group(0)
		else:
			return '{{Path|' + text + '}}'
	line = re.sub(r'(<code>)((/|~/)[^<]*?)(</code>)', pathrepl, line)
	return line

def formatSyntaxStartTag(line):
	global insideCodeTag
	if '{% highlight ' in line:
		line = line.replace('{% highlight bash %}', '<syntaxhighlight lang="bash">')
		line = line.replace('{% highlight css %}', '<syntaxhighlight lang="css">')
		insideCodeTag = True
	return line

def formatSyntaxEndTag(line):
	global insideCodeTag
	if '{% endhighlight %}' in line:
		line = line.replace('{% endhighlight %}', '</syntaxhighlight>')
		insideCodeTag = False
	return line

def formatArrows(line):
	if not insideCodeTag and not line.startswith("> ") and not line.startswith("  > "):
		line = line.replace(' > ', ' → ')
		line = line.replace(' => ', ' → ')
	return line

def formatLinks(line):
	line = re.sub(r'\[([^\]]+?)\]\(#([^\)]+?)\)', r'[[#\2|\1]]', line) # [Text](#anchor-id)
	line = re.sub(r'\[([^\]]+?)\]\(([^\)]+?)\)', r'[\2 \1]', line) # [Text](https://google.com)
	line = re.sub(r'<(http[^\>]+?)>', r'\1', line) # <https://google.com>
	return line


def anchorLink(linkId, linkText):
	return '<span id="{}">[[#{}|{}]]</span>'.format(linkId, linkId, linkText)

def heading(nth, text):
	linkId = text.replace(' ', '_')
	return "<h{}>{}</h{}>".format(nth, anchorLink(linkId, text), nth)

def slugify(text):
	slug = text.encode('ascii', 'ignore').decode('utf-8') # Strip non-ASCII
	slug = slug.lower()
	slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
	slug = re.sub(r'[-]+', '-', slug)
	return slug

#------------
header = """This page aims to list common tweaks a user might make to setup a nice KDE Plasma5 desktop.

-----
"""
formattedText += header

#------------
tipsFilename = './kde_tips.md'

tripleDashCounter = 0

with open(tipsFilename, "r") as fin:
	for line in fin.readlines():
		line = line.rstrip('\n')
		out = ''

		# Convert `code tags`
		line = formatCodeTags(line)
		line = formatShortcutCodeTags(line)
		line = formatPathCodeTags(line)
		line = formatSyntaxStartTag(line)

		# Convert [Label](http://domain.tld)
		# Convert <http://domain.tld>
		if not insideCodeTag:
			line = formatLinks(line)

		# Convert Arrows
		line = formatArrows(line)

		# Headings
		if line.startswith("# ") and not insideCodeTag:
			# out = "= {} =".format(line[2:])
			out = heading(1, line[2:])
		elif line.startswith("## ") and not insideCodeTag:
			# out = "== {} ==".format(line[3:])
			out = heading(2, line[3:])
		elif line.startswith("### ") and not insideCodeTag:
			# out = "=== {} ===".format(line[4:])
			out = heading(3, line[4:])

		# Tip Start
		elif line.startswith("{% capture label %}") and line.endswith("{% endcapture %}{% capture contents %}"):
			label = re.sub(r'{% capture label %}(.+){% endcapture %}{% capture contents %}', r'\1', line) # <https://google.com>
			labelSlug = slugify(label)
			out = '<li id="' + labelSlug + '" class="tip">\n'
			# out += '<a href="#' + labelSlug + '">' + label + '</a>'
			out += '[[#' + labelSlug + '|' + label + ']]\n'
			out += '<p>'
		# Tip End
		elif line.startswith("{% endcapture%}{% include tip.html label=label contents=contents %}"):
			out = '</p>\n'
			out += '</li>'

		# Strip out the variable increments
		elif line.startswith("{% assign i"):
			continue
		
		# Strip out the top jekyll header
		elif line.startswith("---"):
			tripleDashCounter += 1
			if tripleDashCounter == 1:
				ignoringLines = True
				continue
			elif tripleDashCounter == 2:
				ignoringLines = False
				continue

		# Strip out the styling
		elif line.startswith("<style>"):
			ignoringLines = True
			continue
		elif line.startswith("</style>"):
			ignoringLines = False
			continue

		# Strip out the scripts
		elif line.startswith("<script>"):
			ignoringLines = True
			continue
		elif line.startswith("</script>"):
			ignoringLines = False
			continue

		# Style the list item heading
		elif line.startswith("* {:#"): # * {:#cfg-{{ i }}}
			i += 1
			startindex = line.index("}}}") + 3
			text = line[startindex:]
			text = text.strip()
			linkId = "cfg-{}".format(i)
			# anchorTag = '<span id="{}"></span>'.format(linkId)
			out = ';' + '<b>' + anchorLink("cfg-{}".format(i), text) + '</b>'

		# Style the sublist
		elif line.startswith("  * "):
			text = line[4:]
			text = text.strip()
			out = '\n:;<b>' + text + '</b><br />'

		elif line.startswith("    ") and not insideCodeTag:
			text = line[4:]
			text = text.strip()
			# out = '*:' + text
			out += '::' + text + '<br />'

		# Style the list item description
		elif line.startswith("  ") and not insideCodeTag:
			# out = ':' + line[1:]
			out = ':' + line[2:] + '<br />'


		# Regular text
		else:
			out = line

		# Close code tags
		out = formatSyntaxEndTag(out)

		if not ignoringLines:
			# Only allow 1 empty line at a time
			if out == '':
				if lastLineWasEmpty:
					continue
				else:
					lastLineWasEmpty = True
			else:
				lastLineWasEmpty = False

			# Render line
			formattedText += out + '\n'

#------------
footer = """-----

Note that this list is manually kept in sync with https://zren.github.io/kde/#configuration using [https://github.com/Zren/zren.github.io/blob/master/kde_tips_convert.py this script]. — [https://phabricator.kde.org/p/Zren/ Zren]

"""
formattedText += footer

#------------
with open("kde_tips.mediawiki", "w") as fout:
	fout.write(formattedText)

