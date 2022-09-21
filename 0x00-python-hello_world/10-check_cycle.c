#include "lists.h"

/**
 * check_cycle - check if a singly linked list contains a loop
 * @list: pointer to head of a list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && (fast = fast->next))
	{
		if (fast == slow)
			return (1);

		fast = fast->next;
		slow = slow->next;
	}
	return (0);
}
