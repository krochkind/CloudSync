## CloudSync

This script copies all sub-directories and files that exist in a source folder into a destination folder.

- If the source file is newer, it will overwrite the destination file.
- If the source file has not changed since the last time it was synced, it will ignore the file.
- If the destination file is newer than the source, it will prompt if you want to overwrite it.
- If a file exists in the destination folder but not the source folder, it will not do anything to the destination file.

I use this to back up folders to the cloud (via Dropbox).  The source folder is a folder on my local, and the destination folder is a folder that syncs up to the cloud.

There are three variables that need to be set, in the code:
`folder_name`
`source_dir`
`destination_dir`
