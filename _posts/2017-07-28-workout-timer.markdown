---
layout: post
title: Workout Timer
---

![](https://i.imgur.com/2jaqB9Z.png)
![](https://i.imgur.com/fzcY4Tm.png)


Recently I've wanted to make a workout fitness timer. I've already worked on a fancy circle progressbar when working on a battery percent indicator, so I reused that in a system tray plasmoid I've been mocking up.

{% include streamable.html streamableId="a1urw" %}

I decided to try copying the look of the [Sworkit](https://play.google.com/store/apps/details?id=sworkitapp.sworkit.com&hl=en) android app since it seemed simple to replicate the core bits.

After a bit of refactoring of my timer plasmoid to support two different timer "states" (get ready + being) and go from one exercise to another. I set out to perfect JSON serialization since I needed and array of array data type. Instead of encoding it with base64 after stringifying it this time, I left it as raw JSON string so it would be easy to set a default workout in the `config/main.xml`.

For a programmer, the hard part would be the assets. The voice that calls out the next exercise would be easy to record myself, but would be pretty bad quality. It would also create a "huge" download. Megabytes in size!

So I looked into synthetic voices via the command line. Google => [StackOverflow showed](https://askubuntu.com/questions/501910/how-to-text-to-speech-output-using-command-line) that there was 4 different commands. I tried out `spd-say` (`apt install speach-dispacher`) but it would create 4 different entries in the volume mixer. I'd need to call `spd-say -S` after the sound completes, but I decided to check out the rest since the voice was... robotic.

Ubuntu shipped with `say` (`apt install gnustep-gui-runtime`) in 14.04, but it's also a robotic voice (with even less options than `spd-say`).

I also checked out if kde had any but they were either old or too new. Mycroft, the new "cortona" like project has a subproject called [mimic](https://mimic.mycroft.ai/home/usage) but it's probably harder for a user to install since it's not packaged yet.

I ended up using `pip install gTTS` which will download an MP3 from google translator's "voice". I could package the MP3s in the plasmoid. The problem would be licensing. [It seems](https://gamedev.stackexchange.com/questions/22336/can-google-translates-audio-files-be-used-in-a-game) their translation API costs [$20 per million characters](https://cloud.google.com/translate/pricing?csw=1), which works out to 1 cent per 500 letters. Seeing as I'd translate maybe ~20 phrases or so, I'd probably use up a cent or two if I used the API instead. The gTTS python script doesn't use it though.

That still didn't answer the issue of licensing though, so I'll only use them as placeholders for now.

As for the images, a simple google for "exercise filetype:svg" pointed me to a [wikipedia submiter](https://en.wikipedia.org/wiki/File:Push_up_feet_elevated_2_1.svg) who's put [a number of simple images](http://db.everkinetic.com/) under Creative Commons (BA-SA).

He only uploaded the rasterized PNGs of his images though. We can't use PNGs since we need the images to follow the color scheme. We could get away with two outlines in black + white, but we can easily convert those monochromatic PNGs into SVGs with modern day tools.

Google found [this Gist]( https://gist.github.com/ykarikos/2892009) which uses `potrace` and `imagemagick`.

After we convert it we need to add the stylesheet and add `class="ColorScheme-Text" style="fill:currentColor"` to all the svg paths. [I wrote a script](https://gist.github.com/Zren/4b912662281366e66acdb6200bbfe323) in the past to do this programatically in python for icons. A few little changes and it was good to go.

Lastly I wanted to crop the svgs to get rid of some of the whitespace. Inkscape doesn't have a pure command line way to do this, but we can use the command line to automate GUI actions.

{% highlight bash %}
inkscape --verb=FitCanvasToSelectionOrDrawing  --verb=FileSave --verb=FileQuit "file.svg"
{% endhighlight %}

There was a little bit of a conflict with my colorscheme script and this command though. I ended up needing to run them in a specific order, otherwise I'd get a huge chunk of whitespace in the bottom and right.

{% highlight bash %}
./colorschemesvg "file.svg"
inkscape --verb=FitCanvasToSelectionOrDrawing --verb=FileSave --verb=FileQuit "file.svg"
./colorschemesvg "file.svg"
{% endhighlight %}



Next I worked on the configuration interface. It still needs a drag to move but it's functional. Still debating how to layout the 2nd workout.

![](https://i.imgur.com/GnwySNO.png)
