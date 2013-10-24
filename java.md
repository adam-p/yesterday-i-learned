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
* ... in contrast, a `{}` block without the `static` keyword is an instance initializer.
* `if`, `else if`, `else`, `switch`, `do`, and `while` all work familiarly, except `switch`, which apparently didn't accept Strings until SE 7.
* `for ( ; ; )` is an infinite loop.
* [Interfaces](http://docs.oracle.com/javase/tutorial/java/javaOO/classdecl.html): `implements YourInterface1, YourInterface2, ...`
* [Access modifiers](http://docs.oracle.com/javase/tutorial/java/javaOO/variables.html): `public`, `private`, [and more](http://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
* Camel case conventions: `ClassName`, [`verbMethodName`](http://docs.oracle.com/javase/tutorial/java/javaOO/methods.html), `attributeName`
* "You don't have to provide any constructors for your class, but you must be careful when doing this. **The compiler automatically provides a no-argument, default constructor for any class without constructors.**"
* Functions are not first-class: "The Java programming language doesn't let you pass methods into methods. But you can pass an object into a method and then invoke the object's methods."
* When accessing class variables, `this` appears to be optional, i.e. `this.foo` works just as well as `foo`.
* [`this`](http://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html) is used to remove ambiguity when the scope has a variable that has the same name as its outer class attribute.
* A function that accepts `foo(int[] bar)` really accepts an array of ints, which is created using `new int[n]`.
* The default "nothing" constant is `null`.
* The de-facto method of freeing something from memory is `something = null`.
* `try { } catch (Exception e) {}` does not catch undefined variable and attribute accesses, aka [`cannot find symbol`](http://www.roseindia.net/java/java-get-example/cannot-find-symbol.shtml).
* `;` is required after any non-block statement, including `return`.
* [Covariant return type](http://en.wikipedia.org/wiki/Covariant_return_type): *a subclassed method can return a subtype of the superclass method's return type*.
* [Contravariant argument](https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)#Contravariant_method_argument_type): an (unsupported) overloading of a function that accepts a more general argument than its overridden counterpart.
* [`static final type UPPERCASE_UNDERSCORED`](http://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html) defines constants. It can still be `private`, accessible to only instances of this class.
* `final` methods cannot be overridden.
* [Outer classes can only be declared public or package private.](http://docs.oracle.com/javase/tutorial/java/javaOO/nested.html) That is to say, it is either seen, or not seen, by other packages.
* [Static vs non-static inner classes](http://docs.oracle.com/javase/tutorial/java/javaOO/nested.html): non-static inner classes have access to other outer class members.
* Instantiating an inner class: `OuterClass.InnerClass innerObject = outerObject.new InnerClass();`, noting that the `new` keyword goes *after* the outer class name.
* [Shadowing is discouraged](http://stackoverflow.com/questions/1092099/what-is-variable-shadowing-used-for-in-a-java-class)
* **Enums**: `public enum EnumName { OPTION1, OPTION2, OPTION3, ... }` allows you to use the enum like `EnumName.OPTION1`. Enums do not have instances.
* All Enum values can be accessed via `EnumName.values()`.
* [Enums can contain code, variables, and even the void main.](http://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)
* [Making `List`s](http://stackoverflow.com/a/858590/1558430)
* [Generics](https://en.wikipedia.org/wiki/Generics_in_Java): `<T>` means "of type T".

