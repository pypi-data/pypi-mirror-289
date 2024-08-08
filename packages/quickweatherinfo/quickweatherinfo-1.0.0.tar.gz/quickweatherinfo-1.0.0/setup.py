from setuptools import setup 

setup( 
	name='quickweatherinfo', 
	version='1.0.0', 
    license='MIT',
	description='Weather Forecast Data', 
	author='Neha Tiwari', 
	author_email='neha28494@gmail.com', 
    url='https://example.com',
    keywords=['weather', 'forecast', 'openweather'],
	packages=['quickweatherinfo'], 
	install_requires=[ 
		'requests'
	], 
    classifiers=[
        'Development Status :: 3 - Alpha',  # Choose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Who is the audience for your library?
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Type a license again
        'Programming Language :: Python :: 3.5',  # Python versions that your library supports
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
) 
