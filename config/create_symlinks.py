import os

home = os.getenv("HOME")
base_path = os.path.dirname(os.path.abspath(__file__))
zsh_files = ("zshenv", "zshrc", "zlogin", "zlogout")

print "Creating symlinks for zsh configuration into " + home

for zf in zsh_files:
    src = os.path.join(base_path, zf)  # get full path to file
    #src = os.path.abspath(zf)            # get full path to file
    dest = os.path.join(home, "." + zf)  # make linked file hidden
    if os.path.exists(dest):
        # backup original files to FILENAME.orig
        # this will override an existing FILENAME.orig, though!
        orig = dest + ".orig"
        i = 1
        while os.path.exists(orig+"."+str(i)):
            i += 1
        print dest + " exists. Renaming to " + orig + "."+str(i)

        os.rename(dest, orig+"."+str(i))
    print "Creating symlink from {src} to {dest}".format(src=src, dest=dest)
    os.symlink(src, dest)

print "All done!"

