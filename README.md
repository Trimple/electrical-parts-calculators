# electrical-parts-calculators
Simple python 3 script for voltage divider parameters calculation

this script was made mostly to learn git-basics on practical task and to practise code documentation. Also, i'm not very good at python.

This python script allows to calculate resistor divider parameters. Script can:
* Calculate output voltage if input one and both resistances are known
* Calculate input voltage if output one and both resistances are known
* Calculate upper resistor (R1) with standart value if R2 and both voltages are known
* Calculate lower resistor (R2) with standart value if R1 and both voltages are known
* Calculate both R1 and R2 if only voltages are known

Script gets input data with console flags. For example

```bash
python main.py --iv 12.6 --ov  3.3 --r1 24000 --a1 0.05 --a2 0.05

python main.py --iv 25.2 --ov 5
```

Available flags:
* --iv - input voltage in Volts
* --ov - output voltage in Volts
* --r1 - resistance of R1 in Ohms
* --r2 - resistance of R2 in Ohms
* --a1 - accuracy of R1 default value: 0.01 (1%)
* --a2 - accuracy of R2 default value: 0.01 (1%)

Program will calculate all missing parameters if it can. If can't it will show specific mistake message. After calculating parameters it will show console message with all information (voltages, resistances, output mistake, current through circuit, power dissipation in circuit) for every suitable result (can be 2 resalts if program couldn't found proper standart value of resistor).
