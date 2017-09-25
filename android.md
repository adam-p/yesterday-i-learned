# [Android](https://www.reddit.com/r/androiddev/comments/3ka9j0/what_to_know_for_a_mobile_developer_interview/)

![](http://i.imgur.com/2q7uebE.jpg)

> "Imagine being a phone. At launch, everyone loves you and is in line to get you. You amaze every review website or youtube channel out there. You're beautiful, sturdy, incredibly fast and affordable. People flash new roms on you on the daily. Over thirty THOUSAND people discuss you on a dedicated subreddit. There's millions of apps promoting themselves using you for their screenshots. Your owner takes you everywhere. You're with your owner through the best and worst times, always ready to rock. Your owner promotes you to their friends often. Over time, your power button starts getting funky, new phones come out and then one day, your owner is ordering a new phone through your screen. You try stopping them by randomly rebooting one more time, but this only seems to encourage the owner more. One day, you hear the doorbell. Your owner takes their new phone out of the box, with the same excitement they felt back when you were unboxed 2 years ago. They pick you up one last time to post a photo of the new phone, turn you off, take out your SIM and put you in a drawer never to be picked up again. You wonder where you went wrong. Was it the battery life? The camera? The power button? You lay there, waiting for your battery to completely run out, and when it does, you know you've had a good life." - [/u/alectprasad](https://www.reddit.com/r/Android/comments/721w8x/you_just_got_a_new_smartphone_what_is_the_first/dnfmdp4/)

## [Android Guides](https://github.com/codepath/android_guides/wiki)

* Download the SDK before attempting to compile anything.
* Android Studio 0.80 beta is, by default, [broken](http://stackoverflow.com/questions/24465289/android-studio-failure-install-failed-older-sdk).
* Handling menu clicks is as stupid as you want it to be, but [here is a simpler one](http://stackoverflow.com/a/7480103/1558430)
* For whatever reason, [it is impossible to set a negative value on a NumberPicker](http://stackoverflow.com/questions/20968561/android-numberpicker-negative-values). You can only subtract the value by a negative number after the fact.
* Do know what these mean: activity/fragment lifecycles, device rotation, services, broadcasts, background tasks, asynchronous tasks, views, adapters, recyclerview, "view holder pattern"
* Strings are put inside `project_root/app/src/main/res/values/strings.xml`, because nested folders are the best.
* [The plus thing in the XML](http://developer.android.com/training/basics/firstapp/building-ui.html), like `android:id="@+id/edit_message"`, is required only for the line that defines it.
* `android:hint` are placeholder texts.
* [`layout_weight` is a relative number](http://stackoverflow.com/questions/3995825/what-does-androidlayout-weight-mean). A `layout_weight` of 1 means 100% of the width *IF* the control happens to be the only control inside a `LinearView` with the weight specified. If two controls have the weight specified (say 1, 1), then each control shares 50% of the width.
* If `layout_weight` is given, [then](http://developer.android.com/training/basics/firstapp/building-ui.html) `layout_width` is useless (irrelevant), and should be set to 0dp or 0px.
* The back button does ["back navigation"](http://developer.android.com/design/patterns/navigation.html) (whichever activity shown in reverse chronological order); the in-app backs do "up navigation". The term "up" refers to the hierarchical parent of the current activity, a hierarchy you declare in `AndroidManifest.xml`.
* Putting a library into `libs/` seems to do it.
* There are project (`./build.gradle`) and app-level (`./app/build.gradle`) gradle files. The former defines dependencies, and the latter uses them.
* If gradle is too old, update the `classpath 'com.android.tools.build:gradle:2.1.2'`... in the gradle file. Gradle will update itself. [True fact.](http://stackoverflow.com/questions/17634708/android-studio-upgraded-from-0-1-9-to-0-2-0-causing-gradle-build-errors-now/17648742#17648742)
* Order in the layout xml files matters.
* The project's JDK settings is in File > Project Structure, which is not in Settings for studio.
* If you don't know what the fresh hell you are doing, [here is a layouts cheat sheet](http://labs.udacity.com/images/Layout-Cheat-Sheet.pdf).
* Accessing the Internet on the main thread, get this, raises the `NetworkOnMainThreadException`.
* [AsyncTask](http://stackoverflow.com/questions/3921816/can-i-pass-different-types-of-parameters-to-an-asynctask-in-android) takes just one type of parameter, but you can use "the setter" (?) to use additional types, or simply [pass in an `Object`](http://stackoverflow.com/a/9077177) and re-cast from there.
* ["The difference between Handler and AsyncTask is: Use AsyncTask when Caller thread is a UI Thread."](http://stackoverflow.com/a/9800870)
* It is near impossible to [conjure a popup from a non-activity class](http://stackoverflow.com/a/31221646).
* `(an AsyncTask).get()` [immediately gets the value from its execute()](http://stackoverflow.com/a/10972142). Then again, that is a synchronous move.
* Activity [apparently](http://stackoverflow.com/a/9192916/1558430) extends Context.
* Find your dependency versions on [this website](http://search.maven.org/#search%7Cga%7C1%7Cio.reactivex.rxjava). It only searches on mavenCentral, I think.
* [Two-way binding is **not** natively supported](https://medium.com/@fabioCollini/android-data-binding-f9f9d3afc761#.pfcgcnfo5) by the designer thing, but there are lots of [one-way binding libraries](https://developer.android.com/topic/libraries/data-binding/index.html) available.
* To use that `com.android.databinding` plugin, the layout file must have `<Layout>` as the root, not anything else, like `<LinearLayout>`.
* [Java 8 must be explicitly enabled](http://stackoverflow.com/a/37004259/1558430)
* The superclass of your activity has a [`setTitle()`](http://stackoverflow.com/questions/3975550/android-how-to-change-the-application-title) that does what you think it does.
* [Loser answered the wrong base64 question](http://stackoverflow.com/a/29383697/1558430), but it works. [This should work.](http://stackoverflow.com/a/15683305/1558430)
* Two apps signed with the same key can [securely share code and data](https://developer.android.com/studio/publish/app-signing.html#considerations).
* adbd cannot run as root in production builds.
* Daydream is triggered only if the device is allowed to sleep from screen timeout while charging. Pressing the power button at any time will cancel the timeout.
* In some cases, [`onDestroy` is never called when an activity is destroyed.](https://academy.realm.io/posts/sf-fabien-davos-modern-android-ditching-activities-fragments/)
* Sometimes you might want to check if you can run code based on the SDK version with which your app is built (like `Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR2`). Actually, I don't think you'll ever need to do that.
* [try-with-resources is only supported if your minSdkVersion is set to 19 or higher.](https://stackoverflow.com/a/24290875/1558430) It looks like `try (foo = new SomeResourceLikeAFile()) { foo... }`. Multiple resources can be tried by separating with a `;`.
* Use the ["debug GPU overdraw"](https://www.youtube.com/watch?v=I4MhEx-nck4) thing in developer options to check where your app is drawing over a pixel twice or more (which is wasteful), including re-computing the colour over transparent areas.
* Google Play Services keeps track of your boot count in a `shared_prefs/bootCount.xml`.
* `startActivity` accepts an `Intent` rather than `Activity` because reasons.
* If even one of your neurons fire up, you would have noticed that `new Intent(CurrentActivity.this, ...)` and `new Intent(this, ...)` are identical statements.
* IDs are under_scored. Variables are camelCased, As always, because reasons.