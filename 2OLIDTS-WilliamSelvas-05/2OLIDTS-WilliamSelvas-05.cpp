// 2OLIDTS-WilliamSelvas-05.cpp : Este archivo contiene la función "main". La ejecución del programa comienza y termina ahí.
#include <iostream>
#include <vector>
using namespace std;


void pop_arreglo_aves(vector<string> aves) {
	aves.pop_back();
	cout << "Los valores del vector despues del pop \n";
	for (int i = 0; i < aves.size(); ++i) {
		cout << aves[i] << " ";

	}
	cout << "\n";

}
vector<string> push_arreglo_aves(vector<string> aves) {
	//Agrega tres valores al final del vector utilizando push_back()
	aves.push_back("Mayna");
	aves.push_back("Periquitos");
	aves.push_back("Cacatua");
	cout << "Los valores del vector despues de insertar: \n";
	//Iter sobre el vector para impriir los valores
	for (int i = 0; i < aves.size(); ++i) {
		cout << aves[i] << " ";
	}
	cout << "\n";
	return aves;
}

void arreglo_aves(vector<string> aves) {
	cout << " Los valores del vector antes de insertar \n";
	//Iter sobre el vector para impriir los valores
	for (int i = 0; i < aves.size(); ++i) {
		cout << aves[i] << " ";
	}
	cout << "\n";
}

int main()
{
	vector<string> aves = { "Loro gris, ", "Paloma de diamente, ", "Coctel" };
	vector<string> nuevo_aves = {};
	arreglo_aves(aves);
	nuevo_aves = push_arreglo_aves(aves);
	pop_arreglo_aves(nuevo_aves);
	return 0;
}
