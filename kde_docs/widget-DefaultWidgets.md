<!-- ------- -->
{% include docHeader.html label="Default Widgets" %}

{% capture label %}Learn By Example{% endcapture %}
{% capture sectionLeft %}

You can learn by example by reading the default widgets located at:  
`/usr/share/plasma/plasmoids/`

You can fork an existing widget by copying the widget to where the downloaded widgets are installed to:  
`~/.local/share/plasma/plasmoids/`

To properly fork the widget, rename the new folder, then edit the `X-KDE-PluginInfo-Name` in the `metadata.desktop` file to match the new folder name. You will also want to edit the `Name=` in the `metadata.desktop` file as well so you can tell it apart from the widget you forked it from. If might be easier to delete all the translated `Name[fr]=` lines if you don't know your locale code. Finally, delete the `metadata.json` if it exists (or edit it as well).

Finally, run `plasmawindowed` to quickly test the newly forked widget.

{% endcapture %}{% capture sectionRight %}

{% highlight bash %}
cd /usr/share/plasma/plasmoids/
mkdir -p ~/.local/share/plasma/plasmoids
cp -r /usr/share/plasma/plasmoids/org.kde.plasma.analogclock/ ~/.local/share/plasma/plasmoids/
cd ~/.local/share/plasma/plasmoids/
mv ./org.kde.plasma.analogclock ./com.github.zren.myanalogclock
cd ./com.github.zren.myanalogclock
kwriteconfig5 --file="$PWD/metadata.desktop" --group="Desktop Entry" --key="X-KDE-PluginInfo-Name" "com.github.zren.myanalogclock"
kwriteconfig5 --file="$PWD/metadata.desktop" --group="Desktop Entry" --key="Name" "My Analog Clock"
rm ./metadata.json
plasmawindowed com.github.zren.myanalogclock
{% endhighlight %}

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}
