#include "lists.h"
/**
 * ispalindrome - function to check for a palindrome linked list
 * @head: pointer to a pointer pointing to a struct
 * Return: integer
 */
int is_palindrome(listint_t **head)
{
    listint_t *help = *head, *some = *head, *rome = *head;
    int i = 0, countcopy;
    unsigned int count = 0;
    while (help != NULL)
    {
        count++;
        help = help->next;
    }
    countcopy = count;
    int *arr = (int *)malloc(sizeof(countcopy * sizeof(int)));
    while (some != NULL)
    {
        *(arr + i) = some->n;
        some = some->next;
        i++;
    }
    int *brr = (int *)malloc(sizeof(countcopy * sizeof(int))), k = countcopy - 1, K = 0;
    for (; k >= 0; k--)
    {
        *(brr + K) = *(arr + k);
        K++;
    }
    int *crr = (int *)malloc(sizeof(countcopy * sizeof(int))), L = 0, result = 0;
    for (; L < countcopy; L++)
    {
        if (brr[L] == arr[L])
        {
            crr[L] = 1;
            result++;
        }
        else
        {
            crr[L] = 0;
        }
    }
    if (result == countcopy)
    {
        return (1);
    }
    else
    {
        return (0);
    }
}
