#pragma once
#include "CRefCounter.h"

template <typename T>
class CMySmartPointer
{
public:
	CMySmartPointer(const CMySmartPointer &pcOther);
	CMySmartPointer(T *pcPointer);
	~CMySmartPointer();
	T& operator*() { return *pc_pointer; }
	T* operator->() { return pc_pointer; }
	CMySmartPointer & operator=(const CMySmartPointer & cOther);
	T * getT() { return pc_pointer; }
	T at(int iOffset);
	void vSetSize(int iNewSize) { i_size = iNewSize; }

private:
	T * pc_pointer;
	int i_size;
	CRefCounter *pc_counter;
};

template <typename T>
CMySmartPointer<T>::CMySmartPointer(T *pcPointer)
{
	vSetSize(0);
	pc_pointer = pcPointer;
	pc_counter = new CRefCounter();
	pc_counter->iAdd();
}

template <typename T>
CMySmartPointer<T>::CMySmartPointer(const CMySmartPointer & pcOther)
{
	pc_pointer = pcOther.pc_pointer;
	pc_counter = pcOther.pc_counter;
	pc_counter->iAdd();
}

template <typename T>
CMySmartPointer<T>::~CMySmartPointer()
{
	if (pc_counter->iDec() == 0)
	{
		delete pc_counter;
		if (i_size == 0) {
			delete pc_pointer;
		}
		else {
			delete[] pc_pointer;
		}
	}
}

template<typename T>
CMySmartPointer<T> & CMySmartPointer<T>::operator=(const CMySmartPointer & cOther)
{
	pc_counter->iDec();
	pc_counter = cOther.pc_counter;
	pc_pointer = cOther.pc_pointer;

	return *this;
}

template<typename T>
T CMySmartPointer<T>::at(int iOffset)
{
	if (iOffset >= i_size) {
		throw std::out_of_range("iOffset is greater than size.");
	}

	return pc_pointer[iOffset];
}