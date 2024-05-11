0x11-python-network_1

The difference between using req = urllib.request.Request(sys.argv[1])
 and directly using with urllib.request.urlopen(sys.argv[1])
  as response: lies in the flexibility and control over the request that Request provides.

Using urllib.request.Request(sys.argv[1]): This approach creates a Request object, which allows you to specify additional parameters such as headers, data, and the HTTP method (GET, POST, etc.). This is useful when you need to customize the request beyond just the URL. For example, you might want to add custom headers, send data in a POST request, or specify a different HTTP method. The Request object is flexible and can be used with various types of URLs, including HTTP, HTTPS, FTP, and others.
Directly using urllib.request.urlopen(sys.argv[1]): This approach is simpler and is suitable for basic GET requests where no customization is needed. It directly opens the URL and returns a response object. This method is less flexible compared to using Request because it does not allow for easy customization of the request. However, it is sufficient for simple scenarios where you only need to retrieve data from a URL without modifying the request.
In summary, if you need to customize the request (e.g., adding headers, changing the HTTP method, or sending data), use urllib.request.Request. For straightforward GET requests without customization, urllib.request.urlopen suffices.

recource:
(https://docs.python.org/3/library/urllib.request.html)
(https://docs.python.org/3/library/urllib.request.html)
