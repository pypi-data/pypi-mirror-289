import abc
import inspect

def interface(cls):
    cls.__metaclass__ = abc.ABCMeta 
    cls.__interface_methods__ = {
        name for name, value in cls.__dict__.items()
        if callable(value) and not name.startswith("__")
    }

    original_init_subclass = cls.__init_subclass__

    def new_init_subclass(subclass, **kwargs):
        super(cls, subclass).__init_subclass__(**kwargs)
        
        # Verifica se todos os métodos da interface foram implementados
        missing_methods = cls.__interface_methods__ - set(subclass.__dict__)
        if missing_methods:
            raise TypeError(
                f"Can't instantiate class {subclass.__name__} without implementing methods: {', '.join(missing_methods)}"
            )
    
    cls.__init_subclass__ = classmethod(new_init_subclass)
    return cls
