# web_data_visualizer

## Motivacija projekta

Projekat se radi u okviru diplomskog rada na temu: "Prikaz rezultata analize podataka na web-u pomoću Python-a sa konkretnim primjerom".

### Dataset

Skup podataka koji je korišćen je sa Kaggle platforme i nalazi se na sledećem link-u:

https://www.kaggle.com/datasets/azminetoushikwasi/ucl-202122-uefa-champions-league

Dataset sadrži više csv fajlova (attacking.csv, goals.csv, defending.csv), tako da su podaci raspoređeni po više fajlova. Međutim u ovom notebook-u je korišćen samo jedan fajl? Svi fajlovi su spojeni u jedan sa pandasql paketom pomoću upita. Upit i fajl su pronađeni sa sledeće internet adrese:

https://www.kaggle.com/code/rakhaalcander/ucl-2021-2022-player-data-analysis

### Google colab notebook

Na sledećem linku se nalazi colab notebook u kojem se nalazi kod za čišćenje i osnovnu analizu dataset-a koji se koristi u projektu:

https://colab.research.google.com/drive/1Szd1rwLyXHtKhw2lJZUYXxPkQewMyVBP?usp=sharing

### Izgled web sajta

U nastavku su screenshot-ovi web sajta:

![alt text](https://github.com/Balsa-Dogandzic/web_data_visualizer/blob/main/docs/Pocetna.png?raw=True)

![alt text](https://github.com/Balsa-Dogandzic/web_data_visualizer/blob/main/docs/Klubovi.png?raw=True)

![alt text](https://github.com/Balsa-Dogandzic/web_data_visualizer/blob/main/docs/Klub.png?raw=True)

### TODO

1. Još analize u notebook-u
2. Dodati nove kolone u dataset-u (ocjena, golovi po meču itd.)
3. Pronaći još literature
4. Dovršiti stranice: početna, klubovi, klub
5. Napraviti stranice igrači, igrač
