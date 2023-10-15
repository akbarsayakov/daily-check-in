# HTML Script Attributes: defer, async, and module

This README file provides an explanation of the `defer`, `async`, and `module` attributes used with script elements in HTML. These attributes control how scripts are loaded and executed in web pages. Let's delve into each attribute:

## 1. defer Attribute

The `defer` attribute is used to indicate that a script should be executed after the HTML parsing is complete but before the `DOMContentLoaded` event is triggered. When a script with the `defer` attribute is encountered, it is fetched and loaded in the background while HTML parsing continues. Once the HTML parsing is finished, the script is executed in the order they appear in the document. Multiple scripts with the `defer` attribute maintain their order of execution. This attribute is primarily used with classic scripts.

Example:

```html
<script src="script.js" defer></script>
```

## 2. async Attribute

The `async` attribute is used to specify that a script should be fetched and executed asynchronously. When a script with the `async` attribute is encountered, it is fetched in the background while HTML parsing continues. As soon as the script is fetched, it will pause HTML parsing and execute the script. This means that the script may execute out of order with respect to other scripts or the `DOMContentLoaded` event. Multiple scripts with the `async` attribute can execute independently and in any order. This attribute is also primarily used with classic scripts.

Example:

```html
<script src="script.js" async></script>
```

## 3. module Attribute

The `module` attribute is used to define a module script. A module script is a script that supports ECMAScript Modules (ESM), which enables the use of the `import` and `export` statements to create modular code. Module scripts are always deferred by default, meaning they are fetched and executed after the HTML parsing is complete, similar to scripts with the `defer` attribute. Module scripts have their own scope and can be loaded multiple times, but they are only executed once.

Example:

```html
<script type="module">
  import { someFunction } from './module.js'
  // Code using the imported module
</script>
```

It's important to note that module scripts require the `type="module"` attribute. If a module script has the `src` attribute and is loaded from a different domain, it must follow the Cross-Origin Resource Sharing (CORS) protocol.

These attributes provide developers with flexibility in controlling script loading and execution in HTML, allowing for optimized performance and enhanced functionality in web applications.
