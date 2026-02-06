#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 * int val;
 * struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // 1. Criamos um "Nó Cabeça Fictício" (Dummy Head).
    // Isso evita ter que escrever "if (head == NULL)" toda hora.
    struct ListNode *dummyHead = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode *atual = dummyHead; 
    
    int carry = 0; // O famoso "vai-um"

    // 2. O Loop continua enquanto houver nó em l1, OU em l2, OU sobrar um carry
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int soma = carry; // Começa com o valor do "vai-um" anterior

        // Se l1 ainda tem números, soma e avança
        if (l1 != NULL) {
            soma += l1->val;
            l1 = l1->next;
        }

        // Se l2 ainda tem números, soma e avança
        if (l2 != NULL) {
            soma += l2->val;
            l2 = l2->next;
        }

        // 3. Calcula o novo dígito e o novo carry
        carry = soma / 10; // Ex: 15 / 10 = 1 (vai-um)
        int novoDigito = soma % 10; // Ex: 15 % 10 = 5 (fica no nó)

        // 4. Cria o novo nó com o resultado
        atual->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        atual = atual->next; // Avança nosso ponteiro de construção
        atual->val = novoDigito;
        atual->next = NULL;
    }

    // 5. Retornamos o próximo do dummy (que é o verdadeiro início da lista)
    struct ListNode *resultado = dummyHead->next;
    free(dummyHead); // Limpa o nó fictício da memória
    return resultado;
}
