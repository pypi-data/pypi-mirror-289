# morefractions
Morefractions is a package with various classes and functions to manipulate fractions.

## Installation
run the command `pip install morefractions`

## Docs

### Class `Fraction`
`class Fraction(numerator: int | float, denominator: int | float)`

Returns a new Fraction with numerator `numerator` and denominator `denominator`.

#### Methods
`Fraction.reciprocal() -> Fraction`

Returns the inverse of this Fraction.

`Fraction.get_type() -> ("proper" | "improper" | "unit")`

Returns a string indicating whether this Fraction is a proper fraction, an improper fraction or a unit fraction.

### Class `MixedNumber`
`class MixedNumber(whole: int, fraction: Fraction)`

Returns a new MixedNumber with integer part `whole` and fractional part `fraction`.

#### Methods
`MixedNumber.reciprocal() -> MixedNumber`

Returns the inverse of this MixedNumber.

### Functions
`convert_to_fraction(x: int | float | MixedNumber) -> Fraction`

Create a Fraction from x, where x should be an int, float or MixedNumber.

`convert_to_mixed_number(x: int | float | Fraction) -> MixedNumber`

Create a MixedNumber from x, where x should be an int, float or Fraction.

`is_like(x: Fraction, y: Fraction) -> bool`

Returns a boolean indicating whether x and y are like fractions.

## Change Log

### v0.0.0a0
Initial creation