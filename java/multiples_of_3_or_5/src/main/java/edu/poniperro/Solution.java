package edu.poniperro;

public class Solution {
    public int solution(int numero) {
        int suma = 0;
        if(numero>0)  {
            int natural = 0;
            int multiplo_de_3, multiplo_de_5, multiplo_de_15;
            while(true){    //para generar indefinidamente los siguientes numeros
                natural++;
                multiplo_de_3 = natural * 3;
                multiplo_de_5 = natural * 5;
                if(multiplo_de_3<numero || multiplo_de_5<numero){
                    //System.out.println(multiplo_de_3 +"--" + multiplo_de_5);
                    if (multiplo_de_3 < numero) suma += multiplo_de_3;
                    if (multiplo_de_5 < numero) suma += multiplo_de_5;
                }
                else break;
            }
            natural = 0;
            while(true){
                natural++;
                multiplo_de_15 = natural*15;
                if(multiplo_de_15<numero) suma -= multiplo_de_15;
                else break;
            }
        }
        return suma;
    }
}
