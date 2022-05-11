# Sterowanie-urzadzeniami-w-jezyku-naturalnym
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
