desc "Sets the `printed` value of all Messages to true"
desc "Task description"
task :set_printed_on_messages do
  Message.update_all(printed: true)
end
