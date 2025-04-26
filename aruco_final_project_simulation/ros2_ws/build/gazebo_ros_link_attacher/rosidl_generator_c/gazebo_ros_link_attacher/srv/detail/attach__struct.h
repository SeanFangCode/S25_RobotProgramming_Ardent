// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from gazebo_ros_link_attacher:srv/Attach.idl
// generated code does not contain a copyright notice

#ifndef GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__STRUCT_H_
#define GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'model_name_1'
// Member 'link_name_1'
// Member 'model_name_2'
// Member 'link_name_2'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Attach in the package gazebo_ros_link_attacher.
typedef struct gazebo_ros_link_attacher__srv__Attach_Request
{
  rosidl_runtime_c__String model_name_1;
  rosidl_runtime_c__String link_name_1;
  rosidl_runtime_c__String model_name_2;
  rosidl_runtime_c__String link_name_2;
} gazebo_ros_link_attacher__srv__Attach_Request;

// Struct for a sequence of gazebo_ros_link_attacher__srv__Attach_Request.
typedef struct gazebo_ros_link_attacher__srv__Attach_Request__Sequence
{
  gazebo_ros_link_attacher__srv__Attach_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} gazebo_ros_link_attacher__srv__Attach_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Attach in the package gazebo_ros_link_attacher.
typedef struct gazebo_ros_link_attacher__srv__Attach_Response
{
  bool ok;
} gazebo_ros_link_attacher__srv__Attach_Response;

// Struct for a sequence of gazebo_ros_link_attacher__srv__Attach_Response.
typedef struct gazebo_ros_link_attacher__srv__Attach_Response__Sequence
{
  gazebo_ros_link_attacher__srv__Attach_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} gazebo_ros_link_attacher__srv__Attach_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__STRUCT_H_
