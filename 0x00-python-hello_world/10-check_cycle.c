#include "lists.h"
/**
 * check_cycle - checks if a singly-linked list has a cycle
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *sl = list;
	listint_t *ft = list;/**pointers to list**/	

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	while (ft != NULL && ft->next != NULL)
	{
		sl = sl->next;/**moves one step*/
		ft = ft->next->next;/**moves two steps at a time*/

		if (sl == ft)
			return (1);
	}
	return (0);
}
