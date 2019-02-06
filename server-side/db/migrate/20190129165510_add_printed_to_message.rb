class AddPrintedToMessage < ActiveRecord::Migration[5.2]
  def change
    add_column :messages, :printed, :boolean, default: false
  end
end
