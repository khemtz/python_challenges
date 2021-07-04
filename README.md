# python_challenges
Some examples that will help to understand some basic features on python


## validate_ip.py

On this script will takes the value from the args, some examples for run:
```
	$./validate_ip.py 172.16.23.14 
	$./validate_ip.py 2001:0db8:85a3:0000:0000:8a2e:0370:7334
	$./validate_ip.py 11110000.11110000.11110000.11110000 
	$./validate_ip.py "11110000 11110000 11110000 11110000" 
	$./validate_ip.py 1111000011110000.1111000011110000.1111000011110000.1111000011110000.1111000011110000.1111000011110000.1111000011110000.1111000011110000
	$./validate_ip.py "1111000011110000 1111000011110000 1111000011110000 1111000011110000 1111000011110000 1111000011110000 1111000011110000 1111000011110000"
```

## pythagoran.py
taking the pythagoras triangle i assume that for be a valid pythagoran triangle the formula must be true:

a*a + b*b = c*c

![pythagoran triangle](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Trigonometria_01a.svg/1200px-Trigonometria_01a.svg.png)

where:
    A = a Side
    B = a Side
    C = Hypotenuse

so the script try with the diferent combinatiosn of the numbers and if one of this combinations are valid with the formula indicates you how tha numbers must be set.

for use:

```
$ ./pythagoran.py
Bring 3 Integer Numbers (separate by space):3 4 5
These numbers are a valid pythagorean triplet when:
  A (side)=3
  B (side)=4
  C (hypotenuse)=5
```


## NOTES

both scripts have on the first line the location of python3 compiler, for my PC is located on: /usr/bin/python3, in case of the script not runs try to locate where is setted yout python compiler:

``` which python3 ```

or if is better for you just delete the first line and run like that:

``` $python3 pythagoran.py ```
