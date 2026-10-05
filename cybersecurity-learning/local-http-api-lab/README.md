# Local HTTP / API Lab

A small Python exercise that starts a JSON API on the loopback interface, makes two requests, prints the responses and shuts the server down.

**Purpose:** Observe a request path, an HTTP status, response headers and a JSON body.  
**Requirements:** Python 3.9 or later; no third-party packages.  
**Status:** Code is supplied as a learning exercise; record your own run in the [learning log](../learning-log.md).

## Run
Download [http_lab.py](http_lab.py), then run:

```bash
python3 http_lab.py
```

On systems where Python is invoked as `python`, use `python http_lab.py`.

The script binds to **127.0.0.1** and selects an available port. It does not accept an external target URL or contact a remote service.

## Expected observations
| Request | Status | Body |
| --- | --- | --- |
| GET /api/hello | 200 | A JSON greeting |
| GET /api/missing | 404 | A JSON error message |

Each response declares `Content-Type: application/json` and sets `X-Content-Type-Options: nosniff`.

The `nosniff` header tells browsers to respect the declared content type rather than reinterpret it through MIME sniffing. The Python client here simply prints the header; it does not demonstrate browser enforcement.

## Exercise
1. Run the script and compare the two status codes.
2. Find where the server constructs the JSON body.
3. Change the greeting text and run it again.
4. Explain why receiving a JSON body does not imply that the request succeeded.
5. Record what you observed in the learning log.

## Limitations
This is a local educational server, not a production service. It does not implement HTTPS, authentication or authorization. Its header example is not a security audit.

## Reference
[MDN X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options)

[Learning index](../README.md)
