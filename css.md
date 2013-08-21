* CSS3 has `background-size`, whose most useful values are `cover` (scaled and cropped) and `contain` (scaled to fit).
* `text-overflow` allows [custom truncation characters](https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow). It is CSS3. For everything else, there's [mastercard](http://dotdotdot.frebsite.nl/).
* Chrome doesn't support two-valued text-overflows, e.g. `clip ellipsis`.
* Relative paths in an external CSS file is [relative to the file](http://stackoverflow.com/questions/940451/using-relative-url-in-css-file-what-location-is-it-relative-to).
* A `:before` selector with `content: "|";` solves many problems, including stupid site menu separators.
