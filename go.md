## Imports

```
import "foo"
import "bar"

import (  // "Factored" import style is recommended
    "foo"
    "bar"
)
```

* If you `import ("package1" "package2")` etc, you can use the symbol `package1` in the namespace.
* The `foo` in `"package1/foo"` refers to the module that begins with `package foo`. If you do that, `foo` will be in the namespace.
* [In Go, a name is exported if it begins with a capital letter.](https://tour.golang.org/basics/3). This is why `fmt.Println` look stupid.

## Comments

```
// comment
```

## Data types

[Common primitive types](https://tour.golang.org/basics/11): `bool` (default `false`), `string` (default `""`), `int`, `uint`, `byte`, `float64`, `complex128` (default `0`)

To convert a type to another, use type cast

```
var i int = 0
var foo float64 = float64(int)  // or foo := float64(int)
```

* `<<` shifts the bit. `1 << 10` is 1024.

## Entry point

```
package main

func main() {
    // here
}
```

## [Functions](https://tour.golang.org/basics/4)

```
func something(x int, y int) int {  // Same as func something(x, y int) int
    // type comes after the variable name.
    return x + y
}

function two_arguments(foo int, bar int) (int, int) {  // Declare return types of each item
    return foo, bar
}
```

### [Variables](https://tour.golang.org/basics/10) and [Destructured assignment](https://tour.golang.org/basics/6)

```
var foo, bar, baz bool  // type is last
var foo, bar = 0, false  // type -can- be omitted if values are given

foo, bar := two_arguments("hello", "world")  // Use `:=` to assign with the implied type

// you can also infer an infer
baz := bar

```
#### [Constants](https://tour.golang.org/basics/15)

* `const` instead of `var`
* No `:=` assignment; however, since constants can only be character, string, boolean, or numeric values, they will be inferred.
* Convention seems to be `CapitalizedVariableName`.

### [Naked return](https://tour.golang.org/basics/7)

Just typing `return` returns all of its declared variables at the point.
Naked return statements should be avoided to improve readability.

```
func foo(bar int) (x, y int) {  // If a function says it returns x and y...
    x = 1
    y = 2
    return  // ... it returns x and y.
}
```

### `defer`

`defer something()` runs after the rest of the function completes.
You cannot have compound statements like `defer something(); something_else()` but you can have multiple defers, where the [defers are run in reverse order](https://tour.golang.org/flowcontrol/13) (stack).

```
defer fmt.Println("world")
defer fmt.Println("poop")
fmt.Println("hello")

// Prints "hello poop world"
```

## Flow control

* `for` is the only loop. 
    * `for i = 0; i < 10; i++ { ... }` is a for loop.
    * `for i < 10 { ... }` is a while loop.
    * `for { ... }` is an infinite loop.
* `if`
    * `if something { ... }`
    * To initialize an if-scope variable in the if loop: `if foo := assignment_first; something { ... }`
    * [That `foo` is also available in `else`.](https://tour.golang.org/flowcontrol/7)
* `switch`
    * `switch condition { ... }`
    * `switch { ... }` is `switch true { ... }`.
    * `case "something":`
    * [A case body breaks automatically, unless it ends with a `fallthrough` statement.](https://tour.golang.org/flowcontrol/9)
    * Cases can contain function calls.
    

* `NaCl` is apparently [native client](http://talks.golang.org/2014/go1.3.slide#11).
* Go makes use of [Duff's devices](http://en.wikipedia.org/wiki/Duff%27s_device) to unroll loops. Performance benchmarks can be found in the [actual commit](https://github.com/golang/go/commit/6c7cbf086c34ebb88311ba12d3a75adcbdce8ac8). "Loop unrolling revolves around lowering the number of branches made, by batching them together.", and comes at the [cost of file size](http://en.wikipedia.org/wiki/Loop_unrolling).
