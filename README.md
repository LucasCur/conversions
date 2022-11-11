# Conversions

- Conversions is a simple python function that takes in two arguments, with the first being a measurement, (such as "10cm" or "24ft").
- The second argument defines what degree of accuracy any floating point answers will be rounded to - for example, "5" tells conversions to round all conversions to 5 decimal places.

## Example Usage

10 centimetres to 3 decimal places
```
>>> convert("10cm","3")
10cm = 100.000mm
10cm = 0.100m
10cm = 0.000km
10cm = 3.937in
10cm = 0.109yrd
10cm = 0.328ft
```

1 foot to 5 decimal places
```
>>> convert("1ft","5")
1ft = 304.80000mm
1ft = 30.48000cm
1ft = 0.30480m
1ft = 0.00030km
1ft = 12.00000in
1ft = 0.33333yrd
```

## Every Unit of Measurement (UoM)'s Abbreviation

- Millimetre - mm
- Centimetre - cm
- Metre - m
- Kilometre - km
- Inch - in
- Yard - yrd
- Foot - ft
