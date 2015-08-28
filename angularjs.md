* Installing AngularJS: `bower init && install --save angular#~1.2 angular-resource#~1.2` (among whatever else you plan to use)
* Creating an app: `app = angular.module('MyApp', ['ngResource'])`
* Attaching controllers to the app: `app.controller('controllerName', function ($thingsYouUse) {...})`
* ViewModel is, and Controller isn't: [You'll notice - there are no references to the view and zero DOM manipulation in Angular controllers.][stackoverflow]
* Attaching filters (e.g. `{{ 'world' | greet }}`) to the app: `app.filter('greet', function() { return function(name) { return 'Hello, ' + name + '!'; }; })`
* Controllers can be nested; everything attached to the parent's `$scope` will also be available to child controllers within.
* `(app).service() # injects instance of function`; `(app).factory()  # injects function`. [ref](http://viralpatel.net/blogs/angularjs-service-factory-tutorial/)
* Since it believes JS is the best, AngularJS blocks all `form[action=""]` from submitting.
* AngularJS has codenames. `angular.version.codeName`
* AngularJS applications cannot be nested within each other. This makes apps very difficult to integrate.
* AngularJS views cannot be nested, either.
* To stop `{{ templateTags }}` from showing before angularjs loads, use [`ng-bind='templateTags'`](http://stackoverflow.com/a/12866905/1558430) instead to migitate the issue. The element will be blank*, but at least it doesn't show anything ugly.
  * BUT! If there's something in the element, i.e. `<span ng-bind="templateTags">123</span>`, then because the element is HTML valid, that value will show by default.
* `$scope.$emit()` bubbles up to the `$rootScope` and `$scope.$broadcast()` bubbles down.
* [AngularJS team](https://github.com/angular/angular.js/wiki/Understanding-Dependency-Injection): we like repeating ourselves, we like repeating ourselves
```
myMod.provider('greeting', function() {
    this.$get = function() {
        return function(name) {
        };
    };
})

// ===

myMod.factory('greeting', function() {
    return function() {
        return function(name) {
        };
    };
})

// ===

myMod.value('greeting', function(name) {});
```
meaning there is no purpose whatsoever to use `.provider`, and almost no reason to use `.factory`, unless you need to set up something in that scope.

* "The injector (`$injector`) is responsible for actually creating instances of our services using the code we provided via `$provide`", which means `$injector.get('greeting')` is a reinvention of `new greeting`.
* ... which also means `$injector.invoke(function (greeting) { ... });` merely calls `myFunction` with a `new greeting` given to it.
* In webkit, `$0` is the currently selected element in the inspector. So, [`angular.element($0).scope()`](http://stackoverflow.com/questions/13743058/how-to-access-the-angular-scope-variable-in-browsers-console) gets you the scope of that element.
* Directives' `link` function is run just once. That function is responsible for attaching itself to element events and run accordingly.
* `(new $q.defer()).reject` cannot reject multiple things, i.e. a handler attached to `deferred.reject(1, 2, 3)` will only receive 1. jQuery's `Deferred` can, however, so you might want to use that instead.
* [`$state.go('viewName', {parameters...})`](https://github.com/angular-ui/ui-router/wiki/Quick-Reference#stategoto--toparams--options)
* Not specifying a directive's `scope` automatically makes it inherit everything from the parent scope. The reverse (specifying `scope`), which is quite popular for some reason, is called [isolate scope](https://docs.angularjs.org/guide/scope).
* Incidentally, `scope: false` makes a directive [use its parent's scope](http://www.undefinednull.com/2014/02/11/mastering-the-scope-of-a-directive-in-angularjs/) without creating one for itself.
* Only in a loop can you alias a variable with [`ngInit`](http://stackoverflow.com/questions/25938059/how-to-alias-object-property-as-variable-in-ng-repeat): `ng-init='something as original.attribute'`
* [`$scope.$new(true)` creates a new isolate scope](http://stackoverflow.com/a/15560832), where `true` creates an isolate scope, and `false` doesn't. It is not as useful as you think.
* [`finally` and `delete` are keywords you cannot use in IE8](https://github.com/angular/angular.js/commit/f078762d48d0d5d9796dcdf2cb0241198677582c), whether or not it is an attribute. To use `$q.finally`, you need `$q['finally']`.
* `ng-if` creates a child scope while `ng-show`/`ng-hide` does not.
* One reason why AngularJS is slow: ["The JavaScript browser api is event-driven, it is made to respond when stuff (usually user input) happens. This means that events change data. Many new frameworks (Angular, Meteor) reverse this direction and make data changes trigger events."](https://medium.com/@ilyothehorrid/writing-code-for-humans-5b80a89f439c)
* [Ionic's `collection-repeat`](http://ionicframework.com/docs/api/directive/collectionRepeat/) is faster for lists than `ng-repeat`.
* Although [the article](https://medium.com/@fabrik42/cleaner-angularjs-directives-with-curried-functions-57a63c895da5) has nothing to do with currying, binding functions to a scope outside the scope itself is a practice that can be used to flatten a directive.
* Angular promises can also be chained. If a `.then(function () { returns a 5})`, then the next `.then(function (will get the 5) {})`.
* [Calling a controller](http://stackoverflow.com/questions/12488828/) is possible, though the function will not be bound to any HTML, and it will make you mentally special:
```
$injector.get('$controller')('ControllerName', {
    $scope: $injector.get('$rootScope').$new(true),
    // all other dependencies ...
})
```
* `$filter('someFilterName')` gets the filter, so `$filter('someFilterName')('someText')` applies the filter onto that text.