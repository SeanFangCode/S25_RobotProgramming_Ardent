// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from gazebo_ros_link_attacher:srv/Attach.idl
// generated code does not contain a copyright notice
#include "gazebo_ros_link_attacher/srv/detail/attach__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `model_name_1`
// Member `link_name_1`
// Member `model_name_2`
// Member `link_name_2`
#include "rosidl_runtime_c/string_functions.h"

bool
gazebo_ros_link_attacher__srv__Attach_Request__init(gazebo_ros_link_attacher__srv__Attach_Request * msg)
{
  if (!msg) {
    return false;
  }
  // model_name_1
  if (!rosidl_runtime_c__String__init(&msg->model_name_1)) {
    gazebo_ros_link_attacher__srv__Attach_Request__fini(msg);
    return false;
  }
  // link_name_1
  if (!rosidl_runtime_c__String__init(&msg->link_name_1)) {
    gazebo_ros_link_attacher__srv__Attach_Request__fini(msg);
    return false;
  }
  // model_name_2
  if (!rosidl_runtime_c__String__init(&msg->model_name_2)) {
    gazebo_ros_link_attacher__srv__Attach_Request__fini(msg);
    return false;
  }
  // link_name_2
  if (!rosidl_runtime_c__String__init(&msg->link_name_2)) {
    gazebo_ros_link_attacher__srv__Attach_Request__fini(msg);
    return false;
  }
  return true;
}

void
gazebo_ros_link_attacher__srv__Attach_Request__fini(gazebo_ros_link_attacher__srv__Attach_Request * msg)
{
  if (!msg) {
    return;
  }
  // model_name_1
  rosidl_runtime_c__String__fini(&msg->model_name_1);
  // link_name_1
  rosidl_runtime_c__String__fini(&msg->link_name_1);
  // model_name_2
  rosidl_runtime_c__String__fini(&msg->model_name_2);
  // link_name_2
  rosidl_runtime_c__String__fini(&msg->link_name_2);
}

bool
gazebo_ros_link_attacher__srv__Attach_Request__are_equal(const gazebo_ros_link_attacher__srv__Attach_Request * lhs, const gazebo_ros_link_attacher__srv__Attach_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // model_name_1
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->model_name_1), &(rhs->model_name_1)))
  {
    return false;
  }
  // link_name_1
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->link_name_1), &(rhs->link_name_1)))
  {
    return false;
  }
  // model_name_2
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->model_name_2), &(rhs->model_name_2)))
  {
    return false;
  }
  // link_name_2
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->link_name_2), &(rhs->link_name_2)))
  {
    return false;
  }
  return true;
}

bool
gazebo_ros_link_attacher__srv__Attach_Request__copy(
  const gazebo_ros_link_attacher__srv__Attach_Request * input,
  gazebo_ros_link_attacher__srv__Attach_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // model_name_1
  if (!rosidl_runtime_c__String__copy(
      &(input->model_name_1), &(output->model_name_1)))
  {
    return false;
  }
  // link_name_1
  if (!rosidl_runtime_c__String__copy(
      &(input->link_name_1), &(output->link_name_1)))
  {
    return false;
  }
  // model_name_2
  if (!rosidl_runtime_c__String__copy(
      &(input->model_name_2), &(output->model_name_2)))
  {
    return false;
  }
  // link_name_2
  if (!rosidl_runtime_c__String__copy(
      &(input->link_name_2), &(output->link_name_2)))
  {
    return false;
  }
  return true;
}

gazebo_ros_link_attacher__srv__Attach_Request *
gazebo_ros_link_attacher__srv__Attach_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_ros_link_attacher__srv__Attach_Request * msg = (gazebo_ros_link_attacher__srv__Attach_Request *)allocator.allocate(sizeof(gazebo_ros_link_attacher__srv__Attach_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(gazebo_ros_link_attacher__srv__Attach_Request));
  bool success = gazebo_ros_link_attacher__srv__Attach_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
gazebo_ros_link_attacher__srv__Attach_Request__destroy(gazebo_ros_link_attacher__srv__Attach_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    gazebo_ros_link_attacher__srv__Attach_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
gazebo_ros_link_attacher__srv__Attach_Request__Sequence__init(gazebo_ros_link_attacher__srv__Attach_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_ros_link_attacher__srv__Attach_Request * data = NULL;

  if (size) {
    data = (gazebo_ros_link_attacher__srv__Attach_Request *)allocator.zero_allocate(size, sizeof(gazebo_ros_link_attacher__srv__Attach_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = gazebo_ros_link_attacher__srv__Attach_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        gazebo_ros_link_attacher__srv__Attach_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
gazebo_ros_link_attacher__srv__Attach_Request__Sequence__fini(gazebo_ros_link_attacher__srv__Attach_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      gazebo_ros_link_attacher__srv__Attach_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

gazebo_ros_link_attacher__srv__Attach_Request__Sequence *
gazebo_ros_link_attacher__srv__Attach_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_ros_link_attacher__srv__Attach_Request__Sequence * array = (gazebo_ros_link_attacher__srv__Attach_Request__Sequence *)allocator.allocate(sizeof(gazebo_ros_link_attacher__srv__Attach_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = gazebo_ros_link_attacher__srv__Attach_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
gazebo_ros_link_attacher__srv__Attach_Request__Sequence__destroy(gazebo_ros_link_attacher__srv__Attach_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    gazebo_ros_link_attacher__srv__Attach_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
gazebo_ros_link_attacher__srv__Attach_Request__Sequence__are_equal(const gazebo_ros_link_attacher__srv__Attach_Request__Sequence * lhs, const gazebo_ros_link_attacher__srv__Attach_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!gazebo_ros_link_attacher__srv__Attach_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
gazebo_ros_link_attacher__srv__Attach_Request__Sequence__copy(
  const gazebo_ros_link_attacher__srv__Attach_Request__Sequence * input,
  gazebo_ros_link_attacher__srv__Attach_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(gazebo_ros_link_attacher__srv__Attach_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    gazebo_ros_link_attacher__srv__Attach_Request * data =
      (gazebo_ros_link_attacher__srv__Attach_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!gazebo_ros_link_attacher__srv__Attach_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          gazebo_ros_link_attacher__srv__Attach_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!gazebo_ros_link_attacher__srv__Attach_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
gazebo_ros_link_attacher__srv__Attach_Response__init(gazebo_ros_link_attacher__srv__Attach_Response * msg)
{
  if (!msg) {
    return false;
  }
  // ok
  return true;
}

void
gazebo_ros_link_attacher__srv__Attach_Response__fini(gazebo_ros_link_attacher__srv__Attach_Response * msg)
{
  if (!msg) {
    return;
  }
  // ok
}

bool
gazebo_ros_link_attacher__srv__Attach_Response__are_equal(const gazebo_ros_link_attacher__srv__Attach_Response * lhs, const gazebo_ros_link_attacher__srv__Attach_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ok
  if (lhs->ok != rhs->ok) {
    return false;
  }
  return true;
}

bool
gazebo_ros_link_attacher__srv__Attach_Response__copy(
  const gazebo_ros_link_attacher__srv__Attach_Response * input,
  gazebo_ros_link_attacher__srv__Attach_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // ok
  output->ok = input->ok;
  return true;
}

gazebo_ros_link_attacher__srv__Attach_Response *
gazebo_ros_link_attacher__srv__Attach_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_ros_link_attacher__srv__Attach_Response * msg = (gazebo_ros_link_attacher__srv__Attach_Response *)allocator.allocate(sizeof(gazebo_ros_link_attacher__srv__Attach_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(gazebo_ros_link_attacher__srv__Attach_Response));
  bool success = gazebo_ros_link_attacher__srv__Attach_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
gazebo_ros_link_attacher__srv__Attach_Response__destroy(gazebo_ros_link_attacher__srv__Attach_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    gazebo_ros_link_attacher__srv__Attach_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
gazebo_ros_link_attacher__srv__Attach_Response__Sequence__init(gazebo_ros_link_attacher__srv__Attach_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_ros_link_attacher__srv__Attach_Response * data = NULL;

  if (size) {
    data = (gazebo_ros_link_attacher__srv__Attach_Response *)allocator.zero_allocate(size, sizeof(gazebo_ros_link_attacher__srv__Attach_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = gazebo_ros_link_attacher__srv__Attach_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        gazebo_ros_link_attacher__srv__Attach_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
gazebo_ros_link_attacher__srv__Attach_Response__Sequence__fini(gazebo_ros_link_attacher__srv__Attach_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      gazebo_ros_link_attacher__srv__Attach_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

gazebo_ros_link_attacher__srv__Attach_Response__Sequence *
gazebo_ros_link_attacher__srv__Attach_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  gazebo_ros_link_attacher__srv__Attach_Response__Sequence * array = (gazebo_ros_link_attacher__srv__Attach_Response__Sequence *)allocator.allocate(sizeof(gazebo_ros_link_attacher__srv__Attach_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = gazebo_ros_link_attacher__srv__Attach_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
gazebo_ros_link_attacher__srv__Attach_Response__Sequence__destroy(gazebo_ros_link_attacher__srv__Attach_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    gazebo_ros_link_attacher__srv__Attach_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
gazebo_ros_link_attacher__srv__Attach_Response__Sequence__are_equal(const gazebo_ros_link_attacher__srv__Attach_Response__Sequence * lhs, const gazebo_ros_link_attacher__srv__Attach_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!gazebo_ros_link_attacher__srv__Attach_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
gazebo_ros_link_attacher__srv__Attach_Response__Sequence__copy(
  const gazebo_ros_link_attacher__srv__Attach_Response__Sequence * input,
  gazebo_ros_link_attacher__srv__Attach_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(gazebo_ros_link_attacher__srv__Attach_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    gazebo_ros_link_attacher__srv__Attach_Response * data =
      (gazebo_ros_link_attacher__srv__Attach_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!gazebo_ros_link_attacher__srv__Attach_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          gazebo_ros_link_attacher__srv__Attach_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!gazebo_ros_link_attacher__srv__Attach_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
