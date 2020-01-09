while True:
  # Get the next event from the operating system
  event = get_next_event()

  # Get the function that is assigned to handle this event
  a_function_to_handle_the_event = event-handlers[event]

  # If a function has been assigned to handle this event, call the function
  if a_function_to_handle_the_event: a_function_to_handle_the_event()  # Call the event-handler function

  # Stop processing events if the user gives a command to stop the application
  if window_needs_to_close:
    break  # out of the event-loop
