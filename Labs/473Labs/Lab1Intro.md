---
layout: page
permalink: /473Labs/Lab1Intro/
title: Comparative Biomechanics Lab 1 – Intro to video analysis
math: katex
---

## Activity 1
In this lab, you will learn how to use video analysis software to analyze motion. Break into 4 groups and spread out. 
+ Each group will be assigned a computer.
+ On that computer, on the desktop, find the `Lab 1` folder. In that folder you will find a video.
+ The videos will be up to several minutes long. Play the video and watch the motion. You will see animals flying, walking, or swimming, depending on the video assigned to your group.
+ On the first viewing, observe the animals. What do you notice about their motion? How do they move? What parts of their body are moving? How fast are they moving?
    + **IMPORTANT**: Try to answer the question **What can you measure from this video?** What aspects of the motion can you quantify? What units do you have? What variables can you define if you had this video and measurement tools?
+ Work as a group to discuss and note your answers to those questions. You will share your answers with the class.

## Activity 2
Now that you have observed the motion, you will learn how to use video analysis software to measure the motion. 
+ Hit `ctrl-R`, type `cmd`, and hit `enter`. That will open the command line.
+ Type `source argus_env\Scripts\activate` and `enter`
+ Then type `argus-gui` and hit enter. This will open the Argus application (be patient with it opening). Note that you can read the full user manual for Argus at [https://github.com/backyardbiomech/argus_gui/blob/main/docs/user-guide.md](https://github.com/backyardbiomech/argus_gui/blob/main/docs/user-guide.md). You might want to open that in a tab in your browser for reference, but the instructions below should get you started.
+ The first tab in the Argus window is the `Clicker` tab. Click the `+` button to add a new video. Navigate to the `Lab 1` folder on the desktop and select the video file you watched earlier.
+ Click on `Go`. That will open the video in a new window. Don't click it more than once! Be patient as it opens the video.
+ In this window, rather than playing the video, you can click on the video to mark points. Starting off, you can mark one point per frame by clicking on it, which will then also advance a frame. You can then click again to mark the same object in the that frame, and so on. 
+ You can go back a frame with the `b` key. If that frame is already marked, then you can move the mark by just clicking where you want the mark. 
+ You can advance by 50 frames with `shift-F` and go back by 50 frames with `shift-B`.
+ You can zoom in on an area by hovering the mouse over that area and using hitting the `+` key. You can zoom out with the `-` key. You can pan the zoomed video by holding `shift` and clicking and dragging the mouse.
+ Advance to a segment of the video where something interesting is happening that you want to try to measure. Before clicking, discuss what you want to measure. What point on the animal do you want to track? What variable are you trying to measure? How will you define that variable?
+ Once you have a plan, start clicking to mark the point you want to track. Try to mark at least 30 frames. Make a note of the starting and ending frame numbers (visible in the top bar of the window)
+ If you make a mistake, you can always go back to that frame and move the mark. If you want to delete a mark, you can right-click on it, or hit the `d` key.
+ Once you have marked at least 30 frames, hit the `s` key. That will prompt you to select a location to save the data. Save it in the `Lab 1` folder on the desktop, and give it a name like `shark1.csv`. Hit ok.
+ Leave the video window open for now. You will need it again in a moment.
+ Go to that folder and notice that several files were created. Open the `-xypts.csv` file (so with the example name above, this would be `shark1-xypts.csv`) in Excel. 
+ What you do see? What are the columns? What are the rows? What are the unites? What do the numbers mean? Do you think you measured what you wanted to? Discuss this as a group and be prepared to share your answers with the class. 

## Activity 3
After the class discussion, close that Excel file. Go back to the video window.
+ You should now discuss as a group what to measure. This should include:
    + An anatomical length on the animal across time
    + A distance the animal travels across time
    + A speed of the animal across time
    + An angle on the animal across time
+ You can use the same point you tracked before, or you can track a different point. You can get many of the measurements above with the same points, but you will need more than one. How many will you need to get all of those measurements?
+ Do you need to find a different part of the video? What other points on the animal will you track? What variables are you trying to measure? How will you define those variables? What will the units be?
+ To add a new point, hit the `o` key which will open an options window. Click the `Add a track` button and give your new track a name. Hit ok twice. The name of the new track should be at the top of the video window now. 
+ To switch between tracks in the video window, hit the `<` and `>` keys.
+ Mark whatever you think you need to mark to get the measurements you want. Again, try to mark at least 30 frames. Make a note of the starting and ending frame numbers (visible in the top bar of the window).
+ When you are done marking, hit `ctrl-s` to save. That will ask you for a new name for the file. Save it in the `Lab 1` folder on the desktop, and give it a name like `shark2.csv`. Hit ok.
+ Go to that folder and notice that several new files were created. Open the `-xypts.csv` file (so with the example name above, this would be `shark2-xypts.csv`) in Excel.
+ How many columns do you have now, and what are they?
+ From the numbers, how can you calculate the measurements you wanted? What equations will you use? What units will you have? 
    + How do you calculate an anatomical length from those numbers? A distance moved? A speed? An angle?
    + Try to make a graph of what you have. How should you make it and what does it show?
+ Discuss this as a group and be prepared to share your answers with the class.

We will discuss this one last time as a class. These ideas will be critical for your group project later in the semester!