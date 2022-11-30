#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - check if a linked list has a cycle or not
 * @list: a pointer to the list
 * Return: 0 if has no cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *runner, *runner2;

	runner = list;
	runner2 = list;
	while (runner && runner2 && runner2->next)
	{
		runner = runner->next;
		runner2 = runner2->next->next;
		/* if runner and runner2 crush there's a loop */
		if (runner == runner2)
		{
			return (1);
		}
	}
	return (0);
}
