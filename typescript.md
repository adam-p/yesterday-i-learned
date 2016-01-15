# TypeScript

* Basic syntax: `function name(variable: type): type`

## Types
* Numbers: `number` (according to [the handbook](http://www.typescriptlang.org/Handbook), it is to be in lower case)
* Strings: `string`
* Typed arrays: `number[]`
* The `any` type literally means anything. It may well be omitted; the only use of it is to prevent errors when interacting with JS code.
* `void` is *only* used to denote that a function returns nothing (`undefined` or `null`).

## Interfaces

### Class interfaces

Like in any other sane language, an interface is an abtract class with no code in its methods.

```
interface Foo {
    bar: number;
    setBar(baz: number);
}

class FooImpl implements Foo {
    setBar(baz: number) {  // Only constructor variables can be `private`
        this.bar = baz;
    }
}
```

`Foo` is never compiled to the resulting JS file. As far as the script is concerned, `Foo` never existed.

Classes can themselves have a "static" interface imposed on their constructors:

```
interface Foo {
    new (bar: number);
}
class Foo2 {
    constructor(bar: number) { }
}
var CheckedFoo2: Foo = Foo2;  // This may be a bit messy
var foo2Instance = new CheckedFoo2(1);
```

**Private methods cannot be declared in interfaces. Interfaces can only specify public methods.**

### Function interfaces

The thing that is "function interface" in TS controls what is required of an object that is passed into the function. Say you have

```
function foo(bar: object): number {
    return bar.baz;
}
```

It is implicit that the object `bar` must have an attribute `baz` that is a number. Therefore, it can be expressed as an interface

```
interface Bar {
    baz: number;
    optionalParameter?: boolean;  // If it is supplied, it must be a boolean
}
function foo(bar: Bar): number {
    return bar.baz;
}
```

Interfaces are good for catching typos.
It can also be used this way, on function expressions:
```
interface FuncSignature {
    (foo: string, bar: string): number;
}

// The function needs the same signature as its interface.
var func: FuncSignature = function (foo: string, bar: string): number {
    return 5;
}
```

`var func: FuncSignature` can be saved and used on multiple functions, so you might save some work by doing so.

#### Function subtyping

From [the Handbook](http://www.typescriptlang.org/Handbook#type-compatibility-comparing-two-functions), a variable can be assigned a function, then be assigned another function with fewer [but the same types of remaining] parameters than it:

```
var x = (a: number) => 0;
var y = (b: number, s: string) => 0;

y = x; // "every parameter of x has a corresponding compatible parameter in y, so the assignment is allowed"
x = y; // "y has a required second parameter that x does not have, so the assignment is disallowed"
```

Incidentally, since the handbook talks about 'required parameters', this is valid:

```
var x = (a: number) => 0;
var y = (b: number, s?: string) => 0;  // Optional s

y = x; x = y;
```

### Array interfaces
If for some reason you need to make an interface for an already-typed array, you may:

```
interface StringArray {
    [index: number]: string;
}
var foo: StringArray = ['foo', 'bar'];
```

### Extending interfaces

Like classes, interfaces can be extended using the `extends` keyword.
If you use `extends` as a variable name in your existing JS files, you are an idiot.

### Abstract interfaces
Interfaces do not need to be used by any class before it is used. This example shows an interface `Foo` simply being used to check the ways the variable `c` is used. There is no `C` class.

```
interface Foo {
    bar: number;
}

var c: Foo;
c.bar = 5;
```

## Classes

Classes can have `private members: number;` and `static members: numbers`.
They can also have getters and setters, which downpiles to the same thing in ES6, for which [you may need a shim](http://kangax.github.io/compat-table/es5/#Object.defineProperty).

```
class Foo {
    private _bar: string;
    static kek: number;

    get bar(): string {
        console.log(Foo.kek);  // undefined (which is a number, obviously, since we declared it as such)
        return this._bar;
    }

    set bar(baz: string) {
        this._bar = baz;
    }
}
```

Classes can be extended with multiple superclasses, aka. **Mixins**; but, for some reason, we use the keyword `implements` instead of `extends`.

> This treats the classes as interfaces, and only uses the types behind [the mixin classes] rather than the implementation.

### Classes as interfaces


Classes with only static variables can be interfaces.

```
class Point {
    x: number;
    y: number;
}

interface Point3d extends Point {  // Magic
    z: number;
}
```