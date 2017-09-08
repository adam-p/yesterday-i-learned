1. [Ruby has clearly lost the language war.](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) "We’re not looking to contribute to any language war," David added.
1. In Ruby, you put docstrings outside.
1. Methods do not require `()` to call. WTF?
1. Methods that end in `?` are boolean functions by [pure convention](http://stackoverflow.com/a/1345855).
1. And because boolean functions are purely by convention, this also means they can accept parameters: `@foo.bar?('baz')`
1. `?F` apparently means [`"F".ord`](http://stackoverflow.com/a/1878406) for Ruby < 1.9, and just `"F"` in Ruby 1.9+.
1. `!` after a method applies changes the current object. So `a.upcase!` means `a = a.upcase`.
1. `.chomp`, which often follows `gets`, removes the extra line at the end of console inputs.
1. "Ruby prioritizes programmer productivity over program optimization."
1. `if`, `elsif`, `else`, `end`, because `elseif` is just too long (but `elif` is too Python, presumably). No need for `:` at the end of each condition.
  * Because if statements can be multi-line, it can be written in any form of indentation: `b = a? 5 else 3 end`, where `end` is required if you didn't oneliner it.
1. Integer instantiation is `Integer(something)`.
1. `a_string.gsub(/regex/, "what")`
1. `while` is the same everywhere, except you need `end`. No `:` needed.
1. `until` is the backwards `while` (executing while the check is false)
1. There's no `++`, but there's still `+= 1`.
1. `Hash.new(0)` creates a `defaultdict`-like object, whose initial values are `0`s.
1. `Hash` has [some `sort_by` thing](http://gayleforce.wordpress.com/2009/09/28/ruby-sorting-1-when-and-why-to-use-sort_by/) which has some weird `|a, b| b` array syntax.
1. `nil` is all lower case.
1. `an_array.each { |x| puts "#{x}\n" }` is totally possible.
1. Hashes (dicts): the syntax is `{ a => b}`
1. All ruby methods are available via `something.methods.sort`.
1. All ruby methods specific to an object are avaiable via `something.own_methods.sort`.
1. The Ruby REPL is `irb`.
1. [Ruby doesn't have functions](http://stackoverflow.com/a/4294660/1558430); to get a reference to a callable without calling it, use `func_ref = method(:func_name)` or `method_ref = instance.method(:method_name)`, and call with `func_ref.call`.
1. It would have been nice to have said that Ruby method names are also symbols.
1. Any class method automatically has a `self` (also `@`; see below) for the instance, but you can [rebind](http://ruby-doc.org/core-1.9.3/UnboundMethod.html) it with `reference_to_method.bind(some_other_instance)`. It doesn't mean the instance now has that method; it just means you are calling the method with another instance.
1. [`@foo` directly accesses an attribute.](http://stackoverflow.com/a/1693319). `self.foo` accesses it first through a `def foo`, if one exists, then falls back to `@foo`.
1. Results from the last expression is returned.
1. Ruby's `foldr` is called [`inject`](http://blog.jayfields.com/2008/03/ruby-inject.html) (if you use it this way).
1. [The `do` block has lower precedence than the bracket block syntax](http://stackoverflow.com/a/2122457/1558430), allowing you to do concise loops in some cases:

```
1.upto 3 do |x|
    puts x
end

1.upto 3 { |x| puts x }
# SyntaxError: compile error
```

1. From above, "A [`do`] block is like an anonymous function or lambda. The variable between *pipe characters* is the parameter for this block."
1. I think functions can themselves be instances. `def something ... ... @names` is perfectly valid syntax.
1. `def`s need `end`s.
1. The Ruby equivalent of `if __name__ == '__FILE__'` is `if __FILE__ == $0`.
1. `some_obj.respond_to?(attribute)` is a special method that checks if an object has that attribute (or method, which is about the same for Ruby).
1. Having a `attr_accessor :name` line in a class creates automatic getters and setters for every instance's `name`, or `@name`.
1. `def initialize` is the... uh... coffeescript? php? version for Ruby.
1. Since `nil` is Ruby's `None`, `.nil?` is the same as `(... is None)`.
1. You *can* have double quotes in interpolated, doubled quoted strings! [The guide](https://www.ruby-lang.org/en/documentation/quickstart/3/)'s example was `puts "Goodbye #{@names.join(", ")}.  Come back soon!"`
1. `Class.new(...)` returns an instance. Because of Ruby's *awesome* bracket omission, `Class.new` also returns one, with no parameters given to the constructor.
1. To be consistent with their OOP philosophy, `sprintf` is a global function.
1. In a class, putting `private` somewhere in it [makes *everything below that line* private](http://en.wikibooks.org/wiki/Ruby_Programming/Syntax/Classes#Private).
1. Assuming `:method` is the syntax used to access the class method called `method`, `private :method` marks it as private, if put *underneath* the declaration for `method`.
1. [The "double at" (`@@foo`)](http://stackoverflow.com/questions/5890118/what-does-variable-mean-in-ruby) is a class variable, making your previous point false.
1. [The "double less than" (`class << instance`)](http://stackoverflow.com/questions/6182628/ruby-class-inheritance-what-is-double-less-than) adds all methods in that class to a particular instance of some other class, probably because there is no `instance.extend(class.__dict__)` equivalent.
1. Instead of `self.__class__`, it is [`self.class`](http://stackoverflow.com/a/2527911/1558430). `self` is not a named parameter.
1. Functions are not hoisted.
1. Whitespace in blocks doesn't matter. Well, because there is a required `end` keyword.
1. `func do |arg1| ... end` is essentially `genr = func(); (cb(arg1) for arg1 in genr)`, if `func` is a generator function that uses `yield` (and only works with `yield`).
1. Lists can turn into the `func` above by calling `.each`, i.e.`[1,2,3,4].each do |i| ...`
1. ["With blocks"]() are also done using blocks in Ruby:

```
File.open('somefile.txt') do |f|
    puts f.readline
end
```

1. One-liner if statements have the following syntax: `condition ? true : false` (no if, no else)
1. One-liner blocks are also possible. `[1,2,3,4].map{|i| i + 1}` is a block that is acting as a lambda.
1. List filters using `select` and blocks: `[1,2,3,4].select{|i| i % 2 == 0}`
  * `a_list.select(&:foo?)` uses `&` and `Symbol#to_proc` to filter out items in the list whose method `foo?` isn't falsy.
1. Because methods are immediately invoked, obtaining an attribute from it is also an invocation. However:

```
sentence.split.length  # fine
sentence.split().length()  # fine
sentence().split.length  # not fine, strings (or maybe some things just) aren't callable
```

1. The last-run statement in a function is the return value. Guess where coffeescript got this from!
1. There's apparently a `for ... in` syntax, but [nobody uses it, claims redditor.](http://www.reddit.com/r/Python/comments/1k74jb/ruby_vs_python/cbm62q6)
1. `print` is a thing, and `puts` is a thing too. Their equivalents are `print foo,` and `print foo`.
1. `is_a` and `kind_of` are the same method: true if the object is an instance of that class or its subclasses. [`instance_of`](http://stackoverflow.com/a/3893305/1558430), on the other hand, checks for its exact class.
1. [Symbols](http://www.troubleshooters.com/codecorn/ruby/symbols.htm#_What_do_symbols_look_like) are pairs of ids and immutable strings. They look like `:this`, and have performance benefits because of their immutability.
1. Use symbols [whenever you would use a constant](http://stackoverflow.com/a/16621092/1558430), including [dictionary keys](https://github.com/mislav/will_paginate/blob/master/lib/will_paginate.rb).
1. In Ruby 1.9+, [dictionaries whose keys are symbols don't need to use the `=>` association syntax](http://breakthebit.org/post/8453341914/ruby-19-and-the-new-hash-syntax). Use the more "normal" syntax instead: `{simon: "Talek", lorem: "Ipsum"}`
1. Not until Ruby 2.2 did it [GC symbols](https://bugs.ruby-lang.org/issues/7791), creating security issues for Rails sites.
1. The `gem` thing lets you list available versions if you provide two flags: `gem list package_name --remote --all`
1. `[a..b]` includes the `b`th element. `[a...b]` does not. This makes `[a...b]` the [formally correct slicing operator](https://blog.nelhage.com/2015/08/indices-point-between-elements/).
1. There is the `||=` operator, which is actually intuitive: `a = a || ...`
1. [`&:`](http://stackoverflow.com/questions/1961030/ruby-ampersand-colon-shortcut) is the pluck shortcut, which means `|thing| thing.foo`. "The `&` calls `Symbol#to_proc` on the object, and passes it as a block to the method." `:foo`, which is a Symbol, is what gets passed into the method.
1. [Ruby also does the whole `defined?` thing](https://github.com/mislav/will_paginate/blob/master/init.rb) that PHP does. `defined?` appears to be a top-level global, and accepts any class in any namespace.
1. Ruby try/catch/else/finally blocks are named [`begin/rescue/else/ensure`](http://rubylearning.com/satishtalim/ruby_exceptions.html). Because there is no `as`, the exception is assigned with the association syntax (that's right) `rescue SomeExceptionClass => some_variable`
1. There are also `(*positional_arguments)`, `(default=value)`, and  in Ruby 2. There is also `(required_keyword_argument:,  **everything_else)` in Ruby 2.1.
1. A special version of double splat is `(**_)`, which means you ignore all unexpected arguments.
1. Call a function with keyword arguments using a colon instead of equals. `foo(bar: 100)`
1. This also means the minimum Ruby version you should run is 2.
1. `super` (the word) is `super()`.
1. [Single-quoted strings are like Python's `r"raw strings"`.](https://www.ruby-lang.org/en/documentation/ruby-from-other-languages/to-ruby-from-python/)
1. "Python prevents modification of built-ins — Ruby does not."
1. Only `false` and `nil` are falsy. Everything else, including `0` and `0.0`, is truthy.
1. There is no `del`, but you can set something to `nil`. Referencing something that has been set to `nil` never raises `NameError`, however.
1. [`=~` is "matches"](http://programmers.stackexchange.com/questions/46584/what-should-a-python-developer-know-while-learning-ruby): `if mystring =~ /^\s+hello word!/`
1. [A constant is a thing starting with upper case](http://www.local-guru.net/blog/2009/2/10/ruby-symbols-vs-string-vs-constant) and they can be modified. That's right.
1. [The `require()` method is quite similar to `load()`, but it’s meant for a different purpose. You use `load()` to execute code, and you use `require()` to import libraries.](http://stackoverflow.com/questions/318144/what-is-the-difference-between-include-and-require-in-ruby) [If you `extend` a class with a module, that means you're "bringing in" the module's methods as class methods. If you `include` a class with a module, that means you're "bringing in" the module's methods as instance methods.](http://stackoverflow.com/a/14212020)\
1. `3.times { ... }` means "do this 3 times".
1. If a function accepts nothing, its declaration brackets are optional.
1. [Modules are not classes](http://stackoverflow.com/questions/151505/difference-between-a-class-and-a-module). Modules are mixin-equivalents, whereas classes can be instantiated.
1. Ruby is a lot more heavily influenced by Perl than Python is, which is why its syntax is both more powerful and moronic at the same time.
1. [`p foo`](http://stackoverflow.com/questions/1255324/p-vs-puts-in-ruby) == `puts foo.inspect`
1. Slicing a string from some index until the end is not `[n..]`, but [`[n..-1]`](http://stackoverflow.com/questions/3611586/ruby-string-slice-index-strn-infinity), for some reason.
1. Similarly, slicing a string from the beginning is not `[..n]` either. It is `[0..n]`.
1. The parameter used when making a new Hash (dict) is the default value for any keys, default being `nil`. `Hash.new(0)` will have all defaults being 0.
1. Like in python, positional/keyword arguments can have a default only if the arguments before them are also positional/keyword.
1. [Apparently](http://stackoverflow.com/questions/39988613/how-do-i-destructure-a-range-in-ruby) to get the first and last elements from a range (which is not an array for some reason), you just do `array.begin` and `array.end`. That will go through all elements in the range, but what do you know.
1. It is tradition for Rails to [muck with builtin types](http://stackoverflow.com/a/15926695/1558430) so that the integer `1` can have the method `day`.
1. `gem` is really nice, because `gem fetch abc` downloads the package, and `gem install abc.gem` (with the `.gem`) installs it.
