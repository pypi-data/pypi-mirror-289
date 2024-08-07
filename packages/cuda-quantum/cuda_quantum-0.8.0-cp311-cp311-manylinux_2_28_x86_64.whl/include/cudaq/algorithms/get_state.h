/****************************************************************-*- C++ -*-****
 * Copyright (c) 2022 - 2024 NVIDIA Corporation & Affiliates.                  *
 * All rights reserved.                                                        *
 *                                                                             *
 * This source code and the accompanying materials are made available under    *
 * the terms of the Apache License 2.0 which accompanies this distribution.    *
 ******************************************************************************/

#pragma once

#include "common/ExecutionContext.h"
#include "common/KernelWrapper.h"
#include "cudaq/concepts.h"
#include "cudaq/host_config.h"
#include "cudaq/platform.h"
#include "cudaq/platform/QuantumExecutionQueue.h"
#include "cudaq/qis/remote_state.h"
#include "cudaq/qis/state.h"
#include <complex>
#include <vector>

namespace cudaq {

#if CUDAQ_USE_STD20
/// @brief Define a valid kernel concept
template <typename QuantumKernel, typename... Args>
concept KernelCallValid =
    ValidArgumentsPassed<QuantumKernel, Args...> &&
    HasVoidReturnType<std::invoke_result_t<QuantumKernel, Args...>>;
#endif

namespace details {

/// @brief Execute the given kernel functor and extract the
/// state representation.
template <typename KernelFunctor>
state extractState(KernelFunctor &&kernel) {
  // Get the platform.
  auto &platform = cudaq::get_platform();

  // This can only be done in simulation
  if (!platform.is_simulator())
    throw std::runtime_error("Cannot use get_state on a physical QPU.");
  // Create an execution context, indicate this is for
  // extracting the state representation
  ExecutionContext context("extract-state");

  // Perform the usual pattern set the context,
  // execute and then reset
  platform.set_exec_ctx(&context);
  kernel();
  platform.reset_exec_ctx();

  // Return the state data. Since the ExecutionContext
  // is done being used, we'll move the simulation state
  // pointer to the state type. The state will retain
  // value semantics, due to its tracking of this simulation
  // data as a shared_ptr.
  return state(context.simulationState.release());
}

template <typename KernelFunctor>
auto runGetStateAsync(KernelFunctor &&wrappedKernel,
                      cudaq::quantum_platform &platform, std::size_t qpu_id) {
  // This can only be done in simulation
  if (!platform.is_simulator())
    throw std::runtime_error("Cannot use get_state_async on a physical QPU.");

  if (qpu_id >= platform.num_qpus())
    throw std::invalid_argument(
        "Provided qpu_id is invalid (must be <=to platform.num_qpus()).");

  std::promise<state> promise;
  auto f = promise.get_future();
  // Wrapped it as a generic (returning void) function
  QuantumTask wrapped = detail::make_copyable_function(
      [p = std::move(promise), qpu_id, &platform,
       func = std::forward<KernelFunctor>(wrappedKernel)]() mutable {
        ExecutionContext context("extract-state");
        // Indicate that this is an async exec
        context.asyncExec = true;
        // Set the platform and the qpu id.
        platform.set_exec_ctx(&context, qpu_id);
        platform.set_current_qpu(qpu_id);
        func();
        platform.reset_exec_ctx(qpu_id);
        // Extract state data
        p.set_value(state(context.simulationState.release()));
      });

  platform.enqueueAsyncTask(qpu_id, wrapped);
  return f;
}
} // namespace details

/// @brief Return the state representation generated by the kernel at the given
/// runtime arguments.
template <typename QuantumKernel, typename... Args>
auto get_state(QuantumKernel &&kernel, Args &&...args) {
#if defined(CUDAQ_REMOTE_SIM) && !defined(CUDAQ_LIBRARY_MODE)
  // If this is a kernel that we cannot retrieve a name at runtime (C-type
  // function), we cannot use lazy evaluation since the kernel name/quake code
  // is not retrievable. This needs to be directed to the `altLaunchKernel`
  // function, whereby the bridge has generated code to construct the kernel
  // name at runtime.
  if (cudaq::get_quake_by_name(cudaq::getKernelName(kernel), false).empty())
    return details::extractState([&]() mutable {
      cudaq::invokeKernel(std::forward<QuantumKernel>(kernel),
                          std::forward<Args>(args)...);
    });

  return state(new RemoteSimulationState(std::forward<QuantumKernel>(kernel),
                                         std::forward<Args>(args)...));
#else
#if defined(CUDAQ_REMOTE_SIM)
  // Kernel builder is MLIR-based kernel.
  if constexpr (has_name<QuantumKernel>::value) {
    return state(new RemoteSimulationState(std::forward<QuantumKernel>(kernel),
                                           std::forward<Args>(args)...));
  }
#endif
  return details::extractState([&]() mutable {
    cudaq::invokeKernel(std::forward<QuantumKernel>(kernel),
                        std::forward<Args>(args)...);
  });
#endif
}

/// @brief Return type for asynchronous `get_state`.
using async_state_result = std::future<state>;

/// \brief Return the state representation generated by the kernel at the given
/// runtime arguments asynchronously.
///
/// @param `qpu_id` the id of the QPU to run asynchronously on
/// @param kernel the kernel expression, must contain final measurements
/// @param `args` the variadic concrete arguments for evaluation of the kernel.
/// \returns state future, A std::future containing the resultant state vector
///
#if CUDAQ_USE_STD20
template <typename QuantumKernel, typename... Args>
  requires KernelCallValid<QuantumKernel, Args...>
#else
template <typename QuantumKernel, typename... Args,
          typename = std::enable_if_t<
              std::is_invocable_r_v<void, QuantumKernel, Args...>>>
#endif
async_state_result get_state_async(std::size_t qpu_id, QuantumKernel &&kernel,
                                   Args &&...args) {
  auto &platform = cudaq::get_platform();
#if CUDAQ_USE_STD20
  return details::runGetStateAsync(
      [&kernel, ... args = std::forward<Args>(args)]() mutable {
        cudaq::invokeKernel(std::forward<QuantumKernel>(kernel),
                            std::forward<Args>(args)...);
      },
      platform, qpu_id);
#else
  return details::runGetStateAsync(
      [args = std::make_tuple(kernel, args...)]() mutable {
        std::apply(cudaq::invokeKernel, args);
      },
      platform, qpu_id);
#endif
}

/// \brief Return the state representation generated by the kernel at the given
/// runtime arguments asynchronously on the default QPU (id = 0).
///
/// @param kernel the kernel expression, must contain final measurements
/// @param `args` the variadic concrete arguments for evaluation of the kernel.
/// \returns state future, A std::future containing the resultant state vector
///
#if CUDAQ_USE_STD20
template <typename QuantumKernel, typename... Args>
  requires KernelCallValid<QuantumKernel, Args...>
#else
template <typename QuantumKernel, typename... Args,
          typename = std::enable_if_t<
              std::is_invocable_r_v<void, QuantumKernel, Args...>>>
#endif
async_state_result get_state_async(QuantumKernel &&kernel, Args &&...args) {
  return get_state_async(0, std::forward<QuantumKernel>(kernel),
                         std::forward<Args>(args)...);
}

extern "C" {
std::int64_t __nvqpp_cudaq_state_numberOfQubits(state *);
}

} // namespace cudaq
