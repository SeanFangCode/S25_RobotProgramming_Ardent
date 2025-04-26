// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from gazebo_ros_link_attacher:srv/Attach.idl
// generated code does not contain a copyright notice
#include "gazebo_ros_link_attacher/srv/detail/attach__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "gazebo_ros_link_attacher/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "gazebo_ros_link_attacher/srv/detail/attach__struct.h"
#include "gazebo_ros_link_attacher/srv/detail/attach__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // link_name_1, link_name_2, model_name_1, model_name_2
#include "rosidl_runtime_c/string_functions.h"  // link_name_1, link_name_2, model_name_1, model_name_2

// forward declare type support functions


using _Attach_Request__ros_msg_type = gazebo_ros_link_attacher__srv__Attach_Request;

static bool _Attach_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Attach_Request__ros_msg_type * ros_message = static_cast<const _Attach_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: model_name_1
  {
    const rosidl_runtime_c__String * str = &ros_message->model_name_1;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: link_name_1
  {
    const rosidl_runtime_c__String * str = &ros_message->link_name_1;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: model_name_2
  {
    const rosidl_runtime_c__String * str = &ros_message->model_name_2;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: link_name_2
  {
    const rosidl_runtime_c__String * str = &ros_message->link_name_2;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _Attach_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Attach_Request__ros_msg_type * ros_message = static_cast<_Attach_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: model_name_1
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->model_name_1.data) {
      rosidl_runtime_c__String__init(&ros_message->model_name_1);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->model_name_1,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'model_name_1'\n");
      return false;
    }
  }

  // Field name: link_name_1
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->link_name_1.data) {
      rosidl_runtime_c__String__init(&ros_message->link_name_1);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->link_name_1,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'link_name_1'\n");
      return false;
    }
  }

  // Field name: model_name_2
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->model_name_2.data) {
      rosidl_runtime_c__String__init(&ros_message->model_name_2);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->model_name_2,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'model_name_2'\n");
      return false;
    }
  }

  // Field name: link_name_2
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->link_name_2.data) {
      rosidl_runtime_c__String__init(&ros_message->link_name_2);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->link_name_2,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'link_name_2'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_gazebo_ros_link_attacher
size_t get_serialized_size_gazebo_ros_link_attacher__srv__Attach_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Attach_Request__ros_msg_type * ros_message = static_cast<const _Attach_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name model_name_1
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->model_name_1.size + 1);
  // field.name link_name_1
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->link_name_1.size + 1);
  // field.name model_name_2
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->model_name_2.size + 1);
  // field.name link_name_2
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->link_name_2.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _Attach_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_gazebo_ros_link_attacher__srv__Attach_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_gazebo_ros_link_attacher
size_t max_serialized_size_gazebo_ros_link_attacher__srv__Attach_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: model_name_1
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: link_name_1
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: model_name_2
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: link_name_2
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = gazebo_ros_link_attacher__srv__Attach_Request;
    is_plain =
      (
      offsetof(DataType, link_name_2) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _Attach_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_gazebo_ros_link_attacher__srv__Attach_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Attach_Request = {
  "gazebo_ros_link_attacher::srv",
  "Attach_Request",
  _Attach_Request__cdr_serialize,
  _Attach_Request__cdr_deserialize,
  _Attach_Request__get_serialized_size,
  _Attach_Request__max_serialized_size
};

static rosidl_message_type_support_t _Attach_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Attach_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gazebo_ros_link_attacher, srv, Attach_Request)() {
  return &_Attach_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "gazebo_ros_link_attacher/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "gazebo_ros_link_attacher/srv/detail/attach__struct.h"
// already included above
// #include "gazebo_ros_link_attacher/srv/detail/attach__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _Attach_Response__ros_msg_type = gazebo_ros_link_attacher__srv__Attach_Response;

static bool _Attach_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Attach_Response__ros_msg_type * ros_message = static_cast<const _Attach_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: ok
  {
    cdr << (ros_message->ok ? true : false);
  }

  return true;
}

static bool _Attach_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Attach_Response__ros_msg_type * ros_message = static_cast<_Attach_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: ok
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->ok = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_gazebo_ros_link_attacher
size_t get_serialized_size_gazebo_ros_link_attacher__srv__Attach_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Attach_Response__ros_msg_type * ros_message = static_cast<const _Attach_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name ok
  {
    size_t item_size = sizeof(ros_message->ok);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Attach_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_gazebo_ros_link_attacher__srv__Attach_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_gazebo_ros_link_attacher
size_t max_serialized_size_gazebo_ros_link_attacher__srv__Attach_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: ok
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = gazebo_ros_link_attacher__srv__Attach_Response;
    is_plain =
      (
      offsetof(DataType, ok) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _Attach_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_gazebo_ros_link_attacher__srv__Attach_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Attach_Response = {
  "gazebo_ros_link_attacher::srv",
  "Attach_Response",
  _Attach_Response__cdr_serialize,
  _Attach_Response__cdr_deserialize,
  _Attach_Response__get_serialized_size,
  _Attach_Response__max_serialized_size
};

static rosidl_message_type_support_t _Attach_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Attach_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gazebo_ros_link_attacher, srv, Attach_Response)() {
  return &_Attach_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "gazebo_ros_link_attacher/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "gazebo_ros_link_attacher/srv/attach.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t Attach__callbacks = {
  "gazebo_ros_link_attacher::srv",
  "Attach",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gazebo_ros_link_attacher, srv, Attach_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gazebo_ros_link_attacher, srv, Attach_Response)(),
};

static rosidl_service_type_support_t Attach__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &Attach__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, gazebo_ros_link_attacher, srv, Attach)() {
  return &Attach__handle;
}

#if defined(__cplusplus)
}
#endif
