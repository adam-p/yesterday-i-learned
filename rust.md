# Wast

![](http://powersmashrepairs.com.au/wp-content/uploads/2011/10/car-rust.png)

Rust is a systems programming language. It is not a general-purpose language and should not be treated as one.

* Rust users call themselves [rustaceans](http://www.rustaceans.org/).

# [Ownership, borrowing, and lifetimes](https://doc.rust-lang.org/book/ownership.html)

> [To borrow a value, you make a reference to it (a kind of pointer), using the & operator.](https://blog.rust-lang.org/2015/04/10/Fearless-Concurrency.html)

* Rust ensures that there is exactly one binding to any given resource. So, if you assign `a` to `b`, `a` can no longer be used as a reference to that resource. For example:

    let v = vec![1, 2, 3];
    let v2 = v;
    // v can no longer be used

* Similarly, if a *function* accepts an argument, then the reference to that resource is transferred to the new function, and the caller can no longer use the same resource.

    fn take(v: Vec<i32>) { ... }

    let v = vec![1, 2, 3];
    take(v);
    // v can no longer be used

* Borrowing does not apply to some primitive types like `i32`, which are copied by value.

* Resources can either be borrowed as immutable (`&`, default) or mutable (`&mut`). Once borrowed as mutable, the same resource cannot be borrowed again at the same time. (This implies multiple immutable borrows can coexist.)

    (&vec, &mut vec)  // Dies
