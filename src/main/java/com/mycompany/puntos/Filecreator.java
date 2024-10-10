/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.puntos;

import java.io.File;
import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author luism
 */
public class Filecreator {
    
    static int sizePoints;
    static Punto[] points;
    
    public static void pointCreator(){
       
       Scanner scan = new Scanner(System.in);
       System.out.println("Introduce a size for the point's list");
       Filecreator.sizePoints = scan.nextInt();
       Filecreator.points = new Punto[sizePoints];
       
        for(int i = 0; i<sizePoints; i++){
            Random ran = new Random();
            int point_x = ran.nextInt(0,1920);
            int point_y = ran.nextInt(0,1080);
            Punto point = new Punto(point_x, point_y);
            Filecreator.points[i] = point;
        }
        
        
    }
    
    public static void fileWriter(){
        Scanner scan = new Scanner(System.in);
        String currentPath = ".";
        File fileManager = new File(currentPath);
        
        System.out.println("Introduce a name for the file");
        String fileName = scan.nextLine();
        
        
        
    }
    public static void main(String[] args) {
        // TODO code application logic here
       
       pointCreator();
       fileWriter();
       
       
       //File fileManager = new File();
       
       
       
       
       
   }
}
