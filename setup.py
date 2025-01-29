from setuptools import find_packages,setup  
#this will automatically find out allthe packages that are available in the in the entire uh in the entire machine learning application in the directory


from typing import List 


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        print(requirements)
        print("testing the list in the requirements text document")
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


    return requirements


setup(

    name = 'mlproject',
    version = '0.0.1',
    author = 'ally',
    author_email ='allwynvincent11@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)




