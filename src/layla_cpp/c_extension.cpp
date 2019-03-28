#include <Python.h>
#include "pch.h"
#include <iostream>
#include "MathLibrary.h"

static PyObject *sq(PyObject *self, PyObject *args) {
  int input;
  if (!PyArg_ParseTuple(args, "i", &input)) {
    return NULL;
  }

  return PyLong_FromLong((long)input * (long)input);
}

static PyObject *blah(PyObject *self, PyObject *args) {
	// Initialize a Fibonacci relation sequence.
	fibonacci_init(1, 1);
	// Write out the sequence values until overflow.
	do {
		std::cout << fibonacci_index() << ": "
			<< fibonacci_current() << std::endl;
	} while (fibonacci_next());
	// Report count of values written before overflow.
	std::cout << fibonacci_index() + 1 <<
		" Fibonacci sequence values fit in an " <<
		"unsigned 64-bit integer." << std::endl;

	return Py_None;
}

static PyMethodDef example_methods[] = {
    {"square", sq, METH_VARARGS, "Returns a square of an integer."},
    {"blah", blah, METH_VARARGS, "Runs fibonacci stuff in a loop."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef example_definition = {
    PyModuleDef_HEAD_INIT,
    "example",
    "A Python module containing a square() function",
    -1,
    example_methods
};

// The name of the function here should PyInit_<x> where <x> is the module/submodule name in setup.py
PyMODINIT_FUNC PyInit_mycmodule(void) {
  Py_Initialize();
  PyObject *m = PyModule_Create(&example_definition);

  return m;
}