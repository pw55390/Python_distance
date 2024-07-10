Instrukcja: 
w systemie powinny znajdować się biblioteki*: 
- pandas (wersja 2.2.2) - pip install pandas
- geopy (wersja 2.4.1) - pip install geopy
- folium ( wersja 0.17.0) - pip install folium
- tkinter - pip install tk


Aplikacje można uruchamić za pomocą skryptu main.py.Do użytkowania aplikacji konieczne jest połączenie z siecią Internet. 
UWAGA: aplikacja korzysta z pliku town.csv - ten plik musi znajdować się w folderze głównym projektu


1 ) uruchomić main.py - z poziomu konsoli w folderze głównym projektu: python main.py
Używanie aplikacji: 
1) Określ miasto w którym się znajdujesz.
 - Na liście kontynentów należy zaznaczyć (podkreślenie) kontynent - następnie (dwukrotnie) kliknąć przycisk DALEJ. To wyświetli listę krajów na kontynencie - ponownie zaznaczamy.
- Po zaznaczeniu na liście krajów klikamy DALEJ (wystarczy raz) - to wyświetli listę regionów. Region wybieramy w celu zawężenia listy miast. klikamy DALEJ
- to wyświetli listę miast w regionie - wybieramy klikamy DALEJ

2) Określ cel podróży
- ponawiamy operację: wybór kontynentu, kraju,regionu i miasta - za każdym razem jednokrotnie klikamy DALEJ
- To wyświetli odległość w linii prostej (przy uwzględnieniu krzywizny kuli ziemskiej) między dwoma miastami w kilometrach
- Zostaje zapisana do pliku html w katalogu głównym projektu - mapa świata (mapa.html) z zaznaczoną linią między dwoma miastami. 

*biblioteki do zaintalowania znajdują się także w pliku: requirements.txt ( pip install -r requirements.txt ) 