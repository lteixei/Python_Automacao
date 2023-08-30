package core;

import static core.DriverFactory.getDriver;

import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

public class BasePage {
	
/********* @throws InterruptedException ************/
 
	/********* ESCREVE DENTRO DE UMA FRAME ************/
	public void escrever(String name_campo, String texto) throws InterruptedException{
		Thread.sleep(5000);
		getDriver().switchTo().frame("iframe");
		getDriver().findElement(By.xpath(name_campo)).clear();
		getDriver().findElement(By.xpath(name_campo)).sendKeys(texto);
		getDriver().switchTo().defaultContent();
	}
	
	/********* ESCREVE DENTRO DE DUAS FRAMES ************/
	public void escreverComDoisIframes(String name_campo, String texto) throws InterruptedException{
		Thread.sleep(5000);
		getDriver().switchTo().frame(0);
		getDriver().switchTo().frame("iframe");
		getDriver().findElement(By.xpath(name_campo)).clear();
		getDriver().findElement(By.xpath(name_campo)).sendKeys(texto);
		getDriver().switchTo().defaultContent();
		getDriver().switchTo().defaultContent();
	}
	
	/********* ESCREVE FORA DA FRAME ************/
	public void escreverSemTroca(String name_campo, String texto) throws InterruptedException{
		getDriver().findElement(By.xpath(name_campo)).clear();
		getDriver().findElement(By.xpath(name_campo)).sendKeys(texto);
	}	
	
	/********* CLICA NO BOTÃO DENTRO DE UMA FRAME - USANDO ID ************/
	
	public void clicarBotao(String id) {
		getDriver().switchTo().frame("iframe");
		getDriver().findElement(By.id(id)).click();
		getDriver().switchTo().defaultContent();
	}
	
	/********* CLICA NO BOTÃO DENTRO DE DUAS FRAMES - USANDO XPATH ************/
	public void clicarBotaoIframe(String xpath) {
		getDriver().switchTo().frame(0);
		getDriver().switchTo().frame("iframe");
		getDriver().findElement(By.xpath(xpath)).click();
		getDriver().switchTo().defaultContent();
		getDriver().switchTo().defaultContent();
	}
	
	/********* CLICA NO BOTÃO FORA DA FRAME - USANDO ID ************/
	public void clicarBotaoSemTroca(String id) throws InterruptedException {
		Thread.sleep(8000);
		getDriver().findElement(By.id(id)).click();
	}
	
	/********* CLICA NO BOTÃO FORA DA FRAME - USANDO XPATH ************/
	public void clicarXpath(String element) throws InterruptedException {
		Thread.sleep(2000);
		getDriver().findElement(By.xpath(element)).click();
	}
	
	/********* CLICA NO BOTÃO FORA DA FRAME - USANDO CSS ************/
	public void clicarCss(String css) throws InterruptedException {
		Thread.sleep(2000);
		getDriver().findElement(By.cssSelector(css)).click();
	}
}
