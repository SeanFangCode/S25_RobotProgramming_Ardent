// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from gazebo_ros_link_attacher:srv/Attach.idl
// generated code does not contain a copyright notice

#ifndef GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__BUILDER_HPP_
#define GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "gazebo_ros_link_attacher/srv/detail/attach__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace gazebo_ros_link_attacher
{

namespace srv
{

namespace builder
{

class Init_Attach_Request_link_name_2
{
public:
  explicit Init_Attach_Request_link_name_2(::gazebo_ros_link_attacher::srv::Attach_Request & msg)
  : msg_(msg)
  {}
  ::gazebo_ros_link_attacher::srv::Attach_Request link_name_2(::gazebo_ros_link_attacher::srv::Attach_Request::_link_name_2_type arg)
  {
    msg_.link_name_2 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::gazebo_ros_link_attacher::srv::Attach_Request msg_;
};

class Init_Attach_Request_model_name_2
{
public:
  explicit Init_Attach_Request_model_name_2(::gazebo_ros_link_attacher::srv::Attach_Request & msg)
  : msg_(msg)
  {}
  Init_Attach_Request_link_name_2 model_name_2(::gazebo_ros_link_attacher::srv::Attach_Request::_model_name_2_type arg)
  {
    msg_.model_name_2 = std::move(arg);
    return Init_Attach_Request_link_name_2(msg_);
  }

private:
  ::gazebo_ros_link_attacher::srv::Attach_Request msg_;
};

class Init_Attach_Request_link_name_1
{
public:
  explicit Init_Attach_Request_link_name_1(::gazebo_ros_link_attacher::srv::Attach_Request & msg)
  : msg_(msg)
  {}
  Init_Attach_Request_model_name_2 link_name_1(::gazebo_ros_link_attacher::srv::Attach_Request::_link_name_1_type arg)
  {
    msg_.link_name_1 = std::move(arg);
    return Init_Attach_Request_model_name_2(msg_);
  }

private:
  ::gazebo_ros_link_attacher::srv::Attach_Request msg_;
};

class Init_Attach_Request_model_name_1
{
public:
  Init_Attach_Request_model_name_1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Attach_Request_link_name_1 model_name_1(::gazebo_ros_link_attacher::srv::Attach_Request::_model_name_1_type arg)
  {
    msg_.model_name_1 = std::move(arg);
    return Init_Attach_Request_link_name_1(msg_);
  }

private:
  ::gazebo_ros_link_attacher::srv::Attach_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::gazebo_ros_link_attacher::srv::Attach_Request>()
{
  return gazebo_ros_link_attacher::srv::builder::Init_Attach_Request_model_name_1();
}

}  // namespace gazebo_ros_link_attacher


namespace gazebo_ros_link_attacher
{

namespace srv
{

namespace builder
{

class Init_Attach_Response_ok
{
public:
  Init_Attach_Response_ok()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::gazebo_ros_link_attacher::srv::Attach_Response ok(::gazebo_ros_link_attacher::srv::Attach_Response::_ok_type arg)
  {
    msg_.ok = std::move(arg);
    return std::move(msg_);
  }

private:
  ::gazebo_ros_link_attacher::srv::Attach_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::gazebo_ros_link_attacher::srv::Attach_Response>()
{
  return gazebo_ros_link_attacher::srv::builder::Init_Attach_Response_ok();
}

}  // namespace gazebo_ros_link_attacher

#endif  // GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__BUILDER_HPP_
