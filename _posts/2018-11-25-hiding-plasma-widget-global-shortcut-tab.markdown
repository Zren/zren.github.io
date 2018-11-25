---
title: Hiding Plasma Widget Global Shortcut Tab
layout: post
---

First we'll look a the file that wraps the Plasma5 widget's config page. The file is called [AppletConfiguration.qml](https://github.com/KDE/plasma-desktop/blob/master/desktoppackage/contents/configuration/AppletConfiguration.qml) in the `plasma-desktop` repo.

Since the main item in the this file is called `id: root`, my first attempt was to log it in my config page.

{% highlight qml %}
Item {
	id: page

	Component.onCompleted: {
		console.log('root', root)
	}
}
{% endhighlight %}

However, unexpectedly, it logs the StackView instead of a AppletConfiguration instance.

{% highlight log %}
qml: root StackView_QMLTYPE_195_QML_201(0x5620e8559fd0)
{% endhighlight %}

If we try logging `console.log('mainColumn', mainColumn)` we get:

{% highlight log %}
qml: mainColumn QQuickColumnLayout_QML_199(0x5620e84c02b0
{% endhighlight %}

And if we try logging the parent item of `mainColumn` like with `console.log('appletConfiguration', mainColumn.parent)` we get:

{% highlight log %}
qml: appletConfiguration AppletConfiguration_QMLTYPE_196(0x5620e850ec00)
{% endhighlight %}

Now that we've gotten a way to reference the main item of the config window, we could resize the window. Or we could hide the keyboard shortcut tab.

{% highlight qml %}
Item {
	id: page

	Component.onCompleted: {
		// https://github.com/KDE/plasma-desktop/blob/master/desktoppackage/contents/configuration/AppletConfiguration.qml
		var appletConfiguration = mainColumn.parent
		appletConfiguration.width = 1400

		// Remove default Global Keyboard Shortcut config tab.
		var keyboardShortcuts = appletConfiguration.globalConfigModel.get(0)
		appletConfiguration.globalConfigModel.removeCategoryAt(0)
	}
}
{% endhighlight %}

![](https://i.imgur.com/SH26uO2.png)

Please note `AppletConfiguration.qml` is private code, not a public API, so it may change without notice.
