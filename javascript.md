* `window.location.reload()` accepts either `true` or `false` for hard reload.
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
