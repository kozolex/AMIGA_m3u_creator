# Automatic Creation of M3U Files for Amiga ROMs

## Project Description

This project contains a Python script that automates the process of creating `.m3u` files for sets of ROM files for Amiga emulation. The script searches the specified location, checks subdirectories, and then creates `.m3u` files according to specified criteria.

## What are M3U Files?

`.m3u` files are playlist files that contain a list of paths to multimedia files. In the context of Amiga emulation, `.m3u` files are used to manage games that are stored on multiple disks. This allows the emulator to easily switch between different disk files during gameplay.

## How Does the Script Work?

1. The script searches the specified location and identifies all subdirectories.
2. For each subdirectory, it checks if there is a `.m3u` file. If such a file exists, the subdirectory is skipped.
3. If there is no `.m3u` file in the subdirectory, the script checks if there is more than one file.
4. If there is more than one file in the subdirectory, the script creates a `.m3u` file that contains the alphabetically sorted names of all files in the subdirectory.
5. The `.m3u` file is saved in the subdirectory with a name corresponding to the subdirectory name.

## How to Use the Script?

1. Copy the script to your project.
2. Update the `location` variable in the script to point to the location you want to search.
3. Run the script.

```python
# Specify the location to search
location = 'path/to/location'

# Run the main function
main(location)
```

## Requirements

- Python 3.x
- `glob` module (built into the standard Python library)
- `os` module (built into the standard Python library)

## License

This project is licensed under the MIT License. See the LICENSE file for more information.


Now you can run the program from the console by providing the path to the location as an argument:

```bash
python main.py path/to/rom
```

If you have any more questions or need further assistance, feel free to ask!