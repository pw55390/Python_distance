import pandas as pd
from geopy.distance import geodesic
import folium
from tkinter import Tk, Label, Button, Listbox, SINGLE, END, Scrollbar, RIGHT, LEFT, Y, BOTH, Frame

# Wczytanie pliku CSV
miasta_b = pd.read_csv('town.csv')

# Funkcja do wyboru kontynentu
def choose_continent():
    
    next_button.config(command=choose_country)#Przycisk i wywołanie następnej funkcji


def choose_country():
    # Funkcja do wyboru kraju na podstawie wybranego kontynentu
    selec = continent_listbox.curselection()#Wprowadzam zaznaczony kontynent
    if selec:
        selected_continent = continents[selec[0]]
        # Filtracja unikalnych krajów z wybranego kontynentu
        countries = miasta_b[miasta_b['kontynent'] == selected_continent]['kraj'].unique()
        # Aktualizacja tekstu etykiety
        label.config(text="Wybierz kraj:", font=("Helvetica", 16))
        continent_listbox.delete(0, END)#Czyszczenie listboxa
        # Dodanie krajów do listboxa
        for country in countries:
            continent_listbox.insert(END, country)
        # Konfiguracja przycisku DALEJ do wywołania funkcji choose_region
        next_button.config(command=lambda: choose_region(selected_continent, countries))

# Funkcja do wyboru regionu na podstawie wybranego kraju
def choose_region(continent, countries):
    # Pobranie zaznaczonego kraju
    selec = continent_listbox.curselection()
    if selec:
        selected_country = countries[selec[0]]
        # Filtracja unikalnych regionów z wybranego kraju
        regions = miasta_b[miasta_b['kraj'] == selected_country]['region'].unique()
        label.config(text="Wybierz region:", font=("Helvetica", 16))#Aktualizacja tekstu etykiety
        continent_listbox.delete(0, END)# Czyszczenie
        # Dodanie regionów do listboxa
        for region in regions:
            continent_listbox.insert(END, region)
        # Konfiguracja przycisku "Dalej" do wywołania funkcji choose_city
        next_button.config(command=lambda: choose_city(selected_country, regions))

# Funkcja do wyboru miasta na podstawie wybranego regionu
def choose_city(country, regions):
    # Pobranie zaznaczonego regionu
    selec = continent_listbox.curselection()
    if selec:
        selected_region = regions[selec[0]]
        # Filtracja unikalnych miast z wybranego regionu
        cities = miasta_b[miasta_b['region'] == selected_region]['miasto'].unique()
        # Aktualizacja tekstu etykiety
        label.config(text="Wybierz miasto:", font=("Helvetica", 16))
        # Czyszczenie listboxa z poprzednich wpisów
        continent_listbox.delete(0, END)
        # Dodanie miast do listboxa
        for city in cities:
            continent_listbox.insert(END, city)
        # Konfiguracja przycisku "Dalej" do wywołania funkcji select_city
        next_button.config(command=lambda: select_city(cities))

# Funkcja do wyboru miasta docelowego
def select_city(cities):
    # Pobranie zaznaczonego miasta
    selec = continent_listbox.curselection()
    if selec:
        global selected_city
        selected_city = cities[selec[0]]
        # Aktualizacja tekstu etykiety
        label.config(text="Jaki jest cel Twojej podróży?", font=("Helvetica", 16))
        # Czyszczenie listboxa i ukrycie go
        continent_listbox.delete(0, END)
        continent_listbox.pack_forget()
        # Ukrycie przycisku "Dalej"
        next_button.pack_forget()
        # Wyświetlenie nowego listboxa do wyboru kontynentu docelowego
        destination_frame.pack(fill=BOTH, expand=True)
        for continent in continents:
            destination_listbox.insert(END, continent)
        # Wyświetlenie przycisku "Dalej"
        destination_button.pack()

# Funkcja do wyboru kontynentu docelowego
def choose_destination_continent():
    # Pobranie zaznaczonego kontynentu
    selec = destination_listbox.curselection()
    if selec:
        selected_continent = continents[selec[0]]
        # Filtracja unikalnych krajów z wybranego kontynentu
        countries = miasta_b[miasta_b['kontynent'] == selected_continent]['kraj'].unique()
        # Aktualizacja tekstu etykiety
        label.config(text="Wybierz kraj:", font=("Helvetica", 16))
        # Czyszczenie listboxa z poprzednich wpisów
        destination_listbox.delete(0, END)
        # Dodanie krajów do listboxa
        for country in countries:
            destination_listbox.insert(END, country)
        # Konfiguracja przycisku "Dalej" do wywołania funkcji choose_destination_country
        destination_button.config(command=lambda: choose_destination_country(selected_continent, countries))

# Funkcja do wyboru kraju docelowego
def choose_destination_country(continent, countries):
    # Pobranie zaznaczonego kraju
    selec = destination_listbox.curselection()
    if selec:
        selected_country = countries[selec[0]]
        # Filtracja unikalnych regionów z wybranego kraju
        regions = miasta_b[miasta_b['kraj'] == selected_country]['region'].unique()
        # Aktualizacja tekstu etykiety
        label.config(text="Wybierz region:", font=("Helvetica", 16))
        # Czyszczenie listboxa z poprzednich wpisów
        destination_listbox.delete(0, END)
        # Dodanie regionów do listboxa
        for region in regions:
            destination_listbox.insert(END, region)
        # Konfiguracja przycisku "Dalej" do wywołania funkcji choose_destination_region
        destination_button.config(command=lambda: choose_destination_region(selected_country, regions))

# Funkcja do wyboru regionu docelowego
def choose_destination_region(country, regions):
    # Pobranie zaznaczonego regionu
    selec = destination_listbox.curselection()
    if selec:
        selected_region = regions[selec[0]]
        # Filtracja unikalnych miast z wybranego regionu
        cities = miasta_b[miasta_b['region'] == selected_region]['miasto'].unique()
        # Zmiana tekstu etykiety
        label.config(text="Wybierz miasto:", font=("Helvetica", 16))
        # Czyszczenie listboxa z poprzednich wpisów
        destination_listbox.delete(0, END)
        # Dodanie miast do listboxa
        for city in cities:
            destination_listbox.insert(END, city)
        # Konfiguracja przycisku "Dalej" do wywołania funkcji select_destination_city
        destination_button.config(command=lambda: select_destination_city(cities))

# Funkcja do wyboru miasta docelowego
def select_destination_city(cities):
    # Pobranie zaznaczonego miasta docelowego
    selec = destination_listbox.curselection()
    if selec:
        destination_city = cities[selec[0]]
        # Obliczanie odległości między miastami
        distance, city1_coords, city2_coords = calculate_distance(selected_city, destination_city)
        # Wyświetlenie obliczonej odległości
        show_distance(distance, destination_city)
        # Wyświetlenie mapy z zaznaczonymi miastami
        display_map(selected_city, destination_city, city1_coords, city2_coords)

# Funkcja do obliczania odległości między dwoma miastami
def calculate_distance(city1, city2):
    # Pobranie współrzędnych geograficznych pierwszego miasta
    city1_coords = (miasta_b[miasta_b['miasto'] == city1]['lat'].values[0], 
                    miasta_b[miasta_b['miasto'] == city1]['lon'].values[0])
    # Pobranie współrzędnych geograficznych drugiego miasta
    city2_coords = (miasta_b[miasta_b['miasto'] == city2]['lat'].values[0], 
                    miasta_b[miasta_b['miasto'] == city2]['lon'].values[0])
    # Obliczenie odległości między miastami
    distance = geodesic(city1_coords, city2_coords).km
    return distance, city1_coords, city2_coords

# Funkcja do wyświetlania obliczonej odległości
def show_distance(distance, destination_city):
    # Aktualizacja tekstu etykiety z obliczoną odległością
    distance_label.config(text=f"Odległość między {selected_city} a {destination_city} wynosi {distance:.2f} km \nMapa zapisana do mapa.html", font=("Helvetica", 16))
    distance_label.pack()

# Funkcja do wyświetlania mapy z zaznaczonymi miastami
def display_map(city1, city2, coords1, coords2):
    # Utworzenie mapy z zaznaczoną trasą między miastami
    m = folium.Map(location=[(coords1[0] + coords2[0]) / 2, (coords1[1] + coords2[1]) / 2], zoom_start=4)
    folium.Marker(location=coords1, popup=city1).add_to(m)
    folium.Marker(location=coords2, popup=city2).add_to(m)
    folium.PolyLine(locations=[coords1, coords2], color='blue').add_to(m)
    # Zapisanie mapy do pliku HTML
    m.save('mapa.html')

# Uruchomienie aplikacji
root = Tk()
root.title("Lecimy!")
root.geometry("800x600")

# Utworzenie etykiety do wyświetlania komunikatów
label = Label(root, text="Na jakim kontynencie jesteś?", font=("Helvetica", 16))
label.pack()

# Utworzenie ramki do listboxa z kontynentami
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Utworzenie paska przewijania dla listboxa z kontynentami
continent_scrollbar = Scrollbar(frame)
continent_scrollbar.pack(side=RIGHT, fill=Y)

# Utworzenie listboxa do wyboru kontynentu
continent_listbox = Listbox(frame, selectmode=SINGLE, yscrollcommand=continent_scrollbar.set)
continents = miasta_b['kontynent'].unique()
for continent in continents:
    continent_listbox.insert(END, continent)
continent_listbox.pack(side=LEFT, fill=BOTH, expand=True)
continent_scrollbar.config(command=continent_listbox.yview)

# Utworzenie przycisku DALEJ do przechodzenia do kolejnych kroków
next_button = Button(root, text="Dalej", command=choose_continent)
next_button.pack()

# Utworzenie ramki do listboxa z destynacjami
destination_frame = Frame(root)
destination_scrollbar = Scrollbar(destination_frame)
destination_scrollbar.pack(side=RIGHT, fill=Y)

# Utworzenie listboxa do wyboru destynacji
destination_listbox = Listbox(destination_frame, selectmode=SINGLE, yscrollcommand=destination_scrollbar.set)
destination_listbox.pack(side=LEFT, fill=BOTH, expand=True)
destination_scrollbar.config(command=destination_listbox.yview)

# Utworzenie przycisku DALEJ do przechodzenia do wyboru destynacji
destination_button = Button(root, text="Dalej", command=choose_destination_continent)

# Utworzenie etykiety do wyświetlania obliczonej odległości
distance_label = Label(root, text="")

# Uruchomienie głównej pętli aplikacji
root.mainloop()
