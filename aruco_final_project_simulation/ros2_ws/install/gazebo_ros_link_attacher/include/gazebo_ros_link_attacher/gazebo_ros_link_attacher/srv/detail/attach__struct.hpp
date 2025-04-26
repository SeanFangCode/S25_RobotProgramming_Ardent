// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from gazebo_ros_link_attacher:srv/Attach.idl
// generated code does not contain a copyright notice

#ifndef GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__STRUCT_HPP_
#define GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__gazebo_ros_link_attacher__srv__Attach_Request __attribute__((deprecated))
#else
# define DEPRECATED__gazebo_ros_link_attacher__srv__Attach_Request __declspec(deprecated)
#endif

namespace gazebo_ros_link_attacher
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Attach_Request_
{
  using Type = Attach_Request_<ContainerAllocator>;

  explicit Attach_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->model_name_1 = "";
      this->link_name_1 = "";
      this->model_name_2 = "";
      this->link_name_2 = "";
    }
  }

  explicit Attach_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : model_name_1(_alloc),
    link_name_1(_alloc),
    model_name_2(_alloc),
    link_name_2(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->model_name_1 = "";
      this->link_name_1 = "";
      this->model_name_2 = "";
      this->link_name_2 = "";
    }
  }

  // field types and members
  using _model_name_1_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _model_name_1_type model_name_1;
  using _link_name_1_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _link_name_1_type link_name_1;
  using _model_name_2_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _model_name_2_type model_name_2;
  using _link_name_2_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _link_name_2_type link_name_2;

  // setters for named parameter idiom
  Type & set__model_name_1(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->model_name_1 = _arg;
    return *this;
  }
  Type & set__link_name_1(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->link_name_1 = _arg;
    return *this;
  }
  Type & set__model_name_2(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->model_name_2 = _arg;
    return *this;
  }
  Type & set__link_name_2(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->link_name_2 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__gazebo_ros_link_attacher__srv__Attach_Request
    std::shared_ptr<gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__gazebo_ros_link_attacher__srv__Attach_Request
    std::shared_ptr<gazebo_ros_link_attacher::srv::Attach_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Attach_Request_ & other) const
  {
    if (this->model_name_1 != other.model_name_1) {
      return false;
    }
    if (this->link_name_1 != other.link_name_1) {
      return false;
    }
    if (this->model_name_2 != other.model_name_2) {
      return false;
    }
    if (this->link_name_2 != other.link_name_2) {
      return false;
    }
    return true;
  }
  bool operator!=(const Attach_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Attach_Request_

// alias to use template instance with default allocator
using Attach_Request =
  gazebo_ros_link_attacher::srv::Attach_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace gazebo_ros_link_attacher


#ifndef _WIN32
# define DEPRECATED__gazebo_ros_link_attacher__srv__Attach_Response __attribute__((deprecated))
#else
# define DEPRECATED__gazebo_ros_link_attacher__srv__Attach_Response __declspec(deprecated)
#endif

namespace gazebo_ros_link_attacher
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Attach_Response_
{
  using Type = Attach_Response_<ContainerAllocator>;

  explicit Attach_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ok = false;
    }
  }

  explicit Attach_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ok = false;
    }
  }

  // field types and members
  using _ok_type =
    bool;
  _ok_type ok;

  // setters for named parameter idiom
  Type & set__ok(
    const bool & _arg)
  {
    this->ok = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__gazebo_ros_link_attacher__srv__Attach_Response
    std::shared_ptr<gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__gazebo_ros_link_attacher__srv__Attach_Response
    std::shared_ptr<gazebo_ros_link_attacher::srv::Attach_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Attach_Response_ & other) const
  {
    if (this->ok != other.ok) {
      return false;
    }
    return true;
  }
  bool operator!=(const Attach_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Attach_Response_

// alias to use template instance with default allocator
using Attach_Response =
  gazebo_ros_link_attacher::srv::Attach_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace gazebo_ros_link_attacher

namespace gazebo_ros_link_attacher
{

namespace srv
{

struct Attach
{
  using Request = gazebo_ros_link_attacher::srv::Attach_Request;
  using Response = gazebo_ros_link_attacher::srv::Attach_Response;
};

}  // namespace srv

}  // namespace gazebo_ros_link_attacher

#endif  // GAZEBO_ROS_LINK_ATTACHER__SRV__DETAIL__ATTACH__STRUCT_HPP_
