def command(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None

def create_archive(name, zip_name, paths=["wp-content"]):
    import os
    import zipfile

    zip_name= "dev.zip"
    paths=["wp-content"]

    for path in paths:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            for folder_name, subfolders, filenames in os.walk(path):
                for filename in filenames:
                    file_path = os.path.join(folder_name, filename)
                    zip_ref.write(file_path, arcname=os.path.relpath(file_path, path))

    zip_ref.close()