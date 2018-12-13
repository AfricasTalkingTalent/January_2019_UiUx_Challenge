class AddIndexToUsersPhoneNumber < ActiveRecord::Migration[5.2]
  def change
    add_index :users, :phone_number, unique: true
  end
end
