import typing as t

def get_all_paths(json:t.Dict[str,any])->t.Iterable:
    if isinstance(json, dict):
        for key, value in json.items():
            yield f'.{key}'
            yield from (f'.{key}{p}' for p in get_all_paths(json=value))
        
    elif isinstance(json, list):
        for i, value in enumerate(json):
            yield f'[{i}]'
            yield from (f'[{i}]{p}' for p in get_all_paths(json=value))