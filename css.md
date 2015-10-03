* CSS3 has `background-size`, whose most useful values are `cover` (scaled and cropped) and `contain` (scaled to fit).
* `text-overflow` allows [custom truncation characters][mozilla]. It is CSS3. For everything else, there's [mastercard][frebsite].
* Chrome doesn't support two-valued text-overflows, e.g. `clip ellipsis`.
* Relative paths in an external CSS file is [relative to the file][stackoverflow].
* A `:before` selector with `content: "|";` solves many problems, including stupid site menu separators.
* Web components ([decorators][w3]): basically, js templating without the js. Dayum.
* [The lamest jQuery UI theme][jqueryui]
* All you need to make an oval subtraction is `border-radius: 50%;`.
* CSS pseudo elements [do not exist in the DOM][stackoverflow 2].
* For the geeky: `ul { list-style-type: binary; }`
* `calc` (`calc(100% - 40px);`) works in [IE9+, prefix-free][tutorialzine].
* [You can already][tutorialzine] use expressions like `content:attr(data-title)` for `:before` selectors that have a `data-title`.
* Everyone except IE8 supports [multiple background images][caniuse], in the format `background:url('abc.png') repeat x y, url('def.png') repeat x y`.
* It was apparently agreed upon that webapp buttons be used in conjunction with [a normal cursor][stackoverflow 3] instead of a hand.
* Can't set a container's width and height based on the ratio of its background image? [Have an invisible image tag inside the container][stackoverflow 4] so the container displays its background image according to the shrunk ratio of its invisible children.
* There is something called the [`rem` size unit][snook] in CSS3, which stands for "root em". It is the em size multiplied by its parents' size values (e.g. 10rem in a 80% parent is effective 8em)
* [CSS triangles -- a tragedy in five acts][stackoverflow 5] (essentially, three sides of borders combined with something with neither width nor height)
* Can you use scoped css (`<style scoped>`)? [No][caniuse 2], you cannot use scoped CSS.
* [`:visited`][mozilla 2] can only change `color`.
* [`:visited`][mozilla 2] cannot be read by JavaScript.
* `transform: translate/scale/rotate/skew/matrix npx npx` and `opacity` apparently [do not trigger repaints][aerotwist] and are thus CPU-friendly. (This does not apply to non-px animations)
* iOS 6/7 support `position: sticky`, which is like `fixed` except dependent on where the element is relative to the viewport.
* IE8 and under have a 4095-CSS-selector limit in any given page.
* There is a [`text-rendering: optimizeLegibility`][aestheticallyloyal] flag that makes kerning look "normal" according to what the browser. However, page rendering is (slightly) slower, text will sometimes disappear if combined with `text-transform: small-caps`, and disappear completely in WebOS.
* Transforms and translates [*will* mess with z-indices](http://dabblet.com/gist/2463684) by [creating a different stacking context](http://stackoverflow.com/a/10814448), so use these optimisations only when necessary.
* `backface-visibility: hidden` means that, if you flip an object by the z-axis (revealing its back, or *backface*), the object will be hidden instead of inverted.
* `local('☺')` means ["never use the local font"](http://stackoverflow.com/q/3698319/1558430).
* [Uncommon selectors](http://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048):
    * `a:link` (never clicked) and `a:visited` (clicked)
    * `div + p`: only `p`s immediately after a div
    * `div ~ p`: only `p`s immediately before a div
    * `a[href]`: `a`s with any `href`. See also: `a[href^="foo"]` (starts with), `a[href$="foo"]` (ends with),  `a[href*="foo"]` (anywhere), and `a[href~="foo"]` (if `href`, a space-separated value, contains `foo`).
* [Pull and exact amount left and right opposite to each other](http://stackoverflow.com/questions/20979062/bootstrap-right-column-on-top-on-mobile-view) to have a bootstrap left column to appear at the bottom in mobile view.
* Specificity are defined in sets; `(0,0,999,0)` (999 classes) is never greater than `(0,1,0,0)` (one id).
* [Flexbox](http://caniuse.com/#feat=flexbox) is in fact already usable in all reasonable browsers (that is, not IE).
* Flexbox isn't the end-all, either. It has a [known list of Flexbox bugs](https://github.com/philipwalton/flexbugs) across supported browsers that you should know about.
* Set a dummy whose top margin is "100%" to have an element [whose height is the same as its width](http://jsfiddle.net/ansciath/B8FU8/).
* Such a font as [OpenDyslexic](http://opendyslexic.org/) exists.

## XPath

* `//` is *root* if used at the start, or *any descendant* if used anywhere else.
* `/` is *from anywhere* if used at the start, or *direct descendant* if used anywhere else.
* `img[@src="wat"]` filters `img` tags by `src`. The same works for data attributes.

## Design

* "This redesign incorporates two of the worst design trends today: *very low contrast text* and *gratuitously, obnoxiously large fixed headers.*"
    
    Takeaway: *Use high-contrast text*. **Don't use fixed headers**.

[aerotwist]: http://aerotwist.com/blog/pixels-are-expensive/
[aestheticallyloyal]: http://aestheticallyloyal.com/public/optimize-legibility/
[caniuse]: http://caniuse.com/#feat=multibackgrounds
[caniuse 2]: http://caniuse.com/style-scoped
[frebsite]: http://dotdotdot.frebsite.nl/
[jqueryui]: http://jqueryui.com/themeroller/#!zThemeParams=5d000001005a09000000000000003d8888d844329a8dfe02723de3e56fef6f394c7b9c2dcae86fd46a4522d8ce7f4c4ece283da2a0cd205a5a6995b4b03b22e4da76864efd1aaab86290b5d53a6638eea5899160f19f4bcf9cc97eb703db374372ecbc4a1700b03ec54426a82393ca871997be542a299753e3a7aa112a37d68de7ebc5e0a4b421336ada9f0cdc09a45691c68e44edadf588481a8e65505c2a7076fa0062595485585478461c72a8fccd5fac8e09d72ee5e48aa5c425f397e6b5fed846357fdf50e7d28ccb6874a1913279c3be3dbe13160d2d7b41dec59fc18cae93ee21deeb54f845b60a487cf3b8dfb74b6bc7267c4d1e87f17c70c918dd2f340a9414c70cd13c25e48ab39f1e8940db674f85023fc4e2453bc5d9b093c124d701b71ecf369ab48fc1b663b1d84f900bbdd2731bb82ecd40b164e5b73ce53bcda3b64cf1864c4055db6771e82d869b3ad94514879145b3c8d8f3d298d171be10dc8a272853035bb569a5790fd4a49bda81ef59f45336c712111b7b69a9b1c1f7acee9fbce612aa0fe2f2b0323a021b72fe864b5083a0f09591c02739ad82d6c4efcc02b7475532f8d9818b052c3694d4b40585d7d66cd7635542cf5e3ced335147e968ac1b8ce77a9ce0b90876b05d9136ad06768c001021a0e2d8d380dd8d00e54ef2fae94b69e9537c6d6def958713ebb0661c73a12c019898e0917de6e31cfd7518a112524f688bfdd983ec0a702c7043a8695af73f5e32b4530d0dc54ade94bed9db8d3b87e4c318a12a01e1fbb0b68dd184faf5ee643e6c303b2c14777989085fe5d4c1bc9b17407ae7668bd0cb7d54d2c941c0e95c412a80847b9d96843664168139ede3ec69839b76120246e3f2717bbaa3e3d1713f9abc0ce77418e110e915146d6ed9f0b7ac49d977c92c26981d26f1744b86940b2409c4629593b3d194458bd426241449d50e66afbd474a61b76e2c1526a202b9691217010be51b3d5d1b773a5786eda5c5637bc4b6cb380a3708fd8f07843a7946f0ee0a16c737bfa93b613fe17e465848217429d93bad7a58d882d60f5e4c91ed23c45df351ca8c69b8360e947c1089b91e2b2cac275e2b87a6134b763705ea729e4a2a1ce9f3013a46ba2a94bf891f4872bf8ca68e9096f4c05b13efdd76edcd63d0d4660765274a8b394b3e99bc13c22ca92a9e1ca063e52d17bf96b57ffc4de0a40a8529f64ca4987a1487701cd9cf1d94f849448098afefcb17d50ba134185cd669c902cc6e9ddabdb08d30ef99dff70e6d15416ca98d200c3f29c12326872b6d236b40274b44dd239bd0455eff0d74f5aac551d25fa7267100aaeddbf4abaf64521da4adb552b45bc55ce34d41d3cca01a11971290f8fef8e30005
[mozilla]: https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow
[mozilla 2]: https://blog.mozilla.org/security/2010/03/31/plugging-the-css-history-leak/
[snook]: http://snook.ca/archives/html_and_css/font-size-with-rem
[stackoverflow]: http://stackoverflow.com/questions/940451/using-relative-url-in-css-file-what-location-is-it-relative-to
[stackoverflow 2]: http://stackoverflow.com/questions/9395858/event-listener-on-a-css-pseudo-element-such-as-before-or-after
[stackoverflow 3]: http://stackoverflow.com/questions/4121854/is-it-wrong-to-use-the-hand-cursor-for-clickable-items-such-as-buttons
[stackoverflow 4]: http://stackoverflow.com/a/12098334/1558430
[stackoverflow 5]: http://stackoverflow.com/a/7073558/1558430
[tutorialzine]: http://tutorialzine.com/2013/10/12-awesome-css3-features-you-can-finally-use/
[w3]: http://www.w3.org/TR/2013/WD-components-intro-20130606/#decorator-section
