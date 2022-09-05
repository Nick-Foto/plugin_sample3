from define_spec import MyClassSpec as hookspec
from define_class import MyClass as hookimpl
import pluggy


def get_plugin_manager():
    pm = pluggy.PluginManager(project_name="datastore")
    pm.add_hookspecs(hookspec)
    pm.register(hookimpl())
    pm.load_setuptools_entrypoints("datastore")
    return pm

pm = get_plugin_manager()

#supports only keyword arguments
pm.hook.myfunc(path="mypath",create_path=True,delete_ifexists=False)

