# **CPF validator**

## This is a personal project for validating a CPF document, with didactic instructions on how to calculate the validation of check digits

### Introduction

Official Brazilian documents (CPF, CNPJ, voter registration, CNH) have some digits that verify the validity of the others. They are known as check digits. In CPF and CNPJ documents they come after the "-" and serve to validate the authentication of the document number, thus avoiding typing errors and fraud
<pre>
</pre>

## **Validating the FIRST check digit of a CPF**

### CPF example - 145.382.206-20

<p>
It works through weights associated with each number and a division by the prime number 11 at the end.<br />
It starts using the first 9 digits, multiplying them by the descending sequence from 10 to 2, and we add that result
</p>

| 1  | 4  | 5  | 3  | 8  | 2  | 2 | 0 | 6   |
|----|----|----|----|----|----|---|---|-----|
| X  | X  | X  | X  | X  | X  | X | X | X   |
| 10 | 9  | 8  | 7  | 6  | 5  | 4 | 3 | 2   |
| 10 | 36 | 40 | 21 | 48 | 10 | 8 | 0 | 12  |

***10 + 36 + 40 + 21 + 48 + 10 + 8 + 0 + 12 = 185***


With this result we will divide it by 11, but the important thing is not the result, but the modulus:

***185 % 11 = 9***
<pre>
</pre>

The module is 9. Now to calculate the check digit, let's subtract this remainder from the number 11: <br />
***11 - 9 = 2***

The result of the subtraction was 2, the first check digit is equal to 2. If the result of this division is 10 or greater, the penultimate check digit will be 0.

<pre>

</pre>

## **Validating the SECOND check digit of a CPF**

<p>
Similar to the first one, but let's consider the first previously calculated check digit. So the multiplication is done from 11 to 2.
</p>

| 1  | 4  | 5  | 3  | 8  | 2  | 2  | 0 | 6  | 2  |
|----|----|----|----|----|----|----|---|----|----|
| X  | X  | X  | X  | X  | X  | X  | X | X  | X  |
| 11 | 10 | 9  | 8  | 7  | 6  | 5  | 4 | 3  | 2  |
| 11 | 40 | 45 | 24 | 56 | 12 | 10 | 0 | 18 | 4  |

***11 + 40 + 45 + 24 + 56 + 12 + 10 + 0 + 18 + 4 = 220***

<br />

Once again, let's divide by 11 using the modulus:

***220 % 11 = 0***
<br />
<br />

Do the subtraction: <br />
***11 - 0 = 11***

Since the value is equal to or greater than 10, the last digit is 0.

Thus, we confirm the two verification digits of our CPF 145.382.206-**20** and we know that this CPF is valid. Another very important rule is that CPFs with the same numbers as: 111.111.111-11, 222.222.222-22, among others, are valid CPFs by the algorithm but do not exist in the official registry. So this type of CPF cannot be used.