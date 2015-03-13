* In HTML5, `<style>` tags must have the `scoped` attribute if they are in the `<body>` tag. Styles will be applied to its parent and siblings.
* Google uses [a chain of iframes](www.googletagmanager.com/ns.html?id=GTM-NQTT) inside `<noscript` tags, to track users in case the browser has javascript disabled.
* `<meta property="og:image" content="(the facebook share thumbnail)">`
* There is a [`time`](http://www.w3schools.com/tags/tag_time.asp) tag in HTML5, and [it does something](http://jsfiddle.net/trevoro/T4wRq/) if you [tell it to](http://trevoro.net/2013/whats-your-timezone/).
* `&blacktriangledown;` is a thing. [Those bastards](http://www.w3.org/TR/2013/WD-components-intro-20130606/#decorator-section)...
* I hear [it's okay for html comments to be outside the <html> tag](http://stackoverflow.com/questions/365805/is-it-ok-to-put-html-comments-outside-the-html-tags), but [not if it comes before <!DOCTYPE>](http://stackoverflow.com/questions/941100/can-comments-appear-before-the-doctype-declaration). The only two browsers I suspect trouble are firefox and opera.
* HTML5 [allows `a` to contain `div`](http://stackoverflow.com/a/1828032/1558430).
* HTML5 element IDs can begin with a number. `$('#5')`, for example, works.
* Adding `width=device-width` or `user-scalable=no` on [some versions of mobile browsers](https://github.com/ftlabs/fastclick#when-it-isnt-needed) apparently introduces the side benefit of not introducing a hover-click delay.
* [HTML5 tainted canvas](https://developer.mozilla.org/en-US/docs/HTML/CORS_Enabled_Image) is a `(new Image).crossOrigin = ...` change that allows a limited selection of browsers to serve images from any remote origin. This was implemented to allow canvases to reading images to be requested using cookies.
* `crossOrigin` defaults to anonymous. There is no need to specify `anonymous`.
* Serving an anonymous image inside a canvas removes a canvas' ability to be read.
* Hashes can actually go to an ID as well as a name (`#foo` -> `<div id="foo"/>`).
* In HTML5, `a` tags can have a [`download` attribute](http://www.w3schools.com/tags/att_a_download.asp) that forces the link to be downloaded.
* Websites can restrict content sources by appending a header to the response. Here is the one github uses.
* [The `address` element was not created for postal addresses (...) unless those addresses are in fact the relevant contact information for a document or section of a document](http://html5doctor.com/the-address-element/)
* [Nested `span`s are okay.](http://stackoverflow.com/questions/1078127/are-nested-span-tags-ok-in-xhtml) The same probably speaks for other inline elements, too.

```
Content-Security-Policy: default-src *; script-src assets-cdn.github.com www.google-analytics.com collector-cdn.github.com; object-src assets-cdn.github.com; style-src 'self' 'unsafe-inline' 'unsafe-eval' assets-cdn.github.com; img-src 'self' data: assets-cdn.github.com identicons.github.com www.google-analytics.com collector.githubapp.com *.githubusercontent.com *.gravatar.com *.wp.com; media-src 'none'; frame-src 'self' render.githubusercontent.com gist.github.com www.youtube.com player.vimeo.com checkout.paypal.com; font-src assets-cdn.github.com; connect-src 'self' ghconduit.com:25035 live.github.com uploads.github.com s3.amazonaws.com
```

* In Chrome, `<img>` tags with no `src` have a [grey border](http://stackoverflow.com/questions/10848722/google-chrome-images-have-border) that does not go away with any amount of CSS.

## [Writing jank-free webpages](http://aerotwist.com/blog/pixels-are-expensive/)

60fps = limiting each frame to 16ms.

* **USE PAGESPEED** to analyse your *render tree*.
* Three stages of rendering: *Layout* (calculating geometry of where everything ought to be), *Paint* (filling in the page), and *Compositing* (picking a layer to minimise repaints).
* Use the `will-change: wat` CSS directive to let the browser know what will be changed

### Eliminating expensive animations

Expensive animations include:

* Scrolling
* Transition based on variables
