---
layout: docpage
title: Plasma API Docs (Unofficial)
permalink: /kde/docs/
---

<!-- ------- -->
{% include docHeader.html label="Setup" %}

{% capture label %}Folder Structure{% endcapture %}
{% capture sectionLeft %}

{% endcapture %}{% capture sectionRight %}

* `testapplet/`
    * `package/`
        * `contents/`
            * `config/`
                * `config.qml`
                * `main.xml`
            * `ui/`
                * `configGeneral.qml`
                * `main.qml`
        * `metadata.desktop`

<style>
section#folder-structure .right ul {
    border-left: 2px solid #bfcdd8;
    margin-left: 16px;
}
section#folder-structure .right li {
    position: relative;
    list-style-type: none;
    padding-left: 8px;
}
section#folder-structure .right li:before {
    position: absolute;
    left: -8px;
    content: "├";
    margin-right: 0;
}
section#folder-structure .right li:last-child:before {
    content: "└";
}
</style>

{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}metadata.desktop{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}contents/ui/main.qml{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


<!-- ------- -->
{% include docHeader.html label="Qml" %}


{% capture label %}Rectangle{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}RowLayout{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}PlasmaCore.Label{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


<!-- ------- -->
{% include docHeader.html label="Configuration" %}


{% capture label %}contents/config/mail.xml{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}


{% capture label %}contents/config/config.qml{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}

{% capture label %}contents/ui/configGeneral.qml{% endcapture %}
{% capture sectionLeft %}
...
{% endcapture %}{% capture sectionRight %}
...
{% endcapture %}{% include docSection.html label=label sectionLeft=sectionLeft sectionRight=sectionRight %}
