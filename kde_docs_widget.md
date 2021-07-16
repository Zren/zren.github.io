---
layout: docpage
title: Plasma Widget Tutorial
permalink: /kde/docs/widget/
---

This tutorial has been [upstreamed to the KDE Documentation](https://develop.kde.org/docs/plasma/widget/) with improvements like using the newer `PlasmaComponents 3.0` and `QtQuick.Controls 2.0` in your widget. This older tutorial still uses `PlasmaComponents 2.0` and `QQC 1.0`.

<!-- ------- -->
{% include_relative kde_docs/widget-DefaultWidgets.md %}
{% include_relative kde_docs/widget-Setup.md %}
{% include_relative kde_docs/widget-Testing.md %}
{% include_relative kde_docs/widget-Qml.md %}
{% include_relative kde_docs/widget-PlasmaQmlApi.md %}
{% include_relative kde_docs/widget-Configuration.md %}
{% include_relative kde_docs/widget-TranslationsI18n.md %}
{% include_relative kde_docs/widget-Examples.md %}
{% include_relative kde_docs/widget-Examples-BundleIcon.md %}

{% if false %}
{% capture label %}...{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}
{% endif %}

<!-- ------- -->
<script type="text/javascript" src="/js/livereload.js"></script>
