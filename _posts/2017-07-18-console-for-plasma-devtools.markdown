---
layout: post
title: Console for Plasma DevTools
---

Since my last update, I've added a console to the devtools window. QML doesn't have an "exec" function but you can dynamically create components with a string. So we just put our string inside the `Component.onCompleted` event handler. Here's my current exec function.

{% highlight javascript %}
function exec(str) {
	if (str.trim().length == 0) {
		return
	}
	outputView.input(str)
	var comp = 'import QtQuick 2.0; QtObject {\n'
	comp += 'Component.onCompleted: {\n'
	comp += 'try {\n'
	var parsedStr = str.trim()
	parsedStr = parsedStr.replace('console.log(', 'outputView.log(')
	parsedStr = parsedStr.replace('$0', 'elementsView.selectedObj')
	var str1 = parsedStr.substr(0, parsedStr.lastIndexOf('\n') - 1)
	var str2 = parsedStr.substr(parsedStr.lastIndexOf('\n') + 1)
	comp += str1
	comp += 'var _result = ('
	comp += str2
	comp += ')\n'
	comp += 'outputView.output(_result)\n'
	comp += '} catch (e) {\n'
	comp += 'outputView.error(e)\n'
	comp += '}\n'
	comp += 'destroy()\n'
	comp += '}\n'
	comp += '}\n'
	try {
		Qt.createQmlObject(comp, outputView)
	} catch (e) {
		outputView.error(e)
	}
}
{% endhighlight %}

Notice that we replace `console.log(` with a reference to `outputView.log(` so that the user can still use the familiar function without printing to plasmashell's stdout. I may overload the `console` reference later since currently this method doesn't support `console.log.apply(console, ['asdf', 1, 2, 3])` but is simple enough for now.

We also replace `$0` with a reference to the selected item in the elements view like Chrome does. We don't really need $1, $2, etc (2nd+3rd last selected item) but it'd be trivial to have the ElementsView remember a selection history.

If we eventually add autocompletion, we can focus on refactoring and doing things correctly.

Another feature I implemented was animating propety changes in the ElementsView.

{% include streamable.html streamableId="0e9xm" %}

I had to do a number of refactoring in the property view since I was doing a very naive update (1 property change will cause it to check every property). I needed to `bind()` the property we're updating and store all the singal handlers we connect with so that we can disconnect them later.

{% highlight javascript %}
var keys = Object.keys(target)
for (var i in keys) {
	var key = keys[i]
	if (Util.isChangedSignal(target, key)) {
		var propKey = key.substr(0, key.length - 'Changed'.length)
		propListeners[key] = propertyUpdated.bind(propertyTreeView, propKey)
		target[key].connect(propListeners[key])
	}
}
{% endhighlight %}

I recently found out that the panels and the desktop have seperate RootItems so we won't be able to debug the desktop and panel's at the same time (we'll need 2 widgets).

Next up I think I'll work on parsing the "DOM" and creating shortcuts to all the plasma containments and applets.
