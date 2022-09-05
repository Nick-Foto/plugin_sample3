import pluggy

hookimpl = pluggy.HookimplMarker(project_name="datastore")


class MyClass:
    def __init__(self):
        pass

    @hookimpl
    def myfunc(self, path:str, create_path:bool, delete_ifexists:bool):
        print(f"This is inside myfunc, path={path}, create_pat={create_path}, delete_ifexists={delete_ifexists}")



