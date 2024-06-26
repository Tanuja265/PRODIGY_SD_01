#include <stdio.h>
double celToFah(double celsius);
double celToKel(double celsius);
double fahToCel(double fahrenheit);
double fahToKel(double fahrenheit);
double kelToCel(double kelvin);
double kelToFah(double kelvin);

int main() {
    double temperature;
    char unit;
    printf("Enter the temperature value: ");
    scanf("%lf", &temperature);
    printf("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ");
    scanf(" %c", &unit);
    if (unit == 'C' || unit == 'c') {
        double fahrenheit = celToFah(temperature);
        double kelvin = celToKel(temperature);
        printf("Temperature in Fahrenheit: %.2lf F\n", fahrenheit);
        printf("Temperature in Kelvin: %.2lf K\n", kelvin);
    } else if (unit == 'F' || unit == 'f') {
        double celsius = fahToCel(temperature);
        double kelvin = fahToKel(temperature);
        printf("Temperature in Celsius: %.2lf C\n", celsius);
        printf("Temperature in Kelvin: %.2lf K\n", kelvin);
    } else if (unit == 'K' || unit == 'k') {
        double celsius = kelToCel(temperature);
        double fahrenheit = kelToFah(temperature);
        printf("Temperature in Celsius: %.2lf C\n", celsius);
        printf("Temperature in Fahrenheit: %.2lf F\n", fahrenheit);
    } else {
        printf("Invalid unit of measurement.\n");
    }

    return 0;
}
double celToFah(double celsius) {
    return (celsius * 9/5) + 32;
}
double celToKel(double celsius) {
    return celsius + 273.15;
}
double fahToCel(double fahrenheit) {
    return (fahrenheit - 32) * 5/9;
}
double fahToKel(double fahrenheit) {
    return (fahrenheit - 32) * 5/9 + 273.15;
}
double kelToCel(double kelvin) {
    return kelvin - 273.15;
}
double kelToFah(double kelvin) {
    return (kelvin - 273.15) * 9/5 + 32;
}