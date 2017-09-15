1. iOS apps are [`.ipa`](http://en.wikipedia.org/wiki/.ipa) compressed (payload), and `.app` uncompressed.
1. `xcode-select --print-path` gives you where Xcode is installed.
1. `xcodebuild -list -project ???.xcodeproj` tells you what the Xcode project is configured to build, and information like targets and schemes.
1. Adding `build` after that command, i.e. `xcodebuild -project ???.xcodeproj build`, builds the `.app`.
1. "Archive" means "Compile", and "Compile" means something else, and "Build" means neither of the three.
1. iOS app submission requires one screenshot for each screen size your app claims to support.
1. [You cannot install IPAs on the simulator](https://stackoverflow.com/a/517541/1558430) (if it is built for a different CPU architecture).
1. [Why would you pay for a phone made by Google? "You paid for a phone so Google can sell you to advertisers."](https://www.forbes.com/sites/ianmorris/2017/02/10/how-google-blew-it-with-the-pixel-and-pixel-xl/#3a1ca730f3f6) This is not the case for Apple.
1. Force touch is more basic; [3D touch](https://www.wired.com/2015/09/what-is-the-difference-between-apple-iphone-3d-touch-and-force-touch/) is more granular. [It](https://en.wikipedia.org/wiki/Force_Touch#3D_Touch) would appear that iPhones have 3D touch, and all other "trackpad devices" have force touch.
1. According to EverythingApplePro, [Apple releases things on Tuesdays and starts preorders on Fridays](https://www.youtube.com/watch?v=norgCJzrNb4).
1. The Apple A10X chip is the first TSMC 10nm chip to be used by a consumer device.
1. "Mercury" is the Firefox for iOS.
1. There is normally no way to [transfer a file using Bluetooth](http://stackoverflow.com/questions/18884705/transfer-data-between-ios-and-android-via-bluetooth) on iOS. Get a Mac.
1. Chrome for iOS makes requests to `http://localhost:0` for [URL verification][newrelic].
1. "A [provisioning profile](https://pewpewthespells.com/blog/migrating_code_signing.html#introduction-to-code-signing) is a plist file that is cryptographically signed by Apple's CA to ensure it cannot be modified after being created. This allows Apple to have complete control over the deployment mechanism that is used on iOS."
1. [WKWebView](http://blog.initlabs.com/post/100113463211/wkwebview-vs-uiwebview) uses less CPU for WebGL-related tasks on iOS.
1. The iPhone 6s is 0.3mm thicker than the iPhone 6 (for the force touch rubbish). Their casings are not interchangeable.
