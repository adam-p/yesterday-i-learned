* [CoffeeScript should not exist](https://meta.discourse.org/t/is-it-better-for-discourse-to-use-javascript-or-coffeescript/3153/10). Something called the "1JS" princple guarantees that ES5 scripts will continue working when ES6 is out, but CoffeeScript cannot up-compile to ES6.
* Wrapping JS code in backticks makes it legal CoffeeScript.
* I take that back. It doesn't work everywhere.
* Only in CoffeeScript: [classical classes](http://coffeescript.org/#classes), optional arguments (`foo = (bar = {}) ->`), argument unpacking (`foo.bar(args...)`)
* In multi-line arrays, commas are optional. Trailing commas are also removed.
* Ruby-style string interpolation is included in CoffeeScript. Double-quoted strings allow for interpolated values, using `#{ ... }`, and single-quoted strings are literal.
* Multiline strings are allowed in CoffeeScript.
* You want to write `if not a instanceof b`? HAH! WRONG! It compiles to `if ((!a) instanceof b)` because coffeescript.
* `do(a=b, c=d) -> ...` is exactly the same as `(function (a, c) { ... }(b, d));`.
* Apparently the string interpolation syntax in CoffeeScript is [the exact same from Ruby](http://addyosmani.com/blog/backing-up-a-github-account/).
* Anonymous classes are as intuitive as you might expect: `class[ extends AnotherClass]`
* All functions are anonymous functions assigned to variable names. So, you cannot have named functions. This is slower at the cost of (perhaps) fewer hoisting gotchas.
