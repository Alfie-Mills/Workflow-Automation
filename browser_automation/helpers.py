def command(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None

def crawl_dirs(dirs: list=[]):
    """Crawl's an array of directory and gets every filepath in those directories"""
    out = [];
    for path in dirs:
        for folder_name, subfolders, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                out.append(file_path)
    return out