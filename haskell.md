* Integers and Strings are still `5` and `"chris"`. No weird syntax so far.
* `/=` appears to mean "not equal".
* `sort [1,2,3]` sorts values ascending. So, that does nothing.
* `sort "abc"` also works.
* There are tuples. `()` This means function calls are not wrapped in parens.
* `fst (1,2)` gets the *first* item, 1, apparently.
* `let var = expression in body` creates a local scope. It assigns nothing to `var`. That is to say,

```
let x = 8 * 10 in x + x      # with (x = 80)
=> 160                       #    yield x + x
```

* The *cons* (unshift) function: `(:)`. `'a' : []` means `[]` *cons* `'a'`, which yields `["a"]`. Whitespace between `:` matters.
* Likewise, `'a' : 'b' : []` is just "given [], cons b, then cons a". Imagine parentheses.
* `==` compares equality. Err, `['1', '2', '3'] == '123'`.
* map (+1) [1..5] does exactly what it reads.
