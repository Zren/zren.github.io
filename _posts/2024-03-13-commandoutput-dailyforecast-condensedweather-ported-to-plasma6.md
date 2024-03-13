---
layout: post
title: CommandOutput, DailyForecast, CondensedWeather Ported To Plasma 6
---

* **Command Output:** [Plasma 6 Widget](https://store.kde.org/p/2136636/) / [Plasma 5 Widget](https://store.kde.org/p/1166510/)
* **Daily Forecast:** [Plasma 6 Widget](https://store.kde.org/p/2137185/) / [Plasma 5 Widget](https://store.kde.org/p/1287928/)
* **Condensed Weather:** [Plasma 6 Widget](https://store.kde.org/p/2137197/) / [Plasma 5 Widget](https://store.kde.org/p/1353451/)

Also, [@dhruv8sh](https://github.com/dhruv8sh) has [forked](https://github.com/dhruv8sh/plasma-applet-alphablackcontrol) the Plasma 5 [AlphaBlack Control](https://store.kde.org/p/1237963/) widget and ported it to Plasma 6. It can be found at <https://store.kde.org/p/2136860>.

## Porting to Plasma 6

After [finally setting up a Virt-Manager VM with Plasma 6]({% post_url 2024-03-04-opensuse-krypton-plasma-6-setup %}), I've been steadily porting my widget build scripts to Plasma 6.

Most of my old build scripts used `kreadconfig5` to read data from the `.ini` like `.desktop` files to get the widget's namespace (eg: `com.github.zren.commandoutput`) and ServiceType (eg: `Plasma/Applet`).

```sh
packageNamespace=`kreadconfig5 --file="$PWD/package/metadata.desktop" --group="Desktop Entry" --key="X-KDE-PluginInfo-Name"`
packageServiceType=`kreadconfig5 --file="$PWD/package/metadata.desktop" --group="Desktop Entry" --key="X-KDE-ServiceTypes"`
```

The ServiceType can be assumed if I only use this build script for widgets, but I still need to read the former in my `./install` script since I need to check if the namespace is already installed to switch between `kpackagetool6 --install` and `kpackagetool6 --upgrade` since `--install` will fail if the widget already exists in `~/.local/share/plasma/plasmoids`.

```sh
isAlreadyInstalled=false
kpackagetool5 --type="Plasma/Applet" --show="com.github.zren.commandoutput" &> /dev/null
if [ $? == 0 ]; then
	isAlreadyInstalled=true
fi
if $isAlreadyInstalled; then
	kpackagetool5 --type "Plasma/Applet" --upgrade ./package/
	restartPlasmashell=true
else
	kpackagetool5 --type "Plasma/Applet" --install ./package/
fi
```

Since Plasma 6 now forces the use of `metadata.json`, I now need a command that'll read a JSON object key, using only the software installed by default on most distros. I need to check if `jq` is installed by default on every distro since that would simplify things. That said, every distro will have `python3` installed so we can just use it's `json` module.

```bash
packageNamespace=`python3 -c 'import sys, json; print(json.load(sys.stdin).get("KPlugin", {}).get("Id", ""))' < "$PWD/package/metadata.json"`
```

Where things become annoying is with parsing the ServiceType. By default, `desktoptojson` will convert `X-KDE-ServiceTypes=Plasma/Applet` in `metadata.desktop` to this in `metadata.json`.

```json
{ "KPlugin": { "ServiceTypes": [ "Plasma/Applet" ] } }
```

However in Plasma 6, you manually need to convert it to:

```json
{ "KPackageStructure": "Plasma/Applet" }
```

So we need to parse both cases in the build scripts.

```bash
packageServiceType=`python3 -c 'import sys, json; print(json.load(sys.stdin).get("KPackageStructure",""))' < "$PWD/package/metadata.json"`
if [ -z "$packageServiceType" ]; then # desktoptojson will set KPlugin.ServiceTypes[0] instead of KPackageStructure
	packageServiceType=`python3 -c 'import sys, json; print((json.load(sys.stdin).get("KPlugin", {}).get("ServiceTypes", [])+[""])[0])' < "$PWD/package/metadata.json"`
	echo "[warning] metadata.json needs KPackageStructure set in Plasma6"
fi
```

## [Plasma 5] Parsing I18n in metadata.desktop

Next up was the problem I'd been dreading since `metadata.desktop` was deprecated in Plasma 5. Parsing/extracting i18n translations from the new `metadata.json` then modifying the JSON with the new translations.

With the old `metadata.desktop`, the `xgettext` and `msgfmt` tools had a built in ability to edit `.desktop` files.

```bash
# Note: xgettext v0.20.1 (Kubuntu 20.04) and below will attempt to translate Icon,
# so we need to specify Name, GenericName, Comment, and Keywords.
# https://github.com/Zren/plasma-applet-lib/issues/1
# https://savannah.gnu.org/support/?108887
find "${packageRoot}" -name '*.desktop' | sort > "${DIR}/infiles.list"
xgettext --files-from="${DIR}/infiles.list" --language=Desktop \
	-k -kName -kGenericName -kComment -kKeywords \
	-D "${packageRoot}"	-D "${DIR}"
	-o "template.pot.new" \
	|| \
	{ echoRed "[translate/merge] error while calling xgettext. aborting."; exit 1; }
```

```sh
touch "$DIR/LINGUAS" # List all available translation languages
for cat in `find . -name '*.po' | sort`; do
	catLocale=`basename ${cat%.*}` # "fr.po" => "fr"
	echo "${catLocale}" >> "$DIR/LINGUAS"
done

cp -f "$DIR/../metadata.desktop" "$DIR/template.desktop"
sed -i '/^Name\[/ d; /^GenericName\[/ d; /^Comment\[/ d; /^Keywords\[/ d' "$DIR/template.desktop"

msgfmt --desktop --template="$DIR/template.desktop" \
	-d "$DIR/" \
	-o "$DIR/new.desktop"
```

## [Plasma 6] Parsing I18n in metadata.json

KDE might be using `itstool` I think (they use it in `org.kde.plasmashell.metainfo.po`) but `plasma-desktop._json_.po` which contains the `metadata.json` translations doesn't reference it at all.

* [gnu.org/software/gettext/manual/](https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html#index-_002d_002dits_002c-xgettext-option)
* <https://l10n.kde.org/stats/gui/trunk-kf6/package/plasma-desktop/fr/>

```po
#. (itstool) path: component/name
#: org.kde.plasmashell.metainfo.xml:9
msgid "KDE Plasma Desktop"
msgstr "Bureau Plasma de KDE"
```

```po
#: applets/activitypager/metadata.json
msgctxt "Name"
msgid "Activity Pager"
msgstr "Gestionnaire d'activités"
```

When I realized there wasn't a simple tool to extract update `metadata.json` with translations, I realized I'd probably have to write something myself.

Extracting the `Name` and `Description` from `metadata.json` was fairly simple. Just read the keys from JSON and create a simple `template.pot`. We can just ignore filling out the `.pot` header as it gets overwritten in the `xgettext --join-existing` later on.

```py
with open(self.jsonMetaFilepath, 'r') as fin:
	metadata = json.load(fin)
# This template header is overwritten later so the only changes needed is
# 'charset=CHARSET' => 'charset=UTF-8' so that xgettext doesn't complain.
# POT_DEFAULT_HEADER already has the charset=UTF-8 replaced.
newTemplateText = POT_DEFAULT_HEADER
kp = metadata.get('KPlugin', {})
trKeywords = [
	'Name',
	'Description',
]
relativeMetadataPath = os.path.relpath(self.jsonMetaFilepath, self.translateDir)
for keyword in trKeywords:
	keywordMessage = kp.get(keyword, '')
	keywordMessage = keywordMessage.replace('\"', r'\"')
	if keyword != "":
		# keywordText = f"#: {relativeMetadataPath}\nmsgctxt \"{keyword}\"\nmsgid \"{keywordMessage}\"\nmsgstr \"\"\n\n"
		keywordText = f"#: {relativeMetadataPath}\nmsgid \"{keywordMessage}\"\nmsgstr \"\"\n\n"
		newTemplateText += keywordText
with open(newTemplatePath, 'w') as fout:
	fout.write(newTemplateText)
```

Now the tricky part, parsing the translated `language.po` files, then editing the `metadata.json`.

Checkout the regex I used here: <https://regex101.com/r/kEJCVL>

<https://github.com/Zren/plasma-applet-lib/blob/master/kpac#L97>

```py
PoMessage = namedtuple('PoMessage', ['ctxt', 'id', 'str'])
class PoFile:
	def __init__(self, filepath):
		self.filepath = filepath
		self.text = None
		self.messages = []
		with open(self.filepath, 'r') as fin:
			self.text = fin.read()
		self.parse()
	@property
	def msgPattern(self):
		# Edit/Test: https://regex101.com/r/kEJCVL
		patt = r'(msgctxt[ \t]+(".*")[ \t]*\n)?'
		patt += r'((".*"[ \t]*\n)*)'
		patt += r'(msgid[ \t]+(".*")[ \t]*\n)'
		patt += r'((".*"[ \t]*\n)*)'
		patt += r'(msgstr[ \t]+(".*")[ \t]*\n)'
		patt += r'((".*"[ \t]*\n)*)'
		return patt
	def _joinMsgStr(self, line1, line234):
		if line1 is None:
			return None
		elif line234 is None:
			return line1.strip().strip('\"')
		else:
			lines = [line1] + line234.split('\n')
			msgstr = ""
			for line in lines:
				msgstr += line.strip().strip('\"')
			return msgstr
	def parse(self):
		for m in re.finditer(self.msgPattern, self.text):
			msgCtx = self._joinMsgStr(m.group(2), m.group(3))
			msgId = self._joinMsgStr(m.group(6), m.group(7))
			msgStr = self._joinMsgStr(m.group(10), m.group(11))
			msg = PoMessage(msgCtx, msgId, msgStr)
			self.messages.append(msg)
	def getMsgStr(self, msgid, msgctxt=None):
		for msg in self.messages:
			if msg.ctxt == msgctxt and msg.id == msgid:
				return msg.str
		return None
```

An important part was to use `ensure_ascii=False` in `json.dump()` to keep the unicode text.

<https://github.com/Zren/plasma-applet-lib/blob/master/kpac#L881>

```py
with open(self.jsonMetaFilepath, 'r') as fin:
	metadata = json.load(fin)
trKeywordsMap = {
	'Name': '',
	'Description': '',
}
kp = metadata.get('KPlugin', {})
for keyword in trKeywordsMap.keys():
	trKeywordsMap[keyword] = kp.get(keyword, '')
for catFilepath in glob.glob(os.path.join(self.translateDir, '*.po')):
	catFilename = os.path.basename(catFilepath)
	catLocale = os.path.splitext(catFilename)[0]
	catFile = PoFile(catFilepath)
	for keyword, msgid in trKeywordsMap.items():
		catMsgStr = catFile.getMsgStr(msgid)
		catKeyword = f"{keyword}[{catLocale}]"
		if kp.get(catKeyword) != catMsgStr and catMsgStr != "":
			kp[catKeyword] = catMsgStr
with open(filepath, 'w') as fout:
	json.dump(data, fout, ensure_ascii=False, indent='\t', sort_keys=True)
	fout.write('\n') # Trailing newline at EOF
```

## Drawing the rest of the Owl in Plasma 6

Okay now I needed to do everything else listed on:  
<https://develop.kde.org/docs/plasma/widget/porting_kf6/>


Well since I have [like a dozen widgets](https://store.kde.org/u/Zren), I needed to automate some of this.

Manipulating `metadata.json` with python3 is easy enough as we demonstrated above.

<https://github.com/Zren/plasma-applet-lib/blob/22a5d896b36f4d73a96549c980de75406ec77550/kpac#L1055>

For the rest, the easiest way would be with some simple `sed` text replacements. To make life easier I just kept using python though.

<https://github.com/Zren/plasma-applet-lib/blob/22a5d896b36f4d73a96549c980de75406ec77550/kpac#L1216>

Then I grepped for the new `KSvg.` namespaces, and added an `import org.kde.ksvg as KSvg` at the top of the file if it was missing. I may or may not have forgotten to write the rest of the file contents and deleted a few files when testing. Glory to `git checkout path/to/file.txt` for saving my bacon here.

Lastly I detected if the file was `main.qml`, and replaced any line starting with `^Item\s*\{` with `PlasmoidItem {` since I usually keep my code properly indented.

As always, creating a list of all the various `Plasmoid.___` properties to replace was a pain.

#### [Plasma5] Global `plasmoid` property (which is also attached to the widget root item as `Plasmoid`)

* <https://invent.kde.org/plasma/plasma-framework/-/tree/kf5/src/scriptengines/qml/plasmoid/appletinterface.h>
* <https://invent.kde.org/plasma/plasma-framework/-/tree/kf5/src/plasmaquick/appletquickitem.h>
* <https://invent.kde.org/plasma/plasma-framework/-/tree/kf5/src/plasma/applet.h>

#### [Plasma6] `PlasmoidItem` root item

* <https://invent.kde.org/plasma/plasma-framework/-/tree/master/src/plasmaquick/plasmoid/plasmoiditem.h>
* <https://invent.kde.org/plasma/plasma-framework/-/tree/master/src/plasmaquick/appletquickitem.h>

#### [Plasma6] Attached `Plasmoid` similar to `Layout` which dynamically grabs the value from the `Applet` class

* <https://invent.kde.org/plasma/plasma-framework/-/blame/master/src/plasmaquick/private/plasmoidattached_p.cpp#L33>
* <https://invent.kde.org/plasma/plasma-framework/-/tree/master/src/plasma/applet.h>

Since Plasma6 made things a little confusing as to what is in `PlasmoidItem {}` and what is accessed with `Plasmoid.___` I settled on the following for now:

<https://github.com/Zren/plasma-applet-lib/blob/22a5d896b36f4d73a96549c980de75406ec77550/kpac#L1185>

```py
plasmoidPropsPorted = [
	# AppletQuickItem
	'switchWidth', 'switchHeight',
	'compactRepresentation', 'fullRepresentation',
	'preloadFullRepresentation', 'preferredRepresentation',
	'expanded', 'activationTogglesExpanded',
	'hideOnWindowDeactivate',
	# PlasmoidItem
	'toolTipMainText', 'toolTipSubText', 'toolTipTextFormat', 'toolTipItem',
	'hideOnWindowDeactivate',
]
```

The last things I had to [do manually](https://github.com/Zren/plasma-applet-dailyforecast/commit/7af67098b4bce76334fbd63326532674d1443077) was convert the `plasmoid.setAction('refresh, ...)` calls to the new `Plasmoid.contextualActions: [ PlasmaCore.Action {...} ]` which would be a tad too complicated to automate.

I was able to quickly `sed` replace my `plasmoid.action('configure').trigger()` trick to open the config dialog automatically when testing though which I have in most of my widgets.

```qml
PlasmoidItem {
	Component.onCompleted: Plasmoid.internalAction("configure").trigger()
}
```

## In Closing

Overall, with my new script it should be as easy to do most of the dull text replacement work.

The hard part will be converting any deprecated `QQC1.Buttons` and other GUI elements that might have custom styling to their `QQC2.Button` counterparts. [TiledMenu](https://github.com/Zren/plasma-applet-tiledmenu/issues/156) and EventCalendar will probably be more annoying to port than just running the following:

<https://github.com/Zren/plasma-applet-lib/blob/master/kpac>

```sh
python3 ./kpac updatelib ../plasma-applet-lib
python3 ./kpac plasma6
# Scan changes 
python3 ./kpac i18n # Update metadata.json and convert .po => .mo
git commit . -m 'Update'
python3 ./kpac build # Create a zipped .plasmoid
```

I got too tired last night so first things up is porting SimpleWeather today.

This "widgets have been updated" blog post rambled on more than I expected sorry bout that.

