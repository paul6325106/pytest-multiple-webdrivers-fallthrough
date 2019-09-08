# pytest-multiple-webdrivers-fallthrough

An example of reusing browser instances for single and multiple browser tests.

Two approaches are demonstrated:

 * Having a single session scope web driver for most tests, and creating extra browser instances as needed.
   Recommended if most of your tests only require a single browser instance, or if there is limited capacity on your grid.

 * Preallocating a number of web driver instances on the session scope, then exposing the required number on a function scope.
   Recommended if most of your tests require multiple browser instances.
