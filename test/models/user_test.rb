require 'test_helper'

class UserTest < ActiveSupport::TestCase
  def setup
    @user = User.new(name: "John Doe", phone_number: "254700123456")
  end

  test "should be valid" do
    assert @user.valid?
  end
end
