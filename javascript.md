* `window.location.reload()` accepts either `true` or `false` for hard reload.
* `window.location.reload()` does not accept arguments across all browsers.
* You can't send code to the server by POST and have the browser run the same code. (Refused to execute a JavaScript script. Source code of script found within request.)
* The window's `storage` event is fired on [every window using the storage except the window that modified storage][stackoverflow].
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
* `function abc()` in IE8 or above are declared twice, due to a bug in [hoisting and initialisation][github].
* Youtube disables autoplay on mobile devices, even when `autoplay: 1`.
* Detecting document zoom level [is a piece of ass][stackoverflow 2].
* In an [AngularJS][angularjs] controller definition, the variable name for the scope must be `$scope`.
* `Object.defineProperty` creates immutable object constants. [Everything except IE8][mozilla] does it correctly.
* Since the deprecation of IE6 and IE7, `window.elementFromPoint(clientX, clientY)` and `window.getClientRects() -> [t, l, r, b]` are available to you.
* `~~` is a [fast Math.floor][stackoverflow 3], noting some differences about negative numbers ("in that it actually just removes anything to the right of the decimal. This makes a difference when used against a negative number. Also, it will always return a number, and will never give you NaN. If it can't be converted to a number, you'll get 0").
* Ember.js will first render whichever nameless template with the string `{{ outlet }}` in it.
* Ember.js: namespaces must begin with an upper case letter.
* Ember.js: `model` is a keyword. You cannot replace it with `context`.
* In backbone.js, [a `View` is actually a controller][backbonejs].
* `return a, b` returns whichever value is true first.
* [Scroll events do not bubble.][quirksmode]
* There are [typed arrays][mozilla 2].
* `inputElement.selectionStart` is not cross-browser compatible.
* As it turns out, there is a [documented way][wikipedia] of validating JSON.
* `$(":last")` does not require an element.
* `_.bindAll` binds for all future calls, too.
* Although it is always true that a script tag with both src and content will not execute its content, [it doesn't mean it is pretty to tell the src to execute its innerHTML][ejohn].
* `new function () { return ... }` returns the return value instead of an object when the value is an object.
* `typeof null` is `"object"`.
* [The simplest inheritance example out there][stackoverflow 4]
* [data uris are not worth pursuing][mobify]
* There is a built-in [self][stackoverflow 5] keyword, but usually pointing at `window`, it's not all that useful.
* The `with` statement was banned [before it was even cool][mozilla 3].
* A `setTimeout` with a delay of 0 calls the function when the call stack is empty.
* [The 3 snapshot technique][google]: First take a snapshot, then do something and take another snapshot. Repeat the exact same things and take snapshot 3. Finally, "filter objects allocated between snapshots 1 and 2 in snapshot 3's summary view"
* `_.once` keeps returning the value of the original call in subsequent calls.
* Terminology: `_gaq.push(['_trackEvent', 'category', 'action', 'label', 'value']);` [source][google 2]
* [No such thing as tail call optimization][stackoverflow 6]... not one that works, anyway
* [Trampolines][raganwald] are `while` wrappers that call an inner function for as long as the function remains a function, not a primitive value.
* `undefined == null` === `true`. Die in a fire, JS!
* [Second parameter of `JSON.parse`][stackoverflow 7] (reverse applies to `.stringify`, too)
* CORS is not supported before IE8; hence JSONP.
* One use of the named closure (`(function abc() {}())`) is that `abc` is defined only inside the scope, which means recursive closures can be built without using an outside variable.
* `$.each(string)` [stopped working][stackoverflow 8]. Now you will need to split the string first.
* [Detecting `{}.__proto__`][zurb] is one of the fastest ways to tell if a browser is running on a [browser that also runs on mobiles][stackoverflow 9].
* [`debugger`][microsoft].aspx)
* `_.result(a)` returns `a()` if it is a function, or just `a`.
* `Number()` returns 1 or 0.
* If desperate, `_.omit(obj)` makes a copy of the object. `_.omit(obj, key1, key2, ...)` creates a copy without attributes key1 and key2.
* `navigator.onLine` is `true` when the browser is actually online.
* Backbone: `Collection.parse` is called *only* if you resolve the `fetch` XHR with remote JSON. It doesn't do anything if you resolve with an object.
* [JSON on IE8? Nope][stackoverflow 10]
* AJAX on IE? Nope. Need to use `this.response || this.responseText` for any AJAX objects made.
* [Dispatching keyboard events without jQuery][stackoverflow 11]
* Clone an array: [`arr.slice(0)`][stackoverflow 12]
* [Marionette's UI hash][github 2] keeps references to UI elements; `this.ui.checkbox` anywhere in any method means `this.$(the checkbox selector`. This has no use for regions, whose elements are already defined using selectors.
* Apparently [$.Deferred is a monad][voisen].
* There's a [Promises 2.0][msdn], but who uses it?
* >Note that the `bower_components` folder would normally be installed in the root folder but (angular-seed) changes this location through the `.bowerrc` file. Putting it in the app folder makes it easier to serve the files by a webserver.
* Placing `"scripts": { "postinstall": "bower install" }` in `package.json` (npm) installs `bower_components` right after npm finishes.
* `EADDRINUSE` is node's very polite way of saying "port is taken".
* [Promises are streams][github 3].
* `$.fn.not` is [**not** the opposite of `$.fn.is`][ajpiano] -- `$.fn.not` always gives you a truthy return.
* `(An error).stack` gives you the stack.
* Jinja2 and AngularJS template tags can conflict, which prevents Jinja2 from rendering the page. [Solution][blogspot] is to override Jinja2's settings with some other tag: `JINJA_ENVIRONMENT=jinja2.Environment( loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], variable_start_string='((', variable_end_string='))', autoescape=True)` (I think it's a bit hacky, however)
* **NaCl** in tech usually stands for **Na**tive **Cl**ient.
* `"use strict";` in global scope affects the entire script file, but not other scripts on the page.
* To generate revisions of assets, you might need [gulp-rev][npmjs] (see also: the "Works with gulp-rev" section)
* `npm` has a [dedupe](https://www.npmjs.org/doc/cli/npm-dedupe.html) option that groups common dependencies higher up the dependency tree.
* Use `bower` in place of npm for client side packaging to [avoid multiple versions of the same library sent to the client](http://stackoverflow.com/a/18652918).

## Deferred API

* `$.when(<Deferred, Promise, or any object really>, another, another...) => <Promise>`
* `<Deferred>.then(done, fail, progress)`
* `<Deferred>.done(function, function, ...)`
* `<Deferred>.always(function, function, ...)`
* `<Deferred>.fail(function, function, ...)`

## [Writing memory-efficient JavaScript][smashingmagazine]

* Dereferencing (`delete object.key`) does not free memory immediately, but it does take CPU to modify the object, so use sparingly.
* Setting something to `null` does not null the object; it merely sets the reference to `null`, which does not free memory immediately.
* Global objects are never garbage-collected.
* Function-scoped variables are cleaned up when it can no longer be reached (like, if it stays inside the function).
* Unbind event listeners when they're no longer used. This is not done automatically -- you need to keep track.
* Functions that return functions can never be garbage-collected, because the reference to the inner function can be called.
* (However,) any variables no longer used in the function that returns a function will be garbage collected in some cases (V8).
* Anything referenced by timers (`setTimeout` or `setInterval`) will not be garbage collected.
* Try-catches will cause V8 to cancel optimization.
* Don't write large functions; they are hard to optimize (both by humans and engines)
* To store many things of the same type (e.g. Number, String, ...) use an Array, because they are faster to iterate over [than objects with integer keys].
* Sparse arrays (most values are 0) are [slower on V8 than full arrays][jsperf].
* [Except in Safari][jsperf 2], never pre-allocate arrays.
* Avoid element reflowing/redrawing (but this is more of a DOM thing rather than JS)
* node has a [debugger](http://nodejs.org/api/debugger.html). To use it, run `node debug` where you normally run `node`.
* "[Every function in Node.js is asynchronous](http://code.tutsplus.com/tutorials/node-js-for-beginners--net-26314)", even the ones that are normally blocking.

[ajpiano]: http://ajpiano.com/the-opposite-of-jquerys-is-method-is-not-not-it-is-is/
[angularjs]: http://angularjs.org/
[backbonejs]: http://backbonejs.org/#FAQ-mvc
[blogspot]: http://zhangyelei.blogspot.ca/2013/10/variable-placeholder-conflict-between.html
[ejohn]: http://ejohn.org/blog/degrading-script-tags/
[github]: http://kangax.github.io/nfe/
[github 2]: https://github.com/marionettejs/backbone.marionette/blob/master/docs/marionette.itemview.md#organizing-ui-elements
[github 3]: https://gist.github.com/staltz/868e7e9bc2a7b8c1f754#request-and-response
[google]: https://docs.google.com/a/willetinc.com/presentation/d/1wUVmf78gG-ra5aOxvTfYdiLkdGaR9OhXRnOlIcEmu2s/pub?start=false&loop=false&delayms=3000#slide=id.g31ec7af_0_58
[google 2]: https://developers.google.com/analytics/devguides/collection/gajs/eventTrackerGuide#Anatomy
[jsperf]: http://jsperf.com/sparse-arrays-vs-full-arrays
[jsperf 2]: http://jsperf.com/pre-allocated-arrays
[microsoft]: http://msdn.microsoft.com/en-us/library/ie/0bwt76sk\(v=vs.94\
[mobify]: http://www.mobify.com/blog/css-sprites-vs-data-uris-which-is-faster-on-mobile/
[mozilla]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty?redirectlocale=en-US&redirectslug=JavaScript%2FReference%2FGlobal_Objects%2FObject%2FdefineProperty
[mozilla 2]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays/Int32Array
[mozilla 3]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/with
[msdn]: http://blogs.msdn.com/b/rbuckton/archive/2011/08/15/promise-js-2-0-promise-framework-for-javascript.aspx
[npmjs]: https://www.npmjs.org/package/gulp-rev
[quirksmode]: http://www.quirksmode.org/dom/events/scroll.html
[raganwald]: http://raganwald.com/2013/03/28/trampolines-in-javascript.html
[smashingmagazine]: http://www.smashingmagazine.com/2012/11/05/writing-fast-memory-efficient-javascript/
[stackoverflow]: http://stackoverflow.com/a/4689033
[stackoverflow 10]: http://stackoverflow.com/a/4715399/1558430
[stackoverflow 11]: http://stackoverflow.com/a/5920206/1558430
[stackoverflow 12]: http://stackoverflow.com/questions/5024085/whats-the-point-of-slice0-here
[stackoverflow 2]: http://stackoverflow.com/questions/1713771/how-to-detect-page-zoom-level-in-all-modern-browsers
[stackoverflow 3]: http://stackoverflow.com/a/5971668/1558430
[stackoverflow 4]: http://stackoverflow.com/a/1204386/1558430
[stackoverflow 5]: http://stackoverflow.com/questions/3309516/when-to-use-self-in-javascript
[stackoverflow 6]: http://stackoverflow.com/questions/3660577/are-any-javascript-engines-tail-call-optimized
[stackoverflow 7]: http://stackoverflow.com/questions/19281820/deserialization-of-partially-flattened-json/19281911?noredirect=1#19281911
[stackoverflow 8]: http://stackoverflow.com/questions/20075938/jquery-each-to-iterate-over-a-string-in-newer-versions
[stackoverflow 9]: http://stackoverflow.com/a/3082878/1558430
[voisen]: http://sean.voisen.org/blog/2013/10/intro-monads-maybe/
[wikipedia]: http://en.wikipedia.org/wiki/JSON#JavaScript_eval.28.29
[zurb]: http://foundation.zurb.com/docs/upgrading.html
