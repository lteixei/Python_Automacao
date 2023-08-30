package utils;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.io.FileUtils;

import org.apache.commons.io.FileExistsException;
import org.apache.commons.io.FileUtils;
import org.apache.commons.io.IOUtils;

public class ReadUtils {

	private String diretorioArquivos = "C:\\Users\\T3666975\\ProjetosTim\\Chip_Automacao";
	private String nomeArquivo = "Chip_Automacao.txt";
	List<String> linhas = new ArrayList<String>();
	
	public String doReadAndFind(String key1, String key2, int skip){	
		File arquivo = new File(diretorioArquivos, nomeArquivo);
		
		try {
			if (arquivo.exists()) {
				linhas = FileUtils.readLines(arquivo, "UTF-8"); 
			} else {
				throw new Exception("Arquivo não existe");
			}
		} catch (Exception e) {
			System.out.println("Falha ao ler arquivo:" + arquivo.getAbsolutePath());
			e.printStackTrace();
			
		} 
		return find(key1,key2,skip);
		
	}
	
	
	public String find(String key1, String key2, int sequence){
		int n = 0;
		String res="";
		for (String linha : linhas){
			if(linha.indexOf(key1 + ";" + key2) > 0 ){
				if(n > sequence){
					res = linha.substring(0,20);
					break;
				}
				n++;
			}
		}
		return res;
	}

}
