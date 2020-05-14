---
title: NightColor.py for Setting Temp From Terminal
layout: post
---

I recently looked into the [nightcolor widget](https://github.com/KDE/kdeplasma-addons/tree/master/applets/nightcolor) hoping to add a mousewheel control to temporarily force a specific color like the [Redshift Control widget](https://github.com/kde/plasma-redshift-control) does. Unfortunately  I realized the existing API in the NightColor QML plugin doesn't have the function to do so. So I dived into the NightColor DBus API (Using `qdbusviewer`) hoping to run a `qdbus` command.

{% highlight bash %}
$ qdbus org.kde.KWin /ColorCorrect
property read bool org.kde.kwin.ColorCorrect.available
property read uint org.kde.kwin.ColorCorrect.currentTemperature
property read bool org.kde.kwin.ColorCorrect.enabled
property read bool org.kde.kwin.ColorCorrect.inhibited
property read uint org.kde.kwin.ColorCorrect.mode
property read qulonglong org.kde.kwin.ColorCorrect.previousTransitionDateTime
property read uint org.kde.kwin.ColorCorrect.previousTransitionDuration
property read bool org.kde.kwin.ColorCorrect.running
property read qulonglong org.kde.kwin.ColorCorrect.scheduledTransitionDateTime
property read uint org.kde.kwin.ColorCorrect.scheduledTransitionDuration
property read uint org.kde.kwin.ColorCorrect.targetTemperature
signal void org.kde.kwin.ColorCorrect.nightColorConfigChanged(QVariantMap)
method uint org.kde.kwin.ColorCorrect.inhibit()
method void org.kde.kwin.ColorCorrect.nightColorAutoLocationUpdate(double, double)
method QVariantMap org.kde.kwin.ColorCorrect.nightColorInfo()
method bool org.kde.kwin.ColorCorrect.setNightColorConfig(QVariantMap)
method void org.kde.kwin.ColorCorrect.uninhibit(uint cookie)
signal void org.freedesktop.DBus.Properties.PropertiesChanged(QString interface_name, QVariantMap changed_properties, QStringList invalidated_properties)
method QDBusVariant org.freedesktop.DBus.Properties.Get(QString interface_name, QString property_name)
method QVariantMap org.freedesktop.DBus.Properties.GetAll(QString interface_name)
method void org.freedesktop.DBus.Properties.Set(QString interface_name, QString property_name, QDBusVariant value)
method QString org.freedesktop.DBus.Introspectable.Introspect()
method QString org.freedesktop.DBus.Peer.GetMachineId()
method void org.freedesktop.DBus.Peer.Ping()
{% endhighlight %}


It looks like the `setNightColorConfig(QVariantMap)` function will work. I accepts a dictionary of config keys and values.

* <https://github.com/KDE/kwin/blob/master/colorcorrection/colorcorrectdbusinterface.cpp#L268>
* <https://github.com/KDE/kwin/blob/master/colorcorrection/manager.cpp#L724>

Unfortunately neither `qdbus` or `dbus-send` support passing a VariantMap (`a{sv}`) as an argument. So I took realized I needed to write a python script that uses the [dbus module](https://dbus.freedesktop.org/doc/dbus-python/tutorial.html) to call:

{% highlight python %}
setNightColorConfig({'NightTemperature': 4200})
{% endhighlight %}

The dbus module is fairly straighforward. First get the session's `bus`. Then use the NightColor `servicename` and `path` to get the object. Next get the interface of the function we want to call. Here's a simple example that prints the current `nightColorInfo` config properties. It'll list everything we can set.

{% highlight python %}
import dbus

bus = dbus.SessionBus()
obj = bus.get_object('org.kde.KWin', '/ColorCorrect')
iface = dbus.Interface(obj, dbus_interface='org.kde.kwin.ColorCorrect')
props = iface.nightColorInfo()
for key, value in props.items():
	print(key, value)
{% endhighlight %}

Here's my final script.
<https://gist.github.com/Zren/6b9a0cea7b19ab42f239b379bea5e2b9>

You'll notice I also set `Mode=3` to change it to `NightColorMode.Constant` aka "Always On".

Last thing I did was replace my hardcoded `4200` temp, and used python's [argparse module](https://docs.python.org/3.7/library/argparse.html) to parse the terminal command arguments.
