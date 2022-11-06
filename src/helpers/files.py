import os
import pandas

from typing import Optional

from pandas.core.generic import NDFrame


def generateFilenameDirectory(directory: str = "output", filename: str = 'file', ext: Optional[str] = None) -> str:
    if (type(ext) == type(None)):
        raise Exception("extension's file should be defined")

    oDirectory = f"{os.getcwd()}/{directory}"
    oFilename = f"{filename}.{ext}"

    is_directory_exists = os.path.exists(oDirectory)

    if not is_directory_exists:
        os.mkdir(oDirectory)

    path = f"{oDirectory}/{oFilename}"

    return path


def writeToCSV(filename: str = 'file', data: Optional[NDFrame] = None) -> None:
    path = generateFilenameDirectory(filename=filename, ext='csv')

    if (type(data) == type(None)):
        raise Exception("data parameter should not be type of None")
    else:
        try:
            csv_file = pandas.DataFrame(data).to_csv()

            file = open(path, "w")
            file.write(csv_file)
            file.close()
        except:
            raise Exception("Error when try to write to a file")
        finally:
            print(f"Successfully create a/an {filename}.csv file, you can find the result here: {path}")


def writeToExcel(filename: str = 'file', data: NDFrame = None) -> None:
    path = generateFilenameDirectory(filename=filename, ext='xlsx')

    if (type(data) == type(None)):
        raise Exception("data parameter should not be type of None")

    try:
        pandas.DataFrame(data).to_excel(path)
    except:
        raise Exception("Error when try to write to a file")
    finally:
        print(f"Successfully create a/an {filename}.xlsx file, you can find the result here: {path}")
