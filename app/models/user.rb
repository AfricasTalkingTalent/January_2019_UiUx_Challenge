class User < ApplicationRecord
  require 'AfricasTalkingGateway'
  validates :name, presence: true
  validates :phone_number, presence: true, numericality: { only_integer: true },
    length: { minimum: 12 }, uniqueness: true
  has_secure_password
  validates :password, presence: true, length: { minimum: 6 }

  def send_sms(message)
    username = ENV['AT_USERNAME']
    apikey = ENV['AT_API']
    #introduce country code into mobile number if the previous number did not have it
    first_character = mobile_number[0] 
    if first_character == '0'
      mobile_number[0] = '+254'
    end
    gateway = AfricasTalkingGateway.new(username, apikey)
    begin
      reports = gateway.sendMessage(mobile_number, message)
      reports.each {|x|
        # status is either "Success" or "error message"
        puts 'number=' + x.number + ';status=' + x.status + ';messageId=' + x.messageId + ';cost=' + x.cost
      }
    rescue AfricasTalkingGatewayException => ex
      puts 'Encountered an error: ' + ex.message
    end
  end
end
