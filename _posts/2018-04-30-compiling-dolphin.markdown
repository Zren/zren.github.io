---
layout: post
title: Compiling Dolphin
last_modified_at: 2021-01-05
---

First install the build dependencies with `apt-get build-dep`.

{% highlight bash %}
sudo apt-get build-dep dolphin
{% endhighlight %}

If you haven't already, install git.

{% highlight bash %}
sudo apt install git
{% endhighlight %}

Download the repo.

{% highlight bash %}
git clone https://github.com/KDE/dolphin.git
cd dolphin
{% endhighlight %}

Create a build directory, then run `cmake` then `make`. After it finishes compiling, make the dolphin binary executable.

{% highlight bash %}
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
make
chmod +x ./bin/dolphin
{% endhighlight %}

You can test if everything went well by running:

{% highlight bash %}
./bin/dolphin
{% endhighlight %}

If it ran okay you can copy the binary to /usr/local/bin.

{% highlight bash %}
sudo cp ./bin/dolphin /usr/local/bin/dolphin
{% endhighlight %}

Update: I made a video walkthrough for compiling dolphin.

{% include video.html youtubeId="hRz1r_db7hw" %}
