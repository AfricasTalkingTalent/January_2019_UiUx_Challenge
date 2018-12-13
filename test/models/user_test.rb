require 'test_helper'

class UserTest < ActiveSupport::TestCase
  def setup
    @user = User.new(name: "John Doe", phone_number: "254700123456",
                    password: "foobar", password_confirmation: "foobar")
  end

  test "should be valid" do
    assert @user.valid?
  end

  test "name should be present" do
    @user.name = "    "
    assert_not @user.valid?
  end

  test "phone number should be present" do
    @user.phone_number = "    "
    assert_not @user.valid?
  end

  test "phone number should consist of integers only" do
    @user.phone_number = "254string2"
    assert_not @user.valid?
  end

  test "phone number should have at least 12 digits" do
    @user.phone_number = "25470670500"
    assert_not @user.valid?
  end

  test "phone number should be unique" do
    user_clone = @user.dup
    @user.save
    assert_not user_clone.valid?
  end
end
