+++
title = "A dolly with assisted stair climbing"
author = ["Fletcher Porter"]
date = 2024-08-06T00:00:00+03:00
tags = ["mechanical", "electrical", "ucsb"]
draft = false
+++

My bachelor thesis was to design and build a dolly that could carry a heavy, sensitive payload up and down stair with minimal force necessary from the user.  The solution I and my group came up with was to build a motorized dolly.

{{< figure src="/ox-hugo/dolly.jpg" caption="<span class=\"figure-number\">Figure 1: </span>The payload is the black package.  The system was built on top of an off-the-shelf dolly." >}}

The working principle was that a flipper would push against the stairs to either pull the dolly up or resist it going down.  The control was very simple, the user commanded forward, off, or backward.

<a id="figure--fig:dolly-drivetrain"></a>

{{< figure src="/ox-hugo/dolly_drivetrain.jpg" caption="<span class=\"figure-number\">Figure 2: </span>The drivetrain was a motor that turned a perpendicular shaft.  The universal joint and bearings were to take radial loads off of the motor shaft." >}}

{{< figure src="/ox-hugo/dolly_controller.jpg" caption="<span class=\"figure-number\">Figure 3: </span>The controller was just two buttons.  The underlying computation was done by a few logic gates." >}}

The most fun part of this project was that I got to machine most of the parts my self on a manual mill and lathe.

{{< figure src="/ox-hugo/replacement_dolly_axel.png" caption="<span class=\"figure-number\">Figure 4: </span>One of the drawings for a part that I made.  You can see it in figure [2](#figure--fig:dolly-drivetrain) holding each of the wheels on." >}}
