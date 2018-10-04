---
title: Simpler kdesrc-build Script
layout: post
---

Using `kdesrc-build` to compile kde repositories is quite verbose, and by default will build all dependencies which can take ages. So I wrote a script to quickly build a single repo and install it.

Use this after you run a full `kdesrc-build` and build all the dependencies.

{% highlight bash %}
#!/bin/bash

# To Install:
# sudoedit /usr/local/bin/ksrcbuild
# sudo chmod +x /usr/local/bin/ksrcbuild

moduleId="$!"
shift
extraArgs="$@"

if [ -z "$moduleId" ]; then
	echo "A [moduleId] is required."
	echo "    Eg: ksrcbuild [moduleId]"
	echo "To build everything use kdesrc-build."
	echo ""
	exit 1
fi

if [ -z "$extraArgs" ]; then
	# Don't pull updates by default
	# since we probably modified the code.
	extraArgs="--no-src"
fi

kdesrc-build $moduleId --resume-from=$moduleId $extraArgs
{% endhighlight %}

