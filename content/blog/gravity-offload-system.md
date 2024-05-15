+++
title = "Gravity Offload System"
author = ["Fletcher Porter"]
date = 2020-03-16T00:00:00+02:00
tags = ["mechanical", "electrical", "control", "nasa", "jpl", "robosimian"]
draft = false
+++

In 2018 I did an internship at NASA Jet Propulsion Laboratory where I worked on a gravity-offload system to test mobility for a future rover mission to Saturn's moon Enceladus.

Prior to my arrival, there was already an offload system that consisted of a couple constant force springs hanging from a gantry on the ceiling of a shipping container. These springs connected to a robot that would drive on Enceladus-analogue dust. The gantry got pulled along the test chamber by the robot [RoboSimian](https://www.jpl.nasa.gov/robotics-at-jpl/robosimian), but this was problematic because friction in the gantry led to non-vertical forces on the robot, which isn't physical. My task was to add an active system to eliminate this friction.

{{< figure src="/ox-hugo/ContainerTopLevel.png" caption="<span class=\"figure-number\">Figure 1: </span>The testbed was an inclined sandbox inside a shipping container with the gantry welded to the ceiling." >}}

To do that, I made a robot that attached to the gantry and pulled on a chain to propell the system along the chamber. The system had a camera on it that was used to detect the position of the robot and regulate the relative position of the offload system so the robot was always in the center of the frame.

{{< figure src="/ox-hugo/FullAssy_Iso1_transBackgroundWithIBeam.png" caption="<span class=\"figure-number\">Figure 2: </span>The robot bolted on to two gantry carriages and pulled itself along with a chain and sprocket." >}}

Ultimately, the system was very successful. Almost all non-vertical forces were removed by the system, and the system has been able to date for a year and a half with only minimal maintenance according to the team.

{{< figure src="/ox-hugo/GOS_bottomIso.jpg" caption="<span class=\"figure-number\">Figure 3: </span>On the right is the camera that detects RoboSimians position which is fed back into the controller.  Also visible are supporting electronic and the mechanical system in the back." >}}
