#include "lists.h"
/**
  * insert_node - function in C that inserts a number
  * into a sorted singly linked list.
  * @head: head of linked list
  * @number: integer to add
  * Return: the address of the new node, or NULL if it failed
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current && current->next && current->next->n < number)
		current = current->next;
	new->next = current->next;
	current->next = new;
	return (new);
}
