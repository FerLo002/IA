#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define EPOCHS 30000  // Número de épocas de entrenamiento
#define LEARNING_RATE 0.1f  // Tasa de aprendizaje

// Función de activación sigmoide
float sigmoid(float x) {
    return 1.0f / (1.0f + exp(-x));
}

// Derivada de la función sigmoide para el cálculo del gradiente
float sigmoid_derivative(float x) {
    return x * (1.0f - x);
}

// Función XOR utilizando una red de perceptrones de dos capas
int main() {
    // Conjunto de entrenamiento para XOR
    float input[4][2] = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};
    float target[4] = {1, 0, 0, 1};  // Salidas esperadas para XOR

    // Pesos y biases para la capa oculta
    float weights_hidden[2][2];
    float bias_hidden[2] = {-0.5f, -1.5f};  // Valores del bias según el diagrama

    // Pesos y bias para la capa de salida
    float weights_output[2];
    float bias_output = 0.5f;

    // Inicialización aleatoria de los pesos
    for (int i = 0; i < 2; i++) {
        weights_hidden[i][0] = (float)rand() / RAND_MAX - 0.5f;  // Pesos para z1 y z2
        weights_hidden[i][1] = (float)rand() / RAND_MAX - 0.5f;
        weights_output[i] = (float)rand() / RAND_MAX - 0.5f;     // Pesos para la salida
    }

    // Entrenamiento del modelo
    for (int epoch = 0; epoch < EPOCHS; epoch++) {
        float total_error = 0;

        // Iteración sobre cada ejemplo de entrenamiento
        for (int i = 0; i < 4; i++) {
            // Forward propagation para la capa oculta
            float z1_input = input[i][0] * weights_hidden[0][0] + input[i][1] * weights_hidden[1][0] + bias_hidden[0];
            float z2_input = input[i][0] * weights_hidden[0][1] + input[i][1] * weights_hidden[1][1] + bias_hidden[1];
            float z1_output = sigmoid(z1_input);
            float z2_output = sigmoid(z2_input);

            // Forward propagation para la capa de salida
            float output_input = z1_output * weights_output[0] + z2_output * weights_output[1] + bias_output;
            float output = sigmoid(output_input);

            // Error
            float error = target[i] - output;
            total_error += error * error;

            // Backpropagation (ajuste de pesos y biases)
            // Gradiente para la salida
            float delta_output = error * sigmoid_derivative(output);
            weights_output[0] += LEARNING_RATE * delta_output * z1_output;
            weights_output[1] += LEARNING_RATE * delta_output * z2_output;
            bias_output += LEARNING_RATE * delta_output;

            // Gradientes para la capa oculta
            float delta_z1 = delta_output * weights_output[0] * sigmoid_derivative(z1_output);
            float delta_z2 = delta_output * weights_output[1] * sigmoid_derivative(z2_output);

            weights_hidden[0][0] += LEARNING_RATE * delta_z1 * input[i][0];
            weights_hidden[1][0] += LEARNING_RATE * delta_z1 * input[i][1];
            bias_hidden[0] += LEARNING_RATE * delta_z1;

            weights_hidden[0][1] += LEARNING_RATE * delta_z2 * input[i][0];
            weights_hidden[1][1] += LEARNING_RATE * delta_z2 * input[i][1];
            bias_hidden[1] += LEARNING_RATE * delta_z2;
        }

        // Imprimir el error promedio cada 1000 épocas para observar el progreso
        if (epoch % 1000 == 0) {
            printf("Epoch %d, Error promedio: %f\n", epoch, total_error / 4.0f);
        }
    }

    // Probar la red después del entrenamiento
    printf("\nResultados finales:\n");
    for (int i = 0; i < 4; i++) {
        float z1_input = input[i][0] * weights_hidden[0][0] + input[i][1] * weights_hidden[1][0] + bias_hidden[0];
        float z2_input = input[i][0] * weights_hidden[0][1] + input[i][1] * weights_hidden[1][1] + bias_hidden[1];
        float z1_output = sigmoid(z1_input);
        float z2_output = sigmoid(z2_input);

        float output_input = z1_output * weights_output[0] + z2_output * weights_output[1] + bias_output;
        float output = sigmoid(output_input);

        printf("Input: (%d, %d), Output: %f, Esperado: %f\n", (int)input[i][0], (int)input[i][1], output, target[i]);
    }

    return 0;
}
