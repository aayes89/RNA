package rna;

/**
 *
 * @author MSc. Allan Ayes Ramírez, Lic.
 *	   Solución al perceptrón para la tabla XOR lógica
 */
public class RNAxor {

    public static void main(String[] args) {

        /*vector de prueba, tabla de verdad xor
         Las notaciones empleadas (-1,1) o (1,0)
         */
        //double x[][] = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
        double x[][] = {{1, 1}, {1, 0}, {0, 1}, {0, 0}};
        //vector solución
        double y[] = {-1, 1, 1, -1};
        //condición de detención
        boolean error;
        //puntero
        int fila = 0;
        //iteraciones
        int iter = 0;
        /*hacer mientras, al menos una vez (funciona con o sin esta estructura)
         varían los tiempos de obtención de cada entrenamiento*/
        /*do {
         error = false;
         */ while (fila < 4) {
            double w11 = Math.random();//-1.942779536696304;//Pesos neurona 1
            //System.out.println("w11: "+w11);
            double w12 = Math.random();//-2.4033439922084954;
            //System.out.println("w12: "+w12);
            double θ1 = (-1) * Math.random(); //-2.2690966258542424;
            //System.out.println("01: "+θ1);
            double w21 = Math.random();//1.476484576128277;//Pesos neurona 2
            //System.out.println("w21: "+w21);
            double w22 = Math.random();//1.5285706752204653;
            //System.out.println("w22: "+w22);
            double θ2 = (-1) * Math.random();//-1.2654579142409594;
            //System.out.println("02: "+θ2);
            double w31 = Math.random();//-2.7857541174718032;//Pesos neurona 3
            //System.out.println("w3: "+w31);
            double w32 = Math.random();//-2.81730152144229;
            //System.out.println("w32: "+w32);
            double θ3 = (-1) * Math.random();//-2.52832962325685;
            //System.out.println("03: "+θ3);
            //Calculo de las salidas de las neuronas
            double y1 = Math.tanh((x[fila][0] * w11) + (x[fila][1] * w12) + (1 * θ1));
            double y2 = Math.tanh((x[fila][0] * w21) + (x[fila][1] * w22) + (1 * θ2));
            double y3 = Math.tanh((y1 * w31) + (y2 * w32) + (1 * θ3));
            //función de activación
            y3 = (y3 >= 0) ? 1 : -1;
            //controlo las iteraciones por cada entrenamiento
            iter++;
            //verifico
            if (y3 != y[fila]) {
                /*error = true;
                 y1 = Math.tanh((x[fila][0] * w11) + (x[fila][1] * w12) + (1 * θ1));
                 y2 = Math.tanh((x[fila][0] * w21) + (x[fila][1] * w22) + (1 * θ2));
                 y3 = Math.tanh((y1 * w31) + (y2 * w32) + (1 * θ3));*/
            } else {
                System.out.print("Entrada: " + x[fila][0] + " , " + x[fila][1] + " ");
                System.out.println("Iteración: " + iter);
                //Mostrar resultado
                System.out.println("Salida (y3) = " + (int) y3 + "\n");
                fila++;
                iter = 0;
            }
        }
        //} while (error);
    }
}
