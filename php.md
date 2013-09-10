* Did you realise the difference between `||` and `or`, which both exist?
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
