## C

* The variable convention seems to be `underscored_things`.
* *Pointers* (e.g. `int* something`) are something you declare. It *points* to something of the declared type. It should only be assigned addresses (`&something`).
* "Accessing" what a pointer is pointing to uses something like Python's unpacking syntax: if `int* foo` points to something that's `14`, `*foo` gives you `14`.
* A pointer can also be used as if it were a variable. For example, if `*foo` were pointing at something that's 14, you can just `*foo = 50` to change it to 50.
* Declare an array of things: `type var_name[size];`, not `type [size]var_name;`.
* `sizeof` is a thing, and gives you the size of the type, not the object. This means to know how long an array is, you need to do some maths.
* `cin >> any_variable` assigns the variable (including array items) with whatever the user typed in standard in.
* [`O=(int)&O`](https://github.com/duckythescientist/obfuscatedLife/blob/master/remarks.md#int-_2048ointo______): setting a variable equal to the int cast of its memory address is a very short way of generating a random integer.
* [`yada = - ~yada` is equivalent to `++yada` because of 2's complement.](https://github.com/duckythescientist/obfuscatedLife/blob/master/remarks.md#while__-__2048___oo0x41c64e6d123450x7fffffff1024150)
* "Pro tip: when you develop with gcc, don't settle for anything less than `gcc -ansi -pedantic -Wall`" -- [TeMPOraL](https://news.ycombinator.com/item?id=7156405) (`-ansi` being [`c89`](http://stackoverflow.com/questions/10300114/should-i-use-ansi-or-explicit-std-as-compiler-flags))
* "You can go further and specify a particular standard, plus extra warnings not included in -Wall: `gcc -std=gnu99 -pedantic -Wall -Wextra -Werror`" - [nitrogen](https://news.ycombinator.com/item?id=7156405)
* "gcc is 'Gnu Compiler Collection'. If you pass it a C++ file, it will invoke the C++ compiler ('g++') behind the scenes."
* Undeclared variables are implicitly `int`s. This was deprecated after C99, however.
* Writing cross-platform C code: [start from the beginning](http://www.ski-epic.com/source_code_essays/ten_rules_for_writing_cross_platform_c_source_code.html)
* There is such a thing as a [C interpreter](http://www.reddit.com/r/programming/comments/2latu2/c4_c_in_4_functions/clt70uk) and C Scripting... but you probably don't want to do that with `gcc`. `tcc` is a faster choice (`#!/usr/local/bin/tcc -run`)
* `make` can compile a source file directly, like `make file` directly. If the file is called `file.c`, the argument must have its `.c` omitted.
* `Makefile` [tells make what to do in the same directory](http://c.learncodethehardway.org/book/ex2.html). Inside you can specify `CFLAGS`.
* Makefiles must be [indented with tabs](http://stackoverflow.com/questions/2131213/can-you-make-valid-makefiles-without-tab-characters).
* [`CFLAGS="-Wall -Wextra -Werror -std=c99 -pedantic -g3" splint $1 && make $1 ...`](http://stackoverflow.com/a/2574456/1558430).
* [C99](https://en.wikipedia.org/wiki/C99) is stricter than C89; C11 (aka C1X) does not appear to be any stricter.
* [`#include "files"`, and `#include <headers>`.](http://stackoverflow.com/a/50266/1558430)
* [`splint`](http://splint.org/) lints C.
* Splint *really* wants any function calls with unused results to have `(void)` in front of them.
* ~~`puts` is a *nix command.~~
* The only way to write a function that accepts no arguments is to have a `void` in it, i.e. [`rtype func_name(void) { ... }`](http://stackoverflow.com/a/3156437/1558430)
* `main` must [either](http://stackoverflow.com/questions/3156423/why-dont-we-use-void-in-main#comment3246503_3156423) take nothing (`void`), or exactly these two parameters: `int argc, char* argv[]`, and return an `int`.
* `$()` in Makefile is [more portable](http://stackoverflow.com/questions/2214575/passing-arguments-to-make-run#comment2167270_2214593) than `${}`.
* Valgrind the debugger does various checks after compilation. It needs the `-g` flag for CC above to be set.
* `//` commenting must not be used.
* `printf` and co. expect `%f` to actually be `double`, not `float`.
* [`float` requires a trailing `f`](http://stackoverflow.com/a/5026592/1558430); `double` does not. This means all number literals with decimal points are doubles. However, it is possible, for some reason, to assign `float to_a_doule = 10.0`, or `double from_a_float = 10.0f`.
* `long` requires a trailing capital `L`, and its formatting string is `%ld` ('long number').
* `%e` (scientific notation) should only be used on `double`s.
* For whatever reason, `[]` is used to denote arrays; `{}` is used to express an array literal.
* [If you omit the size of the array, an array just big enough to hold the initialization is created.](http://www.tutorialspoint.com/cprogramming/c_arrays.htm)
* Splint disallows `an_array[10]` to be initialised with an array that is not 10 items long. If Splint isn't there, then the array default is 0.
* There is no point writing different code for array access. [Compilers know.](http://stackoverflow.com/questions/4939834/in-c-accessing-my-array-index-is-faster-or-accessing-by-pointer-is-faster)
* [`sizeof an_array`](http://stackoverflow.com/a/204232/1558430) tells you the size of the array, *or* the size of its pointer, [depending on where you got it](http://stackoverflow.com/a/10349610/1558430). ["the usual solution is to pass the length along with the array as a separate argument."](http://stackoverflow.com/questions/37538/how-do-i-determine-the-size-of-my-array-in-c#comment28408105_10349610) (which `argc` is)
* [A bug in Splint](http://stackoverflow.com/questions/10257470/splint-parse-error-in-for-loop) causes variable initialisation inside a for loop to be impossible.
* Strings are `char[]`s or `*char`s. They **must** be manually terminated with [a null byte (`\0`)](http://stackoverflow.com/questions/18688971/c-char-array-initialization#comment27531014_18688992), or Valgrind will complain.
* Arrays of strings are `char[][]`, `*char[]`, or ... `**char` (?), where `char[number of strings][size of each string]`
* [`auto`](http://stackoverflow.com/questions/2192547/where-is-the-c-auto-keyword-used) makes a variable have a function-local lifetime, which is the default. `static` cannot be used.
* The `*` in `int *foo` is attached to the variable. [`int* foo` is invalid syntax.](http://stackoverflow.com/a/4203080/1558430)
* It is [not possible](http://stackoverflow.com/a/4203948/1558430) to declare multiple variables on the same line, because Code Complete says so.
* [Include guards](https://en.wikipedia.org/wiki/Include_guard) prevent the same header from being included more than once. [`#pragma once`](https://en.wikipedia.org/wiki/Pragma_once) works better [in every way](http://stackoverflow.com/a/6793411/1558430). Unfortuntely, since Oracle doesn't support pragma once, we are [stuck](http://stackoverflow.com/a/1144110/1558430) with include guards.
* There are [only three error codes](https://en.wikipedia.org/wiki/Errno.h) you can use.
* > ["The `.PHONY` rule keeps make from doing something with a file named `clean`."](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/) By not looking for files called `clean`, it improves performance.
* [`main` must be a function.](http://stackoverflow.com/questions/33305574/why-does-const-int-main-195-result-in-a-working-program-but-without-the-const) Don't let anyone tell you different.
* When creating an array of a given type, a continuous chunk of memory is assigned, exactly (the size of the type) * (the number of things).
* [Given the way arrays are created](http://stackoverflow.com/questions/381542/with-c-arrays-why-is-it-the-case-that-a5-5a), `foo[4]` is really `*(foo + 4)` or `*(4 + foo)`, which makes `4[foo]` equivalent.
* `thing_t` is supposed to mean "a type called 'thing'". C programmers are against the Hungarian notation.
* [C pointers are not integers](http://nullprogram.com/blog/2016/05/30/); Any pointer type may be converted to an integer type, but the result depends on implementation. (If the pointer is a large negative number, for example, then the behaviour is undefined.)
* 

## C++

* The [`~ClassName`](http://stackoverflow.com/a/1395509/1558430) definition in a class denotes a destructor, because `ClassName` initially is a constructor, but negated by `~` to give the semantic meaning of a destructor. 
* `public:` followed by an indented block of methods, means that anything inside the block is public (same applies to `private`)

```
class Rectangle {
    int width, height;
    public:
        void set_values (int,int);
        int area() {
            return width*height;
        }
};  // semicolon?
```

* [Trigraphs](http://stackoverflow.com/questions/7825055/what-does-the-c-operator-do) are character mappings that map three characters to a single one, not found on older keyboards. For example, "??!" maps to "|".
* You are supposed to use [Smart pointers](http://en.wikipedia.org/wiki/Smart_pointer) now (C++11), which manages memory allocation for you. You should never (supposedly) create references to objects like in C# and Java either; just create objects and C++ will manage the memory for you.
* Operators can be overloaded; for example, to overload `+` for adding two `Class`es together, use `Class operator+(const Class&, const Class&);`
* [Function overloading](https://www.reddit.com/r/programming/comments/3en2px/til_you_can_use_function_overloading_in_c/) is not a standard feature in C, but you can do it in C11 in an ugly way.
* [Ugly (yet valid) C syntax](http://blog.robertelder.org/weird-c-syntax/):
    * Inline return type definitions are possible: `struct foo {...} function () { return foo(...) }`
    * Returning pointers to functions, where `foo` takes in nothing, and returns a function `bar` that takes an int and returns an int: `int ( *foo(void) ) (int i) {  return bar }`
    * [`"Hello"[5] == 5["Hello"]`.](http://stackoverflow.com/a/381549/1558430)
* You can still specify the namespace, `foo::some_func()`, in a file/method `using namespace foo`.
* `std::cout` is [more proper](http://stackoverflow.com/a/4781861/1558430) than `printf` in C++.
* If your header files are C++ only, [name them `.hpp`](http://stackoverflow.com/questions/152555/h-or-hpp-for-your-class-definitions). Otherwise, header files that can be used for both C and C++ should use `.h`.
* C++ struct values can have defaults:

```
struct Foo {
    int no_default;
    int yes_default = 0;
};
```

* There is [struct inheritance](http://stackoverflow.com/questions/979211/struct-inheritance-in-c). Use the colon to denote structs with all fields in the parent struct:

```
struct A { };
struct B : A { };  // Has all A's fields
```

* > [In C++, a struct can have methods, inheritance, etc. just like a C++ class.](http://stackoverflow.com/a/979241/1558430)
* It is possible--get this--to redefine a class/instance method. Instead of using [interfaces](http://www.tutorialspoint.com/cplusplus/cpp_interfaces.htm) like normal humans would (hint: they don't exist), you may define a class in the header, then change the definition of the class.
* According to your colleagues, `new Something()` gives you a pointer to something, whereas `Something()` gives you the exact thing. For the case of `std::string`, [this helpful post](http://stackoverflow.com/questions/8069092/c-string-declaration) explains **four** variants:

```
1. `std::string s = std::string("foo");  // creates a temporary std::string object containing "foo", then assigns it to s`
2. `std::string s = "foo";`  // equivalent to 1. Internally, this runs one of the constructors in std::string that accepts const char*.
3. `std::string s = new std::string("foo"); // compiler error while trying to assign a pointer to a variable of type std::string`
4. `std::string s("foo");`
```
> "One of the main benefits of using std::string is that it manages the underlying string buffer for you automatically, so new-ing it kind of defeats that purpose."
* Function/method names are [`UpperCamelCase`](https://google.github.io/styleguide/cppguide.html#Function_Names), unless they are cheap, (e.g.) "so cheap that you normally wouldn't bother caching its return value when calling it in a loop", in which case they are `underscored_things`; such a function normally consists of only one comparison.
* [`do {...} while (0)`](http://www.pixelstech.net/article/1390482950-do-%7B-%7D-while-%280%29-in-macros) is the de facto way of writing a macro that expands correctly, whether in a one-liner if statement, or in an if-else.
* Macros are not substituted in macros. (Otherwise `#ifdef`s will get complicated)
* Headers can contain other headers, but should not.
* Rule: When addressing compile errors in your programs, always resolve the first error produced first.
* Compared to arrays, **vectors** consume more memory in exchange for the ability to manage storage and [grow dynamically](http://stackoverflow.com/a/6632991/1558430) in an efficient way. Use vector unless you have a very, very small array, and know what you are doing.
* If both a `<foo>` and `<foo.h>` exists, then the `.h` version is deprecated. Use the non-h version.
