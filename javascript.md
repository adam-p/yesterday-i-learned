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

