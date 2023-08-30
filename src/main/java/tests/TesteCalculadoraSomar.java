package tests;

import org.junit.Test;


import pages.calculadora;


public class TesteCalculadoraSomar {
    private static calculadora calculadora;
    public static void main(String[] args) throws Exception {
        //Arrange
	    calculadora = new calculadora();
		int resultadoEsperado = 16;

        //Act
		int resultado = calculadora.somar(10,6);

        //Assert
		if (resultado == resultadoEsperado) {
			System.out.println("Teste OK");
			System.out.println("O resultado esperado era: " + resultadoEsperado + " e o resultado da soma foi: " + resultado);
		} else{
			System.out.println("Teste Falhou");
			System.out.println("O resultado esperado era: " + resultadoEsperado + " e o resultado da soma foi: " + resultado);
		}
    }
}
