class AddPrivateToMessages < ActiveRecord::Migration[5.2]
  def change
    add_column :messages, :private, :boolean, default: false
  end
end
