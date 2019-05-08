---
layout: docpage
title: Plasma Widget Tutorial
permalink: /kde/docs/widget/
---

The KDE wiki has a [Getting Started and Hello World](https://techbase.kde.org/Development/Tutorials/Plasma5) tutorial which you can read as well.

<style>
/* Directory List */
ul.directory-tree,
ul.directory-tree ul {
    border-left: 2px solid #bfcdd8;
    margin-left: 16px;
}
ul.directory-tree li {
    position: relative;
    list-style-type: none;
    padding-left: 8px;
}
ul.directory-tree li:before {
    position: absolute;
    left: -8px;
    content: "├";
    margin-right: 0;
}
ul.directory-tree li:last-child:before {
    content: "└";
}
/* Bootstrap Alerts */
.alert {
    position: relative;
    padding: .75rem 1.25rem;
    margin-bottom: 1rem;
    border: 1px solid transparent;
    border-radius: .25rem;
}
.alert-primary {
    color: #004085;
    background-color: #cce5ff;
    border-color: #b8daff;
}
.alert-secondary {
    color: #383d41;
    background-color: #e2e3e5;
    border-color: #d6d8db;
}
</style>

<!-- ------- -->
{% include_relative kde_docs/widget-DefaultWidgets.md %}
{% include_relative kde_docs/widget-Setup.md %}
{% include_relative kde_docs/widget-Testing.md %}
{% include_relative kde_docs/widget-Qml.md %}
{% include_relative kde_docs/widget-PlasmaQmlApi.md %}
{% include_relative kde_docs/widget-Configuration.md %}
{% include_relative kde_docs/widget-TranslationsI18n.md %}
{% include_relative kde_docs/widget-Examples.md %}

<!-- ------- -->
<script type="text/javascript" src="/js/livereload.js"></script>
