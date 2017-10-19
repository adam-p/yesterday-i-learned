![](http://i.imgur.com/6Lf1OXl.jpg)

1. ["Type inference"](https://softwareengineering.stackexchange.com/a/184183) in Java means `public <T> T foo(T t) { return t; }` returns whatever type you throw at it. It doesn't do more than that because Java devs really really like typing things out: "...the redundant type serves as valuable documentation..."
1. Annotations can be put in function arguments, like `public void foo(@NonNull int[] bar)`. NonNull is from `android.support.annotation`.
1. "Reflection" from Java's point of view is just [the ability to inspect and dynamically call classes, methods, attributes, etc. at runtime.](https://stackoverflow.com/a/37638/1558430) Simple things like calling a method by name counts as reflection.
1. [Want to install Oracle JDK with no tears?](http://www.webupd8.org/2012/01/install-oracle-java-jdk-7-in-ubuntu-via.html)
1. Less draconian than Haskell: `new Integer`s can be added to `int`s and `float`s.
1. It is `println`, not `printLn`.
1. It is possible to `system.out.println` numbers.
1. `float`s are half the size of `double`s.
1. `float`s (e.g. `3.2f`) and `double`s (e.g. 3.2) [should never be compared directly](http://stackoverflow.com/a/16627869/1558430).
1. "Class within a class" is allowed...
1. ... but inner classes cannot have static members, if they are not themselves static.
1. [No optional parameters](http://stackoverflow.com/a/7428077/1558430), but constructors are overloadable, and can be chained to call itself via `this`.
1. Non-static classes cannot be instantiated inside a static function.
1. [Variable names are case-sensitive](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html).
1. [`|=` is an assignment](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html), which means `foo = foo | that thing`.
1. Subclasses are possible, of course, but [`this` and `super` must be called as the constructor's first statement](http://stackoverflow.com/questions/1168345/why-does-this-and-super-have-to-be-the-first-statement-in-a-constructor)
1. Subclassing syntax: `public SubClass extends SuperClass`
1. [*Groovy*](http://groovy.codehaus.org/Download), i.e. `groovysh`, is **not** a Java REPL. Although most Java code is valid Groovy code, Groovy code is not valid Java code. Differences can be seen here:

```
groovy:000> Boolean.valueOf("true")
===> true
groovy:000> Boolean.valueOf('true')
===> true
```

1. [`varargs`](http://docs.oracle.com/javase/1.5.0/docs/guide/language/varargs.html) are denoted with [`...`](http://stackoverflow.com/questions/5224252/what-are-these-three-dots-in-parameter-types), and can be used *only* in the final argument position.
1. Example `varargs`: `public int foo(int ... params) { }`
1. In a particular case where `varargs` is declared with type `Object`: `public int foo(Object ... params) { }`, `foo` accepts anything.
1. [Everything is passed by value](http://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html); object references do not change outside the function.
1. Strong references are your normal `ObjectClass object = new ObjectClass()`. [Weak references](https://weblogs.java.net/blog/2006/05/04/understanding-weak-references) are references that can be garbage-collected at their own pace, so can sometimes become null. Use WeakReferences by wrapping them: 
    `WeakReference<ObjectClass> = new WeakReference<ObjectClass>(object)`
1. `PhantomReference`s are a special type of `WeakReference`, which is always null.
1. [Java REPL](http://www.javarepl.com/console.html)
1. There isn't a `===` comparison operator.
1. [Static inner classes are exactly like external classes except that they have access to all members of the outer class, regardless of access qualifier](http://stackoverflow.com/a/4848071/1558430).
1. `static {}` in a class [acts as the class constructor](http://stackoverflow.com/questions/2943556/static-block-in-java). It is "a good place to put initialization of static variables."
1. ... in contrast, a `{}` block without the `static` keyword is an instance initializer.
1. `if`, `else if`, `else`, `switch`, `do`, and `while` all work familiarly, except `switch`, which apparently didn't accept Strings until SE 7.
1. `for ( ; ; )` is an infinite loop.
1. [Interfaces](http://docs.oracle.com/javase/tutorial/java/javaOO/classdecl.html): `implements YourInterface1, YourInterface2, ...`
1. [Access modifiers](http://docs.oracle.com/javase/tutorial/java/javaOO/variables.html): `public`, `private`, [and more](http://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
1. Camel case conventions: `ClassName`, [`verbMethodName`](http://docs.oracle.com/javase/tutorial/java/javaOO/methods.html), `attributeName`
1. "You don't have to provide any constructors for your class, but you must be careful when doing this. **The compiler automatically provides a no-argument, default constructor for any class without constructors.**"
1. Functions are not first-class: "The Java programming language doesn't let you pass methods into methods. But you can pass an object into a method and then invoke the object's methods."
1. When accessing class variables, `this` appears to be optional, i.e. `this.foo` works just as well as `foo`.
1. The `this` keyword always means the curernt object, even if the current method is not visibly bound to anything. This is like Python's `self`, except `self` is not specified.
1. [`this`](http://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html) is used to remove ambiguity when the scope has a variable that has the same name as its outer class attribute.
1. A function that accepts `foo(int[] bar)` really accepts an array of ints, which is created using `new int[n]`.
1. The default "nothing" constant is `null`.
1. The de-facto method of freeing something from memory is `something = null`.
1. `try { } catch (Exception e) {}` does not catch undefined variable and attribute accesses, aka [`cannot find symbol`](http://www.roseindia.net/java/java-get-example/cannot-find-symbol.shtml).
1. `;` is required after any non-block statement, including `return`.
1. [Covariant return type](http://en.wikipedia.org/wiki/Covariant_return_type): *a subclassed method can return a subtype of the superclass method's return type*.
1. [Contravariant argument](https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)#Contravariant_method_argument_type): an (unsupported) overloading of a function that accepts a more general argument than its overridden counterpart.
1. [`static final type UPPERCASE_UNDERSCORED`](http://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html) defines constants. It can still be `private`, accessible to only instances of this class.
1. `final` methods cannot be overridden.
1. [Outer classes can only be declared public or package private.](http://docs.oracle.com/javase/tutorial/java/javaOO/nested.html) That is to say, it is either seen, or not seen, by other packages.
1. [Static vs non-static inner classes](http://docs.oracle.com/javase/tutorial/java/javaOO/nested.html): non-static inner classes have access to other outer class members.
1. Instantiating an inner class: `OuterClass.InnerClass innerObject = outerObject.new InnerClass();`, noting that the `new` keyword goes *after* the outer class name.
1. [Shadowing is discouraged](http://stackoverflow.com/questions/1092099/what-is-variable-shadowing-used-for-in-a-java-class)
1. **Enums**: `public enum EnumName { OPTION1, OPTION2, OPTION3, ... }` allows you to use the enum like `EnumName.OPTION1`. Enums do not have instances.
1. All Enum values can be accessed via `EnumName.values()`.
1. [Enums can contain code, variables, and even the void main.](http://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)
1. [Enums should be used where speed is not an issue](http://trevore.com/post/should-I-use-enums-in-Android)
1. [Making `List`s](http://stackoverflow.com/a/858590/1558430)
1. The "com" is [the company website's TLD](http://stackoverflow.com/questions/2125293/java-packages-com-and-org) by convention.
1. [Generics](https://en.wikipedia.org/wiki/Generics_in_Java): `<T>` means "of type T".
1. The [`@Override`](http://stackoverflow.com/a/94447/1558430) denotes "I override a parent method"; whether or not it does anything is up to the compiler.
1. `@Override` "came from" `java.lang` automatically for every file, just like the implied `from exceptions import *` in Python.
1. Interfaces can be private. There are virtual no uses for this case.
1. [JLS = Java Language Specification](http://docs.oracle.com/javase/specs/)
1. A class method that returns an instance of itself is used for chaining. Not memory-efficient; just chaining.
1. A method `public void foo(String...bar)` means that [it accepts an arbitrary number of arguments of type `String`](http://stackoverflow.com/a/3158767/1558430). If used in conjunction with other parameters, this must be placed last.
1. `from a import b` [is impossible](http://stackoverflow.com/q/2447880/1558430). Classes must be imported with their own names.
1. `.java` files compile to `.class` files, which are then packaged into `.jar` (Java ARchive) files.
1. [`.jar` files can also contain media](http://en.wikipedia.org/wiki/JAR_\(file_format\))
1. You can import `blah.blah.blah` without having the actual source code -- as long as you have their `class`es.
1. `@SuppressWarnings("unchecked")` in the code means that you confirm [the generic method/function is doing legal things](http://stackoverflow.com/a/1129812/1558430).
1. `Class.forName`, like PHP's `get_class`, returns the class object called that string. The string needs to be the class' full qualifier.
1. Setters that `return this;` are of the [builder pattern](http://en.wikipedia.org/wiki/Builder_pattern). According to a colleague of yours, doing so instead of `return void;` has no real performance differences.
1. [Beans](http://en.wikipedia.org/wiki/JavaBean) are plain objects that contain many other objects, with their properties all encapsulated in getters and setters. Beans cannot have constructors with arguments.
1. Beans are used for cross-network class transfers.
1. [Autoboxing](http://docs.oracle.com/javase/tutorial/java/data/autoboxing.html): something new since 1.5, automatically treating `1` and `new Integer(1)` as the same thing, instead of a primitive and a class, respectively.
1. `//@formatter:off` and `//@formatter:on` control ranges between which Eclipse does not highlight your code. This had no effect on IDEA.
1. Checked exceptions (anything with the syntax `type methodName throws SomeExceptionClass`) must be caught immediately above its execution stack.
1. Classes that extends `Serializable` all require a unique `private static final long serialVersionUID;` value that allows a deserialized object to know which class along the class tree to deserialize back into.
1. There is no difference between Long's notation, [`l` and `L`](http://stackoverflow.com/a/770017/1558430).
1. If maven is used, `pom.xml` decides what is compiled along as dependencies.
1. It is apparently okay to have a type starting with an `@`, such as [`@Interface`](http://stackoverflow.com/questions/918393)
1. Java-style assertions use the colon, i.e. `assert a == 0: "a is not 0.";`
1. [`getBoolean(thing, prop)`](http://with-example.blogspot.ca/2013/07/booleangetboolean-vs-booleanparseboolean.html) checks if thing.prop is `"true"`; `parseBoolean(thing)` check if `thing` is `"true"` regardless of case.
1. Apparently, empty character literals (`''`) are not allowed. It makes no sense anyhow. Empty string is `""`.
1. The syntax for catching multiple exceptions is `SomeExceptionClass|AnotherExceptionClass`.
1. A method can choose not to catch an exception only if it says it `throws` the same exceptions in its own signature.
1. Need to check for `null` everywhere,
 because Java is a very safe language, obviously.
1. Double curlies (`{{ }}`) creates an [instance instantiation block](http://stackoverflow.com/a/5197741). It is a shorthand for something.
1. Without `this.`, `foo` can either refer to the instance variable `foo`, or the static variable `foo`.
1. [`Map` is an interface](http://stackoverflow.com/a/1348246); `HashMap` is the implementation.
1. Concatenating an `Integer` to a `String` to have it automatically become a string is apparently [bad form](http://stackoverflow.com/a/18648773).
1. When instantiating a typed Map (`Map<String String> foo = new HashMap<String, String>();`), the second `String, String` can be omitted because it is obvious. Then again, most things are obvious in Java, but they cannot be omitted.
1. It is impossible to write `(5).toString()`, because fuck you, and fuck literals. To get a `"5"`, you need `new Integer(5).toString()`, or `Integer.toString(5)`. Update: [there are actually a thousand ways to convert an int to a string](http://javadevnotes.com/java-integer-to-string-examples), but `.toString()` isn't one.
1. It is always possible to `return null` in any function, even if the return type is specified not to be null.
1. Rather than assigning `self = this` or something like that, the outer class can be referenced with [`OuterClass.this`](http://stackoverflow.com/questions/2808501/calling-outer-class-function-from-inner-class) instead.
1. All interfaces are static. `static` is redundant.
1. All interface methods are public. `public` is redundant.
1. [`Void` is not `void`](http://stackoverflow.com/a/10839064), because, again, fuck you. `void` is the type, and `Void` is a thing that holds the type.
1. Because inner classes are visible only within the outer class, [an interface method inside a class like that must be public](http://stackoverflow.com/questions/11639741/java-attempting-to-assign-weaker-access-privilege-error) (or at least better than the base class, I am guessing).
1. Where the memory is used to store primitives [depends on the JDK implementation](http://stackoverflow.com/questions/31608220/where-are-string-objects-when-created-using-tostring-methods-stored-in-memory-in) (and which types). In other words, it is best for you to ignore all this.
1. Adding a method inside an interface will instantly (with a lack of a better term) fuck everyone over because none of the implementations have that new method. To combat this, Java 8 adds [`default type funcName() {...}`](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html) to interface definitions. Of course you'll start to wonder the purpose of interfaces if you can have code in it, but I digress.
1. In between `public` and `void`, you can specify [bounded parameters](https://docs.oracle.com/javase/tutorial/java/generics/bounded.html) that specifies ... superclasses of that type that can be passed in, I guess. Today I have not learned.
1. Prior to Java 7, it was impossible to `switch/case` with a string condition.
1. [`java.util.Date` is actually `Timestamp`, with an underlying implementation of a long.](https://news.ycombinator.com/item?id=14179783) Use something else instead, like jodatime.
1. In Java, when you make a new instance of an interface (say `MyList(List)`), you can say ["I depend on any class that does this stuff"](https://stackoverflow.com/questions/1992384/program-to-an-interface-what-does-it-mean) and write stuff like `List foo = new MyList()`. This is more apparent when you write a function that takes in "collections of anything, as long as it is a collection."
1. Remember static types: splitting a String (`foo.split(",")` or something) results in multiple Strings. That requires the type to be `String[]`.
1. There is a [Java REPL online](http://www.javarepl.com/term.html). There isn't one locally, but you can download java-repl, [whatever that web version uses](https://github.com/albertlatacz/java-repl).
1. There is no `someArray[-1]`. Do it with `someArray[someArray.length - 1]`.
1. The [array literal](https://stackoverflow.com/questions/1200621/how-do-i-declare-and-initialize-an-array-in-java) is done with curly brackets. C does the same thing. Blame C.
1. There's an ["effectively final"](https://stackoverflow.com/questions/20938095/difference-between-final-and-effectively-final) state: A variable or parameter whose value is never changed after it is initialized is effectively final. References to objects are also effectively final, even if the objects themselves change. Effectively final variables do not give compiler errors if they were really declared with `final`.
