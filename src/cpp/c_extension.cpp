#include <Python.h>

static PyObject *sq(PyObject *self, PyObject *args) {
  int input;
  if (!PyArg_ParseTuple(args, "i", &input)) {
    return NULL;
  }

  return PyLong_FromLong((long)input * (long)input);
}

static PyMethodDef example_methods[] = {
    {"square", sq, METH_VARARGS, "Returns a square of an integer."},
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