#include <Python.h>
#include "pch.h"
#include <iostream>
#include "MathLibrary.h"

static PyObject *pyfibonacci_init(PyObject *self, PyObject *args) {
  int first, second;
  if (!PyArg_ParseTuple(args, "ii", &first, &second)) {
    return NULL;
  } else {
    fibonacci_init(first, second);
  }

  return Py_None;
}

static PyObject *pyfibonacci_next(PyObject *self, PyObject *args) {
  bool b = fibonacci_next();
  return Py_None;
}

static PyObject *pyfibonacci_current(PyObject *self, PyObject *args) {
  int current = fibonacci_current();
  return PyLong_FromLong((long)current);
}

static PyMethodDef methods[] = {
    {"fibonacci_init", pyfibonacci_init, METH_VARARGS, "Runs fibonacci initializer"},
    {"fibonacci_next", pyfibonacci_next, METH_VARARGS, "Moves the fibonacci sequence ahead by one"},
    {"fibonacci_current", pyfibonacci_current, METH_VARARGS, "Returns current fibonacci number"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef definition = {
    PyModuleDef_HEAD_INIT,
    "example",
    "A Python module for a fibonacci library",
    -1,
    methods
};

// The name of the function here should PyInit_<x> where <x> is the module/submodule name in setup.py
PyMODINIT_FUNC PyInit_mycmodule(void) {
  Py_Initialize();
  PyObject *m = PyModule_Create(&definition);

  return m;
}