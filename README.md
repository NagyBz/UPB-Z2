# UPB-Z2
Zadanie 2 – Implementácia aplikácie na šifrovanie súborov
Vytvorte aplikáciu, ktorá umožní používateľovi šifrovať a dešifrovať súbory symetrickým kľučom K,
náhodne vygenerovaným a uloženým niekde mimo zašifrovaného súboru (popr. správy). Použite symetrickú kryptografiu.
Na riešenie zadania využite hotove kryptograficke API, (nepoužívať vlastné  implementácie kryptografických funkcií).

Python 3.7.9

pip install -r requirements.txt
python encrypt.py -h
python decrypt.py -h

MACOS : mkfile -n 1953125b 1GB_file
LINUX : fallocate -l 1000000000 1GB_file
Windows : fsutil file createnew  1GB_file 1000000000

python encrypt.py -i 1GB_file -o secret
python decrypt.py -i secret -k key.bin

python encrypt.py -i text -o secret
python decrypt.py -i secret -k key.bin


