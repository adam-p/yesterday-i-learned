* Less draconian than Haskell: `new Integer`s can be added to `int`s and `float`s.
* It is `println`, not `printLn`.
* It is possible to `system.out.println` numbers.
* `float`s are half the size of `double`s.
* `float`s (e.g. `3.2f`) and `double`s (e.g. 3.2) [should never be compared directly](http://stackoverflow.com/a/16627869/1558430).
* "Class within a class" is allowed...
* ... but inner classes cannot have static members, if they are not themselves static.
* [No optional parameters](http://stackoverflow.com/a/7428077/1558430), but constructors are overloadable, and can be chained to call itself via `this`.
* Non-static classes cannot be instantiated inside a static function.
* [Variable names are case-sensitive](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html).
* [`|=` is an assignment](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html), which means `foo = foo | that thing`.
* Subclasses are possible, of course, but [`this` and `super` must be called as the constructor's first statement](http://stackoverflow.com/questions/1168345/why-does-this-and-super-have-to-be-the-first-statement-in-a-constructor)
* Subclassing syntax: `public SubClass extends SuperClass`
* [*Groovy*](http://groovy.codehaus.org/Download) is a Java REPL. It is not the same as Ubuntu's `groovy` package.
* [`varargs`](http://docs.oracle.com/javase/1.5.0/docs/guide/language/varargs.html) are denoted with [`...`](http://stackoverflow.com/questions/5224252/what-are-these-three-dots-in-parameter-types), and can be used *only* in the final argument position.
* Example `varargs`: `public int foo(int ... params) { }`
* In a particular case where `varargs` is declared with type `Object`: `public int foo(Object ... params) { }`, `foo` accepts anything.
* [Everything is passed by value](http://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html); object references do not change outside the function.
* [Java REPL](http://www.javarepl.com/console.html)
* There isn't a `===` comparison operator.
* [Static inner classes are exactly like external classes except that they have access to all members of the outer class, regardless of access qualifier](http://stackoverflow.com/a/4848071/1558430).
* `static {}` in a class [acts as the class constructor](http://stackoverflow.com/questions/2943556/static-block-in-java). It is "a good place to put initialization of static variables."
* 