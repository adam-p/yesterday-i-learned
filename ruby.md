* Methods do not require `()` to call. WTF?
* Methods that end in `?` are boolean functions by [pure convention](http://stackoverflow.com/a/1345855). 
* `?F` apparently means [`"F".ord`](http://stackoverflow.com/a/1878406) for Ruby < 1.9, and just `"F"` in Ruby 1.9+.
* `!` after a method applies changes the current object. So `a.upcase!` means `a = a.upcase`.
* `.chomp`, which often follows `gets`, removes the extra line at the end of console inputs.
* "Ruby prioritizes programmer productivity over program optimization."
* `if`, `elsif`, `else`, `end`, because `elseif` is just too long. No need for `:` at the end of each condition.
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
