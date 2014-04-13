# How to use RequireJS

### Have one of these `script` tags in your `head`

```
<script data-main="scripts/main" src="scripts/require.js"></script>
```

This loads `./scripts/require.js`, which fetches `./scripts/main.js`, your app.

# Project structure

## Files

* `package.json`: for calling `npm install` with no arguments.
* `bower.json`: for calling `bower install` with no arguments.
* `Jakefile`: the file that `jake` uses.
