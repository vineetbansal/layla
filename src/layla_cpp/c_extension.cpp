#include <Python.h>
#include "example_dll.h"

static PyObject *pyhello(PyObject *self, PyObject *args) {
  char *who;
  if (!PyArg_ParseTuple(args, "s", &who)) {
    return NULL;
  } else {
    hello(who);
    return Py_None;
  }
}

static PyObject *pyDouble(PyObject *self, PyObject *args) {
  int x;
  if (!PyArg_ParseTuple(args, "i", &x)) {
    return NULL;
  } else {
    return Py_BuildValue("i", Double(x));
  }
}

static PyMethodDef methods[] = {
    {"hello", pyhello, METH_VARARGS, "Say hello"},
    {"Double", pyDouble, METH_VARARGS, "Double a number"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef definition = {
    PyModuleDef_HEAD_INIT,
    "example",
    "A Python module for a mingw dll",
    -1,
    methods
};

// The name of the function here should PyInit_<x> where <x> is the module/submodule name in setup.py
PyMODINIT_FUNC PyInit_mycmodule(void) {
  Py_Initialize();
  PyObject *m = PyModule_Create(&definition);

  return m;
}