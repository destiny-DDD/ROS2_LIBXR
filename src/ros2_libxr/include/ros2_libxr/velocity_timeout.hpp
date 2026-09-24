#ifndef RM_SERIAL_DRIVER__VELOCITY_TIMEOUT_HPP_
#define RM_SERIAL_DRIVER__VELOCITY_TIMEOUT_HPP_

#include <cstdint>

namespace rm_serial_driver::detail {

inline bool IsVelocityCommandTimedOut(std::int64_t now_ms,
                                       std::int64_t last_command_ms,
                                       std::int64_t timeout_ms) noexcept {
  return now_ms - last_command_ms >= timeout_ms;
}

}  // namespace rm_serial_driver::detail

#endif  // RM_SERIAL_DRIVER__VELOCITY_TIMEOUT_HPP_
