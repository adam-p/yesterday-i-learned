* `window.location.reload()` accepts either `true` or `false` for hard reload.
* `window.location.reload()` does not accept arguments across all browsers.
* You can't send code to the server by POST and have the browser run the same code. (Refused to execute a JavaScript script. Source code of script found within request.)
* The window's `storage` event is fired on [every window using the storage except the window that modified storage](http://stackoverflow.com/a/4689033).
* `in` compares by reference, apparently. `'e' in 'hello'.split('')` returns false.
* NaN always compares to false. Only isNaN can compare NaN.
* Delegated selectors save memory (most of the time): `$(parentObject).on(events, selector[, data], function (event) {})`
* Delegated events can be triggered by `.trigger("myCustomEvent", [data])`.
* jQuery will ignore the `data` option when creating an element from string if the element already has data attribute(s).
* `void 0 === undefined`.
* It was possible to define the global `undefined`; not possible anymore, because people were screwing around with it.
* `$([...]).each` is faster when `for` loops when it contains elements, and slower when it contains an ordinary iterable.
* `new Object`, or any object in general (e.g. `Date`), does not require `()` to initialise. Strict mode will throw a warning, though.
* It is possible to run a WebSocket inside a worker.
* `+almostAnything` converts it to an integer. (except objects, arrays, strings... so, almost nothing.)
* A named closure (which is NOT an oxymoron: `(function abc() {... }())` has its function name scoped inside the closure.
* `function abc()` in IE8 or above are declared twice, due to a bug in [hoisting and initialisation](http://kangax.github.io/nfe/).
* Youtube disables autoplay on mobile devices, even when `autoplay: 1`.
* Detecting document zoom level [is a piece of ass](http://stackoverflow.com/questions/1713771/how-to-detect-page-zoom-level-in-all-modern-browsers).
* In an [AngularJS](http://angularjs.org/) controller definition, the variable name for the scope must be `$scope`.
* `Object.defineProperty` creates immutable object constants. [Everything except IE8](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty?redirectlocale=en-US&redirectslug=JavaScript%2FReference%2FGlobal_Objects%2FObject%2FdefineProperty) does it correctly.
* Since the deprecation of IE6 and IE7, `window.elementFromPoint(clientX, clientY)` and `window.getClientRects() -> [t, l, r, b]` are available to you.
* `~~` is a [fast Math.floor](http://stackoverflow.com/a/5971668/1558430), noting some differences about negative numbers ("in that it actually just removes anything to the right of the decimal. This makes a difference when used against a negative number. Also, it will always return a number, and will never give you NaN. If it can't be converted to a number, you'll get 0").
* Ember.js will first render whichever nameless template with the string `{{ outlet }}` in it.
* Ember.js: namespaces must begin with an upper case letter.
* Ember.js: `model` is a keyword. You cannot replace it with `context`.
* In backbone.js, [a `View` is actually a controller](http://backbonejs.org/#FAQ-mvc).
* `return a, b` returns whichever value is true first.
* [Scroll events do not bubble.](http://www.quirksmode.org/dom/events/scroll.html)
* There are [typed arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays/Int32Array).
* `inputElement.selectionStart` is not cross-browser compatible.
* As it turns out, there is a [documented way](http://en.wikipedia.org/wiki/JSON#JavaScript_eval.28.29) of validating JSON.
* `$(":last")` does not require an element.
* `_.bindAll` binds for all future calls, too.
* Although it is always true that a script tag with both src and content will not execute its content, [it doesn't mean it is pretty to tell the src to execute its innerHTML](http://ejohn.org/blog/degrading-script-tags/).
* `new function () { return ... }` returns the return value instead of an object when the value is an object.
* `typeof null` is `"object"`.
* [The simplest inheritance example out there](http://stackoverflow.com/a/1204386/1558430)
* [data uris are not worth pursuing](http://www.mobify.com/blog/css-sprites-vs-data-uris-which-is-faster-on-mobile/)
* There is a built-in [self](http://stackoverflow.com/questions/3309516/when-to-use-self-in-javascript) keyword, but usually pointing at `window`, it's not all that useful.
* The `with` statement was banned [before it was even cool](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with).
* A `setTimeout` with a delay of 0 calls the function when the call stack is empty.
* [The 3 snapshot technique](https://docs.google.com/a/willetinc.com/presentation/d/1wUVmf78gG-ra5aOxvTfYdiLkdGaR9OhXRnOlIcEmu2s/pub?start=false&loop=false&delayms=3000#slide=id.g31ec7af_0_58): First take a snapshot, then do something and take another snapshot. Repeat the exact same things and take snapshot 3. Finally, "filter objects allocated between snapshots 1 and 2 in snapshot 3's summary view"
* `_.once` keeps returning the value of the original call in subsequent calls.
* Terminology: `_gaq.push(['_trackEvent', 'category', 'action', 'label', 'value']);` [source](https://developers.google.com/analytics/devguides/collection/gajs/eventTrackerGuide#Anatomy)
* [No such thing as tail call optimization](http://stackoverflow.com/questions/3660577/are-any-javascript-engines-tail-call-optimized)... not one that works, anyway
* [Trampolines](http://raganwald.com/2013/03/28/trampolines-in-javascript.html) are `while` wrappers that call an inner function for as long as the function remains a function, not a primitive value.
* `undefined == null` === `true`. Die in a fire, JS!
* [Second parameter of `JSON.parse`](http://stackoverflow.com/questions/19281820/deserialization-of-partially-flattened-json/19281911?noredirect=1#19281911) (reverse applies to `.stringify`, too)
* CORS is not supported before IE8; hence JSONP.
* One use of the named closure (`(function abc() {}())`) is that `abc` is defined only inside the scope, which means recursive closures can be built without using an outside variable.
* `$.each(string)` [stopped working](http://stackoverflow.com/questions/20075938/jquery-each-to-iterate-over-a-string-in-newer-versions). Now you will need to split the string first.
* [Detecting `{}.__proto__`](http://foundation.zurb.com/docs/upgrading.html) is one of the fastest ways to tell if a browser is running on a [browser that also runs on mobiles](http://stackoverflow.com/a/3082878/1558430).
* [`debugger`](http://msdn.microsoft.com/en-us/library/ie/0bwt76sk\(v=vs.94\).aspx)
* `_.result(a)` returns `a()` if it is a function, or just `a`.
* `Number()` returns 1 or 0.
* If desperate, `_.omit(obj)` makes a copy of the object. `_.omit(obj, key1, key2, ...)` creates a copy without attributes key1 and key2.
* `navigator.onLine` is `true` when the browser is actually online.
* Backbone: `Collection.parse` is called *only* if you resolve the `fetch` XHR with remote JSON. It doesn't do anything if you resolve with an object.
* [JSON on IE8? Nope](http://stackoverflow.com/a/4715399/1558430)
* AJAX on IE? Nope. Need to use `this.response || this.responseText` for any AJAX objects made.
* [Dispatching keyboard events without jQuery](http://stackoverflow.com/a/5920206/1558430)
* Clone an array: [`arr.slice(0)`](http://stackoverflow.com/questions/5024085/whats-the-point-of-slice0-here)
* [Marionette's UI hash](https://github.com/marionettejs/backbone.marionette/blob/master/docs/marionette.itemview.md#organizing-ui-elements) keeps references to UI elements; `this.ui.checkbox` anywhere in any method means `this.$(the checkbox selector`. This has no use for regions, whose elements are already defined using selectors.
* 

## Deferred API

* `$.when(<Deferred, Promise, or any object really>, another, another...) => <Promise>`
* `<Deferred>.then(done, fail, progress)`
* `<Deferred>.done(function, function, ...)`
* `<Deferred>.always(function, function, ...)`
* `<Deferred>.fail(function, function, ...)`
