The **userfolders** module provides cross-platform access to a user's special folders (or directories) like My Documents, Desktop, and Application Data. It is primarily intended to simplify development of desktop application software.

A quick usage example:

```python
# Get the user's My Documents folder
import userfolders
my_docs = userfolders.get_my_documents()
```

Both Windows and Unix platforms are supported (untested on Mac, currently accepting contributions).

## Fork Notice

This project is a fork of Benjamin Johnson's [userpaths](https://github.com/bmjcode/userpaths) with enhanced Linux Support and modern Python features.


## API Reference

Function | Description
-------- | -----------
`get_appdata()` | Return the current user's roaming Application Data folder.
`get_desktop()` | Return the current user's Desktop folder.
`get_downloads()` | Return the current user's Downloads folder.
`get_local_appdata()` | Return the current user's local Application Data folder.
`get_my_documents()` | Return the current user's My Documents folder.
`get_my_music()` | Return the current user's My Music folder.
`get_my_pictures()` | Return the current user's My Pictures folder.
`get_my_videos()` | Return the current user's My Videos folder.
`get_profile()` | Return the current user's profile folder.

The userfolders API was inspired by, and is partly compatible with, Ryan Ginstrom's [winpaths](http://ginstrom.com/code/winpaths.html). However, userfolders is not intended as a direct replacement for that module.


## Compatibility Note

The userfolders module was originally designed from a Windows-centric perspective. Because of the many differences between the two systems, there are some Windows paths that do not have a direct equivalent on Unix, and vice versa. In these cases, userfolders attempts to return the nearest functional equivalent, but it is up to the user to ensure their application is using the appropriate path for what it seeks to do.
