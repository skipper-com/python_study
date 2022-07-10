def info_kwargs(**kwargs):
    for k in sorted(kwargs.keys()):
      print(f'{k}: {kwargs[k]}')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 