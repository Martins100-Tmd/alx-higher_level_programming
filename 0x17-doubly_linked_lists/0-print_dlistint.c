#include <stdio.h>
#include <stdlib.h>
/**
 * print_dlistint - prints the number of node in a linked list
 * @h: pointer to a doubly linked list
 * Return: size_t
 */
size_t print_dlistint(const dlistint_t *h)
{
	unsigned int count = 0;

	if (h != NULL)
	{
		while (h)
		{
			count++;
			h = h->next;
		}
		return (count);
	}
}
