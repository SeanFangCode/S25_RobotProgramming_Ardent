// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from gazebo_ros_link_attacher:srv/Attach.idl
// generated code does not contain a copyright notice

#ifndef GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__TRAITS_HPP_
#define GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "gazebo_ros_link_attacher/srv/detail/attach__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace gazebo_ros_link_attacher
{

namespace srv
{

inline void to_flow_style_yaml(
  const Attach_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: model_name_1
  {
    out << "model_name_1: ";
    rosidl_generator_traits::value_to_yaml(msg.model_name_1, out);
    out << ", ";
  }

  // member: link_name_1
  {
    out << "link_name_1: ";
    rosidl_generator_traits::value_to_yaml(msg.link_name_1, out);
    out << ", ";
  }

  // member: model_name_2
  {
    out << "model_name_2: ";
    rosidl_generator_traits::value_to_yaml(msg.model_name_2, out);
    out << ", ";
  }

  // member: link_name_2
  {
    out << "link_name_2: ";
    rosidl_generator_traits::value_to_yaml(msg.link_name_2, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Attach_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: model_name_1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "model_name_1: ";
    rosidl_generator_traits::value_to_yaml(msg.model_name_1, out);
    out << "\n";
  }

  // member: link_name_1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "link_name_1: ";
    rosidl_generator_traits::value_to_yaml(msg.link_name_1, out);
    out << "\n";
  }

  // member: model_name_2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "model_name_2: ";
    rosidl_generator_traits::value_to_yaml(msg.model_name_2, out);
    out << "\n";
  }

  // member: link_name_2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "link_name_2: ";
    rosidl_generator_traits::value_to_yaml(msg.link_name_2, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Attach_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace gazebo_ros_link_attacher

namespace rosidl_generator_traits
{

[[deprecated("use gazebo_ros_link_attacher::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const gazebo_ros_link_attacher::srv::Attach_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  gazebo_ros_link_attacher::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use gazebo_ros_link_attacher::srv::to_yaml() instead")]]
inline std::string to_yaml(const gazebo_ros_link_attacher::srv::Attach_Request & msg)
{
  return gazebo_ros_link_attacher::srv::to_yaml(msg);
}

template<>
inline const char * data_type<gazebo_ros_link_attacher::srv::Attach_Request>()
{
  return "gazebo_ros_link_attacher::srv::Attach_Request";
}

template<>
inline const char * name<gazebo_ros_link_attacher::srv::Attach_Request>()
{
  return "gazebo_ros_link_attacher/srv/Attach_Request";
}

template<>
struct has_fixed_size<gazebo_ros_link_attacher::srv::Attach_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<gazebo_ros_link_attacher::srv::Attach_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<gazebo_ros_link_attacher::srv::Attach_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace gazebo_ros_link_attacher
{

namespace srv
{

inline void to_flow_style_yaml(
  const Attach_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: ok
  {
    out << "ok: ";
    rosidl_generator_traits::value_to_yaml(msg.ok, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Attach_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ok
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ok: ";
    rosidl_generator_traits::value_to_yaml(msg.ok, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Attach_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace gazebo_ros_link_attacher

namespace rosidl_generator_traits
{

[[deprecated("use gazebo_ros_link_attacher::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const gazebo_ros_link_attacher::srv::Attach_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  gazebo_ros_link_attacher::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use gazebo_ros_link_attacher::srv::to_yaml() instead")]]
inline std::string to_yaml(const gazebo_ros_link_attacher::srv::Attach_Response & msg)
{
  return gazebo_ros_link_attacher::srv::to_yaml(msg);
}

template<>
inline const char * data_type<gazebo_ros_link_attacher::srv::Attach_Response>()
{
  return "gazebo_ros_link_attacher::srv::Attach_Response";
}

template<>
inline const char * name<gazebo_ros_link_attacher::srv::Attach_Response>()
{
  return "gazebo_ros_link_attacher/srv/Attach_Response";
}

template<>
struct has_fixed_size<gazebo_ros_link_attacher::srv::Attach_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<gazebo_ros_link_attacher::srv::Attach_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<gazebo_ros_link_attacher::srv::Attach_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<gazebo_ros_link_attacher::srv::Attach>()
{
  return "gazebo_ros_link_attacher::srv::Attach";
}

template<>
inline const char * name<gazebo_ros_link_attacher::srv::Attach>()
{
  return "gazebo_ros_link_attacher/srv/Attach";
}

template<>
struct has_fixed_size<gazebo_ros_link_attacher::srv::Attach>
  : std::integral_constant<
    bool,
    has_fixed_size<gazebo_ros_link_attacher::srv::Attach_Request>::value &&
    has_fixed_size<gazebo_ros_link_attacher::srv::Attach_Response>::value
  >
{
};

template<>
struct has_bounded_size<gazebo_ros_link_attacher::srv::Attach>
  : std::integral_constant<
    bool,
    has_bounded_size<gazebo_ros_link_attacher::srv::Attach_Request>::value &&
    has_bounded_size<gazebo_ros_link_attacher::srv::Attach_Response>::value
  >
{
};

template<>
struct is_service<gazebo_ros_link_attacher::srv::Attach>
  : std::true_type
{
};

template<>
struct is_service_request<gazebo_ros_link_attacher::srv::Attach_Request>
  : std::true_type
{
};

template<>
struct is_service_response<gazebo_ros_link_attacher::srv::Attach_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__TRAITS_HPP_
