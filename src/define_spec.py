
import pluggy

hookspec1 = pluggy.HookspecMarker(project_name="datastore")

class MyClassSpec:
    """A hook specification namespace."""

    @hookspec1
    def myfunc(self, path:str, create_path:bool, delete_ifexists:bool):
        ...