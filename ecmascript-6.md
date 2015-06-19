* [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let), which works much like `var`, has the following differences:
    * `let` declarations are not hoisted.
    * If there's a `var` in an `if` block, it will be declared outside the block [to the nearest function scope](http://ariya.ofilabs.com/2013/05/es6-and-block-scope.html). `let` limits its scope to inside the block (which, if you like brackets, makes some sense)
    * `let`s cannot be declared in the same scope twice. So, you cannot use `let`s in multiple `switch` statements.
    * You can use `for(let i = 0;...)` to limit `i` to the `for` block, and jshint won't complain like it does for `var`.
* [Array comprehension](http://ariya.ofilabs.com/2013/02/es6-and-destructuring-assignment.html):

```
[for (x of ANY_ARRAY) for (y of ANY_ARRAY) for (z of ANY_ARRAY) (x + y + z)];  // unlimited number of `for`s

// these two are the same in what they do:
[console.log(t, a) for ({title: t, author: a} of books)];
[for (book of books) console.log(book.title, book.author)];
```

* Destructuring assignment:

```
var [m, d, y] = [3, 14, 1977];  // need to wrap both in array notation
var [,,y] = [3, 14, 1977];  // can ignore variables you don't need
```

* [Proxies](http://ariya.ofilabs.com/2013/07/es6-and-proxy.html): a virtual wrapper that can handle property reads and changes on the original object.

```
var engineer = { name: 'Joe Sixpack', salary: 50 };
 
var interceptor = {
  set: function (receiver, property, value) {
    console.log(property, 'is changed to', value);
    receiver[property] = value;
  }
};
 
engineer = Proxy(engineer, interceptor);
```

* Spread (packing) and Rest (unpacking):

```
function foo(a, b, ...rest) { /* rest is an array */ }
foo(...[1,2,3,4,5]);
```

* Arrow notation: only `=>`, no `->`, and no context binding.

```
array.map((p) => p * 2);  
array.reduce((p, q) => (p + q));  // example with two arguments
```

* [Default arguments](http://ariya.ofilabs.com/2013/02/es6-and-default-argument.html):

```
function foo(bar=5) {
    console.log(bar);
}
```

* Keyword unpacking: given an object as the argument, using a ["set notation" from CoffeeScript](https://github.com/jashkenas/coffeescript/issues/2427) unpacks them into the scope:

```
function foo({x, y=5}) {  // note: object notation (y:5) is not valid syntax at this particular location
    console.log(x);  // 4
}
foo({x: 4, y: 5})
```

* Generators require that ugly asterisk after `function`:

```
   // The asterisk after `function` means that
   // `objectEntries` is a generator
   function* objectEntries(obj) {
        let propKeys = Reflect.ownKeys(obj);

        for (let propKey of propKeys) {
            // `yield` returns a value and then pauses
            // the generator. Later, execution continues
            // where it was previously paused.
            yield [propKey, obj[propKey]];
        }
    }

    for (let [key,value] of objectEntries(jane)) {
        console.log(`${key}: ${value}`);
    }
```

* Imports and [default imports](http://www.2ality.com/2014/09/es6-modules-final.html) are similar, the only difference being whether the import is wrapped in braces.

```
export default function () { return 4 }
export function foo() { return 5 }
// ---
import CallItAnything, {foo} from 'that_file';
CallItAnything();  // 4
foo();  // 5
```

* You can also `import * from 'a library'`.
* `require('a library')` is slower than imports, as the latter can be optimised statically.
