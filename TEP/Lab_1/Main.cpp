#include <iostream>
#include "Lista_1.h"

using namespace std;

int main() {
	int** pi_table;
	b_alloc_table_2_dim(&pi_table, 5, 3);
	b_dealloc_table_2_dim(pi_table, 5, 3);

	char*** ps_table;
	b_alloc_table_3_dim(&ps_table, 5);
	b_dealloc_table_3_dim(ps_table, 5);

	cin.get();
	return 0;
}