from setuptools import find_packages, setup

package_name = 'my_array_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='satyam-mohanty',
    maintainer_email='satyam-mohanty@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'command_publisher = command_comm.command_publisher:main',
        'command_subscriber = command_comm.command_subscriber:main',
    ],
},
)