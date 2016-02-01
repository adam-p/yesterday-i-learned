* Did you realise the difference between `||` and `or`, which both exist?
   * `$a = false || true === $a = (false || true) === $a = true`
   * `$a = false or true === ($a = false) or true === $a = false` (easier to understand if you think about `or die()`)
* http://net-beta.net/ubench/
* Declare all vars; undeclared ones 10 times slower
* Check for function calls in for loops
* Remove @s (reportedly slow) -> harmless errors should be hidden with 0 or `E_NONE`
* Minimize magics. They are slow.
* Check full paths for includes
* Static functions are 4 times faster
* Singletons are (faster / saves memory)
* `[v]p[s]rintf` is 10x faster than `echo("$ $ $")`; `echo (1,2,3)` is also faster
* `unset()`s really work in php.
* Use $_SERVER['REQUEST_TIME'] instead of microtime for start time
* Change `switch` to `else if` (faster)
* `++$i` is faster than `$i++`
* Use `ip2long()` and `long2ip()` to store IP addresses as integers instead of strings
* Avoid global variable changes; cache using local-scope vars first
* `isset($foo[5])` is faster than `strlen($foo) > 5`
* int list keys are always faster than str list keys
* Avoiding classes speeds things up
* `array_push` is slower than `array[] =`
* `strpos` is faster than `strstr`
* `str{5}` is 2x faster than `substr(str,5,1)`
* Even `@` is faster than `error_reporting(0)`
* ... but `isset()` is 5x faster than `@`
* `file_get_contents` is faster than `file`
* For code unlikely to throw exceptions, it's faster to use exception trapping.
* For code likely to throw exceptions, it's faster to check your values rather than raising exceptions.
* `=== null` is 2x faster than `is_null`
* `+` is 2x faster than `array_merge`
* `if` is faster than shorthand
* nested if is logically faster than `&&`
* `$a = 'func'; $a()` is faster than `call_user_func`, but slower than just calling the function
* Avoid $_GLOBALS at all costs; avoid `global a,b,c` too (2x slower than local vars)
* never use `while(next())`
* `foreach` is faster with key
* `foreach as &var` is 3x faster if loop involves writing to var.
* Recursion is 3x slower than not
* It is faster to `strtolower` + `strpos` than to `stripos`. (!!)
* `(int)` is faster than `intval`
* `array()` is marginally faster than `(array)`
* `===` is up to 12 times faster than `==` in all comparisons
* `break` [accepts an integer](http://www.php.net/break) for the number of nests of break out of.
* `{ code }` [effectively does nothing](http://stackoverflow.com/questions/14971123/use-curly-brackets-to-structure-code-in-php).
* [No type-hinting for scalar (primitive) types](http://www.php.net/manual/en/language.oop5.typehinting.php), but `array` is okay, because PHP.
* [No classes within classes](http://stackoverflow.com/questions/1583140/is-it-allowed-to-create-a-php-class-inside-another-class)
* `$str++` incrementss the string bytes by 1 (a becomes b), but [`$str--` removes a character from the string](https://eval.in/60631) because lol
* `$argv` is a thing.
* Searching for [`exec($_GET`](https://github.com/search?q=exec%28%24_GET&ref=cmdform&type=Code) gives you a list of exploitable web apps.
* Every C99 shell has a [backdoor](http://thehackerblog.com/every-c99-php-shell-is-backdoored-aka-free-shells/) that allows the user-set authentication to be bypassed by the author.
* Empirically speaking, it is apparently possible to get a reference of a [require](https://github.com/chintanbanugaria/92five/blob/master/artisan#L30) by [`return`ing something in the file that you require](https://github.com/chintanbanugaria/92five/blob/master/bootstrap/start.php#L76).
    * I am already taking this back. You [cannot return classes or interfaces](http://stackoverflow.com/a/8084184/1558430).
* Interfaces cannot define access types (private/protected). Everything is public.
* `$factorial = function($n) use (&$factorial)`: [For any recursive function,] You need to pass `$factorial` by reference because the variable has not been assigned yet. If you don't pass by reference, PHP will attempt to copy the variable, causing an undefined variable error (notice). - [source](http://www.reddit.com/r/PHP/comments/2leo05/functional_programming_in_php/)
* [For very large numerical inputs, the php mod operator may produce NEGATIVE values, even if neither operator is negative.](http://stackoverflow.com/a/27113242/1558430) To work around this, you can use `fmod` instead.
* Apparently PHP has been encouraging [trailing commas](http://stackoverflow.com/questions/2829581/why-do-php-array-examples-leave-a-trailing-comma) all along. Oops!
* Instead of using sane notations `[$a, $b] = [$b, $a]` or `array($a, $b) = array($b, $a)`, use `list($a, $b) = array($b, $a)` instead.
* [PHP 5.6](http://php.net/releases/5_6_0.php) introduces most things developers take for granted: `...$argument` packing/unpacking, `Type ...$hinting`, and `**  // exponents`.
* [`php://`](http://php.net/manual/en/wrappers.php.php) is the portal to stdin and stdout, if necessary.
* `define()` is now (5.3) superceded by `const` [because it can now define things in global scope](http://stackoverflow.com/questions/2447791/define-vs-const).
* [It is impossible to catch a warning](http://stackoverflow.com/a/1241751) (or an error, for that matter.) so what PHP people do is create an error handler (`set_error_handler`) that raises exceptions, run the offending code in a try-catch block, and catch the same exception that you throw. After the try-catch block, unset the error handler. "And they say PHP isn't a disaster."
* Despite how it is worded in the docs, `finally` doesn't run if any exception is re-thrown from the `catch` block.
* Use [`hash_equals`](http://php.net/manual/en/function.hash-equals.php) for comparing strings sensitive to timing attack.
* Because PHP is weakly-typed, [any md5 string in the form `0e\d+` will be considered as scientific notation](https://www.reddit.com/r/lolphp/comments/34sxw5/md5240610708_md5qnkcdzo/.compact), causing the `==` operator to compare them as numbers.
* PHP has its own [`realpath_cache`](http://jpauli.github.io/2014/06/30/realpath-cache.html) that may cause problems if you attempt to manipulate the same file more than once in multiple system calls.
* Since PHP cannot have an array with `""` as its key (["you can't have empty strings as property names on an object"](https://www.reddit.com/r/lolphp/comments/42gxxd/decodes_to_empty_but_encodes_to_empty_so_you_cant/) ), [a valid JSON of `{"": ""}` is converted to `{"_empty_": ""}`](https://3v4l.org/Tg6GB).
* 