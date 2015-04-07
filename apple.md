* iOS apps are [`.ipa`](http://en.wikipedia.org/wiki/.ipa) compressed (payload), and `.app` uncompressed.
* `xcode-select --print-path` gives you where Xcode is installed.
* `xcodebuild -list -project ???.xcodeproj` tells you what the Xcode project is configured to build, and information like targets and schemes.
* Adding `build` after that command, i.e. `xcodebuild -project ???.xcodeproj build`, builds the `.ipa`. I think.
