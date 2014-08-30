* **Tail call optimisation** refers to the behaviour in recursive functions for when a true function (one that has no side effects) calls itself again as the only operation in the last statement, allowing the computer to run that function while preserving the function's address space.
* **Class P Problems** (or just P) are problems that an algorithm can solve in polynomial time. P is also known as *quickly solvable*.
* **Class NP Problems** (or just NP) are problems that can be solved quickly, provided that the answer is given. NP is also known as *quickly checkable/verifiable*.
* **NP-Complete** problems are problems that are both NP and NP hard.

# Being a developer

A senior anything developer needs to know more than just a specific language. 
I would go so far as to argue there's no such thing as a senior php developer or a senior javascript developer. There's only a *senior* developer.
Basically, if you were handed a project and needed to do it from start to finish on your own, could you?

## Tools & Scoping

* If I gave you a client spec, could you find enough of the holes in it to inform management that their $40,000 bid should really be $120,000?
* Given a client spec, would you be able to select the appropriate tool for the job? That is, should be it Wordpress? Should it be Drupal? Should it be Joomla? (trick question, it should never be Joomla). Should it be Symfony, or Laravel? Should it be 100% custom?

## System Administration & Dev Ops

* Could you spool up an appropriate Amazon server? Could you set up a working environment in Vagrant that is easy for another developer to spin up if you needed their help? 
* Could you obtain an SSL cert and get it hooked up? 
* Could you untangle some nasty push into a git repo?

## Full Stack

* Could you create a responsive, semantically clear HTML front-end? What about javascript? Clean javascript, not some jQuery jungle. 
* Can you manage a MySQL or Postgres DB without help? Going back to tools & scoping, is a relational database even the right solution for project? Should you use a mix of both? 
* Can you cleanly integrate & optimize both (SQL/NoSQL)? 
* Do you know how to scale relational and non-relational databases? 
* Do you know how to utilize transactions in PHP and set up foreign key constraints and cascades to ensure data integrity? 
* What about apache/ngnix and other server-related things?

## Leadership & Teamwork

* If you didn't have the time to do anything yourself, could you effectively manage a team of developers to hit milestones and sprint targets? (effectively becoming a low-level PM) How would you do it? 
* How would you best allocate resources to overcome blockers? 
* Can you lead a code review? 
* Would you know how to assign tasks to the right people such that they become better developers as a result of working on this project - that is, pushing them ever so slightly out of their comfort zone, but not so far that it jeopardizes the product or timelines?

# Algorithms
## [Bloom filter](http://en.wikipedia.org/wiki/Bloom_filter)

Heuristically determine if something is in a set, being correct most of the time.

* + Uses less space than full search

## Clustering
### K-means
```
for data in datas:
    for mean in means:
        if data is closest to this mean:  # "closest" is the euclidean distance
            mean.add data
    return means
```

# Patterns
## Creational patterns
### Builder
### Abstract Factory
### Factory Method
### Prototype
### Singleton

## Structural patterns
### Adapter
### Bridge
### Composite
### Decorator
### Facade
### Flyweight
### Proxy

## Behavioural patterns
### Chain of Responsibility
### Command
### Interpreter
### Mediator
### Memento
### Observer
### State
### Strategy
### Template Method
### Visitor

# Data structures
## Linked lists
## stacks
## queues
## dicts
## trees
### binary search trees
## hashes
## Monads

* [Monads](https://en.wikipedia.org/wiki/Monad_(functional_programming\)) are "functional expressiosns" like `== null`.
* Monads aren't useful alone; they require composition to do real work. *Binding* two monads means `(monad1 ∘ monad2)(x) -> monad1(monad2(x))`.
* When monads are composed, they can short-circuit evaluations, making programs run faster.
* Game theory: sometimes the intuitive option isn't the one you should pick -- nor is the unintuitive option, because that's also what the other guy is thinking. [Here are a few examples](http://wjspaniel.wordpress.com/2014/05/25/game-theory-is-really-counterintuitive/).

# Challenges
* [ ] Erlang (concurrent programming)
* [ ] Java (android) 
* [ ] - [Operating Systems](http://pages.cs.wisc.edu/~remzi/OSTEP/)
* [ ] TCP/IP
* [ ] Machine learning (stocks) 
* [ ] Image (logo) recognition
* [ ] Haskell (functional static programming) 
* [ ] Fabric (deployment)
* [ ] AngularJS (MVC)
* [ ] Hadoop (mapreduce / parallelism)
* [ ] Numpy
* [ ] Julia (science) 
* [ ] I2P, or http://en.wikipedia.org/wiki/NAT_hole_punching
* [ ] ETag tracking

# Projects
* [ ] json-template-based static site that gracefully degrades
* [ ] preloaded image browser
* [x] Jquery data binding
* [ ] Your own drag and drop service
* [ ] GAE load balancer
* [ ] SQL Query Builder