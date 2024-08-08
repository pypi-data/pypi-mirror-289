**UzbekistanWeather paketi haqida qo'llanma**

ishlatilishi:
```python
from uzbekistanweather import UzbekistanWeather

weather = UzbekistanWeather("hudud_nomi") # masalan toshkent yoki andijon
```

```python
print(weather.today())
```
malumot json ko'rinishida qaytib keladi

to'liq kod
```python
from uzbekistanweather import UzbekistanWeather

weather = UzbekistanWeather("toshent")

print(weather.today())
```

siz olishingiz mumkun bo'lgan viloyatlar va hududlar ro'yxati:
**andijon, toshken, buxoro, guliston, jizzax, zarafshon, qarshi, navoiy, namangan, nukus, samarqand, termiz, urganch, farg'ona, xiva**