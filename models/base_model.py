#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel():

    # tODO ''' __iNiT__ method '''
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # storage
        from models import storage
        #!"""!!!!! passing the self it great aidea !!!!!"""
        storage.new(self)

        """Check if kwargs is not empty
           0. Go through each dict
           1. if Skip if the key is '__class__'
           3. elif the key is 'created_at' or 'updated_at', format it to '%Y-%m-%dT%H:%M:%S.%f'
           4. else For other keys, assign the value directly
        """
        if kwargs:  # ? is not impty >>
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value

    # tODO ''' SAVE method '''

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    # tODO '''TO_DICT method'''

    def to_dict(self):
        my_dict_z = {}
        x = self.updated_at.isoformat()
        y = self.created_at.isoformat()

        lk = self.__dict__

        for k, v in lk.items():
            if k == "updated_at":
                my_dict_z["__class__"] = self.__class__.__name__
                my_dict_z[k] = x
                continue
            elif k == "created_at":
                my_dict_z[k] = y
            else:
                my_dict_z[k] = v

        return my_dict_z

    # tODO ''' __STR__ method return string when print the object '''

    def __str__(self):

        clase_name = self.__class__.__name__
        id_us = self.id
        dictn = str(self.__dict__)

        rus_z = "[{:s}] ({:s}) {:s}".format(clase_name, id_us, dictn)

        return rus_z

    #! xxxxxxxxxxxxxxxxxxxx


# self *z
