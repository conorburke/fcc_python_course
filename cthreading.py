# GIL: Global interpreter lock
# allows only one thread to execute

# needed because in CPython memory management is not thread-safe

# avoid:
#     - use multiprocessing
#     - use a different, free-threaded python implementation (Jythohn, IronPython)
#     - use python a s awrapper for third party libraries (C/C++) -> numpy and scipy for example