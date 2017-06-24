def clip(text:str, max_len:'int>0'=80) -> str:
    ''' Return text clipped at the last space before or after max_len '''
    end = len(text)
    if end > max_len:
        space_before = text.rfind(' ', max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    return text[:end].rstrip()


print(clip.__annotations__)

from inspect import signature

sig = signature(clip)
print(sig.return_annotation)
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)