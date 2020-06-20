---
title: QML Connections "onFoo warnings" will get logging category in Qt 5.15.1
layout: post
---

Qt 5.15 has a new deprecation warning:

> `file:///.../ToolButtonStyle.qml:209:13`:
> QML Connections:
> Implicitly defined `onFoo` properties in `Connections` are deprecated.
> Use this syntax instead: `function onFoo(<arguments>) { ... }`

This warning shows up 20-50 times when testing a widget. It's rather annoying, as it drowns out the useful warnings.

According to [the commit that added the warning](https://github.com/qt/qtdeclarative/commit/efe0bec9468d75b768d1e26d2a8b440ade5ba632), the syntax change is to remove some "magic" that figured out which variables are the signal parameters. It is being done for the ability to compile this type of QML code into C++, which is a good reason despite the headache.

So why can't we just implement the new `function onFoo() {}` format in `Connections`? Well it [is not supported in Qt 5.12](https://github.com/qt/qtdeclarative/commit/a2eef6b511988b2435c4e39b6b5551e857ce7775).

Distros using Qt 5.12

* <https://repology.org/project/qt/versions>
* Ubuntu 20.04
* openSUSE Leap 15.2
* Debian Unstable + Testing
* Debian Stable (Qt 5.11)

I can't drop support for most LTS distros. Hell Ubuntu 20.04 is only a few months old.

The only way I've found to hide these warnings, is to use the logging rule `QT_LOGGING_RULES="*.warning=false"`. That hides **all** warnings however, including the useful ones.

Fortunately David Edmundson [sent a patch](https://codereview.qt-project.org/c/qt/qtdeclarative/+/293011) to add a new logging category. The category will be `qt.qml.connections`. So I imagine I'll need to use `QT_LOGGING_RULES="qt.qml.connections.warning=false"` to hide those warnings.

Unfortunately, I'll be stuck living with these spam-like warnings until Qt 5.15.1, which is [scheduled to be released](https://wiki.qt.io/Qt_5.15_Release) in August 2020.

More discussion can be found [on StackOverflow](https://stackoverflow.com/questions/62297192/qml-connections-implicitly-defined-onfoo-properties-in-connections-are-deprecat).
