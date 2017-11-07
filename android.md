# [Android](https://www.reddit.com/r/androiddev/comments/3ka9j0/what_to_know_for_a_mobile_developer_interview/)

![](http://i.imgur.com/2q7uebE.jpg)

> "Imagine being a phone. At launch, everyone loves you and is in line to get you. You amaze every review website or youtube channel out there. You're beautiful, sturdy, incredibly fast and affordable. People flash new roms on you on the daily. Over thirty THOUSAND people discuss you on a dedicated subreddit. There's millions of apps promoting themselves using you for their screenshots. Your owner takes you everywhere. You're with your owner through the best and worst times, always ready to rock. Your owner promotes you to their friends often. Over time, your power button starts getting funky, new phones come out and then one day, your owner is ordering a new phone through your screen. You try stopping them by randomly rebooting one more time, but this only seems to encourage the owner more. One day, you hear the doorbell. Your owner takes their new phone out of the box, with the same excitement they felt back when you were unboxed 2 years ago. They pick you up one last time to post a photo of the new phone, turn you off, take out your SIM and put you in a drawer never to be picked up again. You wonder where you went wrong. Was it the battery life? The camera? The power button? You lay there, waiting for your battery to completely run out, and when it does, you know you've had a good life." - [/u/alectprasad](https://www.reddit.com/r/Android/comments/721w8x/you_just_got_a_new_smartphone_what_is_the_first/dnfmdp4/)

## [Android Guides](https://github.com/codepath/android_guides/wiki)

1. Cyanogen was [Steve Kondik's nickname](https://github.com/cyanogen). He created CyanogenMod.
1. `adb shell dumpsys batterystats --reset` resets the battery graph.
1. The Moto E(2) is [a bitch to fix](https://www.ifixit.com/Guide/Motorola+Moto+E+2nd+Generation+Battery+Replacement/56502).
1. Not being on a stock rom while relocking your bootloader will brick the device, says [this guy](https://forum.xda-developers.com/showpost.php?p=69267541&postcount=9).
1. If your friendly local LineageOS installation complains about [having no `TERM` variable](https://jira.lineageos.org/browse/BUGBASH-556?attachmentViewMode=list), then see if adding `export TERM=xterm` to `/etc/mkshrc` helps.
1. The Pixel has [Snapdragon 821-AB](https://www.xda-developers.com/dissecting-speed-how-oneplus-leveraged-excellent-real-world-performance/), whereas the Oneplus 3T has Snapdragon 821-AC, with a slightly higher boost frequency.
1. Face Unlock is less popular in countries like Saudi Arabia and UAE.
1. Download the SDK before attempting to compile anything.
1. Android Studio 0.80 beta is, by default, [broken](http://stackoverflow.com/questions/24465289/android-studio-failure-install-failed-older-sdk).
1. Handling menu clicks is as stupid as you want it to be, but [here is a simpler one](http://stackoverflow.com/a/7480103/1558430)
1. For whatever reason, [it is impossible to set a negative value on a NumberPicker](http://stackoverflow.com/questions/20968561/android-numberpicker-negative-values). You can only subtract the value by a negative number after the fact.
1. Do know what these mean: activity/fragment lifecycles, device rotation, services, broadcasts, background tasks, asynchronous tasks, views, adapters, recyclerview, "view holder pattern"
1. Strings are put inside `project_root/app/src/main/res/values/strings.xml`, because nested folders are the best.
1. [The plus thing in the XML](http://developer.android.com/training/basics/firstapp/building-ui.html), like `android:id="@+id/edit_message"`, is required only for the line that defines it.
1. `android:hint` are placeholder texts.
1. [`layout_weight` is a relative number](http://stackoverflow.com/questions/3995825/what-does-androidlayout-weight-mean). A `layout_weight` of 1 means 100% of the width *IF* the control happens to be the only control inside a `LinearView` with the weight specified. If two controls have the weight specified (say 1, 1), then each control shares 50% of the width.
1. If `layout_weight` is given, [then](http://developer.android.com/training/basics/firstapp/building-ui.html) `layout_width` is useless (irrelevant), and should be set to 0dp or 0px.
1. The back button does ["back navigation"](http://developer.android.com/design/patterns/navigation.html) (whichever activity shown in reverse chronological order); the in-app backs do "up navigation". The term "up" refers to the hierarchical parent of the current activity, a hierarchy you declare in `AndroidManifest.xml`.
1. Putting a library into `libs/` seems to do it.
1. There are project (`./build.gradle`) and app-level (`./app/build.gradle`) gradle files. The former defines dependencies, and the latter uses them.
1. If gradle is too old, update the `classpath 'com.android.tools.build:gradle:2.1.2'`... in the gradle file. Gradle will update itself. [True fact.](http://stackoverflow.com/questions/17634708/android-studio-upgraded-from-0-1-9-to-0-2-0-causing-gradle-build-errors-now/17648742#17648742)
1. Order in the layout xml files matters.
1. The project's JDK settings is in File > Project Structure, which is not in Settings for studio.
1. If you don't know what the fresh hell you are doing, [here is a layouts cheat sheet](http://labs.udacity.com/images/Layout-Cheat-Sheet.pdf).
1. Accessing the Internet on the main thread, get this, raises the `NetworkOnMainThreadException`.
1. [AsyncTask](http://stackoverflow.com/questions/3921816/can-i-pass-different-types-of-parameters-to-an-asynctask-in-android) takes just one type of parameter, but you can use "the setter" (?) to use additional types, or simply [pass in an `Object`](http://stackoverflow.com/a/9077177) and re-cast from there.
1. ["The difference between Handler and AsyncTask is: Use AsyncTask when Caller thread is a UI Thread."](http://stackoverflow.com/a/9800870)
1. It is near impossible to [conjure a popup from a non-activity class](http://stackoverflow.com/a/31221646).
1. `(an AsyncTask).get()` [immediately gets the value from its execute()](http://stackoverflow.com/a/10972142). Then again, that is a synchronous move.
1. Activity [apparently](http://stackoverflow.com/a/9192916/1558430) extends Context.
1. Find your dependency versions on [this website](http://search.maven.org/#search%7Cga%7C1%7Cio.reactivex.rxjava). It only searches on mavenCentral, I think.
1. [Two-way binding is **not** natively supported](https://medium.com/@fabioCollini/android-data-binding-f9f9d3afc761#.pfcgcnfo5) by the designer thing, but there are lots of [one-way binding libraries](https://developer.android.com/topic/libraries/data-binding/index.html) available.
1. To use that `com.android.databinding` plugin, the layout file must have `<Layout>` as the root, not anything else, like `<LinearLayout>`.
1. [Java 8 must be explicitly enabled](http://stackoverflow.com/a/37004259/1558430)
1. The superclass of your activity has a [`setTitle()`](http://stackoverflow.com/questions/3975550/android-how-to-change-the-application-title) that does what you think it does.
1. [Loser answered the wrong base64 question](http://stackoverflow.com/a/29383697/1558430), but it works. [This should work.](http://stackoverflow.com/a/15683305/1558430)
1. Two apps signed with the same key can [securely share code and data](https://developer.android.com/studio/publish/app-signing.html#considerations).
1. adbd cannot run as root in production builds.
1. Daydream is triggered only if the device is allowed to sleep from screen timeout while charging. Pressing the power button at any time will cancel the timeout.
1. In some cases, [`onDestroy` is never called when an activity is destroyed.](https://academy.realm.io/posts/sf-fabien-davos-modern-android-ditching-activities-fragments/)
1. Sometimes you might want to check if you can run code based on the SDK version with which your app is built (like `Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR2`). Actually, I don't think you'll ever need to do that.
1. [try-with-resources is only supported if your minSdkVersion is set to 19 or higher.](https://stackoverflow.com/a/24290875/1558430) It looks like `try (foo = new SomeResourceLikeAFile()) { foo... }`. Multiple resources can be tried by separating with a `;`.
1. Use the ["debug GPU overdraw"](https://www.youtube.com/watch?v=I4MhEx-nck4) thing in developer options to check where your app is drawing over a pixel twice or more (which is wasteful), including re-computing the colour over transparent areas.
1. Google Play Services keeps track of your boot count in a `shared_prefs/bootCount.xml`.
1. `startActivity` accepts an `Intent` rather than `Activity` because reasons.
1. If even one of your neurons fire up, you would have noticed that `new Intent(CurrentActivity.this, ...)` and `new Intent(this, ...)` are identical statements.
1. IDs are under_scored. Variables are camelCased, As always, because reasons.
1. It is possible to name your package using someone else's domain, like `com.microsoft.lol`.
1. The Nexus 5x has a fake bottom speaker grille.
1. September 2017--a month which will live in infamy--both [BroadPwn](https://blog.exodusintel.com/2017/07/26/broadpwn/) and [Blueborne](https://www.armis.com/blueBorne/) vulnerabilities were released into the wild. In the same month, Google released Android O[nion], rendering all N-based ROMs vulnerable to these attacks.
1. CAF (Code Aurora Forums) is not the project; "Android for MSM" is the project. When dudes say they are based on CAF, they actually mean they are based on Android for MSM by CAF.
1. In a very glitchy way, one-handed mode is shipped with Android 6.0 using the [`wm overscan`](https://forum.xda-developers.com/u/tasker-tips-tricks/guide-hold-swipe-home-button-to-enable-t3330353) command.
1. Android devices can be rooted with the [row hammer effect](https://en.wikipedia.org/wiki/Row_hammer). "Repeatedly accessing data stored in memory chips could flip certain bits," say [Arstechnica](https://arstechnica.com/information-technology/2016/10/using-rowhammer-bitflips-to-root-android-phones-is-now-a-thing/).
1. Stop (my particular android) device from charging using `echo 0 > /sys/class/power_supply/battery/charging_enabled`. (Use 1 to re-enable, or 2 to blow the phone up.)
1. Samsung is not an Android manufacturer for Google; [Samsung is a conglomerate that wants to take Android off Google](https://www.youtube.com/watch?v=2_L9j6mDJBg). No other series of devices have both Samsung and Google Apps suites.
1. Tapping "Cached data" in System>Storage on Android clears caches for all apps. Beware, it also clears Google offline maps and gReader article data.
1. If a Oneplus One boot loops because of a [corrupt `persist` partition](http://www.androidpolice.com/2014/10/13/heres-easy-fix-oneplus-one-sudden-death-bug-results-neverending-boot-loops/), run `make_ext4fs /dev/block/mmcblk0p15`
1. As of ~~Android L~~CyanogenMod 12, the shell now comes with [htop](http://en.wikipedia.org/wiki/Htop) (or its busybox).
1. However much Google results decide to decay, the way to check (your particular android) device's battery percentage is `cat /sys/class/power_supply/battery/capacity`.
1. [The last three digits of a Google Play Services package](https://www.reddit.com/r/Android/comments/3mh7vt/new_google_play_services_8118_438/cvf1ni5) defines the compatible android version, CPU architecture, and PPI, respectively. The most common combination is "030", package for Pre-5 devices.
1. MediaTek is "not that much worse" than Qualcomm *iff* [you don't use custom ROMs](https://www.reddit.com/r/Android/comments/6p8nio/is_mediatek_really_that_worse/).
1. Do not give internet access to Android System WebView. Granting network to this component gives all apps that use this component internet access, even if they aren't themselves whitelisted.
1. "userdebug" seen in Android's build string apparently means something. ["No root because it's a 'user' build, which is what manufacturers ship. 'userdebug' builds which contain root also contain debugging tools and other things that some users might consider to be bugs."](https://www.reddit.com/r/oneplus/comments/3sre4p/exodus_511_nightlies_vs_60_sultans_rom/cx07d0u)
1. ["You may already know that every app/process in Android is assigned an oom_adj value, which indicates the likelihood of it being killed when an out of memory (OOM) situation occurs. More higher it's value, the higher likelihood of it getting killed. Valid range is -17 to +15. (if in the -17 range means it won't get killed)."](http://forum.xda-developers.com/showthread.php?t=2751559)
1. [Android N will have *two* system partitions](https://en.wikipedia.org/wiki/Android_Nougat#Development_platform), one online and one offline. The online one will push updates to the offline one, and they switch once the offline one is updated.
1. Mounting android's system as rw: `mount -o rw,remount,rw /system`
1. Mounting android's system as ro: `mount -o ro,remount,rw /system` (I know right)
1. The file `batterystats.bin` is used to display the battery graph, and [has no impact on battery capacity](https://androidcentral.com/wiping-battery-stats-doesnt-improve-battery-life-says-google-engineer) or battery life.
1. CyanogenMod supports [9 out of however many](https://wiki.lineageos.org/devices/athene/#special-boot-modes) Moto G4s out there.
