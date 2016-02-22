from setuptools import setup


setup(
    name='girder-geospatial',
    version='0.1.0',
    description='Enables the storage and querying of GeoJSON formatted geospatial data',
    author='Kitware, Inc.',
    packages=['geospatial'],
    install_requires=[
        'girder',
        'geojson'
    ],
    entry_points={
        'girder.plugin': 'geospatial2 = geospatial:load'
    },
)
