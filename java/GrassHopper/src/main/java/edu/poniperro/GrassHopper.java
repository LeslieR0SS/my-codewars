package edu.poniperro;

public class GrassHopper {
    public static int findAverage(int[] numeros) {
        int suma = 0;
        for(int i=0; i < numeros.length; i++) suma += numeros[i];
        int promedio = suma/ numeros.length;
        return promedio;
    }
}
