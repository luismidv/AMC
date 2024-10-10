/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.puntos;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
/**
 *
 * @author luism
 */
public class Divideandwin {
    
    private int id;
    private double x,y;
    public static int firstPoint,secondPoint;
    private static boolean betterCase, worstCase;
    private static double middleLine,leftDistance, rightDistance;
    private ArrayList<Divideandwin> worstCaseList;
   


    public Divideandwin( double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    public void worstCaseFunction(Divideandwin[] pointList){
        double dmin;
        if (this.leftDistance < this.rightDistance){
            dmin = this.leftDistance; 
        }else{
            dmin = this.rightDistance;
        }
        double minCordX = middleLine - dmin;
        double maxCordX = middleLine + dmin;
        
        for (int i = 1; i<pointList.length; i++){
            
            if (pointList[i].x > minCordX && pointList[i].x < maxCordX){
                worstCaseList.add(pointList[i]);
                
            }
        }
        
        
        
    }
    
    public static Divideandwin[] forwardAlgorithm(Divideandwin[] pointList){
        //NO LLAMAR ANTES QUE A GETDISTANCEPOINTS
        //RECONOCE EN QUE ZONA SE SITUAN DICHOS PUNTOS DE MENOR DISTANCIA
        //INICIALIZA LOS BOOLEANOS PARA RECONOCER EL CASO EN EL QUE ESTAMOS Y GUARDA LAS DISTANCIAS DI Y DD DEL ENUNCIADO
        int indexToDivide = pointList.length;
        indexToDivide /= 2;
        Divideandwin [] firstPart = Arrays.copyOfRange(pointList, 0, indexToDivide);
        Divideandwin [] secondPart = Arrays.copyOfRange(pointList, indexToDivide, pointList.length);
        middleLine = pointList[indexToDivide].x;
        System.out.println("Primer punto: " + Divideandwin.firstPoint + " Segundo punto: " + Divideandwin.secondPoint + " Middle point: " + indexToDivide);
        if (Divideandwin.firstPoint < indexToDivide && Divideandwin.secondPoint < indexToDivide){
            System.out.println("Entramos al mejor caso izquierda");
            betterCase = true;
            worstCase = false;
            leftDistance = calculateCords(pointList[firstPoint], pointList[secondPoint]);
            
        }else if (Divideandwin.firstPoint > indexToDivide && Divideandwin.secondPoint > indexToDivide){
            System.out.println("Entramos al mejor caso derecha");
            betterCase = true;
            worstCase = false;
            rightDistance = calculateCords(pointList[firstPoint], pointList[secondPoint]);
            
        }else{
            System.out.println("Entramos al peor caso");
            betterCase = false;
            worstCase = true;
            //worstCaseFunction(pointList);
        }
        return pointList;
    }
    
    public static double calculateCords(Divideandwin p1, Divideandwin p2){
        //CALCULA LA DISTANCIA ENTRE LOS DOS PUNTOS RECIBIDOS POR PARAMETRO
        //UTILIZA LA LIBRERÍA MATH
        //PARAMETROS:
            //p1: Objeto del tipo P1Amc
            //p2: Objeto del tipo P2Amc
        //DEVUELVE LA DISTANCIA ENTRE LOS PUNTOS RECIBIDOS
       
        int num = 4;
        double x = p2.x-p1.x;
        return x;
    }
    
    public static void getMinDistancePoints(Divideandwin[] pointList){
        //GUARDA EN LOS ATRIBUTOS FIRST POINT Y SECOND POINT PERTENECIENTES A LA CLASE
        //LOS PUNTOS CON LA MENOR DISTANCIA.
        //POSTERIORMENTE LLAMARIAMOS A FORWARDALGORITHM QUE 
        
        double minDistance = 0;
        
        for (int i = 1; i<pointList.length; i++){
            double distance = calculateCords(pointList[i-1], pointList[i]);
            if (i == 1){
                minDistance = distance;
            }else if(distance < minDistance){
                minDistance = distance;
                Divideandwin.firstPoint = i-1;
                Divideandwin.secondPoint = i;
                
            }
        }
    }
    public static void main(String[] args) {
        Divideandwin [] pointList = new Divideandwin[20];
        Random ran = new Random();
        
        for (int i = 0; i<20; i++){
            double x1 = ran.nextDouble();
            double y1 = ran.nextDouble();
            
            Divideandwin point = new Divideandwin(x1,y1);
            pointList[i] = point;
        }
        getMinDistancePoints(pointList);
        pointList = forwardAlgorithm(pointList);
        //EN CASO DE ENTRAR EN PEOR CASO, TENDRIAMOS QUE LLAMAR AL EXHAUSTIVO SOBRE LA LISTA WORSTCASELIST QUE ES LA FINAL DEL PEOR CASO
        if (worstCase){
            System.out.println("Entramos a exhaustivo peor caso");
            //LLAMADA A EXHAUSTIVO SOBRE ARRAYLIST
        }
            
        }
    
}





  