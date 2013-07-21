* `window.location.reload()` accepts either `true` or `false` for hard reload.
* You can't send code to the server by POST and have the browser run the same code. (Refused to execute a JavaScript script. Source code of script found within request.)
* The window's `storage` event is fired on [every window using the storage except the window that modified storage](http://stackoverflow.com/a/4689033).
* `in` compares by reference, apparently. `'e' in 'hello'.split('')` returns false.
* NaN always compares to false. Only isNaN can compare NaN.
