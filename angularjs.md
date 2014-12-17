* Installing AngularJS: `bower init && install --save angular#~1.2 angular-resource#~1.2` (among whatever else you plan to use)
* Creating an app: `app = angular.module('MyApp', ['ngResource'])`
* Attaching controllers to the app: `app.controller('controllerName', function ($thingsYouUse) {...})`
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
