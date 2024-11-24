import glob
import os
import argparse

# Funkcja do tworzenia pliku .m3u z posortowanymi nazwami plików
def create_m3u(directory):
    # Pobierz wszystkie pliki w katalogu
    files = [f for f in glob.glob(os.path.join(directory, '*.adf')) if os.path.isfile(f)]
    
    # Posortuj pliki alfabetycznie
    files.sort()
    
    # Pobierz nazwę katalogu
    dir_name = os.path.basename(directory)
    
    # Utwórz plik .m3u
    with open(os.path.join(directory, f"{dir_name}.m3u"), 'w') as m3u_file:
        for file in files:
            m3u_file.write(f"{os.path.basename(file)}\n")

# Główna funkcja do przeszukiwania katalogów i tworzenia plików .m3u
def main(location):
    # Pobierz wszystkie podkatalogi w wskazanej lokalizacji
    subdirs = [d for d in glob.glob(os.path.join(location, '*')) if os.path.isdir(d)]
    
    for subdir in subdirs:
        # Sprawdź, czy w podkatalogu istnieje plik .m3u
        if not glob.glob(os.path.join(subdir, '*.m3u')):
            # Pobierz wszystkie pliki w podkatalogu
            files = [f for f in glob.glob(os.path.join(subdir, '*.adf')) if os.path.isfile(f)]
            
            # Jeśli istnieje więcej niż jeden plik, utwórz plik .m3u
            if len(files) > 1:
                create_m3u(subdir)

if __name__ == "__main__":
    # Użyj argparse do obsługi argumentów wiersza poleceń
    parser = argparse.ArgumentParser(description="Automatyczne tworzenie plików .m3u dla ROM-ów Amigi.")
    parser.add_argument('location', type=str, help="Ścieżka do lokalizacji do przeszukania")
    
    args = parser.parse_args()
    
    # Uruchom główną funkcję z podaną lokalizacją
    main(args.location)