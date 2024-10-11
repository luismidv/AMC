/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.puntos;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author luism
 */
public class Filecreator {
    
    static int sizePoints;
    static Punto[] points;
    
    public Filecreator(Punto[] points){
        this.points = points;
        Filecreator.sizePoints = points.length;
    }
    
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
    public static void fileWriter() throws IOException{
        Scanner scan = new Scanner(System.in);
        System.out.println("Introduce a name for the file");
        String fileName = scan.nextLine();
        String currentPath = "./" + fileName+Filecreator.sizePoints +".tsp";
        
        FileWriter fWriter = new FileWriter(currentPath);
        fWriter.write("NAME: " + fileName + "\n" + "TYPE: TSP\nCOMMENT: File created by Luismi and Ageu\n"
                      + "DIMENSION: " + Filecreator.sizePoints + "\nEDGE_WEIGHT_TYPE: GEO\nEDGE_WEIGHT_FORMAT: FUNCTION\n"
                      + "DISPLAY_DATA_TYPE: COORD_DISPLAY\nNODE_COORD_SECTION\n");
        for(int id = 0; id<Filecreator.sizePoints; id++){
            fWriter.write("\t" + id + "\t" + Filecreator.points[id].x + "\t\t" + Filecreator.points[id].y + "\n");
        }
        
        fWriter.write("EOF");
        
        fWriter.close();
    }
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
       pointCreator();
       fileWriter();
       
       
       
       
       
       
   }
}
