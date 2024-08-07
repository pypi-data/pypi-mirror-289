/*
 *  ----------------------------------
 * |         libmem - by rdbo         |
 * |      Memory Hacking Library      |
 *  ----------------------------------
 */

/*
 * Copyright (C) 2023    Rdbo
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License version 3
 * as published by the Free Software Foundation.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 * 
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#ifndef LIBMEM_TYPES_H
#define LIBMEM_TYPES_H

#include <libmem/libmem.h>
#include <Python.h>
#include <structmember.h>
#include <stddef.h>

#define T_SIZE T_PYSSIZET

/****************************************/

/* lm_arch_t */
typedef struct {
	PyObject_HEAD
	lm_arch_t arch;
} py_lm_arch_obj;

int
py_lm_arch_init(PyObject *self,
		PyObject *args,
		PyObject *kwds)
{
	lm_arch_t arch;
	py_lm_arch_obj *pyarch = (py_lm_arch_obj *)self;

	if (!PyArg_ParseTuple(args, "i", &arch))
		return -1;

	pyarch->arch = arch;

	return 0;
}

PyObject *
py_lm_arch_str(PyObject *self)
{
	py_lm_arch_obj *pyarch = (py_lm_arch_obj *)self;
	const char *archstr;

	switch (pyarch->arch) {
	case LM_ARCH_ARMV7: archstr = "LM_ARCH_ARMV7"; break;
	case LM_ARCH_ARMV8: archstr = "LM_ARCH_ARMV8"; break;
	case LM_ARCH_THUMBV7: archstr = "LM_ARCH_THUMBV7"; break;
	case LM_ARCH_THUMBV8: archstr = "LM_ARCH_THUMBV8"; break;

	case LM_ARCH_ARMV7EB: archstr = "LM_ARCH_ARMV7EB"; break;
	case LM_ARCH_THUMBV7EB: archstr = "LM_ARCH_THUMBV7EB"; break;
	case LM_ARCH_ARMV8EB: archstr = "LM_ARCH_ARMV8EB"; break;
	case LM_ARCH_THUMBV8EB: archstr = "LM_ARCH_THUMBV8EB"; break;

	case LM_ARCH_AARCH64: archstr = "LM_ARCH_AARCH64"; break;

	case LM_ARCH_MIPS: archstr = "LM_ARCH_MIPS"; break;
	case LM_ARCH_MIPS64: archstr = "LM_ARCH_MIPS64"; break;
	case LM_ARCH_MIPSEL: archstr = "LM_ARCH_MIPSEL"; break;
	case LM_ARCH_MIPSEL64: archstr = "LM_ARCH_MIPSEL64"; break;

	case LM_ARCH_X86_16: archstr = "LM_ARCH_X86_16"; break;
	case LM_ARCH_X86: archstr = "LM_ARCH_X86"; break;
	case LM_ARCH_X64: archstr = "LM_ARCH_X64"; break;

	case LM_ARCH_PPC32: archstr = "LM_ARCH_PPC32"; break;
	case LM_ARCH_PPC64: archstr = "LM_ARCH_PPC64"; break;
	case LM_ARCH_PPC64LE: archstr = "LM_ARCH_PPC64LE"; break;

	case LM_ARCH_SPARC: archstr = "LM_ARCH_SPARC"; break;
	case LM_ARCH_SPARC64: archstr = "LM_ARCH_SPARC64"; break;
	case LM_ARCH_SPARCEL: archstr = "LM_ARCH_SPARCEL"; break;

	case LM_ARCH_SYSZ: archstr = "LM_ARCH_SYSZ"; break;

	case LM_ARCH_MAX: archstr = "LM_ARCH_MAX"; break;

	default: archstr = "LM_ARCH_NONE"; break;
	}

	return PyUnicode_FromFormat("%s", archstr);
}

static PyTypeObject py_lm_arch_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_arch_t",
	.tp_doc = "Stores a processor architecture",
	.tp_basicsize = sizeof(py_lm_arch_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_str = py_lm_arch_str,
	.tp_repr = py_lm_arch_str,
	.tp_init = py_lm_arch_init
};

/****************************************/

/* lm_process_t */
typedef struct {
	PyObject_HEAD
	lm_process_t proc;
	py_lm_arch_obj *arch;
} py_lm_process_obj;

static PyMemberDef py_lm_process_members[] = {
	{ "pid", T_INT, offsetof(py_lm_process_obj, proc.pid), READONLY, "Process ID" },
	{ "ppid", T_INT, offsetof(py_lm_process_obj, proc.ppid), READONLY, "Parent Process ID" },
	{ "arch", T_OBJECT, offsetof(py_lm_process_obj, arch), READONLY, "Process Architecture" },
	{ "bits", T_SIZE, offsetof(py_lm_process_obj, proc.bits), READONLY, "Process Bits" },
        { "start_time", T_ULONGLONG, offsetof(py_lm_process_obj, proc.start_time), READONLY, "Process Start Time" },
	{ NULL }
};

PyObject *
py_lm_process_get_path(PyObject *self, void *closure)
{
	return PyUnicode_FromString(((py_lm_process_obj *)self)->proc.path);
}

PyObject *
py_lm_process_get_name(PyObject *self, void *closure)
{
	return PyUnicode_FromString(((py_lm_process_obj *)self)->proc.name);
}

PyObject *
py_lm_process_str(PyObject *self)
{
	py_lm_process_obj *pyproc = (py_lm_process_obj *)self;
	PyObject *pyarchstr;
	PyObject *pyfmtstr;

	pyarchstr = PyObject_Str((PyObject *)pyproc->arch);

	pyfmtstr = PyUnicode_FromFormat("lm_process_t(pid = %d, ppid = %d, arch = %s, bits = %zu, start_time = %llu, path = \"%s\", name = \"%s\")", pyproc->proc.pid, pyproc->proc.ppid, PyUnicode_AsUTF8(pyarchstr), pyproc->proc.bits, pyproc->proc.start_time, pyproc->proc.path, pyproc->proc.name);

	Py_DECREF(pyarchstr);

	return pyfmtstr;
}

static PyGetSetDef py_lm_process_accessors[] = {
	{ "path", py_lm_process_get_path, NULL, NULL, NULL },
	{ "name", py_lm_process_get_name, NULL, NULL, NULL },
	{ NULL, NULL, NULL, NULL, NULL }
};

static PyTypeObject py_lm_process_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_process_t",
	.tp_doc = "Stores information about a process",
	.tp_basicsize = sizeof(py_lm_process_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_members = py_lm_process_members,
	.tp_getset = py_lm_process_accessors,
	.tp_str = py_lm_process_str,
	.tp_repr = py_lm_process_str
};

/****************************************/

/* lm_thread_t */
typedef struct {
	PyObject_HEAD
	lm_thread_t thread;
} py_lm_thread_obj;

static PyMemberDef py_lm_thread_members[] = {
	{ "tid", T_INT, offsetof(py_lm_thread_obj, thread.tid), READONLY, "Thread ID" },
	{ "owner_pid", T_INT, offsetof(py_lm_thread_obj, thread.owner_pid), READONLY, "Thread Owner PID" },
	{ NULL }
};

PyObject *
py_lm_thread_str(PyObject *self)
{
	py_lm_thread_obj *pythread = (py_lm_thread_obj *)self;
	return PyUnicode_FromFormat("lm_thread_t(tid = %d)", pythread->thread.tid);
}

static PyTypeObject py_lm_thread_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_thread_t",
	.tp_doc = "Stores information about a thread",
	.tp_basicsize = sizeof(py_lm_thread_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_members = py_lm_thread_members,
	.tp_str = py_lm_thread_str,
	.tp_repr = py_lm_thread_str
};

/****************************************/

/* lm_module_t */
typedef struct {
	PyObject_HEAD
	lm_module_t mod;
} py_lm_module_obj;

static PyMemberDef py_lm_module_members[] = {
	{ "base", T_SIZE, offsetof(py_lm_module_obj, mod.base), READONLY, "Module Base Address" },
	{ "end", T_SIZE, offsetof(py_lm_module_obj, mod.end), READONLY, "Module End Address" },
	{ "size", T_SIZE, offsetof(py_lm_module_obj, mod.size), READONLY, "Module Size" },
	{ NULL }
};

PyObject *
py_lm_module_get_path(PyObject *self, void *closure)
{
	return PyUnicode_FromString(((py_lm_module_obj *)self)->mod.path);
}

PyObject *
py_lm_module_get_name(PyObject *self, void *closure)
{
	return PyUnicode_FromString(((py_lm_module_obj *)self)->mod.name);
}

PyObject *
py_lm_module_str(PyObject *self)
{
	py_lm_module_obj *pymodule = (py_lm_module_obj *)self;
	return PyUnicode_FromFormat("lm_module_t(base = %p, end = %p, size = %p, path = \"%s\", name = \"%s\")", (void *)pymodule->mod.base, (void *)pymodule->mod.end, (void *)pymodule->mod.size, pymodule->mod.path, pymodule->mod.name);
}

static PyGetSetDef py_lm_module_accessors[] = {
	{ "path", py_lm_module_get_path, NULL, NULL, NULL },
	{ "name", py_lm_module_get_name, NULL, NULL, NULL },
	{ NULL, NULL, NULL, NULL, NULL }
};

static PyTypeObject py_lm_module_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_module_t",
	.tp_doc = "Stores information about a module",
	.tp_basicsize = sizeof(py_lm_module_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_members = py_lm_module_members,
	.tp_getset = py_lm_module_accessors,
	.tp_str = py_lm_module_str,
	.tp_repr = py_lm_module_str
};

#endif

/****************************************/

/* lm_symbol_t */
typedef struct {
	PyObject_HEAD
	lm_symbol_t symbol;
	PyObject *name;
} py_lm_symbol_obj;

static PyMemberDef py_lm_symbol_members[] = {
	{ "name", T_OBJECT, offsetof(py_lm_symbol_obj, name), READONLY, "Symbol Name" },
	{ "address", T_SIZE, offsetof(py_lm_symbol_obj, symbol.address), READONLY, "Symbol Address" },
	{ NULL }
};

PyObject *
py_lm_symbol_str(PyObject *self)
{
	py_lm_symbol_obj *pysym = (py_lm_symbol_obj *)self;
	return PyUnicode_FromFormat("lm_symbol_t(name = \"%s\", address = %p)>", PyUnicode_AsUTF8(pysym->name), (void *)pysym->symbol.address);
}

static PyTypeObject py_lm_symbol_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_symbol_t",
	.tp_doc = "Stores information about a symbol",
	.tp_basicsize = sizeof(py_lm_symbol_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_members = py_lm_symbol_members,
	.tp_str = py_lm_symbol_str,
	.tp_repr = py_lm_symbol_str
};

/****************************************/

/* lm_prot_t */
typedef struct {
	PyObject_HEAD
	lm_prot_t prot;
} py_lm_prot_obj;

int
py_lm_prot_init(PyObject *self,
		PyObject *args,
		PyObject *kwds)
{
	lm_prot_t prot;
	py_lm_prot_obj *pyprot = (py_lm_prot_obj *)self;

	if (!PyArg_ParseTuple(args, "i", &prot))
		return -1;

	pyprot->prot = prot;

	return 0;
}

PyObject *
py_lm_prot_str(PyObject *self)
{
	py_lm_prot_obj *pyprot = (py_lm_prot_obj *)self;
	const char *protstr;

	switch (pyprot->prot) {
	case LM_PROT_X: protstr = "LM_PROT_X"; break;
	case LM_PROT_R: protstr = "LM_PROT_R"; break;
	case LM_PROT_W: protstr = "LM_PROT_W"; break;
	case LM_PROT_XR: protstr = "LM_PROT_XR"; break;
	case LM_PROT_XW: protstr = "LM_PROT_XW"; break;
	case LM_PROT_RW: protstr = "LM_PROT_RW"; break;
	case LM_PROT_XRW: protstr = "LM_PROT_XRW"; break;
	default: protstr = "LM_PROT_NONE"; break;
	}

	return PyUnicode_FromFormat("%s", protstr);
}

static PyTypeObject py_lm_prot_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_prot_t",
	.tp_doc = "Stores memory protection flags",
	.tp_basicsize = sizeof(py_lm_prot_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_str = py_lm_prot_str,
	.tp_repr = py_lm_prot_str,
	.tp_init = py_lm_prot_init
};

/****************************************/

/* lm_page_t */
typedef struct {
	PyObject_HEAD
	lm_segment_t segment;
	py_lm_prot_obj *prot;
} py_lm_segment_obj;

static PyMemberDef py_lm_segment_members[] = {
	{ "base", T_SIZE, offsetof(py_lm_segment_obj, segment.base), READONLY, "Segment Base Address" },
	{ "end", T_SIZE, offsetof(py_lm_segment_obj, segment.end), READONLY, "Segment End Address" },
	{ "size", T_SIZE, offsetof(py_lm_segment_obj, segment.size), READONLY, "Segment Size" },
	{ "prot", T_OBJECT, offsetof(py_lm_segment_obj, prot), READONLY, "Segment Protection Flags" },
	{ NULL }
};

PyObject *
py_lm_segment_str(PyObject *self)
{
	py_lm_segment_obj *pysegment = (py_lm_segment_obj *)self;
	PyObject *pyprotstr;
	const char *protstr;
	PyObject *fmtstr;

	pyprotstr = PyObject_Str((PyObject *)pysegment->prot);
	protstr = PyUnicode_AsUTF8(pyprotstr);
	fmtstr = PyUnicode_FromFormat("lm_segment_t(base = %p, end = %p, size = %p, prot = %s)", (void *)pysegment->segment.base, (void *)pysegment->segment.end, (void *)pysegment->segment.size, protstr);

	Py_DECREF(pyprotstr); /* delete protection string object */

	return fmtstr;
}

static PyTypeObject py_lm_segment_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_segment_t",
	.tp_doc = "Stores information about a segment",
	.tp_basicsize = sizeof(py_lm_segment_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_members = py_lm_segment_members,
	.tp_str = py_lm_segment_str,
	.tp_repr = py_lm_segment_str
};

/****************************************/

/* lm_inst_t */
typedef struct {
	PyObject_HEAD
	lm_inst_t inst;
} py_lm_inst_obj;

static PyMemberDef py_lm_inst_members[] = {
	{ "address", T_SIZE, offsetof(py_lm_inst_obj, inst.address), READONLY, "Instruction Address" },
	{ "size", T_SIZE, offsetof(py_lm_inst_obj, inst.size), READONLY, "Instruction Size" },
	{ NULL }
};

PyObject *
py_lm_inst_get_mnemonic(PyObject *self, void *closure)
{
	return (PyObject *)PyUnicode_FromString(((py_lm_inst_obj *)self)->inst.mnemonic);
}

PyObject *
py_lm_inst_get_op_str(PyObject *self, void *closure)
{
	return (PyObject *)PyUnicode_FromString(((py_lm_inst_obj *)self)->inst.op_str);
}

PyObject *
py_lm_inst_get_bytes(PyObject *self, void *closure)
{
	py_lm_inst_obj *inst = (py_lm_inst_obj *)self;
	return (PyObject *)PyByteArray_FromStringAndSize((const char *)inst->inst.bytes, inst->inst.size);
}

PyObject *
py_lm_inst_str(PyObject *self)
{
	char bytes_str[255] = { 0 };
	char *tmp = bytes_str;
	int offset = 0;
	py_lm_inst_obj *pyinst = (py_lm_inst_obj *)self;
	size_t i;

	for (i = 0; i < pyinst->inst.size; ++i) {
		/* OBS: 'bytes_str' MUST BE large enough */
		offset = sprintf(tmp, "%hhx ", pyinst->inst.bytes[i]);
		tmp = &bytes_str[offset];
	}

	if (offset > 0)
		tmp[offset - 1] = '\x00'; /* remove last space */

	return (PyObject *)PyUnicode_FromFormat("<%s %s : %s>", pyinst->inst.mnemonic, pyinst->inst.op_str, bytes_str);
}

static PyGetSetDef py_lm_inst_accessors[] = {
	{ "mnemonic", py_lm_inst_get_mnemonic, NULL, NULL, NULL },
	{ "op_str", py_lm_inst_get_op_str, NULL, NULL, NULL },
	{ "bytes", py_lm_inst_get_bytes, NULL, NULL, NULL },
	{ NULL, NULL, NULL, NULL, NULL }
};

static PyTypeObject py_lm_inst_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_inst_t",
	.tp_doc = "Stores information about an instruction",
	.tp_basicsize = sizeof(py_lm_inst_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_members = py_lm_inst_members,
	.tp_getset = py_lm_inst_accessors,
	.tp_str = py_lm_inst_str,
	.tp_repr = py_lm_inst_str
};

/****************************************/

/* lm_vmt_t */
typedef struct {
	PyObject_HEAD
	lm_vmt_t vmt;
} py_lm_vmt_obj;

PyObject *
py_lm_vmt_str(PyObject *self)
{
	py_lm_vmt_obj *pyvmt = (py_lm_vmt_obj *)self;
	return PyUnicode_FromFormat("<lm_vmt_t(vtable = 0x%zx)>", pyvmt->vmt.vtable);
}

int
py_lm_vmt_init(PyObject *self,
	       PyObject *args,
	       PyObject *kwds)
{
	lm_address_t *vtable;
	py_lm_vmt_obj *pyvmt = (py_lm_vmt_obj *)self;

	if (!PyArg_ParseTuple(args, "k", &vtable))
		return -1;

	LM_VmtNew(vtable, &pyvmt->vmt);

	return 0;
}

void
py_lm_vmt_del(PyObject *self)
{
	py_lm_vmt_obj *pyvmt = (py_lm_vmt_obj *)self;
	
	LM_VmtFree(&pyvmt->vmt);
}

PyObject *
py_lm_vmt_hook(PyObject *self,
	       PyObject *args)
{
	py_lm_vmt_obj *pyvmt = (py_lm_vmt_obj *)self;
	lm_size_t index;
	lm_address_t dst;

	if (!PyArg_ParseTuple(args, "kk", &index, &dst))
		return NULL;

	LM_VmtHook(&pyvmt->vmt, index, dst);

	return Py_BuildValue("");
}

PyObject *
py_lm_vmt_unhook(PyObject *self,
		 PyObject *args)
{
	py_lm_vmt_obj *pyvmt = (py_lm_vmt_obj *)self;
	lm_size_t index;

	if (!PyArg_ParseTuple(args, "k", &index))
		return NULL;

	LM_VmtUnhook(&pyvmt->vmt, index);

	return Py_BuildValue("");
}

PyObject *
py_lm_vmt_get_original(PyObject *self,
		       PyObject *args)
{
	py_lm_vmt_obj *pyvmt = (py_lm_vmt_obj *)self;
	lm_size_t index;
	lm_address_t orig_func;

	if (!PyArg_ParseTuple(args, "k", &index))
		return NULL;

	orig_func = LM_VmtGetOriginal(&pyvmt->vmt, index);

	return PyLong_FromSize_t(orig_func);
}

PyObject *
py_lm_vmt_reset(PyObject *self,
		PyObject *args)
{
	py_lm_vmt_obj *pyvmt = (py_lm_vmt_obj *)self;

	LM_VmtReset(&pyvmt->vmt);

	return Py_BuildValue("");
}

static PyMethodDef py_lm_vmt_methods[] = {
	{ "hook", py_lm_vmt_hook, METH_VARARGS, "Hooks a VMT function at an index" },
	{ "unhook", py_lm_vmt_unhook, METH_VARARGS, "Unhooks a VMT function at an index" },
	{ "get_original", py_lm_vmt_get_original, METH_VARARGS, "Gets the original VMT function at an index" },
	{ "reset", py_lm_vmt_reset, METH_VARARGS, "Resets the original VMT" },
	{ NULL }
};

static PyTypeObject py_lm_vmt_t = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "libmem.lm_vmt_t",
	.tp_doc = "Manages a Virtual Method Table",
	.tp_basicsize = sizeof(py_lm_vmt_obj),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_init = py_lm_vmt_init,
	.tp_finalize = py_lm_vmt_del,
	.tp_methods = py_lm_vmt_methods,
	.tp_str = py_lm_vmt_str,
	.tp_repr = py_lm_vmt_str
};

/****************************************/

