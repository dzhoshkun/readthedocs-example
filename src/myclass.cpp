#include "myclass.h"

namespace mc
{
    MyClass::MyClass(int value)
        : _value(value)
    {

    }

    MyClass::~MyClass()
    {

    }

    int MyClass::get_value()
    {
        return _value;
    }

    void MyClass::set_value(int value)
    {
        _value = value;
    }
}