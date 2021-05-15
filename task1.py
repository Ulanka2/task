def func(name, **kvargs):
    print(f'{name}')
    for item in kvargs:
        print(f'{item} - {kvargs[item]}')

func(name='USA', population='330 million', is_democratic=True)
func(name='Kyrgyzstan', area='200 km2', 
	have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])