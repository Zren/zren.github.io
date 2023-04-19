<!-- ------- -->
### Autostarted Apps

<ul>
{% capture label %}Disable restoring session on Login (restarting apps open during Logout){% endcapture %}{% capture contents %}
  System Settings > Startup & Shutdown
  Desktop Session Tab > On Login: Check Start with an empty session
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### Desktop

<ul>
{% capture label %}Hide the ☰ button in the top corner{% endcapture %}{% capture contents %}
  Right Click the desktop wallpaper > Desktop/Folder View Settings
  Tweaks Tab > Uncheck: Show the desktop toolbox
  Note: Plasma removed this button in Plasma 5.19
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Hide the ☰ button in the panel on the bottom right{% endcapture %}{% capture contents %}
  Right Click the ☰ button > Lock Widgets.
  Note: Plasma removed this button in Plasma 5.19
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Always Hide System Tray Notification Icons{% endcapture %}{% capture contents %}
  Right Click the “Expand System Tray Triangle” > System Tray Settings.
  Entries Tab > Networks > Visibility: Hidden
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable Icon in System Tray{% endcapture %}{% capture contents %}
  Right Click the “Expand System Tray Triangle” > System Tray Settings.
  General Tab > Extra Items > Uncheck: Clipboard, Battery
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Classic “Start” Menu{% endcapture %}{% capture contents %}
  While the widgets are unlocked
  Right Click the “Start” menu > Alternatives > Application Menu
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Don’t sort windows in Taskbar{% endcapture %}{% capture contents %}
  Right Click the empty area on the taskbar next to the tasks > Task Manager Settings
  Behavior Tab > Sorting: Manual
  Behavior Tab > Uncheck: Keep Launchers Separate
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Hide windows from other Desktops in Taskbar{% endcapture %}{% capture contents %}
  Right Click a Task > Task Manager Settings
  Behavior Tab > Show only tasks: > Check: From current desktop
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Pin Apps to Taskbar{% endcapture %}{% capture contents %}
  Launch App
  Right Click app in Taskbar > Check: Show Launcher When Not Running
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Hide audio indicator in window list{% endcapture %}{% capture contents %}
  Right Click a Task > Task Manager Settings
  General Tab > Uncheck: Mark applications that play audio
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable Middle-Click Paste Notes Widget{% endcapture %}{% capture contents %}
  Right Click Desktop Wallpaper > Configure Desktop
  Mouse Actions Tab > Press the Delete icon next to the Middle-Button row.
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Lock Widgets{% endcapture %}{% capture contents %}
  Plasma 5.18 and above has hidden the "lock widgets" toggle. It's very easy to enter "edit mode" with a long press. If you want to get the old locked mode behavior, run the following command:
  {% highlight bash %}
  qdbus org.kde.plasmashell /PlasmaShell evaluateScript 'lockCorona(!locked)'
  {% endhighlight %}
  If you want an easier way to toggle locking widgets in Plasma 5.18, install [Win7ShowDesktop widget](https://store.kde.org/p/1100895/) which has a "Lock Widgets" toggle in it's right click menu.
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable Top Left “Hot Corner”{% endcapture %}{% capture contents %}
  System Settings > Desktop Behaviour
  Screen Edges Tab > Top Left: No Action
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Bind Ctrl+Alt+Left/Right to Switch Desktop{% endcapture %}{% capture contents %}
  System Settings > Desktop Behaviour
  Virtual Desktops Tab > Switching > Shortcuts
  Switch One Desktop Left: `Ctrl+Alt+Left`
  Switch One Desktop Right: `Ctrl+Alt+Right`
  Switch To Desktop 1, 2, …: None
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable Switch Desktop when scrolling over desktop wallpaper{% endcapture %}{% capture contents %}
  Right Click the desktop wallpaper > Desktop/Folder View Settings
  Mouse Actions Tab > Remove: Vertical Scroll => Switch Desktop
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable bouncing cursor when apps open{% endcapture %}{% capture contents %}
  System Settings > Applications
  Change "Bouncing" Cursor to "No Feedback"
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable focus stealing prevention{% endcapture %}{% capture contents %}
  System Settings > Window Management
  Window Behaviour Tab > Focus Stealing Prevention: None
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Fix Alt+Click in certain games/software{% endcapture %}{% capture contents %}
  **Note:** Plasma 5.20 has changed the default to `Meta+Click+Drag`, but these instructions are the same for changing back to `Alt+Click+Drag`.
  `Alt+Click+Drag` was a standard keybinding for moving a window in Linux. It tends to conflict with software designed for Windows like Games, Inkscape and Blender. To fix, we'll change it to `Meta+Click+Drag`.
  System Settings > Window Management
  Window Actions Tab > Inner Window, Titlebar, Frame > Modifier Key: `Meta`
  **OR** set Left button: "Nothing" to disable it completely.
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}“Normal” Alt+Tab popup{% endcapture %}{% capture contents %}
  System Settings > Window Management
  Task Switcher Tab > Click the "star icon"
  Select "Thumbnail Grid" in the dropdown.
  Note: You may need to install a package if "Thumbnail Grid" is missing. `kwin-addons` (Kubuntu / KDE Neon), `kdeplasma-addons` (Arch / Manjaro / Fedora), `plasma5-addons` (OpenSUSE).
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Show Alt+Tab popup as fast as possible{% endcapture %}{% capture contents %}
  Normally it will wait 90 milliseconds before trying to show the popup. This makes quick switches faster since it doesn't need to draw anything.
  We need to set `DelayTime=0` under the group `[TabBox]` in the file `~/.config/kwinrc`, then reload kwin.
  It's easier to use these commands than doing it by hand.
  {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group TabBox --key DelayTime 0
qdbus org.kde.KWin /KWin reconfigure
  {% endhighlight %}
  You can also disable the highlight window effect by going to:
  System Settings > Window Management > Task Switcher Tab
  Uncheck: Show selected window
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable Lock Screen{% endcapture %}{% capture contents %}
  System Settings > Desktop Behaviour > Screen Locking Tab
  Uncheck: Lock screen automatically after __ min
  Uncheck: Lock screen on resume
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable Logout/Shutdown Confirmation{% endcapture %}{% capture contents %}
  System Settings > Startup and Shutdown
  Desktop Session Tab > Uncheck: Confirm Logout
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Redden the Screen at Night{% endcapture %}{% capture contents %}
  This is known as Night Light on Windows and Android
  System Settings > Display and Monitor > Night Color
  Check: Activate Night Color
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Windows Keybindings for moving windows{% endcapture %}{% capture contents %}
  System Settings > Shortcuts > Global Keyboard Shortcuts Tab
  KWin > Show Desktop: `Win+M`
  KWin > Maximize Window: `Win+Up`
  KWin > Minimize Window: `Win+Down`
  KWin > Quick Tile Window to the Left: `Win+Left`
  KWin > Quick Tile Window to the Right: `Win+Right`
  To open the “Start Menu” with the Windows key [see the section below](#windowsmeta-key).
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Present all windows with Win+Tab{% endcapture %}{% capture contents %}
  System Settings > Desktop Behavior
  Desktop Effects Tab > Check Present Windows
  Click the Gear Icon > Change the `Ctrl+F10` shortcut to `Meta+Tab`
  Layout mode: "Natural" => "Flexible Grid"
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Change titlebar height{% endcapture %}{% capture contents %}
  System Settings > Fonts
  Window title > Edit Font Size
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Hide titlebars when maximized (like Ubuntu){% endcapture %}{% capture contents %}
  We need to set `BorderlessMaximizedWindows=true` under the group `[Windows]` in the file `~/.config/kwinrc`, then reload kwin.
  It's easier to use these commmands than doing it by hand.
  {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group Windows --key BorderlessMaximizedWindows true
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Launch app with discrete GPU{% endcapture %}{% capture contents %}
  Also known as using `prime-run` ([PRIME wiki](https://wiki.archlinux.org/index.php/PRIME)) or using the `DRI_PRIME=1` environment variable.
  Open Application Launcher > Right Click app
  Application Tab > Advanced Options
  Discrete GPU > Check: Run using dedicated graphics card
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### Windows/Meta Key

<ul>
{% capture label %}Open “Start Menu” with Windows/Meta key{% endcapture %}{% capture contents %}
  Feature has been added by default since Plasma 5.8.
  If it's not working, make sure your Application Launcher ("Start Menu") widget has a global shortcut like `Alt+F1` set (you can't assign it directly to `Meta`, but it will open with `Meta` if another shortcut is assigned).
  Right Click the KDE Icon > Configure Application Launcher
  Keyboard Shortcuts Tab > Shortcut: `Alt+F1`
  * Latte Dock
    If you're using Latte Dock, you will need to run the following commands [mentioned in it's Wiki](https://github.com/psifidotos/Latte-Dock/wiki/F.A.Q.#q-can-i-use-my-super-key-to-open-the-app-l).
    {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.lattedock,/Latte,org.kde.LatteDock,activateLauncherMenu"
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}
  If you wish to revert what the Meta key opens because you changed it to open KRunner or a Latte Dock widget, run the following:
  {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.plasmashell,/PlasmaShell,org.kde.PlasmaShell,activateLauncherMenu"
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Do not open the "Start Menu" with Windows/Meta key{% endcapture %}{% capture contents %}
  We need to set `Meta=` under the group `[ModifierOnlyShortcuts]` in the file `~/.config/kwinrc`, then reload kwin.
  It's easier to use these commands than doing it by hand.
  {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta ""
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Open KRunner with Windows/Meta key{% endcapture %}{% capture contents %}
  We need to set `Meta=...` under the group `[ModifierOnlyShortcuts]` in the file `~/.config/kwinrc`, then reload kwin.
  It's easier to use these commands than doing it by hand.
  **Plasma 5.18 and above:**
  {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/krunner_desktop,org.kde.kglobalaccel.Component,invokeShortcut,_launch"
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}
  **Plasma 5.17 and below:**
  {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/krunner,org.kde.kglobalaccel.Component,invokeShortcut,run command"
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Open Overview with Windows/Meta key{% endcapture %}{% capture contents %}
  Overview was formerly called "Present Windows" before Plasma 5.23.
  We need to set `Meta=...` under the group `[ModifierOnlyShortcuts]` in the file `~/.config/kwinrc`, then reload kwin.
  It's easier to use these commands than doing it by hand.
  {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/kwin,org.kde.kglobalaccel.Component,invokeShortcut,Expose"
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Open Keyboard Shortcut with Windows/Meta key{% endcapture %}{% capture contents %}
  To run any keyboard shortcut with the Meta key, first open Konsole and run the following commands.
  {% highlight bash %}
qdbus # List all DBus services
qdbus org.kde.kglobalaccel # List all shortcut groups/components
qdbus org.kde.kglobalaccel /component/kwin # List commands
qdbus org.kde.kglobalaccel /component/kwin shortcutNames | sort # List shortcut ids
{% endhighlight %}

  There are other shortcut groups (components) besides `/component/kwin` if you wish to use them. Once you find the "internal shortcut id" of the command you wish to activate, test the following command.

  {% highlight bash %}
qdbus org.kde.kglobalaccel /component/kwin invokeShortcut "Show Desktop"
{% endhighlight %}

  After you figure out the dbus command needed, we need to set `Meta=...` under the group `[ModifierOnlyShortcuts]` in the file `~/.config/kwinrc`, then reload kwin.
  It's easier to use these commands than doing it by hand.
  {% highlight bash %}
kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta "org.kde.kglobalaccel,/component/kwin,org.kde.kglobalaccel.Component,invokeShortcut,Show Desktop"
qdbus org.kde.KWin /KWin reconfigure
{% endhighlight %}
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### Login Screen (SDDM) / Lock Screen

<ul>
{% capture label %}Change Login Screen Wallpaper{% endcapture %}{% capture contents %}
  System Settings > Startup and Shutdown
  Login Screen (SDDM) Tab > Background > Load From File
  We should also change the lock screen.
  System Settings > Desktop Bahaviour
  Screen Locking Tab > Wallpaper > Wallpaper Type: Image
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Auto-Login{% endcapture %}{% capture contents %}
  Note: KDE Wallet will prompt you for your password to get the WiFi password after auto-login.
  System Settings > Startup and Shutdown > Login Screen (SDDM)
  Behavior button > Check: Automatically login as user
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### Dolphin (File Manager)

<ul>
{% capture label %}Double Click to open files{% endcapture %}{% capture contents %}
  * Plasma 5.13
    System Settings > Desktop Behavior > Workspace
    Click Behavior: Double Click to open files and folders
  * <= Plasma 5.12
    System Settings > Input Devices
    Mouse Tab > Icons: Double Click to open files and folders
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Always Show Hidden Files{% endcapture %}{% capture contents %}
  ☰ Control > Adjust View Properties
  Check: Show hidden files
  Apply view properties to: All Folders
  Check: Use these view properties as default
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Browse (.zip / .tar.gz / .rar) with Dolphin{% endcapture %}{% capture contents %}
  ☰ Control > Configure Dolphin
  Navigation Tab > Check: Open archives as folder
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Clean up Context Menu (Right Click Menu){% endcapture %}{% capture contents %}
  ☰ Control > Configure Dolphin
  Services Tab > Uncheck: “Copy To”, “Delete”, “File to activity”, “Send as Email”, “Send to IM”, “Send via Bluetooth”, “Send via KDE Connect”
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Show Terminal Panel{% endcapture %}{% capture contents %}
  ☰ Control > Panels > Terminal (F4)
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Paste into Terminal Panel{% endcapture %}{% capture contents %}
  ☰ Control > Configure Shortcuts
  Paste > Set Alternative (Defaulted to Shift+Insert) as “None”
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable File Indexing (Baloo){% endcapture %}{% capture contents %}
  Some user may want to disable the indexing when:

  * [For some users](https://www.reddit.com/r/kde/search?q=baloo&restrict_sr=on), the `baloo_file` process can slow down the system.
  * The `~/.local/share/baloo/index` can use over a Gigabyte of space.  
    Run `balooctl indexSize` to break the database usage down.

  System Settings > Search
  Uncheck: Enable File Search
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Remove Filmstrip From Video Thumbnails{% endcapture %}{% capture contents %}
  ☰ Control > Configure Dolphin
  General Tab > Previews > Video Files (ffmpegthumbs) > Configure Button
  Uncheck: Embed filmstrip effect
  Note: Since Dolphin 21.12, The GUI toggle was removed. You will need to create and edit `~/.config/ffmpegthumbsrc` to disable the filmstrips. It's easier to run this command:
  {% highlight bash %}
kwriteconfig5 --file ~/.config/ffmpegthumbsrc --group General --key filmstrip false
  {% endhighlight %}
  Finally you will need to delete the `~/.cache/thumbnails/` folder to regenerate the thumbnails.
  {% highlight bash %}
  rm -r ~/.cache/thumbnails/
  {% endhighlight %}
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### Spectacle (Screenshots)

<ul>
{% capture label %}Show Magnifier{% endcapture %}{% capture contents %}
  Configure > General
  Rectangular Region > Check: Show magnifier
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### LibreOffice Writer

<ul>
{% capture label %}Save as .docx by default{% endcapture %}{% capture contents %}
  Tools > Options
  Load/Save > General
  Always save as: "Word 2007-2019 (*.docx)"
  > [LibreOffice wiki](https://help.libreoffice.org/Common/Using_Microsoft_Office_and#Saving_Documents_by_Default_in_Microsoft_Office_Formats)
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### LibreOffice Calc

<ul>
{% capture label %}Set Default Font Size/Family/CellPadding{% endcapture %}{% capture contents %}
  Styles > Manage Styles
  Right click Default > Modify
  Font > Family: Noto Sans (KDE default) might look different for Window users.
  Font > Family: Manually type "Calibri" (Office default) which will map to the free "Carlito" font.
  Font > Size: 12 (Office uses 11)
  Borders > Padding: 2.0 pt
  Ok
  Make sure "Bad", "Good", etc under "Status" also use the correct font.
  File > Templates > Save As Template
  Name: Default
  Category: My Templates
  Check "Set as default template"
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### Steam

<ul>
{% capture label %}Hide “Big Picture”, etc in the System Tray Context Menu{% endcapture %}{% capture contents %}
  Steam > Settings > Interface Tab
  Set Taskbar Preferences > Only Check: Library, Friends, Exit Steam
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Cleanup Friends List{% endcapture %}{% capture contents %}
  Steam > Friends > View Friends List
  Click on the Cog / Settings Icon
  Ignore 'Away' status when sorting friends: On
  Compact Favorites Area: On
  Compact Friends List: On
  Append nickname to friend's name: On
  Hide offline friends in custom categories: On
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Hide “Friend is playing ____” Notifications{% endcapture %}{% capture contents %}
  Steam > Friends > View Friends List
  Click on the Cog / Settings Icon
  Notifications > Uncheck: When friend joins a game
  Notifications > Uncheck: When comes online
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Never Show Advertisement Popups{% endcapture %}{% capture contents %}
  Steam > Settings > Interface Tab
  Uncheck: Notify me about additions to my games and other releases
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Startup in Tray{% endcapture %}{% capture contents %}
  Find Steam in the App Launcher widget
  Right Click Steam > Edit Application
  Application Tab > Command: `/usr/bin/steam -silent %U`
  If you added Steam to the autostarted apps, you will need to edit the command there as well.
  Relevant [bug report](https://github.com/ValveSoftware/steam-for-linux/issues/5806).
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Close Steam to Tray{% endcapture %}{% capture contents %}
  We need to launch steam using `STEAM_FRAME_FORCE_CLOSE=1 steam` as mentioned in [this bug report](https://github.com/ValveSoftware/steam-for-linux/issues/5806), but editing every single game shortcut that Steam generates is a hassle. So we'll set a [session environment variable](https://userbase.kde.org/Session_Environment_Variables/en) by adding `export STEAM_FRAME_FORCE_CLOSE=1` to `~/.config/plasma-workspace/env/path.sh`. It's easier to run this commands:
  {% highlight bash %}echo 'export STEAM_FRAME_FORCE_CLOSE=1' >> ~/.config/plasma-workspace/env/path.sh{% endhighlight %}
  Then logout and back in so that your "panel" is launched with the session variable so that it can pass it to Steam when Steam is launched from the app launcher or desktop shortcut.
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### Clementine

<ul>
{% capture label %}Clean up UI{% endcapture %}{% capture contents %}
  Tools > Preferences
  Playback Tab > Uncheck: Show a glowing animation on the current track
  Search Tab > Uncheck: DigitallyImported, DropBox, Google Drive, Jazz
  Last.fm Tab > Uncheck: Show the “love” amd “ban” buttons
  Last.fm Tab > Uncheck: Show the scrobble button
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Don’t fade between songs{% endcapture %}{% capture contents %}
  Playback Tab > Uncheck: Fade out when stopping a track
  Playback Tab > Uncheck: Cross-fade when changing tracks manually
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Double Click song should play song now{% endcapture %}{% capture contents %}
  Behaviour > Using the menu to add a song will: Always start playing
  Behaviour > Double clicking a song will: Replace the playlist + Always start playing
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### Gtk Apps (Gimp/Hexchat/etc)

<ul>
{% capture label %}Fix white text on white background tooltips{% endcapture %}{% capture contents %}
  System Settings > Colors
  Uncheck: Apply colors to non-Qt applications
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>

### VirtualBox

<ul>
{% capture label %}Prevent Windows/Meta Key from opening the host App Menu{% endcapture %}{% capture contents %}
  Run the Virtual Machine.
  Press the host key (Right `Ctrl`)
  Press `Alt+F3` > More Actions > Special Application Settings
  Window Matching Tab > Window class: [`Exact Match`] `virtualbox machine`
  Appearances & Fixes Tab > Check "Ignore Global Shortcuts"
  Change "Do Not Affect" to "Force", then select "Yes".
  > Note that this also disables Spectacle's screenshot global shortcuts while the VM window is focused.
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>


### Chrome

<ul>
{% capture label %}Overlay tabs on top of the title bar{% endcapture %}{% capture contents %}
  `⋮` Button > Settings
  Appearance > Uncheck: Use system title bar and borders
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Match Titlebar with Desktop Theme{% endcapture %}{% capture contents %}
  Breeze
  Breeze Dark: [Chrome Theme](https://chrome.google.com/webstore/detail/breeze-dark/nkhdomjgcjkhipblklfchdkojecapgmc)
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Enable Hardware Acceleration in Chrome{% endcapture %}{% capture contents %}
  If you notice tearing while playing video, check `chrome://gpu` and see if it says hardware acceleration is unavailable. It's very likely that it's just that chrome doesn't recognize that it can use your GPU.
  > [Original Article](http://www.webupd8.org/2014/01/enable-hardware-acceleration-in-chrome.html)
  Go to `chrome://flags#ignore-gpu-blacklist`, search for "Override software rendering list", enable it and restart Chrome.
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Don't use native Linux notifications{% endcapture %}{% capture contents %}
  Since Chrome v64, Chrome now uses native notifications. If you prefer Chrome's however, you can still use them.
  Go to `chrome://flags#enable-native-notifications`, search for "Enable native notifications", disable it and restart Chrome.
{% endcapture%}{% include tip.html label=label contents=contents %}
</ul>


### Firefox

<ul>

{% capture label %}Use the KDE File selector dialog{% endcapture %}{% capture contents %}
  Make sure you have the `xdg-desktop-portal` and `xdg-desktop-portal-kde` package installed.
  In newer versions of Firefox, you can go to `about:config` and set `widget.use-xdg-desktop-portal` to `true`. 
  Press `Ctrl+Esc` and search to make sure the `xdg-desktop-portal-gtk` process is not running. If it is, end all `xdg-` processes.
  Note: [Older Firefox versions needed](https://askubuntu.com/questions/1100261/how-do-i-make-firefox-64-use-the-kde-file-selection-dialog) the `GTK_USE_PORTAL=1` environment variable set in the Firefox launcher.
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Install privacy addons{% endcapture %}{% capture contents %}
  * [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)
  * [Privacy Badger](https://addons.mozilla.org/en-US/firefox/addon/privacy-badger17/)
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Enable Middle Click AutoScroll{% endcapture %}{% capture contents %}
  ☰ > Preferences > General
  Browsing > Check: Use autoscrolling
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Open New Tab page on startup{% endcapture %}{% capture contents %}
  ☰ > Preferences > Home
  Homepage and new windows: `Firefox Home`
  OR `Custom Url` with `about:newtab`
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Leaner New Tab page{% endcapture %}{% capture contents %}
  ☰ > Preferences > Home
  Uncheck: "Web Search"
  Uncheck: "Recommended by Pocket"
  Uncheck: "Highlights"
  Under "Top Sites" change to "4 rows"
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Leaner toolbar area{% endcapture %}{% capture contents %}
  ☰ > Customize
  Density > Compact
  Drag the Home button from the toolbar into the main area.
  Drag the rectangle spacers to remove them as well.
  Right click the uBlock Origin icon > "Pin to Overflow Menu"
  Right click the "Save to Pocket" icon > "Remove from Address Bar"
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Place close button next to tabs / don't use KDE's titlebar.{% endcapture %}{% capture contents %}
  ☰ > Customize
  Uncheck: "Title Bar"
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable Pocket{% endcapture %}{% capture contents %}
  Go to `about:config`
  Search for `extensions.pocket.enabled` and set it to `false`
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Enable Hardware Acceleration in Firefox{% endcapture %}{% capture contents %}
  If you notice tearing while playing video, check `about:support` and `Ctrl+F` to search for `HW_COMPOSITING`. If it says "blocked by env: Acceleration blocked by platform" then it is not using Hardware Acceleration by default.
  We need to go to `about:config` then set `layers.acceleration.force-enabled` to `true`.
  Restart firefox, and it should now say "force_enabled by user: Force-enabled by pref" under `HW_COMPOSITING` in `about:support`.

  -----

  Firefox is also [working on WebRender](https://wiki.mozilla.org/Platform/GFX/WebRender_Where#Linux), which is "[a GPU based 2D rendering engine for the web written in Rust](https://mozillagfx.wordpress.com/2020/04/30/moz-gfx-newsletter-52/)". You can try enabling it by going to `about:config` and setting `gfx.webrender.all` to `true`. Restart firefox, then go to `about:support` and `Ctrl+F` for `WEBRENDER` to make sure it's enabled.
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Hide Search Dropdown Footer{% endcapture %}{% capture contents %}
  ☰ > Preferences > Search 
  Search Shortcuts: Uncheck All
  Note: Keywords will still work.
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Disable `Ctrl+Tab`'s recently used order{% endcapture %}{% capture contents %}
  Go to `about:config`
  Search for `browser.ctrlTab.recentlyUsedOrder` and set it to `false`
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Browse a website as 2nd User without logging out{% endcapture %}{% capture contents %}
  Install Mozilla's [Multi-Account Containers extension](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)
  Right click the extension's icon in the toolbar > Pin it to the overflow menu.
  You can easily open a new tab in a specific container by clicking and holding the "Open a new tab" button.
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Quickly browse subreddits using custom search engines{% endcapture %}{% capture contents %}
  Create a new Bookmark with:
  Name: `/r/`
  URL: `https://www.reddit.com/r/%S`
  Keyword: `r`
  Now you can type `r kde` to visit [/r/kde](https://www.reddit.com/r/kde)
  Note: Uppercase `%S` will not escape slashes so `r kde/new` works.
  Note: Use lowercase `%s` in searches like `https://duckduckgo.com/?q=%s`
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}First click UrlBar selects all + double click selects word{% endcapture %}{% capture contents %}
  Go to `about:config`
  Search for `browser.urlbar.clickSelectsAll` and set it to `true`
  Search for `browser.urlbar.doubleClickSelectsAll` and set it to `false`
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Show bookmarks toolbar only on new tab{% endcapture %}{% capture contents %}
  Available since Firefox v85+
  Right Click Bookmarks Toolbar > Bookmarks Toolbar > Only Show on New Tab
{% endcapture%}{% include tip.html label=label contents=contents %}

</ul>



### Firefox (`userChrome.css`)

A firefox user can change the look of the browser by editing a css file.
Checkout [/r/FirefoxCSS/](https://www.reddit.com/r/FirefoxCSS/) for help.

<ol>
<li>In FireFox v69 and later, we need to go to <code>about:config</code> and change <code>toolkit.legacyUserProfileCustomizations.stylesheets</code> to <code>true</code>.</li>
<li>Then navigate to <code>~/.mozilla/firefox/</code>, inside will be a randomly generated folder similar to <code>abcdef12.default</code> which you should enter.</li>
<li>Inside the "default" folder, create a new folder called <code>chrome</code>, then create a file called <code>userChrome.css</code>.</li>
<li>You can now edit <code>~/.mozilla/firefox/abcdef12.default/chrome/userChrome.css</code>, and changes will be applied upon restarting Firefox.</li>
</ol>

<ul>

{% capture label %}Remove left tabbar padding when not maximized{% endcapture %}{% capture contents %}
  Then paste the following CSS into `userChrome.css` ([instructions](#firefox-userchromecss)) and restart firefox.
  {% highlight css %}
.titlebar-placeholder[type="pre-tabs"] { display: none; } /* Firefox 64 */
.titlebar-spacer[type="pre-tabs"] { width: 0 !important; } /* Firefox 65+ */
{% endhighlight %}
{% endcapture%}{% include tip.html label=label contents=contents %}

{% capture label %}Cleanup right click menu (aka contextmenu){% endcapture %}{% capture contents %}
  Click on µBlock > Click Settings Icon to open the dashboard
  Uncheck: Make use of context menu where appropriate
  To hide Firefox's default menu items, this [mozilla forum thread](https://support.mozilla.org/en-US/questions/1177488) mentions we need to edit `userChrome.css`. So paste the following CSS into `userChrome.css` ([instructions](#firefox-userchromecss)) and restart firefox.
  {% highlight css %}
#contentAreaContextMenu #context-openlinkincurrent,
#contentAreaContextMenu #context-openlinkinusercontext-menu,
#contentAreaContextMenu #context-bookmarklink,
#contentAreaContextMenu #context-selectall,
#contentAreaContextMenu #context-sendlinktodevice,
#contentAreaContextMenu #context-sendpagetodevice,
#contentAreaContextMenu #context-sep-sendlinktodevice,
#contentAreaContextMenu #context-sep-sendpagetodevice,
#contentAreaContextMenu #context-viewpartialsource-selection {
  display: none !important;
}
{% endhighlight %}
  If you're not a web developer, you can hide "Take a screenshot" by going to `about:config`
  Search for `extensions.screenshots.disabled` and set it to `true`
{% endcapture%}{% include tip.html label=label contents=contents %}

</ul>


