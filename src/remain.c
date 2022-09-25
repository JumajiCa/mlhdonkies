
#include <Python.h>
#include <stdio.h>

double add(int x, int y) {
	return x + y;
}

static PyObject* Pyadd(PyObject* self, PyObject* args) {
	int x, y, sts;

	if (!PyArg_ParseTuple(args, "ii", &x, &y))
		return NULL;
	sts = add(x, y);
	return PyLong_FromLong(sts);
}

static PyObject* version(PyObject* self) {
	return Py_BuildValue("s", "Version 0.01");
}

static PyMethodDef remains = {
	{"Pyadd", Pyadd, METH_VARARGS, "Compute the sum of two numbers."},
	{"version", (PyCFunction)version, METH_NOARGS, "Return method of mudle."},
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef remain = {
        PyModuleDef_HEAD_INIT,
        "remain",
        "remain Module",
        -1,
        &remains
};


PyMODINIT_FUNC PyInit_remain(void) {
	return PyModule_Create(&remain);
}
