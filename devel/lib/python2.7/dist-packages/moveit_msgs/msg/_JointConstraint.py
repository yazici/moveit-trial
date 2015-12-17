# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from moveit_msgs/JointConstraint.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class JointConstraint(genpy.Message):
  _md5sum = "c02a15146bec0ce13564807805b008f0"
  _type = "moveit_msgs/JointConstraint"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Constrain the position of a joint to be within a certain bound
string joint_name

# the bound to be achieved is [position - tolerance_below, position + tolerance_above]
float64 position
float64 tolerance_above
float64 tolerance_below

# A weighting factor for this constraint (denotes relative importance to other constraints. Closer to zero means less important)
float64 weight
"""
  __slots__ = ['joint_name','position','tolerance_above','tolerance_below','weight']
  _slot_types = ['string','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       joint_name,position,tolerance_above,tolerance_below,weight

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(JointConstraint, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.joint_name is None:
        self.joint_name = ''
      if self.position is None:
        self.position = 0.
      if self.tolerance_above is None:
        self.tolerance_above = 0.
      if self.tolerance_below is None:
        self.tolerance_below = 0.
      if self.weight is None:
        self.weight = 0.
    else:
      self.joint_name = ''
      self.position = 0.
      self.tolerance_above = 0.
      self.tolerance_below = 0.
      self.weight = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.joint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4d.pack(_x.position, _x.tolerance_above, _x.tolerance_below, _x.weight))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_name = str[start:end].decode('utf-8')
      else:
        self.joint_name = str[start:end]
      _x = self
      start = end
      end += 32
      (_x.position, _x.tolerance_above, _x.tolerance_below, _x.weight,) = _struct_4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.joint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4d.pack(_x.position, _x.tolerance_above, _x.tolerance_below, _x.weight))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_name = str[start:end].decode('utf-8')
      else:
        self.joint_name = str[start:end]
      _x = self
      start = end
      end += 32
      (_x.position, _x.tolerance_above, _x.tolerance_below, _x.weight,) = _struct_4d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d = struct.Struct("<4d")