def command(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None

def crawl_dirs(dirs: list=[]):
    """Crawl's an array of directory and gets every filepath in those directories"""
    import os;
    out = [];
    for path in dirs:
        for folder_name, subfolders, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                out.append(file_path)
    return out

wp_default_args="--exec=\"error_reporting(E_ALL ^ E_DEPRECATED);define('WP_MEMORY_LIMIT', '512M');\""
