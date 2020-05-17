# Sinhala Lyrics Front End

This project consumes a lyric generative web-app served with ``gunicorn``.

Simply change the callback settings in the `index.html` file.

 ```js
var settings = {"async": true,
                "ur":"http://127.0.0.1:5000/myAPIEndPoint",
                ...,
                }
```
with your correct localhost address and API endpoint.
