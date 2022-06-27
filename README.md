# Sterowanie-urzadzeniami-w-jezyku-naturalnym

struktura domu jset opisana w pliku home.xml
przykładowe testowe pytania znajdują się w resources/example_commands
procedura asystenta i wszystkie operacje niezwiązane z samym TTS i STT są w LoadHome:

program uruchamiany jest poprzez odpalenie pliku main.py

asystent:
    
    podjąłem próbę przetworzenia słów stemming i lemminization, ale nie doszukałem się wygodnych 
    implementacji dla jezyka polskiego. Jedyne co było, to morfeusz, który bardziej komplikował sprawę,
    bo jedyne co mogłem z nim zrobić, to dopasować części mowy
    
    znalazłem jeszcze jakis inny stemmer dzialajacy przez ai, ale dawał inne stemy dla słow o tym samym znaczeniu,
    więc zostałem przy zrobieniu tablicy aliasów

    w LoadHome na sztywno są zapisane tablice z aliasami do każdej z komend/obiektow/pomieszczeń

    1) tokenizuje polecenie na słowa
    2) usuwam polskie stop-words wzięte z jakiegoś githuba ( resources/polish_stopwords ) #potrzebny przypis
    3) dopasowuję do każdego słowa aliasy z informacji których jeszcze nie mam
        najpierw szukam slowa z komendą, jak nie znajdę, to kończę program i zakładam, że coś źle usłyszał
    
        później ustawiam zmienna mówiącą o piętrze domu, pokoju  i obiekcie na null
        i szukam każdego z nich w pozostałych słowach.
        
    4) za pomocą regexow XMLa szukam pasujących urządzeń ( tam gdzie nie było wskazana informacja tj. zostało Null, zostawiam gwiazdkę)

        np. pietro/*/lampa
    5) stosuję komendę na tym wszystkim z uprzednim zapytaniem urzytkownika.

Koniec


Dom składa się z pomieszczeń. Na przykład:
- kuchnia
- salon
- sypialnia
- łazienka
- itp.
W pomieszczeniach znajdują się urządzenia. Na przykład:
- oświetlenie górne
- lampa lewa
- lampa prawa
- lampa nad stołem
- lampa na oknie
- oświetlenie sufitu
- oświetlenie pod szafkami
- oświetlenie schodów
- oświetlenie nocne
- wentylator w łazience
- itp.
Każdemu urządzeniu odpowiada jego identyfikator w systemie sterowania. Na przykład:
- kit/light/up
- liv/lamp/left
- bat/light/mirror
- itp.
Urządzenia można sterować komendami. Na przykład:
- on - załącza urządzenie
- off - wyłącza urządzenie
- toggle - zmienia stan na przeciwny

Chcemy aby urządzenia można było sterować poleceniami w języku naturalnym.
Przykłady poleceń (niekoniecznie poprawnych i na temat) znajdują się z pliku polecenia.txt
Proszę zaproponować strukturę pliku opisującego konfiguracje domu oraz strukturę danych
w języku Python do której będzie wczytywana ta struktura. Następnie proszę napisać funkcję
przekształcającą polecenie w języku naturalnym na odpowiednią komendę. Na przykład:
- załącz oświetlenie w salonie: cmd/liv/light on
- wyłącz lewą lampę w sypialni: cmd/bed/lamp/left off
- wyłącz górna lampę w kuchni : cmd/kit/lam/up off
W przypadku braku wyraźnego polecenia funkcja powinna przyjmować polecenie toggle. Na
przykład:
- oświetlenie pod szafkami : cmd/kit/light/down toggle
W przypadku braku pomieszczenia w poleceniu funkcja powinna przyjmować pomieszczenie
ostatnio wydanego polecenia. Na przykład:
W przypadku nierozpoznania polecenia funkcja powinna informować o problemie. Na
przykład:
- wyłącz żyrandol w łazience: w łazience nie ma żyrandola
- która godzina: nie rozumiem polecenia
Dodatkowo.
Funkcja powinna 'wiedzieć gdzie znajdują się urządzenia. Na przykład załącz oświetlenie
pod szafkami - wiadomo, że dotyczy kuchni.
Funkcja powinna zwracać serię komend. Na przykład dla komendy: wyłącz całe oświetlenie w
salonie należy zwrócić listę komend.
Funkcja powinna znać strukturę domu: Na przykład wyłącz całe oświetlenie na parterze.
Rozwiązanie powinno zawierać krótki opis, kod funkcji z komentarzami oraz zestaw poleceń,
którymi testowano funkcję


1. House structure XML:
https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2