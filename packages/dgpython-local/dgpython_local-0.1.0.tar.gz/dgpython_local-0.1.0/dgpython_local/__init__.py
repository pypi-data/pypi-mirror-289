class dgpl_NotImplementedError(NotImplementedError):
    requested_module_name = None
    module_description = None
    error_text = None

    def __init__(self, requested_module_name, module_description=None, error_text=None):
        self.requested_module_name = requested_module_name
        self.module_description = module_description
        self.error_text = error_text

        if module_description is None:
            msg = f"Requested Dataguzzler-Python local module \"{requested_module_name:s}\" is not available."
            pass
        else:
            msg = f"Requested Dataguzzler-Python local module \"{requested_module_name:s}\" for {self.module_description:s} is not available."
            pass
        if error_text is None:
            msg += f"\nYou probably need to customize your dgpython_local package and add a \"create_{requested_module_name:s}()\" function that instantiates and returns the module. Also don't forget to install your customized package."
            pass
        else:
            msg += "\n"+error_text
            pass
        super().__init__(self, msg)
        pass
            
    
