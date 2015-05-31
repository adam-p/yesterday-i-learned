* *Pointers* (e.g. `int* something`) are something you declare. It *points* to something of the declared type. It should only be assigned addresses (`&something`).
* "Accessing" what a pointer is pointing to uses something like Python's unpacking syntax: if `int* foo` points to something that's `14`, `*foo` gives you `14`.
* A pointer can also be used as if it were a variable. For example, if `*foo` were pointing at something that's 14, you can just `*foo = 50` to change it to 50.
* Declare an array of things: `type var_name[size];`, not `type [size]var_name;`.
* `cin >> any_variable` assigns the variable (including array items) with whatever the user typed in standard in.
* [`O=(int)&O`](https://github.com/duckythescientist/obfuscatedLife/blob/master/remarks.md#int-_2048ointo______): setting a variable equal to the int cast of its memory address is a very short way of generating a random integer.
* [`yada = - ~yada` is equivalent to `++yada` because of 2's complement.](https://github.com/duckythescientist/obfuscatedLife/blob/master/remarks.md#while__-__2048___oo0x41c64e6d123450x7fffffff1024150)
* "Pro tip: when you develop with gcc, don't settle for anything less than `gcc -ansi -pedantic -Wall`" -- [TeMPOraL](https://news.ycombinator.com/item?id=7156405)
* "You can go further and specify a particular standard, plus extra warnings not included in -Wall: `gcc -std=gnu99 -pedantic -Wall -Wextra -Werror`" - [nitrogen](https://news.ycombinator.com/item?id=7156405)
* "gcc is 'Gnu Compiler Collection'. If you pass it a C++ file, it will invoke the C++ compiler ('g++') behind the scenes."
* Undeclared variables are implicitly `int`s. This was deprecated after C99, however.
* Writing cross-platform C code: [start from the beginning](http://www.ski-epic.com/source_code_essays/ten_rules_for_writing_cross_platform_c_source_code.html)
* There is such a thing as a [C interpreter](http://www.reddit.com/r/programming/comments/2latu2/c4_c_in_4_functions/clt70uk) and C Scripting... but you probably don't want to do that with `gcc`. `tcc` is a faster choice (`#!/usr/local/bin/tcc -run`)

## C++

* The variable convention seems to be `underscored_things`.
* `sizeof` is a thing (maybe for C, as well)
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
