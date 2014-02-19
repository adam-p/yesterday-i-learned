![repo logo](http://www.ohai.ca/images/yesterday-i-learned.jpg)

* Integers and Strings are still `5` and `"chris"`. No weird syntax so far.
* Strings are lists of Chars. You can make them by consing many Chars together if you want.
* `5` is an expression. Its value is `5`.
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
* That is, `a : b` means `(cons a b)`.
* Likewise, `'a' : 'b' : []` is just "given [], cons b, then cons a". Imagine parentheses.
* Now that `:` means cons, `0:[1, 2]` equals `[0, 1, 2]`.
* You can build an empty list by consing a bunch of stuff to `[]`, e.g. `1:2:3:[] == [1, 2, 3]`
* Lists must contain items of the same type.
* `==` compares equality. Err, `['1', '2', '3'] == '123'`.
* map (+1) [1..5] does exactly what it reads.
* `$ ghci` gives you `Prelude> `. o_O
* Hugs is faster than GHC, but doesn't allow function definitions in the environment. (That is to say, it is not complete.)
* Haskell is a *lazy* language, where nothing is computed unless it is forced to. That is useful for dealing with 'infinite' things like a list from 0 to infinity.
* Lazy languages in general call by name, instead of call by value.
* Haskell is case-sensitive. "Haskell actually uses case to give meaning."
* That is, variables/functions must begin in lower case, and types must begin in upper case.
* Strings are not the same as characters. Like Java, they differentiate literally by double and single quotes.
* *Pure* functions are functions without side effects. A stricter sense of it is if the function always produces the same result.
* Variables are not memory addresses; they are *names*. You cannot make something else called that (e.g. `x = x + 1` is illegal); that which was named was that.
* Referential Transparency: because Haskell is so strict, that if two functions produce the same result, the two functions are interchangeable.
* `(sqrt 2)`, `sqrt 2`, and `sqrt(2)` all produce the same result. "Even though parentheses are not always needed, sometimes it is better to leave them in anyway; other people will probably have to read your code"
* There seems to be no limit to the size of a number (try `2^5000`), but there is a limit to the number of decimal points (try `1/that number`)
* The 3-item term for tuple is *triple*. 
* Tuples look the same as ones in Python.
* `head` and `tail` is Haskell's way of saying `first` and `rest` in Scheme.
* Concatenation. `"Hello " ++ "World"` == `"Hello World"`
* `show()` turns anything into Strings.
* `read()` turns strings into anything. HOWEVER, it does so only if it knows what to convert to, say `read("123") + 1` == 124
* `foldr()`? reduceRight. `foldl()`? reduce. Reduce is probably what you had in mind.
* `foldr (-) 1 [4, 8, 5] = 4 - (foldr (-) 1 [8, 5]) = 4 - (8 - (5 - foldr (-) 1 [])) = (4 - (8 - (5 - 1)) = 0`
* `foldl` is faster, but `foldr` can work with infinite lists (????)
* In a file, `module Foo where` defines a module called `Foo`.
* `:l Foo` loads module `Foo`.
* A standalone program `Main` must have a method `main` inside it. However, the file need not be "Main.hs".
* `ghc Foo.hs` only compiles a `Foo.hi` file. You need `ghc --make Foo.hs -o foo`. After that, `Test` is an executable.
* `square x = x * x` means "square is a function that takes x in and returns x * x".
* `If` conditionals are done in line-broken one-liners. `foo x = if x < 0 then -1 else 2`
* `-1` cannot be used as a function parameter because `foo -1` could have meant `foo - 1`. Use `foo(-1)` instead.
* It is impossible to have an `if` statement with no `else`.
* Switch cases, what they look like, and what `_` means in them.

```
f x =
    case x of {
        0 -> 1;
        1 -> 5;
        2 -> 2;
        _ -> -1
    }

(braces, semicolons optional but encouraged)
```

* Tabs and space indentations are actually encouraged to be 8 spaces long.
* Functions can be defined piecewise, a bit like overloading.

```
foo 0 = 1
foo 1 = 3
foo 2 = 9001
foo _ = 0
```

* `(foo . bar) 123` is mathematical notation for `foo(bar(123))`.
* `null lst` checks if a list `lst` is empty.

