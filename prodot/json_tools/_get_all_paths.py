import typing as t

def get_all_paths(json:t.Dict[str,any])->t.Iterable:
    '''
    return an iterable that
    runs across the entire main_object, returning
    all possible json_paths of the object
    '''
    def _get_all_paths(json:t.Dict[str,any])->t.Iterable:
        if isinstance(json, dict):
            for key, value in json.items():
                yield f'."{key}"'
                yield from (f'."{key}"{p}' for p in _get_all_paths(json=value))
            
        elif isinstance(json, list):
            for i, value in enumerate(json):
                yield f'[{i}]'
                yield from (f'[{i}]{p}' for p in _get_all_paths(json=value))
                
    # add the json path root character at the beginning of the path
    for i in _get_all_paths(json):
        yield '$'+i
