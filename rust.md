# Wat

* Rust users call themselves [rustaceans](http://www.rustaceans.org/).

# [Ownership, borrowing, and lifetimes](https://doc.rust-lang.org/book/ownership.html)

* Rust ensures that there is exactly one binding to any given resource. So, if you assign `a` to `b`, `a` can no longer be used as a reference to that resource. For example:

```
let v = vec![1, 2, 3];
let v2 = v;
// v can no longer be used
```

* Similarly, if a *function* accepts an argument, then the reference to that resource is transferred to the new function, and the caller can no longer use the same resource.

```
fn take(v: Vec<i32>) { ... }

let v = vec![1, 2, 3];
take(v);
// v can no longer be used
```

* Borrowing does not apply to some primitive types like `i32`, which are copied by value.
