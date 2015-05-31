* Methods do not require `()` to call. WTF?
* Methods that end in `?` are boolean functions by [pure convention](http://stackoverflow.com/a/1345855). 
* And because boolean functions are purely by convention, this also means they can accept parameters: `@foo.bar?('baz')`
* `?F` apparently means [`"F".ord`](http://stackoverflow.com/a/1878406) for Ruby < 1.9, and just `"F"` in Ruby 1.9+.
* `!` after a method applies changes the current object. So `a.upcase!` means `a = a.upcase`.
* `.chomp`, which often follows `gets`, removes the extra line at the end of console inputs.
* "Ruby prioritizes programmer productivity over program optimization."
* `if`, `elsif`, `else`, `end`, because `elseif` is just too long (but `elif` is too Python, presumably). No need for `:` at the end of each condition.
* Integer instantiation is `Integer(something)`.
* `a_string.gsub(/regex/, "what")`
* `while` is the same everywhere, except you need `end`. No `:` needed.
* `until` is the backwards `while` (executing while the check is false)
* There's no `++`, but there's still `+= 1`.
* `Hash.new(0)` creates a `defaultdict`-like object, whose initial values are `0`s.
* `Hash` has [some `sort_by` thing](http://gayleforce.wordpress.com/2009/09/28/ruby-sorting-1-when-and-why-to-use-sort_by/) which has some weird `|a, b| b` array syntax.
* `nil` is all lower case.
* `an_array.each { |x| puts "#{x}\n" }` is totally possible.
* Hashes (dicts): the syntax is `{ a => b}`
* All ruby methods are available via `something.methods.sort`.
* All ruby methods specific to an object are avaiable via `something.own_methods.sort`.
* The Ruby REPL is `irb`.
* [Ruby doesn't have functions](http://stackoverflow.com/a/4294660/1558430); to get a reference to a callable without calling it, use `func_ref = method(:func_name)`, and call with `func_ref.call`.
* Results from the last expression is returned.
* Ruby's `foldr` is called [`inject`](http://blog.jayfields.com/2008/03/ruby-inject.html) (if you use it this way).
* [The `do` block has lower precedence than the bracket block syntax](http://stackoverflow.com/a/2122457/1558430), allowing you to do concise loops in some cases:

```
1.upto 3 do |x|
    puts x
end

1.upto 3 { |x| puts x }
# SyntaxError: compile error
```

* From above, "A [`do`] block is like an anonymous function or lambda. The variable between *pipe characters* is the parameter for this block."
* I think functions can themselves be instances. `def something ... ... @names` is perfectly valid syntax.
* `def`s need `end`s.
* The Ruby equivalent of `if __name__ == '__FILE__'` is `if __FILE__ == $0`.
* `some_obj.respond_to?(attribute)` is a special method that checks if an object has that attribute (or method, which is about the same for Ruby).
* Having a `attr_accessor :name` line in a class creates automatic getters and setters for every instance's `name`, or `@name`.
* `def initialize` is the... uh... coffeescript? php? version for Ruby.
* Since `nil` is Ruby's `None`, `.nil?` is the same as `(... is None)`.
* You *can* have double quotes in interpolated, doubled quoted strings! [The guide](https://www.ruby-lang.org/en/documentation/quickstart/3/)'s example was `puts "Goodbye #{@names.join(", ")}.  Come back soon!"`
* `Class.new(...)` returns an instance. Because of Ruby's *awesome* bracket omission, `Class.new` also returns one, with no parameters given to the constructor.
* To be consistent with their OOP philosophy, `sprintf` is a global function.
* In a class, putting `private` somewhere in it [makes *everything below that line* private](http://en.wikibooks.org/wiki/Ruby_Programming/Syntax/Classes#Private).
* Assuming `:method` is the syntax used to access the class method called `method`, `private :method` marks it as private, if put *underneath* the declaration for `method`.
* [The "double at" (`@@foo`)](http://stackoverflow.com/questions/5890118/what-does-variable-mean-in-ruby) is a class variable, making your previous point false.
* [The "double less than" (`class << instance`)](http://stackoverflow.com/questions/6182628/ruby-class-inheritance-what-is-double-less-than) adds all methods in that class to a particular instance of some other class, probably because there is no `instance.extend(class.__dict__)` equivalent.
* Instead of `self.__class__`, it is [`self.class`](http://stackoverflow.com/a/2527911/1558430). `self` is not a named parameter.
* Functions are not hoisted.
* Whitespace in blocks doesn't matter. Well, because there is a required `end` keyword.
* `func do |arg1| ... end` is essentially `genr = func(); (cb(arg1) for arg1 in genr)`, if `func` is a generator function that uses `yield` (and only works with `yield`).
* Lists can turn into the `func` above by calling `.each`, i.e.`[1,2,3,4].each do |i| ...`
* ["With blocks"]() are also done using blocks in Ruby: 

```
File.open('somefile.txt') do |f|
    puts f.readline
end
```

* One-liner if statements have the following syntax: `condition ? true : false` (no if, no else)
* One-liner blocks are also possible. `[1,2,3,4].map{|i| i + 1}` is a block that is acting as a lambda.
* List filters using `select` and blocks: `[1,2,3,4].select{|i| i % 2 == 0}`
* Because methods are immediately invoked, obtaining an attribute from it is also an invocation. However:

```
sentence.split.length  # fine
sentence.split().length()  # fine
sentence().split.length  # not fine, strings (or maybe some things just) aren't callable
```

* The last-run statement in a function is the return value. Guess where coffeescript got this from!
* There's apparently a `for ... in` syntax, but [nobody uses it, claims redditor.](http://www.reddit.com/r/Python/comments/1k74jb/ruby_vs_python/cbm62q6)
* `print` is a thing, and `puts` is a thing too. Their equivalents are `print foo,` and `print foo`.
* `is_a` and `kind_of` are the same method: true if the object is an instance of that class or its subclasses. [`instance_of`](http://stackoverflow.com/a/3893305/1558430), on the other hand, checks for its exact class.
* [Symbols](http://www.troubleshooters.com/codecorn/ruby/symbols.htm#_What_do_symbols_look_like) are pairs of ids and immutable strings. They look like `:this`, and have performance benefits because of their immutability.
* Not until Ruby 2.2 did it [GC symbols](https://bugs.ruby-lang.org/issues/7791), creating security issues for Rails sites.
* The `gem` thing lets you list available versions if you provide two flags: `gem list package_name --remote --all`