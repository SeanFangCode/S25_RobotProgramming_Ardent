# generated from rosidl_generator_py/resource/_idl.py.em
# with input from gazebo_ros_link_attacher:srv/Attach.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Attach_Request(type):
    """Metaclass of message 'Attach_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_ros_link_attacher')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_ros_link_attacher.srv.Attach_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__attach__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__attach__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__attach__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__attach__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__attach__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Attach_Request(metaclass=Metaclass_Attach_Request):
    """Message class 'Attach_Request'."""

    __slots__ = [
        '_model_name_1',
        '_link_name_1',
        '_model_name_2',
        '_link_name_2',
    ]

    _fields_and_field_types = {
        'model_name_1': 'string',
        'link_name_1': 'string',
        'model_name_2': 'string',
        'link_name_2': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.model_name_1 = kwargs.get('model_name_1', str())
        self.link_name_1 = kwargs.get('link_name_1', str())
        self.model_name_2 = kwargs.get('model_name_2', str())
        self.link_name_2 = kwargs.get('link_name_2', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.model_name_1 != other.model_name_1:
            return False
        if self.link_name_1 != other.link_name_1:
            return False
        if self.model_name_2 != other.model_name_2:
            return False
        if self.link_name_2 != other.link_name_2:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def model_name_1(self):
        """Message field 'model_name_1'."""
        return self._model_name_1

    @model_name_1.setter
    def model_name_1(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'model_name_1' field must be of type 'str'"
        self._model_name_1 = value

    @builtins.property
    def link_name_1(self):
        """Message field 'link_name_1'."""
        return self._link_name_1

    @link_name_1.setter
    def link_name_1(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'link_name_1' field must be of type 'str'"
        self._link_name_1 = value

    @builtins.property
    def model_name_2(self):
        """Message field 'model_name_2'."""
        return self._model_name_2

    @model_name_2.setter
    def model_name_2(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'model_name_2' field must be of type 'str'"
        self._model_name_2 = value

    @builtins.property
    def link_name_2(self):
        """Message field 'link_name_2'."""
        return self._link_name_2

    @link_name_2.setter
    def link_name_2(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'link_name_2' field must be of type 'str'"
        self._link_name_2 = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Attach_Response(type):
    """Metaclass of message 'Attach_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_ros_link_attacher')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_ros_link_attacher.srv.Attach_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__attach__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__attach__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__attach__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__attach__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__attach__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Attach_Response(metaclass=Metaclass_Attach_Response):
    """Message class 'Attach_Response'."""

    __slots__ = [
        '_ok',
    ]

    _fields_and_field_types = {
        'ok': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.ok = kwargs.get('ok', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.ok != other.ok:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def ok(self):
        """Message field 'ok'."""
        return self._ok

    @ok.setter
    def ok(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'ok' field must be of type 'bool'"
        self._ok = value


class Metaclass_Attach(type):
    """Metaclass of service 'Attach'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('gazebo_ros_link_attacher')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'gazebo_ros_link_attacher.srv.Attach')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__attach

            from gazebo_ros_link_attacher.srv import _attach
            if _attach.Metaclass_Attach_Request._TYPE_SUPPORT is None:
                _attach.Metaclass_Attach_Request.__import_type_support__()
            if _attach.Metaclass_Attach_Response._TYPE_SUPPORT is None:
                _attach.Metaclass_Attach_Response.__import_type_support__()


class Attach(metaclass=Metaclass_Attach):
    from gazebo_ros_link_attacher.srv._attach import Attach_Request as Request
    from gazebo_ros_link_attacher.srv._attach import Attach_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
